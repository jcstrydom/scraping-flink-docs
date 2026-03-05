from __future__ import annotations

import argparse
import json
import math
import re
from collections import Counter, defaultdict
from dataclasses import dataclass
from datetime import datetime, UTC
from pathlib import Path
from typing import Any

from firecrawl_scraper.models import DatabaseManager

_TOKEN_RE = re.compile(r"[a-zA-Z0-9_\-.]+")
_HEADING_RE = re.compile(r"^(#{1,6})\s+(.*)$")

_STOPWORDS = {
    "a", "an", "and", "are", "as", "at", "be", "by", "for", "from", "in", "into", "is", "it",
    "of", "on", "or", "that", "the", "this", "to", "with", "when", "which", "what", "how", "why",
}

_CONCEPTS = {
    "checkpoint", "checkpoints", "savepoint", "savepoints", "watermark", "watermarks", "backpressure",
    "state", "stateful", "event time", "processing time", "latency", "throughput", "window", "windows",
    "exactly-once", "at-least-once", "fault tolerance", "rocksdb", "operator state", "keyed state",
}

_API_HINT_RE = re.compile(r"`([A-Z][A-Za-z0-9_]*(?:\.[A-Z][A-Za-z0-9_]*)*)`")
_API_NAME_RE = re.compile(r"\b([A-Z][A-Za-z0-9_]*(?:Function|Operator|Source|Sink|ProcessFunction|Trigger))\b")
_CONFIG_RE = re.compile(r"\b([a-z][a-z0-9_-]*(?:\.[a-z0-9_-]+){1,})\b")
_VERSION_RE = re.compile(r"\b(?:flink\s*)?((?:1|2)\.\d{1,2})\b", re.IGNORECASE)
_CHANGE_RE = re.compile(r"\b(introduced|deprecated|removed|changed)\b", re.IGNORECASE)


@dataclass
class Section:
    section_id: str
    page_id: str
    url: str
    file_path: str
    heading: str
    text: str


@dataclass
class Chunk:
    chunk_id: str
    section_id: str
    page_id: str
    url: str
    heading: str
    text: str


def _tokenize(text: str) -> list[str]:
    return [
        t.lower()
        for t in _TOKEN_RE.findall(text)
        if len(t) > 2 and t.lower() not in _STOPWORDS and not t.startswith("http")
    ]


def _make_index(items: list[dict[str, Any]], text_key: str, id_key: str) -> dict[str, Any]:
    doc_tokens: dict[str, dict[str, int]] = {}
    df: Counter[str] = Counter()
    doc_len: dict[str, int] = {}

    for item in items:
        doc_id = item[id_key]
        counts = Counter(_tokenize(str(item.get(text_key, ""))))
        doc_tokens[doc_id] = dict(counts)
        doc_len[doc_id] = sum(counts.values())
        for token in counts:
            df[token] += 1

    avgdl = (sum(doc_len.values()) / len(doc_len)) if doc_len else 0.0
    return {
        "doc_tokens": doc_tokens,
        "df": dict(df),
        "doc_len": doc_len,
        "num_docs": len(doc_tokens),
        "avgdl": avgdl,
    }


def _bm25_score(query: str, index: dict[str, Any], k1: float = 1.2, b: float = 0.75) -> dict[str, float]:
    q_terms = _tokenize(query)
    if not q_terms:
        return {}

    num_docs = index["num_docs"]
    if num_docs == 0:
        return {}

    scores: defaultdict[str, float] = defaultdict(float)
    avgdl = index["avgdl"] or 1.0
    for term in q_terms:
        df = index["df"].get(term, 0)
        if df == 0:
            continue
        idf = math.log(1 + ((num_docs - df + 0.5) / (df + 0.5)))
        for doc_id, token_counts in index["doc_tokens"].items():
            tf = token_counts.get(term, 0)
            if tf == 0:
                continue
            dl = index["doc_len"].get(doc_id, 0)
            denom = tf + k1 * (1 - b + b * (dl / avgdl))
            scores[doc_id] += idf * ((tf * (k1 + 1)) / denom)
    return dict(scores)


