# Ontology: Flink Knowledge (Middle Ground)

## Purpose
Build a knowledge graph that supports reasoning about Apache Flink design, tuning tradeoffs, and version differences from documentation, without requiring live production telemetry yet.

This sits between:
- docs-only graph navigation, and
- full operational incident graph.

## Scope (v1)
Primary use cases:
1. Explain core Flink concepts and how they relate.
2. Compare APIs/features/config behavior across Flink versions.
3. Recommend implementation/tuning patterns with tradeoffs.
4. Link failure modes to likely causes and mitigations from docs/runbooks.

## Competency Questions
Your graph should answer questions like:
1. What changed for checkpointing behavior between Flink versions X and Y?
2. Which configs affect checkpoint duration and state size tradeoffs?
3. When should I use `KeyedProcessFunction` vs window operators?
4. What are common causes of backpressure and documented mitigations?
5. Which connector options impact latency vs throughput?
6. Which APIs are deprecated, and what should replace them?

## Core Classes
1. `DocSource`
- Represents an original documentation source URL or section root.

2. `DocPage`
- One scraped markdown file representing a page.

3. `DocSection`
- Section/subsection within a page.

4. `Concept`
- Domain concept such as watermark, checkpoint, backpressure, event time.

5. `API`
- Flink API surface: classes/interfaces/functions/operators.

6. `ConfigOption`
- Configuration key + metadata (default, type, scope, version lifecycle).

7. `Pattern`
- Reusable solution approach (e.g., async I/O enrichment, event-time windows).

8. `Tradeoff`
- Explicit engineering tradeoff (latency/throughput, consistency/cost).

9. `FailureMode`
- Documented anti-pattern/problem (state blowup, checkpoint timeout).

10. `Mitigation`
- Practical remediation guidance.

11. `Version`
- Flink release version (e.g., `1.17`, `1.18`, `2.0`).

12. `VersionChange`
- A specific change event tied to versions (introduced/changed/deprecated/removed).

## Key Relationships
Document structure:
1. `DocSource hasPage DocPage`
2. `DocPage hasSection DocSection`
3. `DocSection cites DocSource`

Semantics:
4. `DocSection defines Concept`
5. `DocSection mentions Concept`
6. `DocSection describes API`
7. `DocSection documents ConfigOption`
8. `DocSection describes Pattern`
9. `DocSection describes FailureMode`
10. `DocSection recommends Mitigation`

Reasoning layer:
11. `Concept relatedTo Concept`
12. `Pattern usesAPI API`
13. `Pattern affects Tradeoff`
14. `ConfigOption affects Tradeoff`
15. `FailureMode hasMitigation Mitigation`
16. `FailureMode associatedWith Concept`
17. `API dependsOn Concept`

Versioning:
18. `VersionChange affects Concept`
19. `VersionChange affects API`
20. `VersionChange affects ConfigOption`
21. `VersionChange fromVersion Version`
22. `VersionChange toVersion Version`
23. `VersionChange changeType {introduced|changed|deprecated|removed}`

## Suggested Node Properties
Common provenance properties:
- `source_url`
- `page_title`
- `section_heading`
- `file_path`
- `evidence_text`
- `confidence`
- `extracted_at`

Class-specific examples:
- `ConfigOption`: `key`, `default_value`, `value_type`, `scope`, `stability`
- `API`: `fqcn_or_symbol`, `module`, `status`
- `VersionChange`: `change_summary`, `change_type`, `effective_version`

## Ingestion Rules from Scraped Markdown
1. Parse headings to create `DocSection` hierarchy.
2. Extract code identifiers and Flink symbols to propose `API` nodes.
3. Extract backticked config keys to create `ConfigOption` nodes.
4. Detect version phrases (`since`, `deprecated in`, release notes refs) to create `Version` + `VersionChange`.
5. Extract causal language (`causes`, `leads to`, `avoid`, `recommended`) for `FailureMode`/`Mitigation` and `Tradeoff` edges.
6. Store short evidence spans on edges/nodes for traceability.
7. Keep low-confidence extractions as candidate nodes until reviewed.

## Retrieval Pattern (for RAG)
At query time:
1. Embed query.
2. Retrieve top-k candidate chunks and/or semantic nodes (`Concept`, `API`, `ConfigOption`, `VersionChange`).
3. Anchor into graph with those hits.
4. Traverse 1-2 hops with relation filters (e.g., `affects`, `hasMitigation`, `fromVersion/toVersion`).
5. Collect supporting evidence sections.
6. Rerank and pass final context to LLM with citations.

## Why This Middle Ground Works
- More expressive than docs-only chunk retrieval.
- No requirement for production telemetry or incident data.
- Captures version evolution and design/tuning reasoning.
- Creates a clean path to operational graph expansion later.

## Expansion Path (Later)
When you start running jobs, add:
- `Job`, `Operator`, `Metric`, `Incident`, `Environment`
- links from runtime incidents back to the same `Concept`/`ConfigOption`/`Pattern` nodes.

This avoids rebuilding the model and keeps continuity from learning -> design -> operations.
