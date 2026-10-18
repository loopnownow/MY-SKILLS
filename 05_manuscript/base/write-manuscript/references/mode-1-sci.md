# SCI IMRAD workflow

Generic drafting workflow for Title / Abstract / Intro / Methods / Results / Discussion.
Personal house format, de-AI lists, and lab author defaults are **not** in this pack.

Polish → `05-write-polish`. Venue shape → `05-write-venue`. Reporting checklists → `05-write-reporting`.

## 1.1 When to use

- Draft or rewrite IMRAD sections from supplied facts
- Prediction-model full paper (dual-set Results) using `pipeline-stages.md`
- Methods ethics **placeholders** (`radiology-ethics/approval-consent.md`)
- Experiment/mechanism English outline (do not freeze unrun positive results)
- Generic academic outline (`mode-academic-pipeline.md`)

## 1.2 Workflow

1. Subtask: `draft-section` | `full-imrad` | `methods-skeleton` | `outline`
2. If the user named a venue family, **handoff** `05-write-venue` for shape; do not load a personal format file
3. Open the table below
4. Output the envelope in `MODULE.md`

| Subtask | Open |
|--------|------|
| Section draft | `section-templates.md`, `radiology-writing/*` |
| Prediction full paper | `pipeline-stages.md`, `section-templates.md`, then `05-write-reporting` |
| Ethics sentence | `radiology-ethics/approval-consent.md` (placeholders; no lab IRB default) |
| Claim/citation gate | `radiology-citation/*` |
| Outline | `mode-academic-pipeline.md` |
| Language polish | **handoff** `05-write-polish` |

## 1.3 Honesty

- Do not invent n, AUC, ethics IDs, or unrun experiments.
- Dual-set: training fit / test evaluate. Validation set = external cohort.
- Self-audit after drafting → `06-review-critique` (not this file).