class NaiveKGRAGBuilder:
    def __init__(self, data_dir: str = "data", db_path: str | None = None):
        self.project_root = Path(__file__).resolve().parents[1]
        self.data_dir = self.project_root / data_dir
        self.db_path = db_path

    def _resolve_markdown_path(self, page_id: str, page_prefix: str | None) -> Path | None:
        md_dir = self.data_dir / "markdown_files"
        if not md_dir.exists():
            return None

        if page_prefix:
            safe_prefix = re.sub(r"[^A-Za-z0-9_-]+", "_", page_prefix).strip("_").lower() or "page"
            candidate = md_dir / f"{safe_prefix}_{page_id}.md"
            if candidate.exists():
                return candidate

        matches = list(md_dir.glob(f"*_{page_id}.md"))
        return matches[0] if matches else None

    def _split_sections(self, markdown: str, page_id: str, url: str, file_path: str) -> list[Section]:
        lines = markdown.splitlines()
        if not lines:
            return []

        sections: list[Section] = []
        heading_stack: list[str] = ["root"]
        buffer: list[str] = []
        current_heading = "root"
        seq = 0

        def flush() -> None:
            nonlocal seq, buffer, current_heading
            text = "\n".join(buffer).strip()
            if text:
                section_id = f"section:{page_id}:{seq}"
                sections.append(
                    Section(
                        section_id=section_id,
                        page_id=page_id,
                        url=url,
                        file_path=file_path,
                        heading=current_heading,
                        text=text,
                    )
                )
                seq += 1
            buffer = []

        for line in lines:
            m = _HEADING_RE.match(line)
            if not m:
                buffer.append(line)
                continue

            flush()
            level = len(m.group(1))
            title = m.group(2).strip()
            while len(heading_stack) > level:
                heading_stack.pop()
            while len(heading_stack) < level:
                heading_stack.append(heading_stack[-1])
            heading_stack[level - 1:] = [title]
            current_heading = " > ".join(heading_stack)

        flush()
        return sections

    def _chunk_section(self, section: Section, max_chars: int = 900, overlap: int = 150) -> list[Chunk]:
        text = section.text.strip()
        if len(text) <= max_chars:
            return [
                Chunk(
                    chunk_id=f"chunk:{section.section_id}:0",
                    section_id=section.section_id,
                    page_id=section.page_id,
                    url=section.url,
                    heading=section.heading,
                    text=text,
                )
            ]

        chunks: list[Chunk] = []
        start = 0
        idx = 0
        while start < len(text):
            end = min(len(text), start + max_chars)
            chunk_text = text[start:end].strip()
            if chunk_text:
                chunks.append(
                    Chunk(
                        chunk_id=f"chunk:{section.section_id}:{idx}",
                        section_id=section.section_id,
                        page_id=section.page_id,
                        url=section.url,
                        heading=section.heading,
                        text=chunk_text,
                    )
                )
                idx += 1
            if end >= len(text):
                break
            start = max(0, end - overlap)
        return chunks

    def _extract_entities(self, section: Section) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
        nodes: list[dict[str, Any]] = []
        edges: list[dict[str, Any]] = []
        seen_node_ids: set[str] = set()

        section_text = section.text
        lowered = section_text.lower()

        def add_node(node_type: str, label: str, evidence: str) -> str:
            norm = re.sub(r"[^a-z0-9_.-]+", "_", label.lower()).strip("_")
            node_id = f"{node_type}:{norm}"
            if node_id not in seen_node_ids:
                nodes.append(
                    {
                        "node_id": node_id,
                        "type": node_type,
                        "label": label,
                        "section_id": section.section_id,
                        "page_id": section.page_id,
                        "url": section.url,
                        "evidence": evidence[:240],
                    }
                )
                seen_node_ids.add(node_id)
            edges.append(
                {
                    "source": section.section_id,
                    "target": node_id,
                    "type": "mentions",
                    "evidence": evidence[:240],
                }
            )
            return node_id

        found_concepts: list[str] = []
        for concept in _CONCEPTS:
            if concept in lowered:
                found_concepts.append(concept)
                add_node("concept", concept, section_text)

        for api in set(_API_HINT_RE.findall(section_text)) | set(_API_NAME_RE.findall(section_text)):
            if len(api) > 2:
                add_node("api", api, section_text)

        for config in _CONFIG_RE.findall(section_text):
            if config.startswith("https") or config.startswith("http"):
                continue
            add_node("config_option", config, section_text)

        version_matches = list(_VERSION_RE.findall(section_text))
        if version_matches:
            uniq_versions = sorted(set(version_matches))
            for version in uniq_versions:
                add_node("version", version, section_text)

            change_type_match = _CHANGE_RE.search(section_text)
            if len(uniq_versions) >= 1 and change_type_match:
                version_change_label = f"{change_type_match.group(1).lower()}:{','.join(uniq_versions)}"
                vc_id = add_node("version_change", version_change_label, section_text)
                for version in uniq_versions:
                    v_id = f"version:{version.lower()}"
                    edges.append({"source": vc_id, "target": v_id, "type": "affects_version", "evidence": section_text[:240]})

        unique_concepts = sorted(set(found_concepts))
        for i in range(len(unique_concepts)):
            for j in range(i + 1, len(unique_concepts)):
                c1 = f"concept:{re.sub(r'[^a-z0-9_.-]+', '_', unique_concepts[i].lower()).strip('_')}"
                c2 = f"concept:{re.sub(r'[^a-z0-9_.-]+', '_', unique_concepts[j].lower()).strip('_')}"
                edges.append({"source": c1, "target": c2, "type": "related_to", "evidence": section_text[:200]})

        return nodes, edges

    def build(self, max_pages: int = 30, output_path: str = "data/rag/naive_kg_rag.json") -> dict[str, Any]:
        db = DatabaseManager(db_path=self.db_path) if self.db_path else DatabaseManager()
        session = db.get_session()

        # SQLAlchemy model is imported directly to avoid fragile reflection.
        from firecrawl_scraper.models.database import PageRecord

        page_rows = session.query(PageRecord).order_by(PageRecord.scrape_timestamp.desc()).limit(max_pages).all()
        session.close()

        sections: list[dict[str, Any]] = []
        chunks: list[dict[str, Any]] = []
        nodes: dict[str, dict[str, Any]] = {}
        edges: list[dict[str, Any]] = []

        for row in page_rows:
            md_path = self._resolve_markdown_path(row.page_id, row.prefix)
            if not md_path or not md_path.exists():
                continue

            markdown = md_path.read_text(encoding="utf-8", errors="replace")
            page_sections = self._split_sections(markdown, row.page_id, row.url, str(md_path))

            for section in page_sections:
                sections.append(section.__dict__)
                for chunk in self._chunk_section(section):
                    chunks.append(chunk.__dict__)

                extracted_nodes, extracted_edges = self._extract_entities(section)
                for node in extracted_nodes:
                    if node["node_id"] not in nodes:
                        nodes[node["node_id"]] = node
                edges.extend(extracted_edges)

        node_items = list(nodes.values())
        node_index_docs = [
            {
                "node_id": n["node_id"],
                "text": f"{n['type']} {n['label']} {n.get('evidence', '')}",
            }
            for n in node_items
        ]
        chunk_index_docs = [
            {
                "chunk_id": c["chunk_id"],
                "text": f"{c['heading']}\n{c['text']}",
            }
            for c in chunks
        ]

        graph = {
            "created_at": datetime.now(UTC).isoformat(),
            "config": {"max_pages": max_pages},
            "sections": sections,
            "chunks": chunks,
            "nodes": node_items,
            "edges": edges,
            "indexes": {
                "node": _make_index(node_index_docs, text_key="text", id_key="node_id"),
                "chunk": _make_index(chunk_index_docs, text_key="text", id_key="chunk_id"),
            },
        }

        output = self.project_root / output_path
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(json.dumps(graph), encoding="utf-8")
        return graph


