# Flink Docs Scraper

Scraper/orchestrator project for Apache Flink docs, built around Firecrawl + SQLAlchemy.

It provides:
- Structured page scraping via `ScrapingOrchestrator`
- Persistent metadata in SQLite (`data/scraping.db`)
- Markdown storage (`data/markdown_files/`)
- URL deduplication and traversal queueing
- Optional metadata enrichment (`slug`, `summary`, `headings`) via Ollama/Gemini fallback logic in `ResponseProcessor`

## Project Walk-Through

### 1. Core flow
1. `ScrapingOrchestrator.scrape_and_persist(url)` normalizes and scope-checks the URL.
2. It skips URLs already in `scraped_urls`.
3. It calls Firecrawl to fetch markdown.
4. `ResponseProcessor` parses metadata + child links and writes markdown to disk.
5. `DatabaseManager.save_page_metadata()` upserts the `pages` row.
6. Child links can be queued and processed in batches.

### 2. Traversal model
- Queue type: FIFO (`deque`)
- Add URLs with `add_urls_to_queue()`
- Process with `scrape_batch(max_urls=...)`
- Or start from root with `scrape_from_root(max_depth=...)`
- Deduplication is in-memory for current run; existing URLs can be loaded from DB at startup (`load_existing_urls=True`)

### 3. Storage model
- DB file: `data/scraping.db`
- Markdown files: `data/markdown_files/{prefix}_{page_id}.md`
- ORM table: `pages` (`PageRecord`)

`page_id` note:
- New writes use SHA-256 of the canonical URL as `page_id`.
- Existing rows/files are intentionally not auto-migrated.
- Filenames keep a human-readable prefix: `{prefix}_{page_id}.md`.

Important `pages` columns:
- `page_id`, `url`, `title`, `version`, `prefix`
- `slug`, `summary`, `headings`
- `child_urls`, `parent_url`, `is_root_url`
- `scrape_timestamp`, `content_hash`

### 4. Data quality helpers
`DatabaseManager` includes heading cleanup utilities for existing data:
- `clean_headings_text_links()` cleans link markup/URLs out of `headings[*].text`

Use:

```python
from firecrawl_scraper.models import DatabaseManager

result = DatabaseManager().clean_headings_text_links()
print(result)
```

## Repository Layout

```text
.
├── README.md
├── documentation/
│   ├── QUICKSTART.md
│   ├── ORCHESTRATOR_GUIDE.md
│   └── VISUAL_GUIDE.md
├── notebooks/
│   ├── dev-notebook.ipynb
│   └── example-orchestrator.ipynb
├── scripts/
│   └── single_use_scripts/
├── data/
│   ├── scraping.db
│   └── markdown_files/
├── firecrawl_scraper/
│   ├── models/
│   │   ├── __init__.py
│   │   ├── orchestrator.py
│   │   ├── database.py
│   │   ├── processdata.py
│   │   └── metadata.py
│   └── example-scrape_with_orchestrator.py
└── pyproject.toml
```

## Setup

### Prereqs
- Python `>=3.13` (per `pyproject.toml`)
- Firecrawl API key
- Optional: local Ollama and model if you want summary/slug/headings enrichment

### Install

```bash
uv sync
```

### Environment
Create `.env` in repo root:

```bash
FIRECRAWL_API_KEY=your_key_here
# Optional for Gemini fallback:
# GOOGLE_GEMINI_API_KEY=...
```

## Quick Usage

```python
from firecrawl_scraper.models import ScrapingOrchestrator
import os

orch = ScrapingOrchestrator(
    firecrawl_api_key=os.getenv("FIRECRAWL_API_KEY"),
    root_url="https://nightlies.apache.org/flink/flink-docs-release-1.20/docs/concepts/overview/",
    ask_ollama=False,
)

metadata = orch.scrape_and_persist(orch.root_url)
if metadata and metadata.child_urls:
    orch.add_urls_to_queue(metadata.child_urls)

stats = orch.scrape_batch(max_urls=5)
print(stats)
```

Run the bundled example:

```bash
uv run python firecrawl_scraper/example-scrape_with_orchestrator.py
```

## Runtime APIs

Main class: `firecrawl_scraper/models/orchestrator.py`
- `scrape_and_persist(url)`
- `add_urls_to_queue(urls)`
- `scrape_batch(max_urls=None, stop_on_failure=False)`
- `scrape_from_root(max_depth=None)`
- `has_been_scraped(url)`
- `get_scraping_stats()`
- `to_dict(include_queue=False, queue_preview=20)`

DB class: `firecrawl_scraper/models/database.py`
- `save_page_metadata(metadata_dict)`
- `update_page_fields_by_page_id(page_id, update_fields)`
- `get_all_pages()` / `get_page_by_url(url)` / `url_exists(url)`
- `get_pages_by_version(version)` / `get_unprocessed_pages()`
- `clean_headings_text_links()`

## Documentation Map
- `documentation/QUICKSTART.md`: shortest path to run the project
- `documentation/ORCHESTRATOR_GUIDE.md`: method-by-method API behavior and examples
- `documentation/VISUAL_GUIDE.md`: architecture and flow diagrams
- `documentation/MAINTAINER_CONTEXT.md`: key invariants, paths, and validation commands for future sessions

## Notes
- Scraping scope defaults to the root host and `/docs/` path unless overridden with `allowed_domain` or `allow_outside_domain=True`.
- Re-running with the same DB path resumes naturally because previously scraped URLs are loaded on init by default.

## Naive KG-First RAG (Docs-Oriented)
Initial implementation lives in `flink_rag/` and builds a lightweight docs graph plus chunk index from scraped pages.

Build artifacts:

```bash
uv run python -m flink_rag.build --max-pages 30
```

Query with KG-first retrieval (nodes -> 1-hop expansion -> chunk evidence):

```bash
uv run python -m flink_rag.query "Which config options affect checkpoint latency?"
```

Artifact output path:
- `data/rag/naive_kg_rag.json`

## UI Package (Backend-Swappable)
Interactive UI lives in `rag_ui/` as a separate package.

Architecture:
- UI/API layer depends only on `RAGBackend` protocol (`rag_ui/backend.py`).
- Current backend is an adapter (`rag_ui/adapters.py`) over `NaiveKGRAGEngine`.
- You can replace the backend adapter without changing UI code.

Run:

```bash
uv run uvicorn rag_ui.main:app --reload --port 8000
```

Open:
- `http://127.0.0.1:8000`

Extra guide:
- `documentation/UI_QUICKSTART.md`

## Status
- Current docs are consolidated around the orchestrator + DB workflow in this README.
