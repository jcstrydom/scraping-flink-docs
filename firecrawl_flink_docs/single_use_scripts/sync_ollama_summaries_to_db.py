import argparse
import hashlib
import json
import os
import re
import sys
from pathlib import Path
import dotenv

# Ensure parent directory is in sys.path for module imports
SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from models.processdata import ResponseProcessor
from models.database import DatabaseManager

# Path to markdown files and database
MARKDOWN_DIR = os.path.join(os.path.dirname(__file__), '../data/markdown_files')
DB_PATH = os.path.join(os.path.dirname(__file__), '../data/scraping.db')

def extract_page_id_from_filename(filename):
    # Assumes page_id is the last part before .md
    match = re.match(r'.*_([a-f0-9]{64})\.md$', filename)
    if match:
        return match.group(1)
    return None

def _has_space_slug(slug):
    return isinstance(slug, str) and bool(re.search(r"\s", slug))


def _summary_too_long(summary):
    return isinstance(summary, str) and len(summary.strip()) > 100


def _headings_empty(headings):
    if headings is None:
        return True
    if headings == []:
        return True
    if isinstance(headings, str):
        stripped = headings.strip()
        if stripped in ("", "[]"):
            return True
        try:
            parsed = json.loads(stripped)
            return parsed == []
        except Exception:
            return False
    return False


def _needs_metadata_refresh(page):
    return _has_space_slug(page.slug) or _summary_too_long(page.summary) or _headings_empty(page.headings)


def parse_args():
    parser = argparse.ArgumentParser(description="Sync slug/summary/headings from markdown files to DB using Ollama/Gemini.")
    parser.add_argument("--max-calls", type=int, default=3, help="Maximum LLM calls to execute in this run.")
    parser.add_argument("--provider", default="ollama", choices=["gemini", "ollama", "auto"], help="LLM provider.")
    parser.add_argument("--model", default="mistral:7b", help="Model name/path to use.")
    parser.add_argument("--timeout", type=int, default=180, help="Request timeout in seconds.")
    parser.add_argument("--inspect", action="store_true", help="Print detailed selection and generated metadata.")
    parser.add_argument("--apply", action="store_true", help="Persist updates to DB. Omit for dry-run.")
    return parser.parse_args()


def main():
    args = parse_args()
    if args.provider == "gemini":
        dotenv_path = Path(__file__).resolve().parent.parent / ".env"
        dotenv.load_dotenv(dotenv_path.as_posix())
        if not os.environ.get("GOOGLE_GEMINI_API_KEY"):
            print(f"Missing GOOGLE_GEMINI_API_KEY in {dotenv_path}; aborting Gemini run.")
            return

    db = DatabaseManager(DB_PATH)
    processor = ResponseProcessor()
    all_pages = db.get_all_pages()
    eligible_pages = [p for p in all_pages if _needs_metadata_refresh(p)]
    print(f"Found {len(eligible_pages)} eligible pages matching metadata rules.")

    # Map page_id to markdown filename
    md_files = {extract_page_id_from_filename(f): f for f in os.listdir(MARKDOWN_DIR) if f.endswith('.md')}

    if args.max_calls < 1:
        print("--max-calls must be >= 1")
        return

    calls_made = 0
    processed = 0
    persisted = 0
    skipped_missing_md = 0
    failed = 0
    for page in eligible_pages:
        if calls_made >= args.max_calls:
            break

        page_id = page.page_id
        fname = md_files.get(page_id)
        if not fname:
            print(f"No markdown file found for page_id {page_id}, skipping.")
            skipped_missing_md += 1
            continue

        md_path = os.path.join(MARKDOWN_DIR, fname)
        with open(md_path, 'r', encoding='utf-8') as f:
            md_content = f.read()

        try:
            calls_made += 1
            reasons = []
            if _has_space_slug(page.slug):
                reasons.append("slug_contains_spaces")
            if _summary_too_long(page.summary):
                reasons.append("summary_gt_100_chars")
            if _headings_empty(page.headings):
                reasons.append("headings_empty")
            print(f"[{calls_made}/{args.max_calls}] Processing {fname} (page_id={page_id})")
            if args.inspect:
                current_summary = (page.summary or "").strip()
                print(f"  Current slug: {repr(page.slug)}")
                print(f"  Current summary length: {len(current_summary)}")
                print(f"  Current headings: {repr(page.headings)[:180]}")
                print(f"  Reasons: {', '.join(reasons)}")

            summary_data = processor.extract_summaries_with_ollama(
                markdown=md_content,
                provider=args.provider,
                model=args.model,
                timeout=args.timeout,
            )
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
            if args.inspect:
                summary_preview = (summary or "")[:140]
                print(f"  Proposed slug: {repr(slug)}")
                print(f"  Proposed summary length: {len((summary or '').strip())}")
                print(f"  Proposed headings count: {len(headings or [])}")
                print(f"  Proposed summary preview: {summary_preview}")

            if args.apply:
                db.update_page_fields_by_page_id(page_id, update_fields)
                print(f"Updated page_id {page_id} with summary, slug, headings, content_hash.")
                persisted += 1
            else:
                print("Dry run: no DB update applied. Re-run with --apply to persist.")
            processed += 1
        except Exception as e:
            print(f"Error processing {fname} (page_id: {page_id}): {e}")
            failed += 1

    print("\nRun complete.")
    print(f"Calls made: {calls_made}")
    print(f"Processed: {processed}")
    print(f"Persisted: {persisted}")
    print(f"Failed: {failed}")
    print(f"Skipped (missing markdown): {skipped_missing_md}")
    print("Stopped after max calls. Await approval before continuing.")

if __name__ == '__main__':
    main()
