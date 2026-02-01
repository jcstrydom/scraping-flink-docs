import os
import sqlite3
import polars as pl

# Set polars display options to show full string columns and more rows/cols
pl.Config.set_tbl_rows(100)
pl.Config.set_tbl_cols(100)
pl.Config.set_fmt_str_lengths(200)
pl.Config.set_tbl_width_chars(200)


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
deleted_recs = joined_df.filter(pl.col.md_exists.is_null()).shape[0]

print(f"Total records in DB without corresponding markdown file: {deleted_recs}")
with pl.Config(fmt_str_lengths=200):
    print(joined_df.filter(pl.col.md_exists.is_null()).select(["page_id", "prefix"]))

# Filter: only show DB records where markdown file is missing
missing_df = joined_df.filter(pl.col.md_exists.is_null())
missing_page_ids = missing_df["page_id"].to_list()

print(f"DB records missing markdown files: {len(missing_page_ids)}")
if missing_page_ids:
    print(missing_df)
else:
    print("No records to delete.")

# Step 4: Remove these records from the DB
if missing_page_ids:
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # Use parameterized query for safety
    # Split into batches if very large
    BATCH_SIZE = 100
    for i in range(0, len(missing_page_ids), BATCH_SIZE):
        batch = missing_page_ids[i:i+BATCH_SIZE]
        placeholders = ",".join(["?"] * len(batch))
        query = f"DELETE FROM pages WHERE page_id IN ({placeholders})"
        cur.execute(query, batch)
        print(f"Deleted {cur.rowcount} records from DB in batch {i//BATCH_SIZE+1}")
    conn.commit()
    conn.close()
    print(f"Total deleted: {len(missing_page_ids)}")


