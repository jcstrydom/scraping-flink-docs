
import os
import re
import hashlib
import sys
from pathlib import Path

# Ensure parent directory is in sys.path for module imports
SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from models.processdata import ResponseProcessor
from models.database import DatabaseManager
from models.metadata import PageMetadata

# Path to markdown files and database
MARKDOWN_DIR = os.path.join(os.path.dirname(__file__), '../data/markdown_files')
DB_PATH = os.path.join(os.path.dirname(__file__), '../data/scraping.db')

def extract_page_id_from_filename(filename):
    # Assumes page_id is the last part before .md
    match = re.match(r'.*_([a-f0-9]{64})\.md$', filename)
    if match:
        return match.group(1)
    return None

def main():
    db = DatabaseManager(DB_PATH)
    processor = ResponseProcessor()
    # Get unprocessed pages from DB
    unprocessed_pages = db.get_unprocessed_pages()
    print(f"Found {len(unprocessed_pages)} unprocessed pages in DB.")

    # Map page_id to markdown filename
    md_files = {extract_page_id_from_filename(f): f for f in os.listdir(MARKDOWN_DIR) if f.endswith('.md')}

    for page in unprocessed_pages:
        page_id = page.page_id
        fname = md_files.get(page_id)
        if not fname:
            print(f"No markdown file found for page_id {page_id}, skipping.")
            continue
        md_path = os.path.join(MARKDOWN_DIR, fname)
        with open(md_path, 'r', encoding='utf-8') as f:
            md_content = f.read()
        try:
            summary_data = processor.extract_summaries_with_ollama(markdown=md_content)
            summary = summary_data.get('summary', None)
            slug = summary_data.get('slug', None)
            headings = summary_data.get('headings', None)
            content_hash = hashlib.sha256(md_content.encode('utf-8')).hexdigest()
            update_fields = {
                'summary': summary,
                'slug': slug,
                'headings': headings,
                'content_hash': content_hash
            }
            db.update_page_fields_by_page_id(page_id, update_fields)
            print(f"Updated page_id {page_id} with summary, slug, headings, content_hash.")
        except Exception as e:
            print(f"Error processing {fname} (page_id: {page_id}): {e}")

if __name__ == '__main__':
    main()
