# Quick Start Guide

## 1) Install + Env

```bash
uv sync
```

Create `.env` in repo root:

```bash
FIRECRAWL_API_KEY=your_key_here
# Optional for Gemini fallback:
# GOOGLE_GEMINI_API_KEY=...
```

## 2) Minimal Usage

```python
from firecrawl_flink_docs.models import ScrapingOrchestrator
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

## 3) Run Example Script

```bash
uv run python firecrawl_flink_docs/example-scrape_with_orchestrator.py
```

## 4) Common Patterns

### Resume across sessions

```python
orch = ScrapingOrchestrator(api_key, root_url)
print(orch.get_scraping_stats())
```

The orchestrator loads already-scraped URLs from DB by default.

### Full traversal from root

```python
stats = orch.scrape_from_root(max_depth=3)
print(stats)
```

### Keep scraping in small batches

```python
while orch.queue_size() > 0:
    stats = orch.scrape_batch(max_urls=10)
    print(stats)
```

## 5) Where data is saved

- SQLite DB: `firecrawl_flink_docs/data/scraping.db`
- Markdown files: `firecrawl_flink_docs/data/markdown_files/`

## 6) Useful DB calls

```python
pages = orch.db_manager.get_all_pages()
page = orch.db_manager.get_page_by_url("https://example.com")
exists = orch.db_manager.url_exists("https://example.com")
```

## 7) Clean existing heading text in DB

```python
result = orch.db_manager.clean_headings_text_links()
print(result)
```

This removes markdown links and raw URLs from `headings[*].text`.

## Troubleshooting

### "URL already scraped, skipping"
Expected deduplication behavior.

### API quota/rate pressure
Use lower `max_urls` in `scrape_batch()`.

### Ollama unavailable
Initialize with `ask_ollama=False`.
