# ScrapingOrchestrator Documentation

## Overview

The `ScrapingOrchestrator` class provides a complete framework for managing web scraping workflows with:

- **Database Persistence**: Automatically saves metadata and markdown files
- **URL Deduplication**: Prevents re-scraping of already-processed pages
- **Queue Management**: Intelligent FIFO queue for traversing child URLs
- **Batch Processing**: Scrape single URLs or batches with configurable limits
- **Session Continuity**: Resume scraping from where you left off

## Architecture

### Components

1. **DatabaseManager** (`models/database.py`)
   - SQLite ORM using SQLAlchemy
   - Manages `PageRecord` table with page metadata
   - Provides queries for checking if URLs exist and retrieving pages

2. **ScrapingOrchestrator** (`models/orchestrator.py`)
   - Orchestrates the entire scraping workflow
   - Integrates with Firecrawl for fetching
   - Integrates with ResponseProcessor for data processing
   - Manages URL queue and deduplication

3. **Data Models**
   - `PageMetadata`: Pydantic model for scraped page data
   - `PageRecord`: SQLAlchemy ORM model for database persistence

## Installation

SQLAlchemy is already added to `pyproject.toml` dependencies:

```bash
# Install dependencies
pip install -e .
```

## Quick Start

### Minimal Example

```python
from models import ScrapingOrchestrator
import os
import dotenv

dotenv.load_dotenv()
api_key = os.getenv('FIRECRAWL_API_KEY')

# Initialize orchestrator
orchestrator = ScrapingOrchestrator(
    firecrawl_api_key=api_key,
    root_url='https://example.com/docs/',
    ask_ollama=False  # Set True if Ollama is available
)

# Scrape a URL and persist to database
metadata = orchestrator.scrape_and_persist('https://example.com/docs/page1')

# Add child URLs to queue
if metadata.child_urls:
    orchestrator.add_urls_to_queue(metadata.child_urls)

# Scrape batch from queue
stats = orchestrator.scrape_batch(max_urls=5)
print(f"Scraped {stats['scraped']} pages")
```

## Core Methods

### ScrapingOrchestrator

#### `scrape_and_persist(url) -> Optional[PageMetadata]`

Scrapes a single URL, saves markdown file, and persists metadata to database.

**Parameters:**
- `url` (str): URL to scrape

**Returns:**
- `PageMetadata` if successful
- `None` if URL was already scraped or scrape failed

**Example:**
```python
metadata = orchestrator.scrape_and_persist('https://example.com/docs/overview')
if metadata:
    print(f"Title: {metadata.title}")
    print(f"Child URLs: {len(metadata.child_urls)}")
```

#### `has_been_scraped(url) -> bool`

Checks if a URL has already been scraped (prevents duplicates).

**Parameters:**
- `url` (str): URL to check

**Returns:**
- `True` if URL has been scraped
- `False` otherwise

**Example:**
```python
if orchestrator.has_been_scraped('https://example.com/docs/page1'):
    print("Already scraped, skipping")
else:
    orchestrator.scrape_and_persist('https://example.com/docs/page1')
```

#### `add_urls_to_queue(urls) -> None`

Adds URLs to the scraping queue, automatically filtering out already-scraped ones.

**Parameters:**
- `urls` (List[Tuple[str, str]]): List of (link_text, link_url) tuples

**Example:**
```python
child_urls = [
    ("Getting Started", "https://example.com/docs/getting-started"),
    ("API Reference", "https://example.com/docs/api"),
]
orchestrator.add_urls_to_queue(child_urls)
```

#### `get_next_url() -> Optional[Tuple[str, str]]`

Gets the next URL from the queue (FIFO).

**Returns:**
- (link_text, link_url) tuple or None if queue is empty

#### `queue_size() -> int`

Returns the current number of URLs in the queue.

#### `scrape_batch(max_urls=None, stop_on_failure=False) -> dict`

Scrapes a batch of URLs from the queue.

