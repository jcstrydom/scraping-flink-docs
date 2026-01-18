"""
Database models and session management for scraping persistence.
"""

from sqlalchemy import create_engine, Column, String, DateTime, Boolean, Text, Integer, JSON, ForeignKey
from sqlalchemy.orm import declarative_base, Session, relationship
from datetime import datetime
from pathlib import Path
import logging

Base = declarative_base()


class PageRecord(Base):
    """
    ORM model for storing scraped page metadata.
    Maps to PageMetadata but persists to database.
    """
    __tablename__ = "pages"
    
    page_id = Column(String(64), primary_key=True, index=True)
    url = Column(String(2048), unique=True, index=True, nullable=False)
    title = Column(String(512), nullable=True)
    version = Column(String(64), nullable=True)
    prefix = Column(String(256), nullable=True)
    slug = Column(String(128), nullable=True)
    summary = Column(Text, nullable=True)
    parent_url = Column(String(2048), nullable=True)
    is_root_url = Column(Boolean, default=False)
    
    # JSON storage for complex types
    headings = Column(JSON, default=list)
    child_urls = Column(JSON, default=list)  # List of [text, url] pairs
    
    scrape_timestamp = Column(DateTime, default=datetime.utcnow, index=True)
    content_hash = Column(String(64), nullable=True, index=True)
    
    # Relationship to children
    children = relationship("PageRecord", remote_side=[url], foreign_keys=[parent_url], primaryjoin="PageRecord.parent_url == PageRecord.url", viewonly=True)
    
    def __repr__(self):
        return f"<PageRecord(page_id={self.page_id}, url={self.url}, title={self.title})>"


class DatabaseManager:
    """
    Manages SQLite database for scraping persistence.
    Handles initialization, session management, and common queries.
    """
    
    def __init__(self, db_path: str = None):
        """
        Initialize database manager.
        
        Args:
            db_path: Path to SQLite database file. Defaults to ./data/scraping.db
        """
        if db_path is None:
            script_dir = Path(__file__).parent.parent
            db_path = script_dir / "data" / "scraping.db"
        
        self.db_path = Path(db_path)
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self.logger = logging.getLogger(__name__)
        
        db_url = f"sqlite:///{self.db_path}"
        self.engine = create_engine(db_url, echo=False)
        Base.metadata.create_all(self.engine)
    
    def get_session(self) -> Session:
        """Get a new database session."""
        from sqlalchemy.orm import sessionmaker
        SessionLocal = sessionmaker(bind=self.engine)
        return SessionLocal()
    
    def url_exists(self, url: str, session: Session = None) -> bool:
        """Check if a URL has already been scraped."""
        close_session = False
        if session is None:
            session = self.get_session()
            close_session = True
        
        try:
            result = session.query(PageRecord).filter(PageRecord.url == url).first()
            return result is not None
        finally:
            if close_session:
                session.close()
    
    def get_page_by_url(self, url: str, session: Session = None) -> PageRecord:
        """Retrieve a page record by URL."""
        close_session = False
        if session is None:
            session = self.get_session()
            close_session = True
        
        try:
            return session.query(PageRecord).filter(PageRecord.url == url).first()
        finally:
            if close_session:
                session.close()
    
    def _sanitize_metadata(self, metadata_dict: dict) -> dict:
        """
        Convert Pydantic types (like HttpUrl) to native Python types.
        
        Args:
            metadata_dict: The metadata dictionary that may contain Pydantic types
        
        Returns:
            Sanitized dictionary with native Python types
        """
        sanitized = {}
        for key, value in metadata_dict.items():
            # Convert Pydantic HttpUrl and other Pydantic types to strings
            if hasattr(value, '__class__') and 'pydantic' in value.__class__.__module__:
                sanitized[key] = str(value)
            else:
                sanitized[key] = value
        return sanitized
    
    def save_page_metadata(self, metadata_dict: dict, session: Session = None) -> PageRecord:
        """
        Save or update page metadata from a PageMetadata object dict.
        
        Args:
            metadata_dict: Dict from PageMetadata.to_dict()
            session: Optional existing session
        
        Returns:
            PageRecord instance
        """
        
        close_session = False
        if session is None:
            session = self.get_session()
            close_session = True
        
        try:
            # Sanitize metadata to convert Pydantic types to native Python types
            metadata_dict = self._sanitize_metadata(metadata_dict)
            
            self.logger.debug(f"Saving metadata for page_id: {metadata_dict.get('page_id')}")
            
            # Check if page already exists
            existing = session.query(PageRecord).filter(
            PageRecord.page_id == metadata_dict['page_id']
            ).first()
            
            if existing:
                self.logger.info(f"Updating existing page: {metadata_dict['page_id']}")
                # Update existing record
                for key, value in metadata_dict.items():
                    if hasattr(existing, key) and key != 'page_id':
                        setattr(existing, key, value)
                page_record = existing
            else:
                self.logger.info(f"Creating new page record: {metadata_dict['page_id']}")
                # Create new record
                page_record = PageRecord(**metadata_dict)
                session.add(page_record)

            session.commit()
            self.logger.info(f"Successfully saved page_id: {metadata_dict['page_id']}")
            return page_record
        except Exception as e:
            self.logger.error(f"Error saving metadata for page_id {metadata_dict.get('page_id')}: {str(e)}", exc_info=True)
            session.rollback()
            raise e
        finally:
            if close_session:
                session.close()
    
    def get_all_pages(self, session: Session = None) -> list:
        """Get all scraped pages."""
        close_session = False
        if session is None:
            session = self.get_session()
            close_session = True
        
        try:
            return session.query(PageRecord).all()
        finally:
            if close_session:
                session.close()
    
    def get_pages_by_version(self, version: str, session: Session = None) -> list:
        """Get all pages for a specific Flink version."""
        close_session = False
        if session is None:
            session = self.get_session()
            close_session = True
        
        try:
            return session.query(PageRecord).filter(PageRecord.version == version).all()
        finally:
            if close_session:
                session.close()
