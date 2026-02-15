import dotenv, os, re, ast, json, time
import urllib.parse
import urllib.request
import urllib.error
import hashlib
import logging

from .metadata import PageMetadata
import os
from pathlib import Path


class ResponseProcessor:


    def __init__(self, root_url: str = None, log_level: int = logging.INFO):
        # Configure console logger
        self.logger = logging.getLogger(f"{__name__}.{self.__class__.__name__}")
        self.logger.setLevel(log_level)
        
        # Add console handler if not already present
        if not self.logger.handlers:
            handler = logging.StreamHandler()
            handler.setLevel(log_level)
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)
        
        self.logger.debug("Initializing ResponseProcessor", extra={"root_url": root_url})
        if root_url:
            self.root_url = root_url


    def extract_prefix(self, url, remove_start: str = 'https://nightlies.apache.org/', remove_end: str = '/docs/') -> str:
        self.logger.debug("extract_prefix called", extra={"url": url, "remove_start": remove_start, "remove_end": remove_end})
        pattern = re.compile(re.escape(remove_start) + r'.*?' + re.escape(remove_end))
        rest = pattern.sub('', url, 1)
        cleaned = re.sub(r'[^A-Za-z]+', '_', rest).strip('_')
        result = re.sub(r'_+', '_', cleaned)
        self.logger.debug("extract_prefix result", extra={"prefix": result})
        return result
    
    def extract_version(self, url, version_prefix: str = 'https://nightlies.apache.org/flink/'):
        self.logger.debug("extract_version called", extra={"url": url, "version_prefix": version_prefix})
        pattern = re.compile(re.escape(version_prefix) + r'([^/]+)/docs/')
        match = pattern.search(url)
        if match:
            version = match.group(1)
            self.logger.debug("extract_version result", extra={"version": version})
            return version
        self.logger.debug("extract_version result", extra={"version": None})
        return None
    
    def prefix_to_hash(self, prefix: str, numeric: bool = False):
        self.logger.debug("prefix_to_hash called", extra={"prefix": prefix, "numeric": numeric})
        h = hashlib.sha256(prefix.encode('utf-8')).hexdigest()
        result = int(h[:16], 16) if numeric else h
        self.logger.debug("prefix_to_hash result", extra={"hash": result})
        return result
    
    ## Add a function that receives the full markdown content and creates a hash off the content
    def content_to_hash(self, content: str, numeric: bool = False):
        self.logger.debug("content_to_hash called", extra={"content_length": len(content), "numeric": numeric})
        h = hashlib.sha256(content.encode('utf-8')).hexdigest()
        result = int(h[:16], 16) if numeric else h
        self.logger.debug("content_to_hash result", extra={"hash": result})
        return result
    
    def _normalize_url(self, url: str) -> str:
        parts = urllib.parse.urlsplit(url)

        # normalize scheme and netloc, remove fragment
        scheme = parts.scheme.lower()
        netloc = parts.netloc.lower()
        if (scheme == 'http' and netloc.endswith(':80')) or (scheme == 'https' and netloc.endswith(':443')):
            netloc = netloc.rsplit(':', 1)[0]

        normalized = urllib.parse.urlunsplit((scheme, netloc, parts.path or '/','',''))
        normalized = normalized.rstrip('/')

        self.logger.debug("_normalize_url", extra={"input": url, "normalized": normalized})
        return normalized
    
    
    def extract_markdown_links(self, text):
        """
        Extract unique markdown page links (text, url) from `text`, excluding image links.
        Fragments (anchors) are removed so multiple section links to the same page yield one entry.
        """

        pattern = re.compile(r'(?<!\!)\[(?P<text>[^\]]+)\]\((?P<url>https?://[^\s)]+)\)')
        seen = set()
        ret = []

        matches = list(pattern.finditer(text))
        self.logger.debug("extract_markdown_links found matches", extra={"count": len(matches)})

        for m in matches:
            raw_url = m.group('url').replace('\\', '')
            parts = urllib.parse.urlsplit(raw_url)

            # normalize scheme and netloc, remove fragment
            normalized = self._normalize_url(raw_url)

            if (normalized in seen) or (normalized == self._normalize_url(self.root_url)):
                continue
            seen.add(normalized)

            desc = re.sub(r'\s+', ' ', m.group('text')).strip()
            desc = re.sub(r'[^A-Za-z\s]+', '', desc)
            desc = re.sub(r'\s+', ' ', desc).strip()
            ret.append((desc, normalized))

        self.logger.debug("extract_markdown_links result", extra={"unique_count": len(ret)})
        return ret
    
    def _request_ollama(self, prompt: str, model: str, host: str, timeout: int=180) -> str:
        payload = json.dumps({
            "model": model,
            "prompt": prompt,
            "stream": False,
            
        }).encode('utf-8')

        url = host.rstrip('/') + "/api/generate"
        req = urllib.request.Request(url, data=payload, headers={"Content-Type": "application/json","timeout": timeout}, method="POST")
        try:
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                resp_text = resp.read().decode('utf-8', errors='replace')

            response_json = json.loads(resp_text)
            return response_json.get('response', '')
        except urllib.error.HTTPError as e:
            body = e.read().decode('utf-8', errors='ignore') if hasattr(e, 'read') else ''
            self.logger.exception("Ollama HTTP error", extra={"status": getattr(e, 'code', None), "body": body})
            raise
        except Exception:
            self.logger.exception("Failed contacting Ollama server")
            raise

    def _request_gemini(self, prompt: str, model: str, api_key: str, timeout: int = 180) -> str:
        """
        Call Gemini using the official google-genai SDK.
        Returns model text content (string) or raises on failure.
        """
        if not api_key:
            raise ValueError("Missing GOOGLE_GEMINI_API_KEY")

        from google import genai
        from google.genai import types

        # SDK accepts model names like "gemini-1.5-flash"; normalize if caller passed "models/...".
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

        # Primary SDK surface
        text = getattr(response, "text", None)
        if isinstance(text, str) and text.strip():
            return text

        # Fallback: reconstruct text from candidates/parts if .text is empty.
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
        """
        Fallback: extract headings from markdown using regex if Ollama fails.
        Returns a list of dicts: [{"level": int, "text": str}]
        """
        import re
        headings = []
        for line in markdown.splitlines():
            m = re.match(r'^(#+)\s+(.*)', line)
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
            isinstance(h, dict) and isinstance(h.get("level"), int) and isinstance(h.get("text"), str)
            for h in headings
        ):
            headings = self._extract_headings_from_text(str(payload.get("headings", ""))) or self._fallback_extract_headings(markdown)

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
            # Use first sentence/line from prose response when model ignores requested structure.
            summary_text = re.split(r"(?<=[.!?])\s+", first_line, maxsplit=1)[0].strip()

        slug_text = slug_match.group(1).strip() if slug_match else ""
        if not slug_text:
            # Prefer first markdown heading as slug source, then summary source.
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

    def extract_summaries_with_ollama(
            self,
            markdown: str,
            model: str = "llama3.2:3b",
            host: str = "http://localhost:11434",
            timeout: int = 180,
            retries: int = 3,
            retry_delay: float = 5.0,
            provider: str = "ollama") -> dict:
        """
        Send `markdown` to an Ollama instance and ask for JSON containing:
          - slug: one-word lowercase summary
          - summary: ~100 character summary
          - headings: list of {"level":int, "text":str}

        Returns a dict with keys: `slug`, `summary`, `headings` (or raises on hard failure).
        """
        self.logger.info("extract_summaries_with_ollama called", extra={"model": model, "host": host, "markdown_len": len(markdown)})
        # Determine provider behavior: 'auto' (try Ollama, fallback to Gemini),
        # 'ollama' (force Ollama only), 'gemini' (force Gemini only).
        provider = provider.lower() if provider else 'auto'
        use_ollama = False
        gemini_key = None

        if provider == 'gemini':
            # forced Gemini: load key from .env
            try:
                dotenv_path = Path(__file__).parent.parent / '.env'
                dotenv.load_dotenv(dotenv_path.as_posix())
                gemini_key = os.environ.get('GOOGLE_GEMINI_API_KEY')
                if not gemini_key:
                    self.logger.warning("Provider=gemini but no GOOGLE_GEMINI_API_KEY found in .env; falling back to regex headings")
                    return {"slug": None, "summary": None, "headings": self._fallback_extract_headings(markdown)}
            except Exception:
                self.logger.exception("Failed loading .env for Gemini key; falling back")
                return {"slug": None, "summary": None, "headings": self._fallback_extract_headings(markdown)}
        elif provider == 'ollama':
            try:
                req = urllib.request.Request(host.rstrip('/'), method="HEAD")
                urllib.request.urlopen(req, timeout=timeout)
                use_ollama = True
            except Exception:
                self.logger.warning("Provider=ollama but host not reachable; falling back to regex headings", extra={"host": host})
                return {"slug": None, "summary": None, "headings": self._fallback_extract_headings(markdown)}
        else:  # auto
            try:
                req = urllib.request.Request(host.rstrip('/'), method="HEAD")
                urllib.request.urlopen(req, timeout=timeout)
                use_ollama = True
            except Exception:
                self.logger.warning("Ollama host is not reachable, will try Gemini if API key present", extra={"host": host})
                try:
                    dotenv_path = Path(__file__).parent.parent / '.env'
                    dotenv.load_dotenv(dotenv_path.as_posix())
                    gemini_key = os.environ.get('GOOGLE_GEMINI_API_KEY')
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

        src = 'Ollama' if use_ollama else 'Gemini'
        self.logger.debug(f"Requesting combined metadata from {src}")
        self.logger.debug(f"Combined metadata prompt: \n '{combined_prompt[:500]}' \n...")

        for attempt in range(retries):
            try:
                self.logger.debug(f"{src} API call for combined metadata, attempt {attempt+1}/{retries}")
                if use_ollama:
                    resp = self._request_ollama(combined_prompt, model, host, timeout)
                else:
                    # Use Gemini via REST API. If provided `model` doesn't look like a Gemini name,
                    # fall back to a sensible default.
                    if model and model.startswith('models/'):
                        gemini_model = model
                    else:
                        gemini_model = 'models/gemini-2.0-flash'
                    api_key = gemini_key or os.environ.get('GOOGLE_GEMINI_API_KEY')
                    resp = self._request_gemini(combined_prompt, gemini_model, api_key, timeout)

                self.logger.debug(f"{src} combined metadata response received", extra={"response": resp[:2000]})
                parsed = self._parse_combined_metadata_payload(resp, markdown)
                if not parsed.get("slug") and not parsed.get("summary") and not parsed.get("headings"):
                    raise ValueError("Could not parse combined metadata payload")
                return parsed
            except Exception as e:
                self.logger.warning(f"{src} API call failed for combined metadata (attempt {attempt+1}/{retries}): {e}")
                if attempt < retries - 1:
                    time.sleep(retry_delay)

        return {
            "slug": "",
            "summary": "",
            "headings": self._fallback_extract_headings(markdown)
        }
    
    def save_markdown_file(self, data: dict, content: str, save_dir: str = './data/markdown_files/'):
        
        # Get the directory of the current script and resolve relative paths from there
        script_dir = Path(__file__).parent.parent
        save_path = script_dir / save_dir
        save_path.mkdir(parents=True, exist_ok=True)
        
        file_name = save_path / f"{data.get('prefix')}_{data.get('page_id')}.md"
        try:
            with open(file_name, "w", encoding="utf-8") as f:
                f.write(content)
            self.logger.info("Saved markdown file", extra={"file": str(file_name)})
        except Exception:
            self.logger.exception("Failed saving markdown file", extra={"file": str(file_name)})




    def parse_raw_response(self, raw_response: str,parent_url: str = None, ask_ollama: bool = True) -> dict:
        self.logger.info("parse_raw_response called", extra={"raw_response_keys": list(raw_response.keys())})
        data_dict = {}
        data_dict['title'] = raw_response['metadata']['title']
        data_dict['url'] = raw_response['metadata']['url']
        self.logger.debug("parse_raw_response called", extra={"url": data_dict['url'], "parent_url": parent_url})
        if parent_url:
            data_dict['is_root_url'] = False
        else:
            data_dict['is_root_url'] = True
            self.root_url = data_dict['url']
        data_dict['parent_url'] = parent_url

        data_dict['content_hash'] = self.content_to_hash(raw_response['markdown'], numeric=False)
        data_dict['version'] = self.extract_version(data_dict['url'])
        
        data_dict['prefix'] = self.extract_prefix(data_dict['url'])
        data_dict['page_id'] = self.prefix_to_hash(data_dict['prefix'])
        data_dict['child_urls'] = self.extract_markdown_links(raw_response['markdown'])
        if ask_ollama:
            summaries = self.extract_summaries_with_ollama(raw_response['markdown'])
            data_dict['slug'] = summaries.get('slug', '')
            data_dict['summary'] = summaries.get('summary', '')
            data_dict['headings'] = summaries.get('headings', [])

        return data_dict

    def process_response(self, raw_response: dict, ask_ollama: bool = True) -> dict:
        data_dict = self.parse_raw_response(raw_response, ask_ollama=ask_ollama)
        metadata = PageMetadata.model_validate(data_dict)
        self.save_markdown_file(data_dict, raw_response['markdown'])
        self.logger.info("process_response completed", extra={"page_id": data_dict.get('page_id'), "url": data_dict.get('url')})
        return metadata
    
    