**Parameters:**
- `max_urls` (int, optional): Maximum URLs to scrape. Default: all
- `stop_on_failure` (bool): Stop on first failure. Default: False

**Returns:**
Dictionary with keys:
- `scraped`: Number successfully scraped
- `failed`: Number failed
- `skipped`: Number skipped (already done)
- `queue_remaining`: URLs left in queue
- `total_scraped_session`: Total in this batch

**Example:**
```python
# Scrape first 10 URLs from queue
stats = orchestrator.scrape_batch(max_urls=10)
print(f"Scraped {stats['scraped']}, failed {stats['failed']}")
```

#### `scrape_from_root(max_depth=None) -> dict`

Starts scraping from the root URL and automatically traverses all child URLs.

**Parameters:**
- `max_depth` (int, optional): Maximum traversal depth. Default: unlimited

**Returns:**
Dictionary with final statistics

**Example:**
```python
# Traverse up to 2 levels deep
stats = orchestrator.scrape_from_root(max_depth=2)
print(f"Total scraped: {stats['total_scraped']}")
print(f"Depth levels traversed: {stats['depth_levels']}")
```

⚠️ **Warning:** Be careful with API quotas when using `scrape_from_root` without depth limits!

#### `get_scraping_stats() -> dict`

Returns overall statistics about the scraping session.

**Returns:**
Dictionary with keys:
- `root_url`: Root URL
- `total_scraped_urls`: Total unique URLs scraped
- `failed_urls`: Number of failed scrapes
- `queue_pending`: URLs remaining in queue
- `database_pages`: Total pages in database

**Example:**
```python
stats = orchestrator.get_scraping_stats()
print(f"Total scraped: {stats['total_scraped_urls']}")
print(f"Database location: {stats['database_location']}")
```

### DatabaseManager

#### `url_exists(url) -> bool`

Check if a URL has been scraped.

#### `get_page_by_url(url) -> Optional[PageRecord]`

Retrieve page record by URL.

#### `save_page_metadata(metadata_dict) -> PageRecord`

Save or update page metadata.

#### `get_all_pages() -> List[PageRecord]`

Get all scraped pages.

#### `get_pages_by_version(version) -> List[PageRecord]`

Get all pages for a specific Flink version.

**Example:**
```python
pages = orchestrator.db_manager.get_pages_by_version('flink-docs-release-1.20')
print(f"Found {len(pages)} pages for Flink 1.20")
```

## Database Schema

### pages table

| Column | Type | Notes |
|--------|------|-------|
| `page_id` | VARCHAR(64) | Primary key, SHA256 hash |
| `url` | VARCHAR(2048) | Unique, indexed |
| `title` | VARCHAR(512) | Page title |
| `version` | VARCHAR(64) | Flink version |
| `prefix` | VARCHAR(256) | URL prefix |
| `slug` | VARCHAR(128) | One-word identifier |
| `summary` | TEXT | ~100 char summary |
| `parent_url` | VARCHAR(2048) | Parent page URL |
| `is_root_url` | BOOLEAN | True for root pages |
| `headings` | JSON | Extracted headings |
| `child_urls` | JSON | List of child links |
| `scrape_timestamp` | DATETIME | When scraped |
| `content_hash` | VARCHAR(64) | SHA256 of content |

## Workflow Examples

### Example 1: Single URL Scrape

```python
# Scrape one page
metadata = orchestrator.scrape_and_persist(url)
if metadata:
    print(f"Saved: {metadata.title}")
```

### Example 2: Manual Queue Management

```python
# Add URLs manually
urls = [
    ("Page 1", "https://example.com/1"),
    ("Page 2", "https://example.com/2"),
]
orchestrator.add_urls_to_queue(urls)

# Process one at a time
while orchestrator.queue_size() > 0:
    text, url = orchestrator.get_next_url()
    orchestrator.scrape_and_persist(url)
```

### Example 3: Batch with Child URL Discovery

