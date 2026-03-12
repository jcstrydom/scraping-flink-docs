from __future__ import annotations

from pathlib import Path

from flink_rag.naive_kg_rag import (
    DEFAULT_KG_ARTIFACT_PATH,
    DEFAULT_NAIVE_ARTIFACT_PATH,
    NaiveKGRAGEngine,
    NaiveRAGEngine,
)

from .backend import BackendQueryResult, EvidenceItem, NodeItem


class NaiveRAGBackend:
    """Adapter from chunk-only naive RAG engine to UI backend protocol."""

    def __init__(self, graph_path: str = DEFAULT_NAIVE_ARTIFACT_PATH):
        graph = Path(graph_path)
        if graph.is_absolute():
            resolved = graph
        else:
            resolved = Path(__file__).resolve().parents[1] / graph
        self.engine = NaiveRAGEngine(graph_path=str(resolved))

    def query(
        self,
        question: str,
        top_nodes: int = 6,
        top_chunks: int = 6,
        hops: int = 1,
        mode: str = "naive",
    ) -> BackendQueryResult:
        raw = self.engine.query(question=question, top_chunks=top_chunks)

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

        return BackendQueryResult(question=question, nodes=[], evidence=evidence)


class NaiveKGRAGBackend:
    """Adapter from current naive KG-RAG engine to UI backend protocol."""

    def __init__(self, graph_path: str = DEFAULT_KG_ARTIFACT_PATH):
        graph = Path(graph_path)
        if graph.is_absolute():
            resolved = graph
        else:
            resolved = Path(__file__).resolve().parents[1] / graph
        self.engine = NaiveKGRAGEngine(graph_path=str(resolved))

    def query(
        self,
        question: str,
        top_nodes: int = 6,
        top_chunks: int = 6,
        hops: int = 1,
        mode: str = "kg",
    ) -> BackendQueryResult:
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


class DualRAGBackend:
    """Backend that routes between naive and KG artifacts based on request mode."""

    def __init__(
        self,
        naive_graph_path: str = DEFAULT_NAIVE_ARTIFACT_PATH,
        kg_graph_path: str = DEFAULT_KG_ARTIFACT_PATH,
    ):
        self.naive = NaiveRAGBackend(graph_path=naive_graph_path)
        self.kg = NaiveKGRAGBackend(graph_path=kg_graph_path)

    def query(
        self,
        question: str,
        top_nodes: int = 6,
        top_chunks: int = 6,
        hops: int = 1,
        mode: str = "naive",
    ) -> BackendQueryResult:
        if mode == "kg":
            return self.kg.query(
                question=question,
                top_nodes=top_nodes,
                top_chunks=top_chunks,
                hops=hops,
                mode=mode,
            )
        return self.naive.query(
            question=question,
            top_nodes=top_nodes,
            top_chunks=top_chunks,
            hops=hops,
            mode=mode,
        )
