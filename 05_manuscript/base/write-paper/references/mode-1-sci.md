# SCI IMRAD workflow

Generic drafting workflow for Title / Abstract / Intro / Methods / Results / Discussion.
Personal house format, de-AI lists, and lab author defaults are **not** in this pack.

Polish → `humanize`. Venue shape → this pack (`05_manuscript/base/write-paper/radiology-writing/journal-family-writing-style.md`, `05_manuscript/base/write-paper/radiology-writing/nature-family-shape.md`). Reporting checklists → `check-reporting`.

## 1.1 When to use

- Draft or rewrite IMRAD sections from supplied facts
- Prediction-model full paper (dual-set Results) using `pipeline-stages.md`
- Methods ethics **placeholders** (`05_manuscript/base/write-paper/radiology-ethics/approval-consent.md`)
- Experiment/mechanism English outline (do not freeze unrun positive results)
- Generic academic outline (`mode-academic-pipeline.md`)

## 1.2 Workflow

1. Subtask: `draft-section` | `full-imrad` | `methods-skeleton` | `outline`
2. If the user named a venue family, open venue-shape files in this pack (`05_manuscript/base/write-paper/radiology-writing/journal-family-writing-style.md`, `05_manuscript/base/write-paper/radiology-writing/nature-family-shape.md`, `radiology-polishing/`); do not load a personal format file
3. Open the table below
4. Output the envelope in `MODULE.md`

| Subtask | Open |
|--------|------|
| Section draft | `section-templates.md`, `radiology-writing/*` |
| Prediction full paper | `pipeline-stages.md`, `section-templates.md`, then `check-reporting` |
| Ethics sentence | `05_manuscript/base/write-paper/radiology-ethics/approval-consent.md` (placeholders; no lab IRB default) |
| Claim/citation gate | `radiology-citation/*` |
| Outline | `mode-academic-pipeline.md` |
| Language polish | **handoff** `humanize` |

## 1.3 Honesty

- Do not invent n, AUC, ethics IDs, or unrun experiments.
- Dual-set: training fit / test evaluate. Validation set = external cohort.
- Self-audit after drafting → `self-review` (not this file).
