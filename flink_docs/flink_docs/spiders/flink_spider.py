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
        child_links = [a['href'] for a in soup.find_all("a", href=True)
                       if a['href'].startswith("http") and "flink" in a['href']]

        yield FlinkDocItem(
            title=title_text,
            url=response.url,
            version=version,
            crawl_run=datetime.now().strftime("%Y%m%d_poc"),
            crawl_timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            provenance=response.url.split("/")[2],
            child_links=child_links,
            markdown_content=markdown_content
        )

    def html_to_markdown(self, container):
        lines = []
        for el in container.descendants:
            if el.name and el.name.startswith("h") and el.name[1].isdigit():
                level = int(el.name[1])
                lines.append("#" * level + " " + el.get_text(strip=True))
            elif el.name == "p":
                lines.append(el.get_text(strip=True))
            elif el.name == "code" and el.parent.name == "pre":
                lines.append("```")
                lines.append(el.get_text())
                lines.append("```")
            elif el.name == "table":
                rows = []
                for row in el.find_all("tr"):
                    cols = [col.get_text(strip=True) for col in row.find_all(["td", "th"])]
                    rows.append("| " + " | ".join(cols) + " |")
                if rows:
                    lines.extend(rows)
            elif el.name in ["blockquote", "div"] and "admonition" in el.get("class", []):
                lines.append("> " + el.get_text(strip=True))
        return "\n\n".join(lines)
