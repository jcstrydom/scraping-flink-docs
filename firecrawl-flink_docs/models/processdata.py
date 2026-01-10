import dotenv, os, re, ast
import urllib.parse
import hashlib

from .metadata import PageMetadata


class ResponseProcessor:

    def __init__(self,root_url: str = None):
        if root_url:
            self.root_url = root_url


    def extract_prefix(self, url, remove_start: str = 'https://nightlies.apache.org/', remove_end: str = '/docs/') -> str:
        pattern = re.compile(re.escape(remove_start) + r'.*?' + re.escape(remove_end))
        rest = pattern.sub('', url, 1)
        cleaned = re.sub(r'[^A-Za-z]+', '_', rest).strip('_')
        return re.sub(r'_+', '_', cleaned)
    
    def prefix_to_hash(self, prefix: str, numeric: bool = False):
        h = hashlib.sha256(prefix.encode('utf-8')).hexdigest()
        return int(h[:16], 16) if numeric else h
    
    def _normalize_url(self, url: str) -> str:
        parts = urllib.parse.urlsplit(url)

        # normalize scheme and netloc, remove fragment
        scheme = parts.scheme.lower()
        netloc = parts.netloc.lower()
        if (scheme == 'http' and netloc.endswith(':80')) or (scheme == 'https' and netloc.endswith(':443')):
            netloc = netloc.rsplit(':', 1)[0]

        normalized = urllib.parse.urlunsplit((scheme, netloc, parts.path or '/','',''))
        normalized = normalized.rstrip('/')

        return normalized
    
    
    def extract_markdown_links(self, text):
        """
        Extract unique markdown page links (text, url) from `text`, excluding image links.
        Fragments (anchors) are removed so multiple section links to the same page yield one entry.
        """

        pattern = re.compile(r'(?<!\!)\[(?P<text>[^\]]+)\]\((?P<url>https?://[^\s)]+)\)')
        seen = set()
        ret = []

        for m in pattern.finditer(text):
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

        return ret
    
    def save_markdown_file(self, data: dict, content: str, save_dir: str = './data/markdown_files/'):
        file_name = f"{save_dir}{data.get('prefix')}_{data.get('page_id')}.md"
        with open(file_name, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Saved markdown file: {file_name}")

        
    def parse_raw_response(self, raw_response: str,parent_url: str = None) -> dict:
        data_dict = {}

        data_dict['title'] = raw_response['metadata']['title']
        data_dict['url'] = raw_response['metadata']['url']
        if parent_url:
            data_dict['is_root_url'] = False
        else:
            data_dict['is_root_url'] = True
            self.root_url = data_dict['url']
        data_dict['parent_url'] = parent_url
        
        data_dict['prefix'] = self.extract_prefix(data_dict['url'])
        data_dict['page_id'] = self.prefix_to_hash(data_dict['prefix'])
        data_dict['child_urls'] = self.extract_markdown_links(raw_response['markdown'])

        return data_dict

    def process_response(self, raw_response: dict) -> dict:
        data_dict = self.parse_raw_response(raw_response)
        metadata = PageMetadata.model_validate(data_dict)
        self.save_markdown_file(data_dict, raw_response['markdown'])
        
        return metadata
    