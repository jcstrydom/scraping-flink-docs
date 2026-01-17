# ScrapingOrchestrator - Visual Guide

## System Architecture Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                    YOUR SCRAPING CODE                           │
│                                                                 │
│  orchestrator = ScrapingOrchestrator(api_key, root_url)        │
│  orchestrator.scrape_and_persist(url)                          │
│  orchestrator.scrape_batch(max_urls=5)                         │
└──────────────────────────┬──────────────────────────────────────┘
                           │
        ┌──────────────────┴──────────────────┐
        │                                     │
        ▼                                     ▼
┌───────────────────────────┐       ┌────────────────────┐
│  ScrapingOrchestrator     │       │  URL Queue (FIFO)  │
│  ───────────────────────  │       │  ────────────────  │
│ • Orchestrates workflow   │◄──────┤  Store URLs        │
│ • Manages queue           │       │  Auto-discovery    │
│ • Tracks scraped URLs     │       │                    │
│ • Coordinates DB save     │       └────────────────────┘
│ • Logs all operations     │
└───────────┬──────────┬───┘
            │          │
            ▼          ▼
    ┌─────────────┐  ┌──────────────────┐
    │ Firecrawl   │  │ ResponseProcessor│
    │ (Scraper)   │  │ (Parser)         │
    │             │  │                  │
    │ • Fetch URL │  │ • Extract MD     │
    │ • Raw HTML  │  │ • Find links     │
    │ • Metadata  │  │ • Extract meta   │
    │             │  │ • Call Ollama    │
    └─────────────┘  └──────────────────┘
            │          │
            └────┬─────┘
                 │
                 ▼
        ┌──────────────────┐
        │  PageMetadata    │
        │  (Pydantic)      │
        │                  │
        │ • page_id        │
        │ • title          │
        │ • child_urls     │
        │ • headings       │
        │ • timestamp      │
        └────┬─────────────┘
             │
        ┌────┴───────────────┐
        │                    │
        ▼                    ▼
    ┌────────────────┐  ┌──────────────────────┐
    │ Markdown Files │  │  DatabaseManager     │
    │                │  │  ─────────────────── │
    │ Path:          │  │  SQLite + SQLAlchemy │
    │ ./data/        │  │                      │
    │ markdown_files/│  │ • save_metadata()    │
    │ {id}_{hash}.md │  │ • url_exists()       │
    │                │  │ • get_all_pages()    │
    │ Contains:      │  │ • get_pages_by_*()   │
    │ • Full markdown│  │                      │
    │ • All content  │  └──────────────────────┘
    │ • Tables, code │           │
    │ • Images refs  │           │
    └────────────────┘           │
                                 ▼
                        ┌──────────────────┐
                        │ SQLite Database  │
                        │ ─────────────── │
                        │ ./data/          │
                        │ scraping.db      │
                        │                  │
                        │ pages table:     │
                        │ • page_id        │
                        │ • url            │
                        │ • title          │
                        │ • version        │
                        │ • child_urls     │
                        │ • timestamp      │
                        │ • content_hash   │
                        │ • ... (14 cols)  │
                        └──────────────────┘
```

## Data Flow Sequence

```
┌─────────────────────────────────────────────────────────────────────┐
│                        SCRAPING WORKFLOW                            │
└─────────────────────────────────────────────────────────────────────┘

Step 1: Initialize
────────────────
  ScrapingOrchestrator(api_key, root_url)
         │
         ├─→ Create DatabaseManager
         │   └─→ Load existing URLs from DB (deduplication set)
         │
         ├─→ Create ResponseProcessor
         │   └─→ Ready for processing
         │
         └─→ Initialize empty queue

