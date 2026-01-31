import os
import sqlite3
import polars as pl

# Step 1: List all markdown files
md_dir = os.path.join(os.path.dirname(__file__), "data", "markdown_files")
md_files = [f for f in os.listdir(md_dir) if f.endswith(".md")]

# Step 2: Extract page_ids from filenames
def extract_page_id(filename):
    # Assumes format: ..._<page_id>.md
    base = os.path.splitext(filename)[0]
    return base.split("_")[-1]

md_page_ids = set(extract_page_id(f) for f in md_files)

# Build polars DataFrame for markdown files: columns are 'page_id'
md_df = pl.DataFrame({
    "page_id": list(md_page_ids),
    "md_exists": [True] * len(md_page_ids),
})

# Step 3: Read all page_ids and prefix from the DB
db_path = os.path.join(os.path.dirname(__file__), "data", "scraping.db")
conn = sqlite3.connect(db_path)
cur = conn.cursor()
cur.execute("SELECT page_id, prefix FROM pages")
db_rows = cur.fetchall()
conn.close()

# Build polars DataFrame for DB rows: columns are 'page_id', 'prefix'
db_df = pl.DataFrame({
    "page_id": [row[0] for row in db_rows],
    "prefix": [row[1] for row in db_rows],
})

# Left join db_df to md_df on 'page_id'
joined_df = db_df.join(md_df, on="page_id", how="left")


# Filter: only show DB records where markdown file is missing
deleted_recs = joined_df.filter(pl.col.md_exists.is_null()).shape[0]

print(f"Total records in DB without corresponding markdown file: {deleted_recs}")
joined_df.filter(pl.col.md_exists.is_null()).select(["page_id", "prefix"]).show()
