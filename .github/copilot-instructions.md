# Copilot / AI assistant instructions for this repository

This file contains concise, actionable guidance to help an AI coding assistant be productive in the `flink-docs` scraper project.

## High level overview
- Purpose: scrape and persist Apache Flink documentation using `firecrawl`, normalize pages and store metadata + markdown files.
- Main runtime pieces:
  - `ScrapingOrchestrator` (firecrawl_flink_docs/models/orchestrator.py): coordinates scraping, queueing, deduplication, and persistence.
  - `ResponseProcessor` (firecrawl_flink_docs/models/processdata.py): normalizes URLs, extracts child links, computes `prefix`/`page_id`, optionally calls Ollama for summaries, and saves markdown to disk.
  - `DatabaseManager` (firecrawl_flink_docs/models/database.py): SQLite via SQLAlchemy; `PageRecord` is the ORM mapping.

## How to run (developer workflows)
- Install runtime dependencies listed in `pyproject.toml` (Python >=3.13). Primary libs: `firecrawl`, `sqlalchemy`, `pydantic`, `beautifulsoup4`, `scrapy`.
- Example run (recommended):
  - Create a `.env` with `FIRECRAWL_API_KEY` or export env var.
  - Run the example orchestrator:

```bash
python firecrawl_flink_docs/example-scrape_with_orchestrator.py
```

- Quick Firecrawl CLI examples are in `firecrawl_flink_docs/run-crawling.py` and `run-scraping.py` (direct HTTP example).
- Database location: default is `firecrawl_flink_docs/data/scraping.db`. Markdown files are written to `firecrawl_flink_docs/data/markdown_files/`.

## Project-specific conventions and patterns
- URL canonicalization: use `_normalize_url()` in `processdata.py` and the Pydantic `_normalize_url` in `metadata.py` — always normalize URLs before comparing or storing.
- `page_id`: computed as sha256 hex of canonical URL when missing (see `PageMetadata._compute_page_id`). Avoid creating alternative ID schemes.
- `prefix` and `version`: `ResponseProcessor.extract_prefix()` and `extract_version()` parse Flink-specific paths (nightlies.apache.org/flink/.../docs/). Use these helpers when deriving filenames or version tags.
- Markdown link extraction: `ResponseProcessor.extract_markdown_links()` returns list of `(text, normalized_url)` tuples, deduplicated and with fragments removed — use that format when adding to queues or saving to DB.
- DB upsert semantics: `DatabaseManager.save_page_metadata()` updates by `page_id` if it exists; callers should pass `PageMetadata.to_dict()`.
- Allowed-scope behavior: `ScrapingOrchestrator` infers `allowed_domain` from `root_url` (defaults to `.../docs/`). `allow_outside_domain` toggles scope enforcement. Respect this logic when adding URLs to queue.

## Integration points & external dependencies
- Firecrawl: used for scraping. API key required in `FIRECRAWL_API_KEY` env var or `.env`.
- Ollama (optional): `ResponseProcessor.extract_summaries_with_ollama()` posts to `http://localhost:11434` by default. If Ollama is down the extractor returns empty `slug/summary/headings` — do not fail the pipeline.
- SQLite: small local DB via SQLAlchemy. `DatabaseManager` creates DB and tables on init.

## Files to consult for implementation reference
- Runtime entrypoints: `firecrawl_flink_docs/example-scrape_with_orchestrator.py`, `firecrawl_flink_docs/run-crawling.py`.
- Main logic: `firecrawl_flink_docs/models/orchestrator.py`, `firecrawl_flink_docs/models/processdata.py`, `firecrawl_flink_docs/models/database.py`, `firecrawl_flink_docs/models/metadata.py`.
- Documentation and guides: `documentation/QUICKSTART.md`, `documentation/ORCHESTRATOR_GUIDE.md`, `documentation/VISUAL_GUIDE.md`.

## Quick coding hints for the assistant
- Keep URL normalization consistent: call `_normalize_url()` before any equality checks or DB lookups.
- When editing or extending the DB schema, update `Base.metadata.create_all(self.engine)` usage and migrate existing data manually — there are no migrations in repo.
- For adding debug logging, follow the existing pattern: attach a StreamHandler only when `logger.handlers` is empty to avoid duplicate logs.
- When adding features that call Ollama, provide a safe fallback (empty strings) when the host is unreachable.
- Tests: none provided. Add small runnable examples (or notebooks) rather than complex test harnesses.

## Example snippets to reuse
- Instantiate orchestrator:
```python
from models import ScrapingOrchestrator
orch = ScrapingOrchestrator(
    firecrawl_api_key=FIRECRAWL_API_KEY,
    root_url='https://nightlies.apache.org/flink/flink-docs-release-1.20/docs/concepts/overview/',
    ask_ollama=False
)
```

## Final notes
- Keep changes minimal and consistent with existing patterns (URL normalization, Pydantic validation, DB upsert-by-page_id).
- If you need to run anything locally, mention the required `FIRECRAWL_API_KEY` and where the DB/markdown output will appear.

Please review — tell me if you want this split into a longer `AGENTS.md` or more examples for testing. 
