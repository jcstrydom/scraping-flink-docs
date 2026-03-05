from __future__ import annotations

from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel, Field

from .backend import RAGBackend


class QueryRequest(BaseModel):
    question: str = Field(min_length=2, max_length=2000)
    top_nodes: int = Field(default=6, ge=1, le=30)
    top_chunks: int = Field(default=6, ge=1, le=30)
    hops: int = Field(default=1, ge=0, le=2)


class NodeResponse(BaseModel):
    node_id: str
    node_type: str
    label: str


class EvidenceResponse(BaseModel):
    heading: str
    url: str
    file_path: str | None
    text: str
    score: float


class QueryResponse(BaseModel):
    question: str
    nodes: list[NodeResponse]
    evidence: list[EvidenceResponse]


def create_app(backend: RAGBackend) -> FastAPI:
    app = FastAPI(title="RAG UI", version="0.1.0")
    static_dir = Path(__file__).resolve().parent / "static"

    @app.get("/health")
    def health() -> dict[str, str]:
        return {"status": "ok"}

    @app.get("/")
    def index() -> FileResponse:
        return FileResponse(static_dir / "index.html")

    @app.post("/api/query", response_model=QueryResponse)
    def query(request: QueryRequest) -> QueryResponse:
        try:
            result = backend.query(
                question=request.question,
                top_nodes=request.top_nodes,
                top_chunks=request.top_chunks,
                hops=request.hops,
            )
        except Exception as exc:
            raise HTTPException(status_code=500, detail=f"Backend query failed: {exc}") from exc

        return QueryResponse(
            question=result.question,
            nodes=[
                NodeResponse(node_id=node.node_id, node_type=node.node_type, label=node.label)
                for node in result.nodes
            ],
            evidence=[
                EvidenceResponse(
                    heading=item.heading,
                    url=item.url,
                    file_path=item.file_path,
                    text=item.text,
                    score=item.score,
                )
                for item in result.evidence
            ],
        )

    return app
