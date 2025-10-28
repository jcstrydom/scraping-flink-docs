from firecrawl import Firecrawl

firecrawl = Firecrawl(api_key='fc-24d13097a6024b0cae93ab6ff1b55b94')

# Crawl with scrape options
response = firecrawl.crawl('https://example.com',
    limit=100,
    scrape_options={
        'formats': [
            'markdown',
            { 'type': 'json', 'schema': { 'type': 'object', 'properties': { 'title': { 'type': 'string' } } } }
        ],
        'proxy': 'auto',
        'maxAge': 600000,
        'onlyMainContent': True
    }
)