import os
import re
import hashlib
from firecrawl_flink_docs.models.processdata import ResponseProcessor
from firecrawl_flink_docs.models.database import DatabaseManager
from firecrawl_flink_docs.models.metadata import PageMetadata

# Path to markdown files and database
MARKDOWN_DIR = os.path.join(os.path.dirname(__file__), '../data/markdown_files')
DB_PATH = os.path.join(os.path.dirname(__file__), '../data/scraping.db')

def extract_page_id_from_filename(filename):
    # Assumes page_id is the last part before .md
    match = re.match(r'.*_([a-f0-9]{64})\\.md$', filename)
    if match:
        return match.group(1)
    return None

def main():
    # 1. Read all markdown file names
    md_files = [f for f in os.listdir(MARKDOWN_DIR) if f.endswith('.md')]
    print(f"Found {len(md_files)} markdown files.")

    # 2. Iterate and process
    db = DatabaseManager(DB_PATH)
    for fname in md_files:
        page_id = extract_page_id_from_filename(fname)
        if not page_id:
            print(f"Skipping {fname}: could not extract page_id.")
            continue
        md_path = os.path.join(MARKDOWN_DIR, fname)
        with open(md_path, 'r', encoding='utf-8') as f:
            md_content = f.read()
        # 2.1 Extract summary, slug, headings
        summary_data = ResponseProcessor.extract_summaries_with_ollama(md_content)
        summary = summary_data.get('summary', '')
        slug = summary_data.get('slug', '')
        headings = summary_data.get('headings', [])
        # Compute content_hash (sha256 of markdown content)
        content_hash = hashlib.sha256(md_content.encode('utf-8')).hexdigest()
        
        # 2.2 Update DB
        update_fields = {
            'summary': summary,
            'slug': slug,
            'headings': headings,
            'content_hash': content_hash
        }
        db.update_page_fields_by_page_id(page_id, update_fields)
        print(f"Updated page_id {page_id} with summary, slug, headings, content_hash.")

if __name__ == '__main__':
    main()
