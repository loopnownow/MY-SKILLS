---
name: "design-study"
domain: "03_research"
description: Study design, feasibility, validation blueprints.
owner: "03_research/base/design-study/MODULE.md"
---

# design-study

Capability body: [MODULE.md](MODULE.md). Do not duplicate it here.

## Hard constraints (project-start)

- When starting a project, run this chain **before** analysis: `design-study` → `lit-search` → `verify-refs`.
- Name the guideline that defines the endpoint or clinical decision (issuing body + year) before `lit-search`.
- Do not invent clinical numbers.
- Project-start literature deliverables (NLM + abstracts) land under `ref/refer/` after `lit-search` / `verify-refs`.
