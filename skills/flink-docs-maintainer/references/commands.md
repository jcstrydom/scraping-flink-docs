# Commands

## Compile

```bash
uv run python -m py_compile firecrawl_scraper/models/*.py firecrawl_scraper/example-scrape_with_orchestrator.py scripts/single_use_scripts/*.py scripts/single_use_scripts/initial_exploration_scripts/*.py tests/*.py
```

## Tests

```bash
uv run --with pytest python -m pytest -q tests
```

## Useful search

```bash
rg -n "page_id|data/scraping.db|data/markdown_files|firecrawl_scraper"
```