class NaiveKGRAGEngine:
    def __init__(self, graph_path: str = "data/rag/naive_kg_rag.json"):
        self.project_root = Path(__file__).resolve().parents[1]
        self.graph_path = self.project_root / graph_path
        self.graph = json.loads(self.graph_path.read_text(encoding="utf-8"))

        self.nodes = {n["node_id"]: n for n in self.graph["nodes"]}
        self.sections = {s["section_id"]: s for s in self.graph["sections"]}
        self.chunks = {c["chunk_id"]: c for c in self.graph["chunks"]}

        self.section_to_chunks: defaultdict[str, list[dict[str, Any]]] = defaultdict(list)
        for chunk in self.graph["chunks"]:
            self.section_to_chunks[chunk["section_id"]].append(chunk)

        self.adj: defaultdict[str, list[dict[str, Any]]] = defaultdict(list)
        for edge in self.graph["edges"]:
            self.adj[edge["source"]].append(edge)
            if edge["type"] == "related_to":
                self.adj[edge["target"]].append({
                    "source": edge["target"],
                    "target": edge["source"],
                    "type": edge["type"],
                    "evidence": edge.get("evidence", ""),
                })

    def query(self, question: str, top_nodes: int = 6, top_chunks: int = 6, hops: int = 1) -> dict[str, Any]:
        node_scores = _bm25_score(question, self.graph["indexes"]["node"])
        top_node_ids = [k for k, _ in sorted(node_scores.items(), key=lambda kv: kv[1], reverse=True)[:top_nodes]]

        anchor_sections: dict[str, float] = defaultdict(float)
        for node_id in top_node_ids:
            node = self.nodes.get(node_id)
            if not node:
                continue
            section_id = node.get("section_id")
            if section_id:
                anchor_sections[section_id] += node_scores.get(node_id, 0.0)

            if hops > 0:
                for edge in self.adj.get(node_id, []):
                    if edge["type"] == "related_to" and edge["target"] in self.nodes:
                        neighbor = self.nodes[edge["target"]]
                        sec_id = neighbor.get("section_id")
                        if sec_id:
                            anchor_sections[sec_id] += node_scores.get(node_id, 0.0) * 0.35

        chunk_scores = _bm25_score(question, self.graph["indexes"]["chunk"])

        combined: dict[str, float] = defaultdict(float)
        for section_id, score in anchor_sections.items():
            for chunk in self.section_to_chunks.get(section_id, []):
                combined[chunk["chunk_id"]] += score

        for chunk_id, score in chunk_scores.items():
            combined[chunk_id] += score * 0.6

        top_chunk_ids = [k for k, _ in sorted(combined.items(), key=lambda kv: kv[1], reverse=True)[:top_chunks]]
        contexts = []
        for chunk_id in top_chunk_ids:
            chunk = self.chunks[chunk_id]
            contexts.append(
                {
                    "chunk_id": chunk_id,
                    "heading": chunk["heading"],
                    "url": chunk["url"],
                    "file_path": chunk.get("file_path", self.sections.get(chunk["section_id"], {}).get("file_path")),
                    "text": chunk["text"],
                    "score": round(combined[chunk_id], 4),
                }
            )

        return {
            "question": question,
            "top_nodes": [self.nodes[n] for n in top_node_ids if n in self.nodes],
            "contexts": contexts,
        }


