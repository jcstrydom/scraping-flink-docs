import json

from flink_rag.naive_kg_rag import NaiveKGRAGBuilder, NaiveKGRAGEngine, NaiveRAGEngine, run_eval


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


def test_naive_query_requires_prebuilt_chunk_index(tmp_path):
    graph = {
        "created_at": "2026-03-05T00:00:00Z",
        "mode": "naive",
        "sections": [],
        "chunks": [],
        "indexes": {},
    }
    graph_path = tmp_path / "naive.json"
    graph_path.write_text(json.dumps(graph), encoding="utf-8")

    try:
        NaiveRAGEngine(graph_path=str(graph_path))
    except ValueError as exc:
        assert "missing chunk index" in str(exc)
    else:
        raise AssertionError("Expected ValueError when chunk index is missing")


def test_run_eval_outputs_report(tmp_path):
    naive_graph = {
        "created_at": "2026-03-05T00:00:00Z",
        "mode": "naive",
        "sections": [{"section_id": "s1", "page_id": "p1", "url": "https://example.com", "file_path": "/tmp/a.md", "heading": "Checkpointing", "text": "checkpoint interval"}],
        "chunks": [{"chunk_id": "c1", "section_id": "s1", "page_id": "p1", "url": "https://example.com", "heading": "Checkpointing", "text": "checkpoint interval affects latency"}],
        "indexes": {
            "chunk": {
                "doc_tokens": {"c1": {"checkpoint": 1, "interval": 1, "latency": 1}},
                "df": {"checkpoint": 1, "interval": 1, "latency": 1},
                "doc_len": {"c1": 3},
                "num_docs": 1,
                "avgdl": 3.0,
            },
        },
    }
    kg_graph = {
        "created_at": "2026-03-05T00:00:00Z",
        "mode": "kg",
        "sections": [{"section_id": "s1", "page_id": "p1", "url": "https://example.com", "file_path": "/tmp/a.md", "heading": "Checkpointing", "text": "checkpoint interval"}],
        "chunks": [{"chunk_id": "c1", "section_id": "s1", "page_id": "p1", "url": "https://example.com", "heading": "Checkpointing", "text": "checkpoint interval affects latency"}],
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
                "doc_tokens": {"c1": {"checkpoint": 1, "interval": 1, "latency": 1}},
                "df": {"checkpoint": 1, "interval": 1, "latency": 1},
                "doc_len": {"c1": 3},
                "num_docs": 1,
                "avgdl": 3.0,
            },
        },
    }

    naive_path = tmp_path / "naive.json"
    kg_path = tmp_path / "kg.json"
    questions_path = tmp_path / "questions.md"
    report_path = tmp_path / "eval.json"
    naive_path.write_text(json.dumps(naive_graph), encoding="utf-8")
    kg_path.write_text(json.dumps(kg_graph), encoding="utf-8")
    questions_path.write_text("1. Which option controls checkpoint interval?\n2. How is checkpoint latency tuned?\n", encoding="utf-8")

    report = run_eval(
        naive_graph_path=str(naive_path),
        kg_graph_path=str(kg_path),
        eval_questions_path=str(questions_path),
        output_path=str(report_path),
        top_chunks=2,
    )

    assert report_path.exists()
    assert report["summary"]["naive"]["questions_evaluated"] == 2
    assert report["summary"]["kg"]["questions_evaluated"] == 2
