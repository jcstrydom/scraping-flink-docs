# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FlinkDocsItem(scrapy.Item):
    title = scrapy.Field()
    url = scrapy.Field()
    version = scrapy.Field()
    crawl_run = scrapy.Field()
    crawl_timestamp = scrapy.Field()
    provenance = scrapy.Field()
    child_links = scrapy.Field()
    markdown_content = scrapy.Field()