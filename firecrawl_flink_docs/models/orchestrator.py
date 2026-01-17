"""
Scraping orchestrator that manages the full scraping workflow:
- Persisting data to database
- Managing URL queues
- Deduplicating already-scraped URLs
"""

import logging
from collections import deque
from typing import Optional, Set, Tuple, List
from datetime import datetime

from firecrawl import Firecrawl

from .processdata import ResponseProcessor
from .metadata import PageMetadata
from .database import DatabaseManager, PageRecord


class ScrapingOrchestrator:
    """
    Orchestrates the full scraping workflow including:
    - Fetching pages with Firecrawl
    - Processing responses
    - Persisting to database
    - Managing URL traversal queue
    - Preventing duplicate scrapes
    """
    
    def __init__(
        self,
        firecrawl_api_key: str,
        root_url: str,
        db_path: Optional[str] = None,
        log_level: int = logging.INFO,
        ask_ollama: bool = True,
        load_existing_urls: bool = True
    ):
        """
        Initialize the scraping orchestrator.
        
        Args:
            firecrawl_api_key: API key for Firecrawl service
            root_url: Starting URL for the scraping
            db_path: Path to SQLite database (optional)
            log_level: Logging level
            ask_ollama: Whether to use Ollama for extracting summaries/slugs
            load_existing_urls: Whether to load previously scraped URLs from database.
                If True (default), considers all URLs from DB as already scraped.
                If False, only tracks URLs in current session.
        """
        self.logger = logging.getLogger(f"{__name__}.{self.__class__.__name__}")
        self.logger.setLevel(log_level)
        
        if not self.logger.handlers:
            handler = logging.StreamHandler()
            handler.setLevel(log_level)
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)
        
        self.firecrawl = Firecrawl(api_key=firecrawl_api_key)
        self.processor = ResponseProcessor(root_url=root_url, log_level=log_level)
        self.db_manager = DatabaseManager(db_path=db_path)
        self.ask_ollama = ask_ollama
        self.load_existing_urls = load_existing_urls
        
        self.root_url = root_url
        self.url_queue: deque = deque()
        self.scraped_urls: Set[str] = set()
        self.failed_urls: Set[str] = set()
        
        self.logger.info(
            "ScrapingOrchestrator initialized",
            extra={
                "root_url": root_url,
                "db_path": self.db_manager.db_path,
                "ask_ollama": ask_ollama,
                "load_existing_urls": load_existing_urls
            }
        )
        
        # Load already-scraped URLs from database on init if requested
        if self.load_existing_urls:
            self._load_scraped_urls()
    
    def _load_scraped_urls(self) -> None:
        """Load all previously scraped URLs from database into memory."""
        try:
            existing_pages = self.db_manager.get_all_pages()
            self.scraped_urls = {page.url for page in existing_pages}
            self.logger.info(
                "Loaded existing scraped URLs from database",
                extra={"count": len(self.scraped_urls)}
            )
        except Exception as e:
            self.logger.error("Failed loading existing scraped URLs", extra={"error": str(e)})
    
    def has_been_scraped(self, url: str) -> bool:
        """
        Check if a URL has already been scraped.
        
        Args:
            url: URL to check
        
        Returns:
            True if URL has been scraped, False otherwise
        """
        normalized = self.processor._normalize_url(url)
        return normalized in self.scraped_urls
    
    def scrape_and_persist(self, url: str) -> Optional[PageMetadata]:
        """
        Scrape a single URL, process it, and persist to database.
        
        Args:
            url: URL to scrape
        
        Returns:
            PageMetadata if successful, None if failed or already scraped
        """
        normalized_url = self.processor._normalize_url(url)
        
        # Check if already scraped
        if self.has_been_scraped(normalized_url):
            self.logger.info("URL already scraped, skipping", extra={"url": normalized_url})
            return None
        
        try:
            self.logger.info("Scraping URL", extra={"url": normalized_url})
            
            # Fetch with Firecrawl
            response = self.firecrawl.scrape(
                url=normalized_url,
                wait_for=2000,
                only_main_content=True,
                formats=['markdown'],
            )
            
            # Process the response
            parent_url = self._get_parent_url_for_url(normalized_url)
            processed_data = self.processor.parse_raw_response(
                response.model_dump(),
                parent_url=parent_url,
                ask_ollama=self.ask_ollama
            )
            
            # Save markdown file
            self.processor.save_markdown_file(
                processed_data,
                response.model_dump()['markdown']
            )
            
            # Convert to PageMetadata and save to database
            metadata = PageMetadata.model_validate(processed_data)
            metadata_dict = metadata.to_dict()
            self.db_manager.save_page_metadata(metadata_dict)
            
            # Track this URL as scraped
            self.scraped_urls.add(normalized_url)
            
            self.logger.info(
                "Successfully scraped and persisted URL",
                extra={
                    "url": normalized_url,
                    "page_id": metadata.page_id,
                    "child_urls_count": len(metadata.child_urls)
                }
            )
            
            return metadata
            
        except Exception as e:
            self.logger.error(
                "Failed to scrape and persist URL",
                extra={"url": normalized_url, "error": str(e)}
            )
            self.failed_urls.add(normalized_url)
            return None
    
    def add_urls_to_queue(self, urls: List[Tuple[str, str]]) -> None:
        """
        Add URLs (with link text) to the scraping queue, filtering out already-scraped ones.
        
        Args:
            urls: List of (link_text, link_url) tuples
        """
        added = 0
        skipped = 0
        
        for text, url in urls:
            normalized = self.processor._normalize_url(url)
            
            if self.has_been_scraped(normalized):
                skipped += 1
                self.logger.debug("URL already scraped, skipping queue add", extra={"url": normalized})
                continue
            
            if normalized not in self.url_queue:
                self.url_queue.append((text, normalized))
                added += 1
        
        self.logger.info(
            "Added URLs to queue",
            extra={"added": added, "skipped": skipped, "queue_size": len(self.url_queue)}
        )
    
    def get_next_url(self) -> Optional[Tuple[str, str]]:
        """
        Get the next URL from the queue (FIFO).
        
        Returns:
            (link_text, link_url) tuple or None if queue is empty
        """
        if self.url_queue:
            return self.url_queue.popleft()
        return None
    
    def queue_size(self) -> int:
        """Get current queue size."""
        return len(self.url_queue)
    
    def _get_parent_url_for_url(self, url: str) -> Optional[str]:
        """
        Determine the parent URL for a given URL.
        For the root URL, parent is None. Otherwise, check database.
        
        Args:
            url: The URL to find parent for
        
        Returns:
            Parent URL or None
        """
        if url == self.root_url:
            return None
        
        # Check if we've already processed this URL's parent
        # For now, return None - can be enhanced to track parent relationships
        return None
    
    def scrape_batch(self, max_urls: int = None, stop_on_failure: bool = False) -> dict:
        """
        Scrape a batch of URLs from the queue.
        
        Args:
            max_urls: Maximum number of URLs to scrape (None = all in queue)
            stop_on_failure: Whether to stop on first failure
        
        Returns:
            Statistics dict with counts
        """
        scraped_count = 0
        failed_count = 0
        skipped_count = 0
        
        max_urls = max_urls or len(self.url_queue)
        
        for _ in range(min(max_urls, len(self.url_queue))):
            url_entry = self.get_next_url()
            if not url_entry:
                break
            
            link_text, url = url_entry
            
            result = self.scrape_and_persist(url)
            
            if result:
                scraped_count += 1
                # Add child URLs to queue for traversal
                if result.child_urls:
                    self.add_urls_to_queue(result.child_urls)
            elif self.has_been_scraped(url):
                skipped_count += 1
            else:
                failed_count += 1
                if stop_on_failure:
                    self.logger.warning("Stopping batch due to failure", extra={"url": url})
                    break
        
        stats = {
            "scraped": scraped_count,
            "failed": failed_count,
            "skipped": skipped_count,
            "queue_remaining": len(self.url_queue),
            "total_scraped_session": scraped_count + failed_count + skipped_count
        }
        
        self.logger.info("Batch scraping completed", extra=stats)
        return stats
    
    def scrape_from_root(self, max_depth: int = None) -> dict:
        """
        Start scraping from the root URL and traverse all child URLs.
        
        Args:
            max_depth: Maximum depth to traverse (None = unlimited)
        
        Returns:
            Statistics dict with final counts
        """
        self.logger.info("Starting scrape from root URL", extra={"root_url": self.root_url})
        
        # Start with root URL
        if not self.has_been_scraped(self.root_url):
            root_metadata = self.scrape_and_persist(self.root_url)
            if root_metadata and root_metadata.child_urls:
                self.add_urls_to_queue(root_metadata.child_urls)
        
        total_stats = {
            "total_scraped": 0,
            "total_failed": 0,
            "total_skipped": 0,
            "depth_levels": 0
        }
        
        depth = 0
        while self.queue_size() > 0 and (max_depth is None or depth < max_depth):
            depth += 1
            self.logger.info(
                f"Processing depth level {depth}",
                extra={"queue_size": self.queue_size()}
            )
            
            batch_stats = self.scrape_batch()
            total_stats["total_scraped"] += batch_stats["scraped"]
            total_stats["total_failed"] += batch_stats["failed"]
            total_stats["total_skipped"] += batch_stats["skipped"]
            total_stats["depth_levels"] = depth
        
        self.logger.info("Root scraping completed", extra=total_stats)
        return total_stats
    
    def get_scraping_stats(self) -> dict:
        """Get overall scraping statistics."""
        return {
            "root_url": self.root_url,
            "total_scraped_urls": len(self.scraped_urls),
            "failed_urls": len(self.failed_urls),
            "queue_pending": len(self.url_queue),
            "database_pages": len(self.db_manager.get_all_pages())
        }
