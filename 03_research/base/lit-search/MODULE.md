---
name: "lit-search"
domain: "03_research"
trigger: ["文献检索", "PubMed", "search"]
outputs: ["search_set"]
owner: "03_research/base/lit-search/MODULE.md"
---

# Literature search

Contract only for lit-search (query and screening): scope, bans, phase names, and pointers. The recipe and the revision authority live in `03_research/advanced/`; this file does not restate a procedure. Pack data (`rules/`, `data/`, `references/`) stays beside it as data.

Generic search / source hierarchy / public datasets for radiology AI.
Advanced search logs and the lit bank stay in `03_research/advanced/`.

## Open these files

| File | Open when |
|---|---|
| [references/literature.md](references/literature.md) | Searching, screening or organizing literature; concept combinations, source hierarchy, 2023-2026 evidence layer |
| [references/public-datasets.md](references/public-datasets.md) | Public datasets (TCIA, TCGA, GEO, CPTAC, IDC), external-validation cohorts, public-data mechanism work |
| [references/sources.md](references/sources.md) | The user asks why a rule exists, or advice turns on a current reporting guideline |

## Handoffs

- Read full text / verify a DOI → `verify-refs`
- Retraction status of a cited paper → `verify-refs` (integrity stage)
- Full text / OA PDF batch → `lit-fulltext`
- 选刊 → `find-journal` (not this pack)
- Advanced lit bank and intake → `03_research/advanced/lit-bank.md`, `03_research/advanced/intake.md`