Step 2: Scrape Single URL
──────────────────────
  orchestrator.scrape_and_persist(url)
         │
         ├─→ Check: has_been_scraped(url)?
         │   ├─→ YES: Return None (skip)
         │   └─→ NO: Continue
         │
         ├─→ Fetch with Firecrawl
         │   └─→ Get HTML + metadata
         │
         ├─→ Process with ResponseProcessor
         │   ├─→ Extract markdown
         │   ├─→ Parse child URLs
         │   ├─→ Extract metadata
         │   └─→ Call Ollama (optional)
         │
         ├─→ Save markdown file
         │   └─→ ./data/markdown_files/{prefix}_{page_id}.md
         │
         ├─→ Save to database
         │   ├─→ DatabaseManager.save_page_metadata()
         │   └─→ Store in ./data/scraping.db
         │
         ├─→ Track in memory
         │   └─→ Add to scraped_urls set
         │
         └─→ Return PageMetadata

Step 3: Add to Queue
────────────────
  orchestrator.add_urls_to_queue(metadata.child_urls)
         │
         ├─→ Loop through URLs
         │
         ├─→ For each URL:
         │   ├─→ Normalize URL
         │   ├─→ Check: has_been_scraped()?
         │   │   ├─→ YES: Skip (count as 'skipped')
         │   │   └─→ NO: Add to queue (count as 'added')
         │   │
         │   └─→ Check: Already in queue?
         │       ├─→ YES: Skip (avoid duplicates)
         │       └─→ NO: Append to deque
         │
         └─→ Return with statistics

Step 4: Batch Process Queue
──────────────────────
  orchestrator.scrape_batch(max_urls=5)
         │
         ├─→ Loop: while queue_size > 0 AND count < max_urls
         │
         ├─→ Get next URL from queue
         │   └─→ queue.popleft() (FIFO)
         │
         ├─→ Scrape and persist (repeats Step 2)
         │   │
         │   └─→ If successful AND has child_urls:
         │       └─→ Automatically add to queue (loop back to Step 3)
         │
         ├─→ Track results:
         │   ├─→ scraped (success count)
         │   ├─→ failed (error count)
         │   ├─→ skipped (already done)
         │   └─→ queue_remaining (URLs left)
         │
         └─→ Return statistics dict

Step 5: Resume Session
──────────────────
  new_orchestrator = ScrapingOrchestrator(api_key, root_url)
         │
         ├─→ Load database
         │   └─→ Populate scraped_urls set from DB
         │
         ├─→ Check progress
         │   └─→ get_scraping_stats()
         │       └─→ Show total_scraped_urls, etc.
         │
         └─→ Continue from where you left off
             └─→ scrape_batch() will skip already-done URLs
```

## Queue Management Visualization

```
Initial State (empty):
┌─────────────────────────┐
│      URL Queue (FIFO)   │
│                         │
│      [empty]            │
└─────────────────────────┘

After Scraping Root:
┌─────────────────────────┐
│      URL Queue (FIFO)   │
│                         │
│  ┌──────────────────┐   │
│  │  Getting Started │   │  ← Add to front (top)
│  │  DataStream API  │   │  ← Add next
│  │  SQL/Table API   │   │  ← Add next
│  │  Concepts        │   │  ← Add next
│  └──────────────────┘   │
└─────────────────────────┘

After Scraping First (Getting Started):
┌─────────────────────────┐
│      URL Queue (FIFO)   │
│                         │
│  ┌──────────────────┐   │
│  │  DataStream API  │   │  ← Still here
│  │  SQL/Table API   │   │  ← Still here
│  │  Concepts        │   │  ← Still here
│  │  Streaming SQL   │   │  ← Child of "Getting Started"
│  │  Event Time      │   │  ← Child of "Getting Started"
│  └──────────────────┘   │
└─────────────────────────┘
        ↓
   Removed → (Getting Started was scraped)

