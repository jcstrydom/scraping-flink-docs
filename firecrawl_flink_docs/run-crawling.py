from firecrawl import Firecrawl
import dotenv
import os

dotenv.load_dotenv()
firecrawl = Firecrawl(api_key=os.getenv('FIRECRAWL_API_KEY'))

print("\n Starting crawl...")

# Crawl with scrape options
response = firecrawl.crawl('https://nightlies.apache.org/flink/flink-docs-release-1.20/docs/concepts/overview/',
    limit=10,
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



print("\n Crawl finished...\n Writing output to flink_firecrawl_output.json")

with open("flink_firecrawl_output.json", "w", encoding="utf-8") as f:
    f.write(response.text)

print("\n DONE!")

