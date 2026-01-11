import dotenv, os, re, ast, json
import urllib.parse
import urllib.request
import urllib.error
import hashlib
import logging

from .metadata import PageMetadata


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
    
    def _request_ollama(self, prompt: str, model: str, host: str, timeout: int) -> str:
        payload = json.dumps({
            "model": model,
            "prompt": prompt,
            "stream": False
        }).encode('utf-8')

        url = host.rstrip('/') + "/api/generate"
        req = urllib.request.Request(url, data=payload, headers={"Content-Type": "application/json"}, method="POST")
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

    def extract_summaries_with_ollama(self, markdown: str, model: str = "llama3.2:3b", host: str = "http://localhost:11434", timeout: int = 30) -> dict:
        """
        Send `markdown` to an Ollama instance and ask for JSON containing:
          - slug: one-word lowercase summary
          - summary: ~100 character summary
          - headings: list of {"level":int, "text":str}

        Returns a dict with keys: `slug`, `summary`, `headings` (or raises on hard failure).
        """
        self.logger.info("extract_summaries_with_ollama called", extra={"model": model, "host": host, "markdown_len": len(markdown)})

        # Check if host is reachable
        try:
            req = urllib.request.Request(host.rstrip('/'), method="HEAD")
            urllib.request.urlopen(req, timeout=timeout)
        except Exception:
            self.logger.warning("Ollama host is not reachable", extra={"host": host})
            return {"slug": "", "summary": "", "headings": []}


        slug_prompt = (
            "You are senior copy writer. Given the full markdown content, write a specific 'slug' from the page.\n"
            "A 'slug' is a single-word, lowercase identifier (no spaces) that will specifically summarize the page.\n"
            "Only respond with this 'slug'.\n\n"
            "MARKDOWN:\n" + markdown
        )

        summary_prompt = (
            "You are senior copy writer. Given the full markdown content, create a specific 'summary' that identifies the page.\n"
            "In this case a 'summary' is a concise specific sentence that identifies the page, and is only around 100 characters long.\n"
            "Only respond with this 'summary'.\n\n"
            "MARKDOWN:\n" + markdown
        )

        headings_prompt = (
            "You are senior copy writer. Given the full markdown content, extract all headings from the page.\n"
            "Each heading must be described by a:\n"
            " * 'level' - which is the index of the heading on the page (type=integer)\n"
            " * 'text' - the text of the heading (type=string)\n"
            "Example: {\"headings\":[{\"level\":1,\"text\":\"Concepts\"},{\"level\":2,\"text\":\"Flink’s APIs\"}]}\n"
            "Respond with a valid JSON payload providing the top-level 'headings' key, with it's list.\n"
            "ONLY provide JSON object, with no back-ticks and no further description.\n\n"
            "MARKDOWN:\n" + markdown
        )

        respons_dict = {}
        for n,prompt in zip(['slug', 'summary', 'headings'], [slug_prompt, summary_prompt, headings_prompt]):
            resp = self._request_ollama(prompt, model, host, timeout)
            if n == 'headings':
                self.logger.debug("Received headings response from Ollama", extra={"response": resp})
                self.logger.debug(f"Response [lenght={len(resp)}]: \n '{resp}' \n...")
                try:
                    self.logger.debug("Parsing headings JSON from Ollama", extra={"response": resp})
                    headings_json = json.loads(resp)
                    respons_dict[n] = headings_json.get('headings', [])
                except json.JSONDecodeError:
                    try:
                        self.logger.error("Failed parsing headings JSON from Ollama, trying ast.literal_eval", extra={"response": resp})
                        headings_resp = ast.literal_eval(resp)
                        respons_dict[n] = headings_resp['headings']
                    except Exception:
                        self.logger.error("Failed to evaluate headings response", extra={"response": resp})
                        respons_dict[n] = []
            else:
                respons_dict[n] = resp.strip()
        
        return respons_dict
    
    def save_markdown_file(self, data: dict, content: str, save_dir: str = './data/markdown_files/'):
        file_name = f"{save_dir}{data.get('prefix')}_{data.get('page_id')}.md"
        try:
            with open(file_name, "w", encoding="utf-8") as f:
                f.write(content)
            self.logger.info("Saved markdown file", extra={"file": file_name})
        except Exception:
            self.logger.exception("Failed saving markdown file", extra={"file": file_name})



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
    
    