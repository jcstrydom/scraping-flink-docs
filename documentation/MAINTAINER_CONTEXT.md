# Maintainer Context

## Current Project Shape
- Scraper package: `firecrawl_scraper/`
- Shared data root (scraper + future RAG): `data/`
- Utility/one-off scripts: `scripts/single_use_scripts/`
- Notebooks: `notebooks/`
- Automated tests: `tests/`

## Key Decisions (Do Not Regress)
- `page_id` for new writes is SHA-256 of canonical URL, not prefix hash.
- Existing DB rows/files are intentionally **not auto-migrated**.
- Markdown filename format stays human-readable: `{prefix}_{page_id}.md`.
- Default persistence paths:
  - DB: `data/scraping.db`
  - Markdown: `data/markdown_files/`

## Important Modules
- Orchestration: `firecrawl_scraper/models/orchestrator.py`
- Processing: `firecrawl_scraper/models/processdata.py`
- Metadata enrichment: `firecrawl_scraper/models/metadata_enricher.py`
- DB layer: `firecrawl_scraper/models/database.py`
- URL normalization utilities: `firecrawl_scraper/models/url_utils.py`

## Fast Validation Commands
- Compile check:
  - `uv run python -m py_compile firecrawl_scraper/models/*.py firecrawl_scraper/example-scrape_with_orchestrator.py scripts/single_use_scripts/*.py scripts/single_use_scripts/initial_exploration_scripts/*.py tests/*.py`
- Tests:
  - `uv run --with pytest python -m pytest -q tests`

## Test Scope Note
- Run tests from `tests/` only.
- `scripts/single_use_scripts/test_*.py` are utility scripts, not CI tests.

## Next Workstream
- Add RAG as a separate sibling package (for example `flink_rag/`) using the same root `data/` hierarchy.
