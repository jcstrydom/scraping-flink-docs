from fastapi.testclient import TestClient

from rag_ui.app import create_app
from rag_ui.backend import BackendQueryResult, EvidenceItem, NodeItem


class FakeBackend:
    def query(self, question: str, top_nodes: int = 6, top_chunks: int = 6, hops: int = 1) -> BackendQueryResult:
        return BackendQueryResult(
            question=question,
            nodes=[NodeItem(node_id="concept:checkpoint", node_type="concept", label="checkpoint")],
            evidence=[
                EvidenceItem(
                    heading="Checkpointing",
                    url="https://example.com/docs/checkpointing",
                    file_path="/tmp/checkpointing.md",
                    text="checkpoint interval impacts latency",
                    score=0.89,
                )
            ],
        )


class ErrorBackend:
    def query(self, question: str, top_nodes: int = 6, top_chunks: int = 6, hops: int = 1):
        raise RuntimeError("boom")


def test_health_and_index_route():
    client = TestClient(create_app(FakeBackend()))

    health = client.get("/health")
    assert health.status_code == 200
    assert health.json() == {"status": "ok"}

    index = client.get("/")
    assert index.status_code == 200
    assert "Flink Docs RAG" in index.text
    assert "query-form" in index.text


def test_api_status_ready():
    client = TestClient(create_app(FakeBackend()))
    resp = client.get("/api/status")
    assert resp.status_code == 200
    assert resp.json()["ready"] is True


def test_api_query_success():
    client = TestClient(create_app(FakeBackend()))

    resp = client.post(
        "/api/query",
        json={"question": "How do checkpoints affect latency?", "top_nodes": 4, "top_chunks": 4, "hops": 1},
    )

    assert resp.status_code == 200
    body = resp.json()
    assert body["question"] == "How do checkpoints affect latency?"
    assert len(body["nodes"]) == 1
    assert len(body["evidence"]) == 1
    assert body["nodes"][0]["node_type"] == "concept"


def test_api_query_validation_error_for_short_question():
    client = TestClient(create_app(FakeBackend()))

    resp = client.post("/api/query", json={"question": "x"})

    assert resp.status_code == 422


def test_api_query_backend_error_is_500():
    client = TestClient(create_app(ErrorBackend()))

    resp = client.post("/api/query", json={"question": "valid question"})

    assert resp.status_code == 500
    assert "Backend query failed" in resp.json()["detail"]


def test_api_query_unavailable_backend_is_503():
    def broken_factory():
        raise FileNotFoundError("missing graph file")

    client = TestClient(create_app(broken_factory))
    resp = client.post("/api/query", json={"question": "valid question"})
    assert resp.status_code == 503
    assert "Backend unavailable" in resp.json()["detail"]
