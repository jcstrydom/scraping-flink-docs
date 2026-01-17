

# 📚 Flink Docs Scraper

A comprehensive scraper for Apache Flink documentation that combines web scraping with intelligent data persistence. Features include automatic URL deduplication, SQLite database storage, batch processing, and session resumption. Built with Firecrawl and SQLAlchemy for robust, production-ready documentation harvesting.

## **INDEX**

## 🚀 Start Here

**New to this project?** Start with these in order:

1. **[QUICKSTART.md](documentation/QUICKSTART.md)** ⭐ (5 min read)
   - 30-second setup
   - Three main use cases
   - Common patterns
   - API cheat sheet

2. **[WHAT_WAS_ADDED.md](documentation/WHAT_WAS_ADDED.md)** (10 min read)
   - What functionality was added
   - Requirements checklist
   - File structure
   - Benefits summary

3. **[VISUAL_GUIDE.md](documentation/VISUAL_GUIDE.md)** (15 min read)
   - Architecture diagrams
   - Data flow sequences
   - Queue visualization
   - Performance characteristics

## 📖 Deep Dives

**Want to understand everything?** Read these for details:

- **[ORCHESTRATOR_GUIDE.md](documentation/ORCHESTRATOR_GUIDE.md)** - Complete API Reference
  - All methods documented
  - Parameter explanations
  - Return values
  - Code examples
  - Database schema
  - Workflow examples
  - Troubleshooting

- **[IMPLEMENTATION_SUMMARY.md](documentation/IMPLEMENTATION_SUMMARY.md)** - Technical Overview
  - Architecture explanation
  - Component breakdown
  - Dependencies added
  - Next steps

## 💻 Hands-On

**Want to try it?** Use these:

1. **[dev-notebook.ipynb](firecrawl_flink_docs/dev-notebook.ipynb)**
   - 6 interactive examples
   - Cell-by-cell walkthrough
   - Test in Jupyter

2. **[scrape_with_orchestrator.py](firecrawl_flink_docs/scrape_with_orchestrator.py)**
   - Production-ready script
   - Run with: `python scrape_with_orchestrator.py`
   - Demonstrates best practices

## 🎯 By Use Case

