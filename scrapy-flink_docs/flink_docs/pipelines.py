# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# # useful for handling different item types with a single interface
# from itemadapter import ItemAdapter


# class FlinkDocsPipeline:
#     def process_item(self, item, spider):
#         return item


import os
import sqlite3
from datetime import datetime

class FlinkDocPipeline:
    def open_spider(self, spider):
        self.conn = sqlite3.connect("metadata.sqlite")
        self.cur = self.conn.cursor()
        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS documents (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            url TEXT,
            version TEXT,
            crawl_run TEXT,
            crawl_timestamp TEXT,
            provenance TEXT,
            child_links TEXT
        )
        """)
        self.conn.commit()

    def process_item(self, item, spider):
        # Save metadata
        self.cur.execute("""
        INSERT INTO documents (title, url, version, crawl_run, crawl_timestamp, provenance, child_links)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            item['title'],
            item['url'],
            item['version'],
            item['crawl_run'],
            item['crawl_timestamp'],
            item['provenance'],
            ",".join(item['child_links'])
        ))
        self.conn.commit()

        # Save Markdown
        out_dir = os.path.join("content", item['version'])
        os.makedirs(out_dir, exist_ok=True)
        # Create filename from title, version, and timestamp
        title_slug = self.slugify(item['title'])
        timestamp = item['crawl_timestamp'].replace(" ", "_").replace(":", "-")
        filename = os.path.join(out_dir, f"flink-{item['version']}_{title_slug}_{timestamp}.md")
        with open(filename, "w", encoding="utf-8") as f:
            f.write(item['markdown_content'])

        return item

    def slugify(self, text):
        return "".join(c if c.isalnum() else "-" for c in text.lower()).strip("-")

    def close_spider(self, spider):
        self.conn.close()