```python
# Scrape root
root = orchestrator.scrape_and_persist(root_url)
if root and root.child_urls:
    orchestrator.add_urls_to_queue(root.child_urls)

# Scrape children
stats = orchestrator.scrape_batch(max_urls=10)

# The batch scraping automatically:
# 1. Fetches each URL
# 2. Processes the response
# 3. Saves markdown files
# 4. Persists metadata
# 5. Adds new child URLs to queue
# 6. Skips already-scraped URLs
```

### Example 4: Resume from Database

```python
# Create new orchestrator - it loads existing URLs from DB
new_orchestrator = ScrapingOrchestrator(
    firecrawl_api_key=api_key,
    root_url=root_url,
    db_path='./data/scraping.db'  # Uses existing DB
)

# Can immediately see what's been scraped
stats = new_orchestrator.get_scraping_stats()
print(f"Previously scraped: {stats['total_scraped_urls']}")

# Continue scraping from queue
new_orchestrator.scrape_batch(max_urls=5)
```

### Example 5: Query Results

```python
# Get all pages
pages = orchestrator.db_manager.get_all_pages()
for page in pages:
    print(f"{page.title}")
    print(f"  URL: {page.url}")
    print(f"  Scraped: {page.scrape_timestamp}")

# Get pages by version
v120_pages = orchestrator.db_manager.get_pages_by_version('flink-docs-release-1.20')
print(f"Total pages: {len(v120_pages)}")
```

## File Structure

```
firecrawl_flink_docs/
├── models/
│   ├── __init__.py          # Exports all models
│   ├── metadata.py          # PageMetadata pydantic model
│   ├── processdata.py       # ResponseProcessor
│   ├── database.py          # DatabaseManager & PageRecord (NEW)
│   └── orchestrator.py      # ScrapingOrchestrator (NEW)
├── data/
│   ├── scraping.db          # SQLite database (auto-created)
│   └── markdown_files/      # Saved markdown files
├── dev-notebook.ipynb       # Updated with examples
└── scrape_with_orchestrator.py  # Standalone script (NEW)
```

## Tips & Best Practices

### 1. **Incremental Scraping**
```python
# Don't scrape everything at once - use batches
for i in range(10):
    stats = orchestrator.scrape_batch(max_urls=5)
    print(f"Batch {i+1}: {stats['scraped']} scraped")
```

### 2. **Monitor Progress**
```python
# Check current status
stats = orchestrator.get_scraping_stats()
print(f"Progress: {stats['total_scraped_urls']} scraped, "
      f"{stats['queue_pending']} pending")
```

### 3. **Handle Failures Gracefully**
```python
# Scrape but don't stop on failures
stats = orchestrator.scrape_batch(max_urls=10, stop_on_failure=False)
print(f"Failed: {stats['failed']} - will retry later")
```

### 4. **Save Bandwidth**
```python
# Check before scraping
if not orchestrator.has_been_scraped(url):
    orchestrator.scrape_and_persist(url)
```

### 5. **Resume from Database**
```python
# The database persists across sessions
orchestrator = ScrapingOrchestrator(...)
stats = orchestrator.get_scraping_stats()
print(f"Resume: {len(orchestrator.scraped_urls)} already done")
```

## Troubleshooting

### Issue: "URL already scraped, skipping"
**Solution:** This is expected behavior - duplicate URLs are prevented. Check the database to see what's been scraped.

### Issue: Database errors
**Solution:** Make sure `./data/` directory is writable. The database is created automatically.

### Issue: Running out of API quota
**Solution:** Use `max_urls` parameter in `scrape_batch()` to control rate, or set delays between batches.

### Issue: Ollama not responding
**Solution:** Set `ask_ollama=False` when initializing orchestrator to skip summary extraction.

## Future Enhancements

Possible improvements:
- Rate limiting and exponential backoff
- Retry logic for failed URLs
- Webhook callbacks on completion
- Export to different formats (JSON, CSV, etc.)
- Multi-threaded batch processing
- URL filtering/whitelist patterns
