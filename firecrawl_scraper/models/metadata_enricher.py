from __future__ import annotations

import ast
import json
import logging
import os
import re
import time
import urllib.error
import urllib.request
from pathlib import Path

import dotenv


class MetadataEnricher:
    """
    Extracts slug/summary/headings from markdown using Ollama or Gemini with
    resilient parsing and regex-based fallback behavior.
    """

    def __init__(self, log_level: int = logging.INFO):
        self.logger = logging.getLogger(f"{__name__}.{self.__class__.__name__}")
        self.logger.setLevel(log_level)

        if not self.logger.handlers:
            handler = logging.StreamHandler()
            handler.setLevel(log_level)
            formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)

    def _request_ollama(self, prompt: str, model: str, host: str, timeout: int = 180) -> str:
        payload = json.dumps(
            {
                "model": model,
                "prompt": prompt,
                "stream": False,
            }
        ).encode("utf-8")

        url = host.rstrip("/") + "/api/generate"
        req = urllib.request.Request(
            url,
            data=payload,
            headers={"Content-Type": "application/json", "timeout": timeout},
            method="POST",
        )
        try:
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                resp_text = resp.read().decode("utf-8", errors="replace")

            response_json = json.loads(resp_text)
            return response_json.get("response", "")
        except urllib.error.HTTPError as e:
            body = e.read().decode("utf-8", errors="ignore") if hasattr(e, "read") else ""
            self.logger.exception("Ollama HTTP error", extra={"status": getattr(e, "code", None), "body": body})
            raise
        except Exception:
            self.logger.exception("Failed contacting Ollama server")
            raise

    def _request_gemini(self, prompt: str, model: str, api_key: str, timeout: int = 180) -> str:
        if not api_key:
            raise ValueError("Missing GOOGLE_GEMINI_API_KEY")

        from google import genai
        from google.genai import types

        model_name = model[7:] if model.startswith("models/") else model

        client = genai.Client(api_key=api_key)
        self.logger.debug("Calling Gemini SDK generate_content", extra={"model": model_name, "timeout": timeout})
        response = client.models.generate_content(
            model=model_name,
            contents=prompt,
            config=types.GenerateContentConfig(
                temperature=0.2,
                max_output_tokens=512,
            ),
        )

        text = getattr(response, "text", None)
        if isinstance(text, str) and text.strip():
            return text

        candidates = getattr(response, "candidates", None) or []
        parts = []
        for candidate in candidates:
            content = getattr(candidate, "content", None)
            content_parts = getattr(content, "parts", None) or []
            for part in content_parts:
                part_text = getattr(part, "text", None)
                if isinstance(part_text, str) and part_text:
                    parts.append(part_text)
        return "\n".join(parts)

    def _fallback_extract_headings(self, markdown: str):
        headings = []
        for line in markdown.splitlines():
            m = re.match(r"^(#+)\s+(.*)", line)
            if m:
                level = len(m.group(1))
                text = m.group(2).strip()
                headings.append({"level": level, "text": text})
        return headings

    def _normalize_combined_metadata(self, payload: dict, markdown: str) -> dict:
        slug = str(payload.get("slug", "") or "").strip().lower()
        slug = re.sub(r"\s+", "", slug)
        slug = re.sub(r"[^a-z0-9_-]", "", slug)

        summary = str(payload.get("summary", "") or "").strip()
        summary = re.sub(r"\s+", " ", summary)
        if len(summary) > 100:
            summary = summary[:100].rstrip()

        headings = payload.get("headings", [])
        if isinstance(headings, str):
            parsed = None
            try:
                parsed = json.loads(headings)
            except Exception:
                try:
                    parsed = ast.literal_eval(headings)
                except Exception:
                    parsed = None
            if isinstance(parsed, list):
                headings = parsed

        if not isinstance(headings, list) or not all(
            isinstance(h, dict) and isinstance(h.get("level"), int) and isinstance(h.get("text"), str) for h in headings
        ):
            headings = self._extract_headings_from_text(str(payload.get("headings", ""))) or self._fallback_extract_headings(
                markdown
            )

        return {"slug": slug, "summary": summary, "headings": headings}

    def _extract_headings_from_text(self, text: str):
        lines = [ln.strip() for ln in text.splitlines() if ln.strip()]
        headings = []
        for ln in lines:
            m_hash = re.match(r"^(#{1,6})\s+(.+)$", ln)
            if m_hash:
                headings.append({"level": len(m_hash.group(1)), "text": m_hash.group(2).strip()})
                continue
            m_level = re.match(r"(?i)^[-*]?\s*level\s*[:=]\s*(\d+)\s*[,|;]\s*text\s*[:=]\s*(.+)$", ln)
            if m_level:
                headings.append({"level": int(m_level.group(1)), "text": m_level.group(2).strip(" \"'")})
                continue
            m_hn = re.match(r"(?i)^h([1-6])\s*[:\-]\s*(.+)$", ln)
            if m_hn:
                headings.append({"level": int(m_hn.group(1)), "text": m_hn.group(2).strip()})
        return headings if headings else None

    def _parse_combined_metadata_payload(self, response_text: str, markdown: str):
        cleaned = response_text.strip()
        cleaned = re.sub(r"^```json|^```|```$", "", cleaned, flags=re.MULTILINE).strip()

        candidates = [cleaned]
        match = re.search(r"\{.*\}", cleaned, re.DOTALL)
        if match:
            candidates.append(match.group(0))

        for candidate in candidates:
            payload = None
            try:
                payload = json.loads(candidate)
            except Exception:
                try:
                    payload = json.loads(candidate.replace("'", '"'))
                except Exception:
                    try:
                        payload = ast.literal_eval(candidate)
                    except Exception:
                        payload = None
            if isinstance(payload, dict):
                return self._normalize_combined_metadata(payload, markdown)

        slug_match = re.search(r"(?im)^slug\s*[:=]\s*([a-z0-9_-]+)\s*$", cleaned)
        summary_match = re.search(r"(?im)^summary\s*[:=]\s*(.+)$", cleaned)
        headings_block = re.search(r"(?ims)^headings\s*:\s*(.*)$", cleaned)
        headings_text = headings_block.group(1).strip() if headings_block else ""

        summary_text = summary_match.group(1).strip() if summary_match else ""
        if not summary_text and cleaned:
            first_line = cleaned.splitlines()[0].strip()
            summary_text = re.split(r"(?<=[.!?])\s+", first_line, maxsplit=1)[0].strip()

        slug_text = slug_match.group(1).strip() if slug_match else ""
        if not slug_text:
            source = ""
            md_headings = self._fallback_extract_headings(markdown)
            if md_headings:
                source = md_headings[0].get("text", "")
            if not source:
                source = summary_text
            words = re.findall(r"[a-z0-9]+", source.lower())
            slug_text = words[0] if words else ""

        parsed = {
            "slug": slug_text,
            "summary": summary_text,
            "headings": self._extract_headings_from_text(headings_text) or self._fallback_extract_headings(markdown),
        }
        return self._normalize_combined_metadata(parsed, markdown)

    def extract(
        self,
        markdown: str,
        model: str = "llama3.2:3b",
        host: str = "http://localhost:11434",
        timeout: int = 180,
        retries: int = 3,
        retry_delay: float = 5.0,
        provider: str = "ollama",
    ) -> dict:
        self.logger.info("extract metadata called", extra={"model": model, "host": host, "markdown_len": len(markdown)})
        provider = provider.lower() if provider else "auto"
        use_ollama = False
        gemini_key = None

        if provider == "gemini":
            try:
                dotenv_path = Path(__file__).parent.parent / ".env"
                dotenv.load_dotenv(dotenv_path.as_posix())
                gemini_key = os.environ.get("GOOGLE_GEMINI_API_KEY")
                if not gemini_key:
                    self.logger.warning(
                        "Provider=gemini but no GOOGLE_GEMINI_API_KEY found in .env; falling back to regex headings"
                    )
                    return {"slug": None, "summary": None, "headings": self._fallback_extract_headings(markdown)}
            except Exception:
                self.logger.exception("Failed loading .env for Gemini key; falling back")
                return {"slug": None, "summary": None, "headings": self._fallback_extract_headings(markdown)}
        elif provider == "ollama":
            try:
                req = urllib.request.Request(host.rstrip("/"), method="HEAD")
                urllib.request.urlopen(req, timeout=timeout)
                use_ollama = True
            except Exception:
                self.logger.warning(
                    "Provider=ollama but host not reachable; falling back to regex headings", extra={"host": host}
                )
                return {"slug": None, "summary": None, "headings": self._fallback_extract_headings(markdown)}
        else:
            try:
                req = urllib.request.Request(host.rstrip("/"), method="HEAD")
                urllib.request.urlopen(req, timeout=timeout)
                use_ollama = True
            except Exception:
                self.logger.warning("Ollama host is not reachable, will try Gemini if API key present", extra={"host": host})
                try:
                    dotenv_path = Path(__file__).parent.parent / ".env"
                    dotenv.load_dotenv(dotenv_path.as_posix())
                    gemini_key = os.environ.get("GOOGLE_GEMINI_API_KEY")
                    if not gemini_key:
                        self.logger.warning("No GOOGLE_GEMINI_API_KEY found in .env; falling back to local regex headings")
                        return {"slug": None, "summary": None, "headings": self._fallback_extract_headings(markdown)}
                except Exception:
                    self.logger.exception("Failed loading .env for Gemini key; falling back")
                    return {"slug": None, "summary": None, "headings": self._fallback_extract_headings(markdown)}

        combined_prompt = (
            "You are senior copy writer. Given the full markdown content, return metadata.\n"
            "Preferred output format: a single JSON object with keys slug, summary, headings.\n"
            "Rules:\n"
            "1) slug: one-word, lowercase identifier, no spaces.\n"
            "2) summary: one concise sentence around 100 characters.\n"
            "3) headings: list of objects with keys 'level' (integer heading depth from markdown # count) and 'text' (string).\n"
            "JSON example:\n"
            "{\"slug\":\"concepts\",\"summary\":\"Overview of Flink concepts and APIs.\",\"headings\":[{\"level\":1,\"text\":\"Concepts\"},{\"level\":2,\"text\":\"Flink APIs\"}]}\n"
            "If you cannot provide JSON, use EXACTLY this fallback format:\n"
            "slug: <slug>\n"
            "summary: <summary>\n"
            "headings:\n"
            "H1: <heading text>\n"
            "H2: <heading text>\n"
            "Provide only metadata output, no explanations.\n\n"
            "MARKDOWN:\n" + markdown
        )

        src = "Ollama" if use_ollama else "Gemini"
        self.logger.debug(f"Requesting combined metadata from {src}")
        self.logger.debug(f"Combined metadata prompt: \n '{combined_prompt[:500]}' \n...")

        for attempt in range(retries):
            try:
                self.logger.debug(f"{src} API call for combined metadata, attempt {attempt + 1}/{retries}")
                if use_ollama:
                    resp = self._request_ollama(combined_prompt, model, host, timeout)
                else:
                    gemini_model = model if model and model.startswith("models/") else "models/gemini-2.0-flash"
                    api_key = gemini_key or os.environ.get("GOOGLE_GEMINI_API_KEY")
                    resp = self._request_gemini(combined_prompt, gemini_model, api_key, timeout)

                self.logger.debug(f"{src} combined metadata response received", extra={"response": resp[:2000]})
                parsed = self._parse_combined_metadata_payload(resp, markdown)
                if not parsed.get("slug") and not parsed.get("summary") and not parsed.get("headings"):
                    raise ValueError("Could not parse combined metadata payload")
                return parsed
            except Exception as e:
                self.logger.warning(f"{src} API call failed for combined metadata (attempt {attempt + 1}/{retries}): {e}")
                if attempt < retries - 1:
                    time.sleep(retry_delay)

        return {"slug": "", "summary": "", "headings": self._fallback_extract_headings(markdown)}
