import hashlib

from firecrawl_scraper.models.processdata import ResponseProcessor


def test_parse_raw_response_uses_canonical_url_hash_for_page_id():
    processor = ResponseProcessor(root_url="https://example.com/docs/root")
    raw_response = {
        "metadata": {"title": "Page", "url": "https://example.com/docs/topic/"},
        "markdown": "# Topic\n\nText",
    }

    parsed = processor.parse_raw_response(raw_response, ask_ollama=False)

    expected_url = "https://example.com/docs/topic"
    expected_page_id = hashlib.sha256(expected_url.encode("utf-8")).hexdigest()
    assert parsed["page_id"] == expected_page_id


def test_extract_markdown_links_deduplicates_anchors_and_skips_images():
    processor = ResponseProcessor(root_url="https://example.com/docs/root")
    markdown = (
        "![img](https://example.com/docs/image.png)\n"
        "[One](https://example.com/docs/a#first)\n"
        "[Two](https://example.com/docs/a#second)\n"
        "[Other](https://other.example/docs/z)\n"
    )

    links = processor.extract_markdown_links(markdown)

    assert links == [("One", "https://example.com/docs/a"), ("Other", "https://other.example/docs/z")]


def test_save_markdown_file_keeps_human_prefix_and_uses_url_hash_when_missing_page_id(tmp_path):
    processor = ResponseProcessor(root_url="https://example.com/docs/root")
    data = {"prefix": "My Prefix/Topic", "url": "https://example.com/docs/file"}
    content = "# content"

    processor.save_markdown_file(data, content, save_dir=str(tmp_path))

    page_id = hashlib.sha256("https://example.com/docs/file".encode("utf-8")).hexdigest()
    expected_file = tmp_path / f"my_prefix_topic_{page_id}.md"
    assert expected_file.exists()
    assert expected_file.read_text(encoding="utf-8") == content
