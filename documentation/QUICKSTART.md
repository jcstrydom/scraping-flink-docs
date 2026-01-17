# Quick Start Guide: ScrapingOrchestrator

## 30-Second Setup

```python
from models import ScrapingOrchestrator
import os

# Initialize
orch = ScrapingOrchestrator(
    firecrawl_api_key=os.getenv('FIRECRAWL_API_KEY'),
    root_url='https://example.com/docs/',
    ask_ollama=False
)

# Scrape a URL (saves to DB + markdown file)
metadata = orch.scrape_and_persist('https://example.com/docs/page1')

# Add child URLs to queue
if metadata and metadata.child_urls:
    orch.add_urls_to_queue(metadata.child_urls)

# Scrape batch from queue
stats = orch.scrape_batch(max_urls=5)
print(f"Scraped {stats['scraped']} pages")
```

## Three Main Use Cases

### Use Case 1: Single URL Scrape
```python
metadata = orch.scrape_and_persist(url)
# ✅ Fetches page
# ✅ Saves markdown file to ./data/markdown_files/
# ✅ Saves metadata to ./data/scraping.db
# ✅ Returns PageMetadata object
```

### Use Case 2: Prevent Re-scraping
```python
if not orch.has_been_scraped(url):
    orch.scrape_and_persist(url)
# Checks both in-memory cache and database
# Smart URL normalization handles URL variations
```

### Use Case 3: Traverse and Queue
```python
root = orch.scrape_and_persist(root_url)
if root.child_urls:
    orch.add_urls_to_queue(root.child_urls)

while orch.queue_size() > 0:
    stats = orch.scrape_batch(max_urls=10)
    print(f"Scraped {stats['scraped']}, {stats['queue_remaining']} left")
```

## Database Location

SQLite database: `./data/scraping.db`

Query with Python:
```python
# Get all scraped pages
pages = orch.db_manager.get_all_pages()
for p in pages:
    print(p.title, p.url)

# Get pages by version
pages = orch.db_manager.get_pages_by_version('flink-docs-release-1.20')

# Check if URL exists
exists = orch.db_manager.url_exists('https://example.com/page')
```

## Common Patterns

### Pattern 1: Resume Scraping (Session Persistence)
```python
# Session 1: Scrape and stop
orch = ScrapingOrchestrator(api_key, root_url)
orch.scrape_batch(max_urls=5)  # Saves to DB

# Session 2: Resume later
orch = ScrapingOrchestrator(api_key, root_url)  # Loads from DB
stats = orch.get_scraping_stats()
print(f"Previously scraped {stats['total_scraped_urls']} URLs")
orch.scrape_batch(max_urls=5)  # Continue
```

### Pattern 2: Avoid API Quota Limits
```python
# Scrape in small batches to avoid quota
for i in range(100):
    stats = orch.scrape_batch(max_urls=2)
    if stats['failed'] > 0:
        print(f"Errors detected, pausing...")
        break
```

### Pattern 3: Full Site Traversal
```python
# Traverse up to 3 levels deep
stats = orch.scrape_from_root(max_depth=3)
print(f"Total: {stats['total_scraped']} pages")
```

### Pattern 4: Selective Scraping
```python
# Only scrape certain URL patterns
for text, url in some_urls:
    # Skip URLs matching pattern
    if '/api/' not in url:
        orch.add_urls_to_queue([(text, url)])

stats = orch.scrape_batch()
```

## Monitoring Progress

```python
# Quick stats
stats = orch.get_scraping_stats()
print(f"📊 Progress:")
print(f"   Scraped: {stats['total_scraped_urls']}")
print(f"   Failed: {stats['failed_urls']}")
print(f"   Pending: {stats['queue_pending']}")
print(f"   DB Location: {stats['database_location']}")

# Queue size
print(f"Queue: {orch.queue_size()} URLs remaining")

# Failed URLs
print(f"Failed URLs: {orch.failed_urls}")
```

## Troubleshooting

### Problem: "URL already scraped, skipping"
→ This is normal behavior. The system prevents duplicate scrapes.

### Problem: Database locked
→ Make sure `./data/` is writable and you're not running multiple instances

### Problem: Ollama timeout
→ Set `ask_ollama=False` when initializing orchestrator

### Problem: API rate limit
→ Use smaller `max_urls` values in `scrape_batch()`

## What Gets Saved

### Files
- **Markdown files**: `./data/markdown_files/{prefix}_{page_id}.md`
- **Database**: `./data/scraping.db`

### Database Columns
| Column | Purpose |
|--------|---------|
| `page_id` | SHA256 hash of URL (unique ID) |
| `url` | Full normalized URL |
| `title` | Page title from metadata |
| `version` | Flink version |
| `child_urls` | JSON list of (text, url) tuples |
| `is_root_url` | Boolean |
| `scrape_timestamp` | When page was scraped |

## API Cheat Sheet

```python
# Initialization
orch = ScrapingOrchestrator(firecrawl_api_key, root_url)

# Scraping
metadata = orch.scrape_and_persist(url)           # Single URL
stats = orch.scrape_batch(max_urls=5)             # Batch from queue
stats = orch.scrape_from_root(max_depth=2)        # Full traversal

# Queue Management
orch.add_urls_to_queue([(text, url), ...])        # Add URLs
next_url = orch.get_next_url()                    # Get next
orch.queue_size()                                 # Queue length

# Deduplication
orch.has_been_scraped(url)                        # Check if done

# Database Queries
pages = orch.db_manager.get_all_pages()           # All pages
pages = orch.db_manager.get_pages_by_version(v)   # Filter by version
page = orch.db_manager.get_page_by_url(url)       # Get one page

# Statistics
stats = orch.get_scraping_stats()                 # Overview
```

## Examples in the Repo

1. **Notebook**: `dev-notebook.ipynb` - 6 complete examples
2. **Script**: `scrape_with_orchestrator.py` - Production-ready example
3. **Full Guide**: `ORCHESTRATOR_GUIDE.md` - Detailed documentation

## Questions?

Check `ORCHESTRATOR_GUIDE.md` for:
- Detailed method signatures
- Workflow diagrams
- Best practices
- Advanced features
