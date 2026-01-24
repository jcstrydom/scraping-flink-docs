#!/usr/bin/env python3
"""
Example script demonstrating the ScrapingOrchestrator.
Run this to scrape Flink docs with automatic persistence and deduplication.
"""

import logging
import os
import dotenv
from models import ScrapingOrchestrator

# Load environment variables
dotenv.load_dotenv(dotenv.find_dotenv(".env"))
FIRECRAWL_API_KEY = os.getenv('FIRECRAWL_API_KEY')

if not FIRECRAWL_API_KEY:
    raise ValueError("FIRECRAWL_API_KEY not set in .env file")

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

def main():
    """Main scraping orchestration."""
    
    root_url = 'https://nightlies.apache.org/flink/flink-docs-release-1.20/docs/concepts/overview/'
    
    # Initialize orchestrator
    orchestrator = ScrapingOrchestrator(
        firecrawl_api_key=FIRECRAWL_API_KEY,
        root_url=root_url,
        db_path=None,  # Uses default: ./data/scraping.db
        log_level=logging.INFO,
        ask_ollama=False  # Set to True if Ollama is running for summaries
    )
    
    print("\n" + "="*70)
    print("🚀 FLINK DOCS SCRAPING WITH ORCHESTRATOR")
    print("="*70)
    
    # Option 1: Scrape single URL
    print("\n📌 Scraping root URL...")
    metadata = orchestrator.scrape_and_persist(root_url)
    
    if metadata:
        print(f"✅ Scraped: {metadata.title}")
        print(f"   Child URLs found: {len(metadata.child_urls)}")
        
        # Queue child URLs for next iteration
        if metadata.child_urls:
            orchestrator.add_urls_to_queue(metadata.child_urls)
            print(f"   Added {len(metadata.child_urls)} child URLs to queue")
    
    # Option 2: Batch scrape from queue
    print(f"\n📋 Queue size: {orchestrator.queue_size()}")
    
    if orchestrator.queue_size() > 0:
        print("\n🔄 Scraping batch (first 5 URLs)...")
        stats = orchestrator.scrape_batch(max_urls=5)
        
        print("\n📊 Batch Results:")
        print(f"   ✅ Successfully scraped: {stats['scraped']}")
        print(f"   ❌ Failed: {stats['failed']}")
        print(f"   ⏭️  Skipped (already done): {stats['skipped']}")
        print(f"   📋 Queue remaining: {stats['queue_remaining']}")
    
    # Show final statistics
    print("\n" + "="*70)
    final_stats = orchestrator.get_scraping_stats()
    print("📈 FINAL STATISTICS")
    print("="*70)
    print(f"Root URL: {final_stats['root_url']}")
    print(f"Total unique URLs scraped: {final_stats['total_scraped_urls']}")
    print(f"Failed URLs: {final_stats['failed_urls']}")
    print(f"Pending URLs in queue: {final_stats['queue_pending']}")
    print(f"Pages in database: {final_stats['database_pages']}")
    print(f"Database location: {orchestrator.db_manager.db_path}")
    print("="*70 + "\n")
    
    # Show some pages
    print("📚 Sample pages in database:")
    all_pages = orchestrator.db_manager.get_all_pages()
    for page in all_pages[:3]:
        print(f"   - {page.title}")
    
    # To continue scraping from where we left off, just re-instantiate
    # and continue calling scrape_batch() - the URLs are tracked in the DB!
    print("\n💡 Tip: To continue scraping later, just create a new orchestrator")
    print("   with the same db_path - it will resume from where you left off!")

if __name__ == "__main__":
    main()
