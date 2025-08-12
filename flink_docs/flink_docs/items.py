# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class FlinkDocItem(scrapy.Item):
    title = scrapy.Field()
    url = scrapy.Field()
    version = scrapy.Field()
    crawl_run = scrapy.Field()
    crawl_timestamp = scrapy.Field()
    provenance = scrapy.Field()
    child_links = scrapy.Field()  # list of URLs
    content_md_path = scrapy.Field()  # path to saved markdown file
