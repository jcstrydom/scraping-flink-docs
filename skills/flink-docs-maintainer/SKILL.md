---
name: flink-docs-maintainer
description: Maintain and evolve the `flink-docs` repository with the correct project structure, invariants, and validation workflow. Use when working on scraper code under `firecrawl_scraper/`, shared repo data under `data/`, automation scripts under `scripts/`, tests, or docs; and whenever you need to bootstrap a session, refactor safely, or verify changes before merge.
---

# Flink Docs Maintainer

Use this skill to keep work aligned with the repository conventions and to avoid regressions in scraping identity/data handling while the project grows a separate RAG leg.

## Workflow

1. Read `documentation/MAINTAINER_CONTEXT.md` first for current invariants and repo map.
2. Confirm target area and boundaries:
   - scraper package: `firecrawl_scraper/`
   - shared data: `data/`
   - utilities: `scripts/single_use_scripts/`
   - tests: `tests/`
3. Preserve key invariants:
   - `page_id` for new writes is canonical URL SHA-256
   - existing rows/files are not auto-migrated unless explicitly requested
   - markdown filename shape stays `{prefix}_{page_id}.md`
4. Prefer small safe refactors with verification:
   - update code
   - run compile/tests from `references/commands.md`
   - patch docs when paths or behavior change
5. Before finishing, summarize changed files and whether compile/tests passed.

## Guardrails

- Treat `data/` as shared project state for scraper and future RAG.
- Keep scraper-specific logic in `firecrawl_scraper/`.
- Keep one-off/ops scripts outside the package under `scripts/`.
- Do not silently widen scope into RAG architecture unless asked.

## References

- Runtime and validation commands: `references/commands.md`
