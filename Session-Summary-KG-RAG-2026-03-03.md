# Session Summary: Flink KG + RAG Direction

Date: 2026-03-03

## What We Clarified
1. **Naive RAG flow** was confirmed as valid:
- chunk docs -> embed chunks -> embed query -> similarity search -> send top-k chunks + question to LLM.

2. **Document-centric / Graph-augmented RAG** was refined:
- embeddings remain the primary entry-point retrieval,
- graph structure is used for expansion, constraints, and reasoning,
- edges are usually not embedded; node text is embedded.

3. **Important conceptual distinction**:
- A docs graph helps navigate documentation semantics.
- A real operational KG models runtime behavior and troubleshooting.

## Files Created This Session
1. `Ontology-Flink-Operational-Optimization.md`
- Operational ontology for troubleshooting and performance optimization.
- Includes entities such as Job/Operator/Metric/Incident/Remediation.

2. `Ontology-Flink-Knowledge-Middle-Ground.md`
- Middle-ground ontology (current recommended starting point).
- Focuses on concepts, APIs, config options, tradeoffs, failure modes, mitigations, and version changes.
- Designed for docs-derived reasoning before live job telemetry is available.

## Recommended Current Direction
Start with the middle-ground ontology because you are not yet running production Flink jobs.

Why:
1. It supports richer reasoning than simple docs traversal.
2. It directly supports version-change analysis.
3. It avoids overfitting to operational entities you cannot populate yet.

## Practical Next Step Plan (Next Session)
1. Pick 20-50 high-value docs pages (version, config, state/checkpointing, time/watermarks, connectors).
2. Implement extraction pipeline for:
- `DocSection`, `Concept`, `API`, `ConfigOption`, `Version`, `VersionChange`, `FailureMode`, `Mitigation`, `Tradeoff`, `Pattern`.
3. Load graph and validate with competency questions.
4. Build hybrid retrieval:
- vector retrieval for entry points,
- 1-2 hop graph expansion,
- evidence reranking and citation packaging.

## Initial Competency Questions to Validate
1. What changed in checkpointing behavior between versions X and Y?
2. Which config options most influence checkpoint duration and state size?
3. Which APIs/patterns are recommended for low-latency event-time processing?
4. What failure modes are linked to backpressure and what mitigations are documented?

## Open Decisions for Next Time
1. Graph backend choice (Neo4j vs RDF stack).
2. Canonical ID strategy for nodes (`flink:<type>:<normalized-key>`).
3. Confidence threshold for auto-created edges.
4. Which Flink versions to baseline first.

## Resume Prompt
Use this when resuming:

"Continue from `Ontology-Flink-Knowledge-Middle-Ground.md`. Help me implement extraction + graph load for a first 30-page Flink docs subset, including `VersionChange` and `ConfigOption` mappings."
