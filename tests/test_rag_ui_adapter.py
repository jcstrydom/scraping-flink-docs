import json

from rag_ui.adapters import NaiveKGRAGBackend


def test_naive_kg_adapter_maps_engine_output(tmp_path):
    graph = {
        "created_at": "2026-03-05T00:00:00Z",
        "sections": [{"section_id": "s1", "page_id": "p1", "url": "https://example.com", "file_path": "/tmp/a.md", "heading": "H", "text": "T"}],
        "chunks": [{"chunk_id": "c1", "section_id": "s1", "page_id": "p1", "url": "https://example.com", "heading": "H", "text": "checkpoint latency"}],
        "nodes": [{"node_id": "concept:checkpoint", "type": "concept", "label": "checkpoint", "section_id": "s1", "page_id": "p1", "url": "https://example.com", "evidence": "checkpoint"}],
        "edges": [{"source": "s1", "target": "concept:checkpoint", "type": "mentions", "evidence": "checkpoint"}],
        "indexes": {
            "node": {
                "doc_tokens": {"concept:checkpoint": {"concept": 1, "checkpoint": 1}},
                "df": {"concept": 1, "checkpoint": 1},
                "doc_len": {"concept:checkpoint": 2},
                "num_docs": 1,
                "avgdl": 2.0,
            },
            "chunk": {
                "doc_tokens": {"c1": {"checkpoint": 1, "latency": 1}},
                "df": {"checkpoint": 1, "latency": 1},
                "doc_len": {"c1": 2},
                "num_docs": 1,
                "avgdl": 2.0,
            },
        },
    }

    graph_path = tmp_path / "graph.json"
    graph_path.write_text(json.dumps(graph), encoding="utf-8")

    backend = NaiveKGRAGBackend(graph_path=str(graph_path))
    result = backend.query("checkpoint latency")

    assert result.nodes
    assert result.nodes[0].node_type == "concept"
    assert result.evidence
    assert result.evidence[0].url == "https://example.com"
