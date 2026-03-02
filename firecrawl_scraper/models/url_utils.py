"""
Shared URL normalization helpers for page identity and deduplication.
"""

from __future__ import annotations

from typing import Optional
import urllib.parse


def normalize_url(raw: Optional[str]) -> Optional[str]:
    if raw is None:
        return None

    parts = urllib.parse.urlsplit(str(raw))
    scheme = parts.scheme.lower()
    netloc = parts.netloc.lower()

    if (scheme == "http" and netloc.endswith(":80")) or (scheme == "https" and netloc.endswith(":443")):
        netloc = netloc.rsplit(":", 1)[0]

    path = parts.path or "/"
    normalized = urllib.parse.urlunsplit((scheme, netloc, path.rstrip("/"), "", ""))
    return normalized
