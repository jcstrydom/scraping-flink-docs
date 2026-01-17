import scrapy
from bs4 import BeautifulSoup
from datetime import datetime
from flink_docs.items import FlinkDocItem

class FlinkSpider(scrapy.Spider):
    name = "flink_docs"

    start_urls = [
        # Flink 1.19 example page
        "https://nightlies.apache.org/flink/flink-docs-release-1.19/docs/dev/datastream/overview/",
        # Flink 2.1 example page (flink-stable assumed to be 2.1 now)
        "https://nightlies.apache.org/flink/flink-docs-stable/docs/dev/table/"
    ]

    def parse(self, response):
        self.logger.info(f"Parsing URL: {response.url}")
        soup = BeautifulSoup(response.text, "html.parser")

        # Detect version
        if "flink-docs-release-1.19" in response.url:
            version = "1.19"
        elif "flink-docs-stable" in response.url:
            version = "2.1"
        else:
            version = "unknown"

        # Extract title
        title = soup.find("h1")
        title_text = title.get_text(strip=True) if title else "Untitled"

        # Extract content and convert to markdown
        content_div = soup.find("main") or soup  # docs pages use <main>
        markdown_content = self.html_to_markdown(content_div)

        # Extract child links
        child_links = []
        for a in soup.find_all("a", href=True):
            href = a['href']
            if href.startswith("http") and "flink" in href:
                child_links.append(href)
            elif href.startswith("/") and not href.startswith("//"):
                # Convert relative URLs to absolute
                base_url = "/".join(response.url.split("/")[:3])
                child_links.append(base_url + href)

        item = FlinkDocItem()
        item['title'] = title_text
        item['url'] = response.url
        item['version'] = version
        item['crawl_run'] = datetime.now().strftime("%Y%m%d_poc")
        item['crawl_timestamp'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        item['provenance'] = response.url.split("/")[2]
        item['child_links'] = child_links
        item['markdown_content'] = markdown_content
        
        self.logger.info(f"About to yield item with title: {title_text}")
        self.logger.info(f"Item keys: {list(item.keys())}")
        yield item
        self.logger.info(f"Item yielded successfully")

    def html_to_markdown(self, container):
        lines = []
        processed_elements = set()

        for el in container.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'pre', 'table', 'blockquote']):
            if id(el) in processed_elements:
                continue
            processed_elements.add(id(el))

            if el.name and el.name.startswith("h") and el.name[1].isdigit():
                level = int(el.name[1])
                text = el.get_text(strip=True)
                if text:
                    lines.append("#" * level + " " + text)
            elif el.name == "p":
                text = el.get_text(strip=True)
                if text:
                    lines.append(text)
            elif el.name == "pre":
                code_text = el.get_text()
                if code_text.strip():
                    lines.append("```")
                    lines.append(code_text)
                    lines.append("```")
            elif el.name == "table":
                rows = []
                for row in el.find_all("tr"):
                    cols = [col.get_text(strip=True) for col in row.find_all(["td", "th"])]
                    if cols:
                        rows.append("| " + " | ".join(cols) + " |")
                if rows:
                    lines.extend(rows)
            elif el.name == "blockquote":
                text = el.get_text(strip=True)
                if text:
                    lines.append("> " + text)

        return "\n\n".join(filter(None, lines))