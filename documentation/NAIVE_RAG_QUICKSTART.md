# Naive RAG Quickstart

## Goal
Use a chunk-only lexical baseline first, while still keeping a KG-assisted mode available for comparison.

## Build
```bash
uv run python -m flink_rag.build --max-pages 30
```

Output artifacts:
- `data/rag/naive_rag.json`
- `data/rag/kg_rag.json`

Automatic evaluation output:
- `data/rag/evals/latest.json`

## Query
```bash
uv run python -m flink_rag.query "Which config options affect checkpoint latency?"
```

Optional KG-assisted mode:
```bash
uv run python -m flink_rag.query --mode kg "Which config options affect checkpoint latency?"
```

Explicit artifact overrides:
```bash
uv run python -m flink_rag.query --mode naive --naive-graph data/rag/naive_rag.json "..."
uv run python -m flink_rag.query --mode kg --kg-graph data/rag/kg_rag.json "..."
```

Response includes:
- `top_nodes`: empty in naive mode, populated in KG mode
- `contexts`: chunk evidence with `url` and `file_path` citations

## Current Retrieval Flows
Naive mode (`--mode naive`, default):
1. BM25 rank chunks directly.
2. Return top evidence chunks.

KG mode (`--mode kg`):
1. BM25 rank KG nodes.
2. Anchor to sections linked to top nodes.
3. Optional 1-hop `related_to` expansion.
4. Blend with chunk BM25 scores.
5. Return top evidence chunks.

## Notes
- Naive mode is the baseline and usually the best first quality/performance checkpoint.
- KG mode remains available for controlled A/B comparison.
- Query-time logic only reads prebuilt artifacts and indexes; it does not build chunks or graph data on the fly.
