# Visual Guide

## Architecture

```text
Your Code
   |
   v
ScrapingOrchestrator
   |-- Firecrawl (fetch markdown)
   |-- ResponseProcessor (parse links + metadata)
   |-- DatabaseManager (persist/query/cleanup)
   |-- URL Queue (FIFO traversal)
   v
Storage
   |-- firecrawl_flink_docs/data/scraping.db
   `-- firecrawl_flink_docs/data/markdown_files/*.md
```

## Single URL Flow

```text
scrape_and_persist(url)
  -> normalize + scope check
  -> dedupe check (in-memory scraped_urls)
  -> Firecrawl scrape
  -> ResponseProcessor parse_raw_response
  -> save markdown file
  -> save_page_metadata (DB upsert)
  -> add normalized url to scraped_urls
  -> return PageMetadata
```

## Queue / Batch Flow

```text
add_urls_to_queue(child_urls)
  -> filter out-of-scope
  -> filter already-scraped
  -> append new urls to deque

scrape_batch(max_urls)
  -> pop queue FIFO
  -> scrape_and_persist(url)
  -> enqueue newly discovered children
  -> return counters (scraped/failed/skipped/queue_remaining)
```

## Root Traversal Flow

```text
scrape_from_root(max_depth)
  -> scrape root if needed
  -> enqueue root children
  -> loop by depth while queue not empty
       -> scrape_batch()
  -> return totals
```

## Persistence View

```text
DB table: pages
  page_id (pk), url (unique), title, version, prefix,
  slug, summary, parent_url, is_root_url,
  headings (JSON), child_urls (JSON),
  scrape_timestamp, content_hash
```

## Data Cleanup Flow (Headings)

```text
clean_headings_text_links()
  -> iterate all rows
  -> for each headings[*].text:
       - convert [text](url) => text
       - remove bare URLs
       - normalize whitespace
  -> update changed rows
  -> commit once
  -> return counters
```

## Session Resume

```text
New orchestrator instance + same DB path
  -> load_existing_urls=True
  -> scraped_urls populated from DB
  -> previously scraped URLs skipped automatically
```
