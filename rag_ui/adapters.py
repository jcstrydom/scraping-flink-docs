from __future__ import annotations

from pathlib import Path

from flink_rag.naive_kg_rag import NaiveKGRAGEngine

from .backend import BackendQueryResult, EvidenceItem, NodeItem


class NaiveKGRAGBackend:
    """Adapter from current naive KG-RAG engine to UI backend protocol."""

    def __init__(self, graph_path: str = "data/rag/naive_kg_rag.json"):
        graph = Path(graph_path)
        if graph.is_absolute():
            resolved = graph
        else:
            resolved = Path(__file__).resolve().parents[1] / graph
        self.engine = NaiveKGRAGEngine(graph_path=str(resolved))

    def query(self, question: str, top_nodes: int = 6, top_chunks: int = 6, hops: int = 1) -> BackendQueryResult:
        raw = self.engine.query(question=question, top_nodes=top_nodes, top_chunks=top_chunks, hops=hops)

        nodes = [
            NodeItem(
                node_id=str(item.get("node_id", "")),
                node_type=str(item.get("type", "")),
                label=str(item.get("label", "")),
            )
            for item in raw.get("top_nodes", [])
        ]

        evidence = [
            EvidenceItem(
                heading=str(item.get("heading", "")),
                url=str(item.get("url", "")),
                file_path=item.get("file_path"),
                text=str(item.get("text", "")),
                score=float(item.get("score", 0.0)),
            )
            for item in raw.get("contexts", [])
        ]

        return BackendQueryResult(question=question, nodes=nodes, evidence=evidence)