### "I want to scrape one URL"
→ [QUICKSTART.md - Use Case 1](firecrawl_flink_docs/QUICKSTART.md#use-case-1-single-url-scrape)

### "I want to avoid re-scraping"
→ [QUICKSTART.md - Use Case 2](firecrawl_flink_docs/QUICKSTART.md#use-case-2-prevent-re-scraping)

### "I want to traverse all child pages"
→ [QUICKSTART.md - Use Case 3](firecrawl_flink_docs/QUICKSTART.md#use-case-3-traverse-and-queue)

### "I want to resume scraping later"
→ [QUICKSTART.md - Pattern 1](firecrawl_flink_docs/QUICKSTART.md#pattern-1-resume-scraping-session-persistence)

### "I want to avoid API limits"
→ [QUICKSTART.md - Pattern 2](firecrawl_flink_docs/QUICKSTART.md#pattern-2-avoid-api-quota-limits)

### "I want to traverse a whole site"
→ [QUICKSTART.md - Pattern 3](firecrawl_flink_docs/QUICKSTART.md#pattern-3-full-site-traversal)

### "I want to query saved data"
→ [ORCHESTRATOR_GUIDE.md - DatabaseManager](firecrawl_flink_docs/ORCHESTRATOR_GUIDE.md#databasemanager)

### "I want to understand the architecture"
→ [VISUAL_GUIDE.md](firecrawl_flink_docs/VISUAL_GUIDE.md)

## 🔍 API Reference

| Class | Methods | Location |
|-------|---------|----------|
| **ScrapingOrchestrator** | `scrape_and_persist()`, `has_been_scraped()`, `add_urls_to_queue()`, `scrape_batch()`, `scrape_from_root()`, `get_scraping_stats()` | [models/orchestrator.py](firecrawl_flink_docs/models/orchestrator.py) |
| **DatabaseManager** | `url_exists()`, `get_page_by_url()`, `save_page_metadata()`, `get_all_pages()`, `get_pages_by_version()` | [models/database.py](firecrawl_flink_docs/models/database.py) |
| **PageRecord** | ORM model for database | [models/database.py](firecrawl_flink_docs/models/database.py) |
| **PageMetadata** | Data model (pydantic) | [models/metadata.py](firecrawl_flink_docs/models/metadata.py) |

## 📊 What Was Implemented

✅ **Persistence**: SQLite database + markdown files  
✅ **Traversal**: FIFO queue with depth control  
✅ **Deduplication**: Smart URL tracking with normalization  

For details: [WHAT_WAS_ADDED.md](documentation/WHAT_WAS_ADDED.md)

## 🗂️ File Structure

```
scraping-flink-docs/
├── documentation/
│   ├── 📄 QUICKSTART.md                    ← START HERE
│   ├── 📄 WHAT_WAS_ADDED.md
│   ├── 📄 VISUAL_GUIDE.md
│   ├── 📄 ORCHESTRATOR_GUIDE.md
│   ├── 📄 IMPLEMENTATION_SUMMARY.md
│
├── firecrawl_flink_docs/
│   ├── models/
│   │   ├── __init__.py                 (updated)
│   │   ├── metadata.py                 (existing)
│   │   ├── processdata.py              (existing)
│   │   ├── database.py                 (NEW)
│   │   └── orchestrator.py             (NEW)
│   │
│   ├── data/
│   │   ├── scraping.db                 (auto-created)
│   │   └── markdown_files/             (auto-created)
│   │
│   ├── dev-notebook.ipynb              (updated with examples)
│   └── scrape_with_orchestrator.py     (NEW - example script)
│
├── 📄 README.md
├── pyproject.toml                      (updated - added sqlalchemy)
└── scrapy-flink_docs/                  (existing)
```

## ⚡ Quick Reference

### Initialize
```python
from models import ScrapingOrchestrator
orch = ScrapingOrchestrator(api_key, root_url)
```

### Scrape
```python
metadata = orch.scrape_and_persist(url)  # Single URL
stats = orch.scrape_batch(max_urls=5)    # Batch
stats = orch.scrape_from_root(max_depth=2)  # Full traversal
```

### Queue
```python
orch.add_urls_to_queue(urls)             # Add to queue
orch.queue_size()                        # Check size
orch.get_next_url()                      # Get next
```

### Check
```python
orch.has_been_scraped(url)               # Was it scraped?
orch.get_scraping_stats()                # Overall stats
```

### Database
```python
pages = orch.db_manager.get_all_pages()  # All pages
page = orch.db_manager.get_page_by_url(url)  # One page
orch.db_manager.url_exists(url)          # Check existence
```

## 🎓 Learning Path

**Beginner (15 min)**
1. Read [QUICKSTART.md](documentation/QUICKSTART.md)
2. Look at [dev-notebook.ipynb](firecrawl_flink_docs/dev-notebook.ipynb) cells 1-3
3. Try one example in Python

**Intermediate (45 min)**
1. Read [WHAT_WAS_ADDED.md](documentation/WHAT_WAS_ADDED.md)
2. Work through [dev-notebook.ipynb](firecrawl_flink_docs/dev-notebook.ipynb) all cells
3. Run [scrape_with_orchestrator.py](firecrawl_flink_docs/scrape_with_orchestrator.py)
4. Read [VISUAL_GUIDE.md](documentation/VISUAL_GUIDE.md)

**Advanced (2 hours)**
1. Read [ORCHESTRATOR_GUIDE.md](documentation/ORCHESTRATOR_GUIDE.md) completely
2. Read source code: [models/orchestrator.py](firecrawl_flink_docs/models/orchestrator.py)
3. Read source code: [models/database.py](firecrawl_flink_docs/models/database.py)
4. Customize for your needs

## 🚨 Common Issues & Solutions

| Issue | Solution | Reference |
|-------|----------|-----------|
| "URL already scraped" | This is expected! Deduplication working. | [QUICKSTART.md](documentation/QUICKSTART.md#troubleshooting) |
| Database errors | Make sure `./data/` is writable | [ORCHESTRATOR_GUIDE.md](documentation/ORCHESTRATOR_GUIDE.md#troubleshooting) |
| API quota exceeded | Use smaller `max_urls` values | [QUICKSTART.md](documentation/QUICKSTART.md#pattern-2-avoid-api-quota-limits) |
| Ollama timeout | Set `ask_ollama=False` | [ORCHESTRATOR_GUIDE.md](documentation/ORCHESTRATOR_GUIDE.md#troubleshooting) |

## 📝 Examples

### Example 1: Basic Usage (1 min)
```python
from models import ScrapingOrchestrator
import os

orch = ScrapingOrchestrator(
    firecrawl_api_key=os.getenv('FIRECRAWL_API_KEY'),
    root_url='https://example.com/docs/',
)

# Scrape and save
metadata = orch.scrape_and_persist('https://example.com/docs/page1')
print(f"Saved: {metadata.title}")
```

### Example 2: Full Traversal (5 min)
```python
# Queue child URLs
if metadata.child_urls:
    orch.add_urls_to_queue(metadata.child_urls)

# Process batch
stats = orch.scrape_batch(max_urls=5)
print(f"Scraped: {stats['scraped']}, Failed: {stats['failed']}")
```

### Example 3: Resume (1 min)
```python
# Load existing database
orch = ScrapingOrchestrator(api_key, root_url)

# Check what's done
stats = orch.get_scraping_stats()
print(f"Already have {stats['total_scraped_urls']} pages")

# Continue scraping
orch.scrape_batch(max_urls=5)
```

For more: [QUICKSTART.md](documentation/QUICKSTART.md) or [ORCHESTRATOR_GUIDE.md](documentation/ORCHESTRATOR_GUIDE.md)

## 💡 Pro Tips

1. **Session Persistence**: Database survives between Python sessions!
2. **Smart Deduplication**: URLs normalized for variations (/, #, case)
3. **Auto Discovery**: Child URLs automatically added to queue
4. **Error Resilient**: Failures logged separately, scraping continues
5. **Queryable**: Full database of scraped content, searchable by version

## 🔗 Dependencies

- `firecrawl` - Web scraping
- `pydantic` - Data validation
- `sqlalchemy` - Database ORM ← **NEW**
- `beautifulsoup4` - HTML parsing
- `scrapy` - Scraping framework

## ❓ FAQ

**Q: Does it work with existing data?**  
A: Yes! Database loads existing URLs on init. Zero duplication.

**Q: Can I pause and resume?**  
A: Yes! Database persists everything. Just create new orchestrator.

**Q: Does it handle errors?**  
A: Yes! Failed URLs tracked separately. Scraping continues.

**Q: Can I query saved pages?**  
A: Yes! Full SQL database with timestamps, versions, etc.

**Q: Does it support multiple versions?**  
A: Yes! Filter by version with `get_pages_by_version()`

**Q: What if I run out of API quota?**  
A: Use small `max_urls` values. Database tracks progress.

## 📞 Next Steps

1. **Try it**: Run [QUICKSTART.md](documentation/QUICKSTART.md) example
2. **Explore**: Open [dev-notebook.ipynb](firecrawl_flink_docs/dev-notebook.ipynb)
3. **Understand**: Read [VISUAL_GUIDE.md](documentation/VISUAL_GUIDE.md)
4. **Deep dive**: Study [ORCHESTRATOR_GUIDE.md](documentation/ORCHESTRATOR_GUIDE.md)
5. **Deploy**: Adapt [scrape_with_orchestrator.py](firecrawl_flink_docs/scrape_with_orchestrator.py)

---

**Last Updated**: January 2026  
**Status**: ✅ Complete & Ready to Use  
**Test Coverage**: Examples in notebook and script