def _build_cli() -> None:
    parser = argparse.ArgumentParser(description="Build naive docs-first KG+RAG graph artifacts")
    parser.add_argument("--max-pages", type=int, default=30)
    parser.add_argument("--output", type=str, default="data/rag/naive_kg_rag.json")
    args = parser.parse_args()

    builder = NaiveKGRAGBuilder()
    graph = builder.build(max_pages=args.max_pages, output_path=args.output)
    print(
        json.dumps(
            {
                "output": args.output,
                "sections": len(graph["sections"]),
                "chunks": len(graph["chunks"]),
                "nodes": len(graph["nodes"]),
                "edges": len(graph["edges"]),
            },
            indent=2,
        )
    )


def _query_cli() -> None:
    parser = argparse.ArgumentParser(description="Query naive docs-first KG+RAG artifacts")
    parser.add_argument("question", type=str)
    parser.add_argument("--graph", type=str, default="data/rag/naive_kg_rag.json")
    parser.add_argument("--top-nodes", type=int, default=6)
    parser.add_argument("--top-chunks", type=int, default=6)
    parser.add_argument("--hops", type=int, default=1)
    args = parser.parse_args()

    engine = NaiveKGRAGEngine(graph_path=args.graph)
    result = engine.query(question=args.question, top_nodes=args.top_nodes, top_chunks=args.top_chunks, hops=args.hops)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    _build_cli()
