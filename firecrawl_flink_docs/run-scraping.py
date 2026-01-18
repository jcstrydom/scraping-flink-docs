import requests

url = "https://api.firecrawl.dev/v2/scrape"

payload = {
  "url": "https://nightlies.apache.org/flink/flink-docs-release-1.20/docs/dev/datastream/overview/",
  "onlyMainContent": False,
  "maxAge": 172800000,
  "parsers": [
    "pdf"
  ],
  "formats": [
    "markdown"
  ]
}

headers = {
    "Authorization": "Bearer fc-24d13097a6024b0cae93ab6ff1b55b94",
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

# print(response.json())

with open("flink_firecrawl_output.json", "w", encoding="utf-8") as f:
    f.write(response.text)