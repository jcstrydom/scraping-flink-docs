from firecrawl_scraper.models.metadata_enricher import MetadataEnricher


def test_parse_combined_metadata_payload_from_json_block():
    enricher = MetadataEnricher()
    markdown = "# Title\n## Section"
    response = """```json
    {"slug":"docs","summary":"Overview of docs","headings":[{"level":1,"text":"Title"}]}
    ```"""

    parsed = enricher._parse_combined_metadata_payload(response, markdown)

    assert parsed["slug"] == "docs"
    assert parsed["summary"] == "Overview of docs"
    assert parsed["headings"] == [{"level": 1, "text": "Title"}]
