---
name: "verify-refs"
domain: "03_research"
description: Citation validation / BibTeX format-write (former Scientific citation-management).
owner: "03_research/base/verify-refs/MODULE.md"
---

# verify-refs

Capability body: [MODULE.md](MODULE.md).

## Hard constraints (project-start)

- Full text is **not** required for the project-start chain.
- Deliver **NLM citation format + abstract list**.
- Store under `ref/refer/` (formerly「参考文献」 / `materials/citation`).
- `ref/citation/` remains audit ledger only (`CITATION_AUDIT` etc.); do not conflate with `ref/refer/`.
