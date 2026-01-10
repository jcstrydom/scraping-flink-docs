from __future__ import annotations
from typing import List, Tuple, Optional
from datetime import datetime, timezone
import hashlib
import urllib.parse

from pydantic import BaseModel, Field, HttpUrl, field_validator, model_validator


def _normalize_url(raw: Optional[str]) -> Optional[str]:
    if raw is None:
        return None
    parts = urllib.parse.urlsplit(str(raw))
    scheme = parts.scheme.lower()
    netloc = parts.netloc.lower()
    if (scheme == "http" and netloc.endswith(":80")) or (scheme == "https" and netloc.endswith(":443")):
        netloc = netloc.rsplit(":", 1)[0]
    path = parts.path or "/"
    # remove fragment and trailing slash
    normalized = urllib.parse.urlunsplit((scheme, netloc, path.rstrip("/"), "", ""))
    return normalized


class PageMetadata(BaseModel):
    """
    Minimal metadata model for a scraped page.
    Fields:
      - page_id: hex sha256 of canonical URL (computed if omitted)
      - title: human title
      - url: canonical page URL
      - previous_url: optional previous page URL
      - is_root_url: whether this is a root/index page
      - next_urls: list of (link_text, link_url) tuples
      - scrape_timestamp: UTC timestamp of scrape
    """

    
    page_id: Optional[str] = Field(None, description="sha256 hex of canonical url")
    title: Optional[str] = None
    url: HttpUrl
    slug: Optional[str] = None
    summary: Optional[str] = None
    headings: Optional[List[dict]] = None
    parent_url: Optional[HttpUrl] = None
    is_root_url: bool = False
    child_urls: List[Tuple[str, str]] = Field(default_factory=list)
    scrape_timestamp: datetime = Field(default_factory=lambda: datetime.now().astimezone().replace(tzinfo=None))

    # normalize URL-like fields before validation/parsing
    @field_validator("url", mode="before")
    def _norm_url_field(cls, v):
        return _normalize_url(v)

    @field_validator("parent_url", mode="before")
    def _norm_parent_url_field(cls, v):
        return _normalize_url(v)
    
    @field_validator('is_root_url', mode="before")
    def _norm_is_root_url_field(cls, v):
        return bool(v)

    @field_validator("child_urls", mode="before")
    def _norm_child_urls(cls, v):
        # Expect a list of (text, url) pairs; normalize URLs and strip fragments
        if not v:
            return []
        normalized = []
        for item in v:
            if not item:
                continue
            text, raw_url = item[0], item[1]
            norm = _normalize_url(raw_url)
            if norm:
                normalized.append((text.strip(), norm))
        # deduplicate preserving order
        seen = set()
        dedup = []
        for t, u in normalized:
            if u in seen:
                continue
            seen.add(u)
            dedup.append((t, u))
        return dedup

    @model_validator(mode="after")
    def _compute_page_id(self):
        if not self.page_id:
            # compute sha256 of canonical url
            h = hashlib.sha256(str(self.url).encode("utf-8")).hexdigest()
            self.page_id = h
        return self

    def to_dict(self, **kwargs):
        # thin wrapper for pydantic model_dump to control output if needed
        return self.model_dump(**kwargs)
    
    def __repr__(self):
        if not self.headings:
            self.headings = []
        if not self.slug:
            self.slug = ""
        if not self.summary:
            self.summary = ""
        return  f"< PageMetadata page_id={self.page_id},\n  url={self.url},\n  title={self.title}," + \
                f"\n  slug={self.slug},\n  summary={self.summary},\n  headings[{len(self.headings)}]=\n  --> " + \
                    f"{'\n  --> '.join([f' {d['level']}: {d['text']}' for d  in self.headings])}," + \
                f"\n  is_root_url={self.is_root_url}," + \
                f"\n  parent_url={self.parent_url}," + \
                f"\n  child_urls[{len(self.child_urls)}]=\n  --> " + \
                    f"{'\n  --> '.join([f' {text} ({url})' for text, url in self.child_urls])}," + \
                f"\n  scrape_timestamp={self.scrape_timestamp} >"
        