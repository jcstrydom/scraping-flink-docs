# Naive KG-First RAG Quickstart

## Goal
Build a docs-first retrieval pipeline where query handling starts from KG nodes and then gathers chunk evidence.

## Build
```bash
uv run python -m flink_rag.build --max-pages 30
```

Output artifact:
- `data/rag/naive_kg_rag.json`

## Query
```bash
uv run python -m flink_rag.query "Which config options affect checkpoint latency?"
```

Response includes:
- `top_nodes`: KG anchors (concept/api/config/version)
- `contexts`: chunk evidence with `url` and `file_path` citations

## Current Retrieval Flow
1. BM25 rank KG nodes.
2. Anchor to sections linked to top nodes.
3. Optional 1-hop `related_to` expansion.
4. Blend with chunk BM25 scores.
5. Return top evidence chunks.

## Notes
- This implementation is intentionally heuristic and lightweight.
- It is suitable as a baseline before adding embedding-based reranking or a graph database backend.
