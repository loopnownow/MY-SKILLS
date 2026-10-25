---
name: "write-paper"
domain: "05_manuscript"
trigger: ["SCI写作", "写引言", "写讨论", "IMRAD", "起草全文", "期刊体例", "Nature family", "house style", "venue template"]
inputs: ["results_tables", "draft"]
outputs: ["imrad_draft", "venue_shape"]
quality_control: "numbers only from supplied results; no invented n/AUC/ethics IDs"
owner: "05_manuscript/base/write-paper/MODULE.md"
---

# trigger is documentation only; not independently discoverable.

# IMRAD draft and venue shape

Draft and revise **scientific prose** (Title / Abstract / Introduction / Methods / Results /
Discussion), plus venue house style and article shape once a journal family is known.

**Not in this pack (stay in A personal, or other fine ids):**

- Personal house format / title-page defaults
- de-AI forbidden lists and detectors
- Lab ethics IRB wording and author-line defaults
- Language polish → [`humanize`](../humanize/MODULE.md)
- 选刊 / where to submit → A `03_research` (journal-selection) / `lit-search`. Do not add `journal-selection.md` here.
- TRIPOD / CLAIM / CLEAR checklists → [`check-reporting`](../../qc/check-reporting/MODULE.md)
- Self-audit → `self-review`; other-paper review → `peer-review`; response → `revise`

## When to use

- Draft or rewrite IMRAD sections from supplied facts
- Shape a draft to a named venue family (article shape / house voice — not 选刊)
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
7. Missing facts → comments / open q
8. **Negation / incompleteness (owner 2026-10-23):** Process-negation sentences that flag work not done or CYA hedges (e.g. 「某某未做」「我们未做」「未进行…»; *we did not* / *not performed* / *was not done* / *not examined*) **must not appear in 正文** (manuscript, revised manuscript, or response letter). Put them **only** in Word 批注 (author **A**), and every such 批注 **must** include **建议修改后内容**. Bare flags fail. Does **not** ban empirical negative findings that are study results (e.g. *no significant difference*, *X was not associated with Y*). Canonical: `05_manuscript/qc/anti-leak-placeholders.md` AL-5; `07_response/qc/disclaimer-comment-only.md`.uestions, never fabricated body text
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
| `polish` | **handoff** → `humanize` |
| `venue-shape` | this file + [journal-family-writing-style.md](radiology-writing/journal-family-writing-style.md) + [nature-family-shape.md](radiology-writing/nature-family-shape.md) + [radiology-polishing/](radiology-polishing/) + [journal-patterns-2023-2026.md](references/journal-patterns-2023-2026.md) |
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
| Figures | patient-flow → `draw-flowchart`; plots → `plot-figures` |

## Venue shape (in-skill)

Use after the target journal family is known (Radiology-family vs Nature-family article shape, house voice, word and figure budgets). This is not journal selection / 选刊. Journal lists (blacklist / graylist / whitelist) stay in `03_research/base/find-journal/`.

| File | Open when |
|---|---|
| `radiology-writing/journal-family-writing-style.md` | Journal-family wording and counts for a named family (JCO, NEJM AI, ...); verify against the live guide |
| `radiology-writing/nature-family-shape.md` | Nature-portfolio shape (unstructured abstract, Extended Data, Methods placement) |
| `radiology-polishing/radiology-house-style.md` | Radiology-family voice, spelling, abbreviations, and Nature-family deltas |
| `radiology-polishing/venue-voice-and-house-style.md` | Venue voice and tone once the target venue is known |
| `references/journal-patterns-2023-2026.md` | Dated venue-family writing patterns (not a submit-here list) |

## Envelope

```text
Skill: write-paper
Subtask: draft-section | full-imrad | methods-skeleton | outline | venue-shape
Venue: (unknown unless user named one)

[Draft]

Missing inputs:
- ...

Next: humanize (language) · venue-shape (in this pack) · self-review (self-audit)
```
