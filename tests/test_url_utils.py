from firecrawl_scraper.models.url_utils import normalize_url


def test_normalize_url_lowercases_strips_default_ports_and_fragment():
    assert normalize_url("HTTPS://Example.com:443/docs/page/#intro") == "https://example.com/docs/page"


def test_normalize_url_handles_root_path():
    assert normalize_url("http://example.com:80/") == "http://example.com"
