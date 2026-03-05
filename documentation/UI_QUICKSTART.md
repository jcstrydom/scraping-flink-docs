# RAG UI Quickstart

## Design Goal
The UI is separated from RAG internals through a backend contract:
- UI depends on `RAGBackend` protocol only.
- Backend adapters map any engine output into stable UI response objects.

This keeps UX stable when replacing RAG implementations.

## Package Layout
- `rag_ui/backend.py`: backend protocol + data contract.
- `rag_ui/adapters.py`: adapter for current `NaiveKGRAGEngine`.
- `rag_ui/app.py`: FastAPI app (routes + API schema).
- `rag_ui/static/index.html`: frontend UI.
- `rag_ui/main.py`: default app entrypoint.

## Swapping Backends (No UI Changes)
Implement the `RAGBackend` protocol and pass it to `create_app()`:

```python
from rag_ui.app import create_app
from rag_ui.backend import BackendQueryResult, EvidenceItem, NodeItem

class MyBackend:
    def query(self, question: str, top_nodes: int = 6, top_chunks: int = 6, hops: int = 1) -> BackendQueryResult:
        return BackendQueryResult(
            question=question,
            nodes=[NodeItem(node_id="concept:x", node_type="concept", label="x")],
            evidence=[EvidenceItem(heading="h", url="u", file_path=None, text="t", score=1.0)],
        )

app = create_app(MyBackend())
```

## Run
Make sure a graph artifact exists:
```bash
uv run python -m flink_rag.build --max-pages 30
```

Start the UI:
```bash
uv run uvicorn rag_ui.main:app --reload --port 8000
```

Open:
- `http://127.0.0.1:8000`

## Tests
```bash
uv run --with pytest python -m pytest -q tests/test_rag_ui_app.py tests/test_rag_ui_adapter.py tests/test_rag_ui_static.py
```
