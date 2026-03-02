# ScrapingOrchestrator Guide

## Overview

`ScrapingOrchestrator` coordinates scraping, parsing, persistence, deduplication, and queue traversal.

Primary modules:
- `firecrawl_scraper/models/orchestrator.py`
- `firecrawl_scraper/models/database.py`
- `firecrawl_scraper/models/processdata.py`
- `firecrawl_scraper/models/metadata.py`

## Constructor

```python
ScrapingOrchestrator(
    firecrawl_api_key: str,
    root_url: str,
    db_path: str | None = None,
    log_level: int = logging.INFO,
    ask_ollama: bool = True,
    load_existing_urls: bool = True,
    allowed_domain: str | None = None,
    allow_outside_domain: bool = False,
)
```

Notes:
- If `db_path` is not set, default DB is `data/scraping.db`.
- Scope defaults to same host as `root_url` under `/docs/` path.
- `load_existing_urls=True` seeds in-memory dedupe from DB on startup.

## ScrapingOrchestrator Methods

### `scrape_and_persist(url) -> Optional[PageMetadata]`
Scrapes one URL, writes markdown, upserts DB row, returns `PageMetadata`.
Returns `None` for already-scraped, out-of-scope, or failed URLs.

### `has_been_scraped(url) -> bool`
Checks normalized URL membership in `self.scraped_urls`.

### `add_urls_to_queue(urls: list[tuple[str, str]]) -> None`
Adds `(link_text, link_url)` entries to queue if not scraped and in allowed scope.

### `get_next_url() -> Optional[tuple[str, str]]`
Pops next queue item (FIFO).

### `queue_size() -> int`
Returns queue length.

### `scrape_batch(max_urls=None, stop_on_failure=False) -> dict`
Processes queue items up to limit.
Returns:
- `scraped`
- `failed`
- `skipped`
- `queue_remaining`
- `total_scraped_session`

### `scrape_from_root(max_depth=None) -> dict`
Scrapes root (if needed), then traverses queued child URLs breadth-first by queue batches.
Returns:
- `total_scraped`
- `total_failed`
- `total_skipped`
- `depth_levels`

### `get_scraping_stats() -> dict`
Returns:
- `root_url`
- `total_scraped_urls`
- `failed_urls`
- `queue_pending`
- `database_pages`

### `to_dict(include_queue=False, queue_preview=20) -> dict`
Returns a serializable runtime snapshot, including config/scope fields and optional queue preview.

## DatabaseManager Methods

### Write/update
- `save_page_metadata(metadata_dict)`
- `update_page_fields_by_page_id(page_id, update_fields)`

### Reads
- `url_exists(url)`
- `get_page_by_url(url)`
- `get_all_pages()`
- `get_pages_by_version(version)`
- `get_unprocessed_pages()`

### Data cleanup
- `clean_headings_text_links()`
  - Cleans markdown links and raw URLs from `headings[*].text`
  - Commits updates in place
  - Returns counters: `processed_rows`, `updated_rows`, `updated_headings`

## Data Schema (`pages`)

- `page_id` (PK)
- `url` (unique)
- `title`
- `version`
- `prefix`
- `slug`
- `summary`
- `parent_url`
- `is_root_url`
- `headings` (JSON)
- `child_urls` (JSON)
- `scrape_timestamp`
- `content_hash`

## End-to-End Example

```python
from firecrawl_scraper.models import ScrapingOrchestrator
import os

orch = ScrapingOrchestrator(
    firecrawl_api_key=os.getenv("FIRECRAWL_API_KEY"),
    root_url="https://nightlies.apache.org/flink/flink-docs-release-1.20/docs/concepts/overview/",
    ask_ollama=False,
)

root = orch.scrape_and_persist(orch.root_url)
if root and root.child_urls:
    orch.add_urls_to_queue(root.child_urls)

while orch.queue_size() > 0:
    print(orch.scrape_batch(max_urls=10))

print(orch.get_scraping_stats())
```

## Scope Control Example

```python
orch = ScrapingOrchestrator(
    firecrawl_api_key=api_key,
    root_url=root_url,
    allowed_domain="nightlies.apache.org/flink/flink-docs-release-1.20/docs/",
    allow_outside_domain=False,
)
```

## Operational Notes

- For resumable runs, keep the same DB path.
- For faster iterative runs, use `scrape_batch(max_urls=...)` instead of unbounded traversal.
- If metadata enrichment is not needed, set `ask_ollama=False`.