Continue deque.popleft() each iteration
```

## Deduplication Check Flow

```
has_been_scraped(url)?
         │
         ├─→ Normalize URL
         │   ├─→ Remove fragment (#)
         │   ├─→ Remove trailing slash
         │   ├─→ Lowercase scheme/netloc
         │   └─→ Standard form
         │
         └─→ Check: url in scraped_urls?
             ├─→ YES (found in memory)
             │   └─→ Return True (skip)
             │
             └─→ NO (not in memory)
                 └─→ Check database?
                     ├─→ Found → Return True
                     └─→ Not found → Return False

Benefit: URL variations handled:
  ✓ http://example.com == http://example.com/
  ✓ https://example.com == https://example.com#section
  ✓ Case-insensitive for domain
```

## Database Growth Over Time

```
Time → Scraping Progress

Session 1:
├─ Scrape: /concepts/overview/
├─ Scrape: /try-flink/
├─ Scrape: /dev/datastream/
└─ Save: 3 pages to DB

Database after Session 1: 3 pages ✓

Session 2 (Resume):
├─ Load DB: 3 pages (remember what's done)
├─ Scrape: /deployment/
├─ Scrape: /operations/
└─ Save: 2 more pages to DB (5 total)

Database after Session 2: 5 pages ✓

Session 3:
├─ Load DB: 5 pages
├─ Try: /concepts/overview/ (skip - already done)
├─ Scrape: /monitoring/
└─ Save: 1 more page to DB (6 total)

Database after Session 3: 6 pages ✓

Result: Zero duplicate effort! Resume seamlessly!
```

## Code Workflow Examples

### Example 1: Simple Linear Scraping
```
Code:                          Action:
─────────────────────────────────────
orch = Orchestrator(...)  →  Initialize
                             
url = root_url            →  Pick URL
orch.scrape_and_persist() →  Scrape & save ✓
```

### Example 2: Queue-Based Traversal
```
Code:                          Flow:
─────────────────────────────────────────
root = scrape_and_persist()  →  [Scrape Root]
                                     │
add_urls_to_queue(root.child_urls) → [Queue children]
                                     │
while queue_size() > 0:              │
  scrape_batch()           →  [Scrape batch]
                                     │
                                [Add new children to queue]
                                     │
                                [Loop until empty]
```

### Example 3: Session Persistence
```
Session 1:                     Session 2:
─────────────                  ──────────
orch = Orch(...)      →        orch = Orch(...) 
                               ↑ Same database!
scrape_batch(5)       →        Load previous progress
Save to DB ✓                   
                               stats = get_stats()
Stop                           → Shows 5 already done
                               
                               scrape_batch(5)  
                               → Continues from scratch,
                               → Skips old 5,
                               → Does new 5
```

## Performance Characteristics

```
Operation           | Time     | Memory | I/O
────────────────────|──────────|─────────|──────
scrape_and_persist  | ~5-10s   | Low    | Medium
  ├─ Firecrawl      |   ~5s    | Low    | Medium (API)
  ├─ Process        |  ~1-2s   | Low    | Low
  ├─ Save markdown  |  ~100ms  | Low    | Medium
  └─ Save to DB     |   ~50ms  | Low    | Low

has_been_scraped    | ~1ms     | Low    | None (memory)
add_urls_to_queue   | ~10ms    | Low    | Low
scrape_batch(5)     | ~30-60s  | Low    | Medium
get_scraping_stats  | ~1ms     | Low    | Low

Database size growth:
  ~1KB per page metadata
  ~50-200KB per markdown file
  Total: ~100-200KB per page
```

## Troubleshooting Decision Tree

```
Problem: Nothing is being saved
├─ Check database:
│  └─ db_manager.get_all_pages() returns []?
│     └─ Make sure scrape_and_persist() succeeded
│
└─ Check markdown files:
   └─ ls ./data/markdown_files/ is empty?
      └─ Check ResponseProcessor.save_markdown_file()

Problem: Scraping same URL twice
├─ Check has_been_scraped():
│  └─ Should return True after first scrape
│
└─ Check URL normalization:
   └─ Different URLs?
      └─ Maybe query strings or anchors differ

Problem: Queue not growing
├─ Check metadata.child_urls:
│  └─ May be empty page
│
└─ Check add_urls_to_queue() logs:
   └─ URLs already scraped? (skipped)

Problem: Database corrupted
├─ Delete: ./data/scraping.db
└─ Restart: Creates fresh database
   Note: Markdown files preserved!
```
