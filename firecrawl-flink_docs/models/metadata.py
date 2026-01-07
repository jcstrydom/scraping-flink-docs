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
    normalized = urllib.parse.urlunsplit((scheme, netloc, path.rstrip("/"), parts.query, ""))
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
    previous_url: Optional[HttpUrl] = None
    is_root_url: bool = False
    next_urls: List[Tuple[str, str]] = Field(default_factory=list)
    scrape_timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    # normalize URL-like fields before validation/parsing
    @field_validator("url", mode="before")
    def _norm_url_field(cls, v):
        return _normalize_url(v)

    @field_validator("previous_url", mode="before")
    def _norm_previous_url_field(cls, v):
        return _normalize_url(v)

    @field_validator("next_urls", mode="before")
    def _norm_next_urls(cls, v):
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