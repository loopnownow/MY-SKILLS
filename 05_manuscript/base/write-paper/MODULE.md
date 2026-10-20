---
name: "write-paper"
domain: "05_manuscript"
trigger: ["SCI写作", "写引言", "写讨论", "IMRAD", "起草全文"]
inputs: ["results_tables", "draft"]
outputs: ["imrad_draft"]
quality_control: "numbers only from supplied results; no invented n/AUC/ethics IDs"
owner: "05_manuscript/base/write-paper/MODULE.md"
---

# trigger is documentation only; not independently discoverable.

# Generic IMRAD manuscript draft

Draft and revise **scientific prose** (Title / Abstract / Introduction / Methods / Results /
Discussion). This pack is **generic IMRAD only**.

**Not in this pack (stay in A personal, or other fine ids):**

- Personal house format / title-page defaults
- de-AI forbidden lists and detectors
- Lab ethics IRB wording and author-line defaults
- Language polish → [`polish-language`](../polish-language/MODULE.md)
- Venue house style / article shape → [`05_manuscript/base/write-venue/`](../write-venue/MODULE.md)
- 选刊 / where to submit → A `03_research` (journal-selection) / `lit-search`
- TRIPOD / CLAIM / CLEAR checklists → [`check-reporting`](../check-reporting/MODULE.md)
- Self-audit → `self-review`; other-paper review → `peer-review`; response → `revise`

## When to use

- Draft or rewrite IMRAD sections from supplied facts
- Keep observational language (`associated with`) unless the design supports causation
- Export a Methods skeleton from `methods_template_export.md`

**Do not use this module** for polish-only passes, 选刊, or 回复审稿人.

## Hard rules

1. Numbers stick to assertions (n, AUC, CI, *P*); no empty claims
2. Introduction: problem → guideline definition → gap → approach (`radiology-writing/introduction.md`)
3. Observational designs: *associated with*, not causal verbs
4. Consistent terms; expand abbreviations at first use
5. Introduction and Discussion sentences run 10–30 words, one main proposition each; no run of short sentences (a personal layer may override)
6. Do not invent results, citations, ethics numbers, or unrun experiments
7. Missing facts → comments / open questions, never fabricated body text
8. Patient-level split language when the study is predictive
9. Dual-set reporting when the user supplied both training and test metrics
10. Reporting guidelines (TRIPOD, CLAIM, CLEAR) are not named in the Introduction; route to `check-reporting`
11. Related studies are synthesized, not listed: at most one triplet per paragraph, no repeated sentence frames


## Modes

| Mode | Open |
|------|------|
| `draft-section` | this file + [section-templates.md](references/section-templates.md) + [radiology-writing/](radiology-writing/) |
| `full-imrad` | [mode-1-sci.md](references/mode-1-sci.md) + [pipeline-stages.md](references/pipeline-stages.md) (prediction papers) |
| `methods-skeleton` | [methods_template_export.md](references/methods_template_export.md) + [radiology-writing/methods.md](radiology-writing/methods.md) |
| `ethics-sentence` | [radiology-ethics/approval-consent.md](radiology-ethics/approval-consent.md) — placeholders only; no lab default IRB |
| `outline` | [mode-academic-pipeline.md](references/mode-academic-pipeline.md) |
| `polish` | **handoff** → `polish-language` |
| `venue-shape` | **handoff** → `05_manuscript/base/write-venue/` |
| `reporting` | **handoff** → `check-reporting` |

## IMRAD map

| Section | File |
|---------|------|
| Abstract | [radiology-writing/structured-abstract.md](radiology-writing/structured-abstract.md) |
| Architecture | [radiology-writing/article-architecture.md](radiology-writing/article-architecture.md) |
| Methods | [radiology-writing/methods.md](radiology-writing/methods.md) |
| Results | [radiology-writing/results.md](radiology-writing/results.md) |
| Discussion | [radiology-writing/discussion.md](radiology-writing/discussion.md) |
| Citation gate | [radiology-citation/claim-verification-gate.md](radiology-citation/claim-verification-gate.md) |
| Figures | patient-flow → `04-fig-flow`; plots → `04-fig-plot` |

## Envelope

```text
Skill: write-paper
Subtask: draft-section | full-imrad | methods-skeleton | outline
Venue: (unknown unless user named one)

[Draft]

Missing inputs:
- ...

Next: polish-language (language) · 05_manuscript/base/write-venue/ (shape) · self-review (self-audit)
```
