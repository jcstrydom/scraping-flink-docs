BOT_NAME = "flink_docs"
SPIDER_MODULES = ["flink_docs.spiders"]
NEWSPIDER_MODULE = "flink_docs.spiders"
ROBOTSTXT_OBEY = False
DOWNLOAD_DELAY = 1
CONCURRENT_REQUESTS = 2

# Enable JSON feed export
FEEDS = {
    'output.json': {
        'format': 'json',
        'overwrite': True,
    },
}

# Keep the pipeline for database storage (optional) - temporarily disabled
# ITEM_PIPELINES = {
#     "flink_docs.pipelines.FlinkDocPipeline": 300,
# }

LOG_LEVEL = "INFO"