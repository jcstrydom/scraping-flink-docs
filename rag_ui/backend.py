from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol


@dataclass
class EvidenceItem:
    heading: str
    url: str
    file_path: str | None
    text: str
    score: float


@dataclass
class NodeItem:
    node_id: str
    node_type: str
    label: str


@dataclass
class BackendQueryResult:
    question: str
    nodes: list[NodeItem]
    evidence: list[EvidenceItem]


class RAGBackend(Protocol):
    """Stable query contract the UI depends on."""

    def query(self, question: str, top_nodes: int = 6, top_chunks: int = 6, hops: int = 1) -> BackendQueryResult:
        ...
