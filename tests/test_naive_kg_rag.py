import json

from flink_rag.naive_kg_rag import NaiveKGRAGBuilder, NaiveKGRAGEngine


def test_split_sections_and_entity_extraction():
    builder = NaiveKGRAGBuilder()
    markdown = """# Checkpointing\ncheckpoint latency and backpressure are related.\n\nUse `KeyedProcessFunction`.\nconfig key: execution.checkpointing.interval\n\n## Versions\nIntroduced in Flink 1.19 and changed in 1.20.\n"""

    sections = builder._split_sections(
        markdown=markdown,
        page_id="p1",
        url="https://example.com/docs/checkpoints",
        file_path="/tmp/p1.md",
    )

    assert len(sections) >= 2

    nodes, edges = builder._extract_entities(sections[0])
    node_types = {node["type"] for node in nodes}
    assert "concept" in node_types
    assert "api" in node_types
    assert "config_option" in node_types
    assert any(edge["type"] == "mentions" for edge in edges)


def test_kg_first_query_returns_contexts(tmp_path):
    graph = {
        "created_at": "2026-03-05T00:00:00Z",
        "sections": [
            {
                "section_id": "section:p1:0",
                "page_id": "p1",
                "url": "https://example.com/docs/checkpoints",
                "file_path": "/tmp/p1.md",
                "heading": "Checkpointing",
                "text": "checkpoint interval controls latency.",
            }
        ],
        "chunks": [
            {
                "chunk_id": "chunk:section:p1:0:0",
                "section_id": "section:p1:0",
                "page_id": "p1",
                "url": "https://example.com/docs/checkpoints",
                "heading": "Checkpointing",
                "text": "execution.checkpointing.interval influences checkpoint latency.",
            }
        ],
        "nodes": [
            {
                "node_id": "config_option:execution.checkpointing.interval",
                "type": "config_option",
                "label": "execution.checkpointing.interval",
                "section_id": "section:p1:0",
                "page_id": "p1",
                "url": "https://example.com/docs/checkpoints",
                "evidence": "execution.checkpointing.interval influences checkpoint latency",
            }
        ],
        "edges": [
            {
                "source": "section:p1:0",
                "target": "config_option:execution.checkpointing.interval",
                "type": "mentions",
                "evidence": "execution.checkpointing.interval",
            }
        ],
        "indexes": {
            "node": {
                "doc_tokens": {
                    "config_option:execution.checkpointing.interval": {
                        "config_option": 1,
                        "execution.checkpointing.interval": 1,
                        "checkpoint": 1,
                        "latency": 1,
                    }
                },
                "df": {
                    "config_option": 1,
                    "execution.checkpointing.interval": 1,
                    "checkpoint": 1,
                    "latency": 1,
                },
                "doc_len": {"config_option:execution.checkpointing.interval": 4},
                "num_docs": 1,
                "avgdl": 4.0,
            },
            "chunk": {
                "doc_tokens": {
                    "chunk:section:p1:0:0": {
                        "execution.checkpointing.interval": 1,
                        "checkpoint": 1,
                        "latency": 1,
                        "influences": 1,
                    }
                },
                "df": {
                    "execution.checkpointing.interval": 1,
                    "checkpoint": 1,
                    "latency": 1,
                    "influences": 1,
                },
                "doc_len": {"chunk:section:p1:0:0": 4},
                "num_docs": 1,
                "avgdl": 4.0,
            },
        },
    }

    graph_path = tmp_path / "naive_kg_rag.json"
    graph_path.write_text(json.dumps(graph), encoding="utf-8")

    engine = NaiveKGRAGEngine(graph_path=str(graph_path))
    result = engine.query("Which config controls checkpoint latency?", top_nodes=3, top_chunks=3, hops=1)

    assert result["contexts"]
    assert result["top_nodes"]
    assert result["top_nodes"][0]["type"] == "config_option"
