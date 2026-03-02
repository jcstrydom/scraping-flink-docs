import re
import hashlib
import logging

from .metadata import PageMetadata
from .metadata_enricher import MetadataEnricher
from .url_utils import normalize_url
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
        self.metadata_enricher = MetadataEnricher(log_level=log_level)


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

    def url_to_hash(self, url: str, numeric: bool = False):
        """
        Compute a stable hash from the canonical URL.
        This is the canonical identity used for page_id.
        """
        normalized_url = self._normalize_url(url)
        h = hashlib.sha256(normalized_url.encode("utf-8")).hexdigest()
        result = int(h[:16], 16) if numeric else h
        self.logger.debug("url_to_hash result", extra={"url": normalized_url, "hash": result})
        return result
    
    ## Add a function that receives the full markdown content and creates a hash off the content
    def content_to_hash(self, content: str, numeric: bool = False):
        self.logger.debug("content_to_hash called", extra={"content_length": len(content), "numeric": numeric})
        h = hashlib.sha256(content.encode('utf-8')).hexdigest()
        result = int(h[:16], 16) if numeric else h
        self.logger.debug("content_to_hash result", extra={"hash": result})
        return result
    
    def _normalize_url(self, url: str) -> str:
        normalized = normalize_url(url) or ""
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
        return self.metadata_enricher.extract(
            markdown=markdown,
            model=model,
            host=host,
            timeout=timeout,
            retries=retries,
            retry_delay=retry_delay,
            provider=provider,
        )
    
    def save_markdown_file(self, data: dict, content: str, save_dir: str = "data/markdown_files"):
        # Resolve relative paths from repo root so scraper and RAG can share /data.
        project_root = Path(__file__).resolve().parents[2]
        save_path = Path(save_dir)
        if not save_path.is_absolute():
            save_path = project_root / save_path
        save_path.mkdir(parents=True, exist_ok=True)
        
        raw_prefix = str(data.get("prefix") or "")
        human_prefix = re.sub(r"[^A-Za-z0-9_-]+", "_", raw_prefix).strip("_").lower() or "page"
        page_id = data.get("page_id")
        if not page_id and data.get("url"):
            page_id = self.url_to_hash(str(data.get("url")))

        file_name = save_path / f"{human_prefix}_{page_id}.md"
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
        # Canonical ID is URL-hash for all new writes.
        # Existing DB rows/files are intentionally not auto-migrated.
        data_dict['page_id'] = self.url_to_hash(data_dict['url'])
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
        self.save_markdown_file(metadata.to_dict(), raw_response['markdown'])
        self.logger.info("process_response completed", extra={"page_id": data_dict.get('page_id'), "url": data_dict.get('url')})
        return metadata
    
    
