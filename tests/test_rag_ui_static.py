from pathlib import Path


def test_static_index_contains_expected_ids():
    index_file = Path(__file__).resolve().parents[1] / "rag_ui" / "static" / "index.html"
    html = index_file.read_text(encoding="utf-8")

    assert "id=\"query-form\"" in html
    assert "id=\"question\"" in html
    assert "id=\"nodes\"" in html
    assert "id=\"evidence\"" in html
    assert "/api/query" in html
