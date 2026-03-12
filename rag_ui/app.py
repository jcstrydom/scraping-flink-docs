from __future__ import annotations

from collections.abc import Callable
from pathlib import Path
from typing import Literal

from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel, Field

from .backend import RAGBackend


class QueryRequest(BaseModel):
    question: str = Field(min_length=2, max_length=2000)
    mode: Literal["naive", "kg"] = "naive"
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
    mode: Literal["naive", "kg"]
    nodes: list[NodeResponse]
    evidence: list[EvidenceResponse]


def create_app(backend: RAGBackend | Callable[[], RAGBackend]) -> FastAPI:
    app = FastAPI(title="RAG UI", version="0.1.0")
    static_dir = Path(__file__).resolve().parent / "static"
    backend_instance: RAGBackend | None = None
    backend_error: str | None = None

    def resolve_backend() -> RAGBackend:
        nonlocal backend_instance, backend_error
        if backend_instance is not None:
            return backend_instance
        if backend_error is not None:
            raise RuntimeError(backend_error)

        try:
            if hasattr(backend, "query"):
                backend_instance = backend
            else:
                backend_instance = backend()
        except Exception as exc:
            backend_error = f"{type(exc).__name__}: {exc}"
            raise RuntimeError(backend_error) from exc
        return backend_instance

    @app.get("/health")
    def health() -> dict[str, str]:
        return {"status": "ok"}

    @app.get("/api/status")
    def backend_status() -> dict[str, str | bool]:
        try:
            resolve_backend()
            return {"ready": True, "error": "", "modes": "naive,kg"}
        except Exception as exc:
            return {"ready": False, "error": str(exc)}

    @app.get("/")
    def index() -> FileResponse:
        return FileResponse(static_dir / "index.html")

    @app.post("/api/query", response_model=QueryResponse)
    def query(request: QueryRequest) -> QueryResponse:
        try:
            resolved_backend = resolve_backend()
        except Exception as exc:
            raise HTTPException(
                status_code=503,
                detail=f"Backend unavailable. Build/check artifact and backend config. Cause: {exc}",
            ) from exc

        try:
            result = resolved_backend.query(
                question=request.question,
                top_nodes=request.top_nodes,
                top_chunks=request.top_chunks,
                hops=request.hops,
                mode=request.mode,
            )
        except Exception as exc:
            raise HTTPException(status_code=500, detail=f"Backend query failed: {exc}") from exc

        return QueryResponse(
            question=result.question,
            mode=request.mode,
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
