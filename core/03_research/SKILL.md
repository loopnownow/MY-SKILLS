---
name: medical-research-design-and-evidence
description: >
  Design studies and synthesize evidence. Use for 选题, 选刊, 研究设计, 样本量,
  STROBE/CONSORT/TRIPOD/PRISMA, imaging feasibility, frontier, 国自然.
  Do not use for 写稿, 润色, 写引言, 写讨论, 评阅, or 回复审稿人.
---

# Medical Research Design and Evidence (integrated)

## Purpose

Turn a clinical/biomedical idea into a defensible protocol and evidence base.

## Capability map (load as needed)

| Task | Path |
|------|------|
| Imaging study design / feasibility | `bundles/radiology-design/MODULE.md` |
| Frontier directions | `bundles/radiology-frontier/MODULE.md` |
| Radiology design/lit checklists | `references/radiology/` |
| 领域/期刊格局（选题用，不写引言） | `references/radiology/literature.md` |
| 国自然 / NSFC 申报书结构 | `references/radiology/grant-writing.md` |

## Modes

### Evidence mode
Gaps, conflict, mechanism, journal fit — from `references/radiology/` (literature / frontier / journal-selection).  
Manuscript Introduction/Discussion citations → `05_manuscript` `intro-discussion-evidence.md`.

### Design mode
Question/hypothesis, design, eligibility, exposure, endpoints, covariates, sample size, missing data, bias, reporting guideline.

### Protocol critique mode
Design-outcome mismatch, selection bias, immortal time, confounding, overadjustment, train/val leakage, weak endpoints, unsupported causal language.

### Imaging design / frontier mode
Use radiology-design + frontier modules; prefer problem+data over hype. Blocking: slice-level split as external validation, no labels, n too small for claim.

## Evidence workflow

1. Define clinical/research question (PICO when clinical).
2. For journal/design evidence use `references/radiology/`. For manuscript I/D citations → `05_manuscript`. Do not invent PMID/DOI.
3. Separate direct / indirect / mechanistic / conflicting evidence.
4. Extract n, design, effects, CIs, follow-up, limitations.
5. Synthesize; state gap and how the proposed study addresses it.
6. **Never claim a paper supports a statement it does not support.** Do not invent PMID/DOI.

## Study-design workflow

1. Estimand / primary objective.
2. Design that identifies it.
3. Analytic population before outcomes.
4. Pre-specify primary/secondary outcomes.
5. Confounders / causal diagrams when useful.
6. Missing-data strategy; validation plan if prediction.
7. Reporting framework: STROBE / CONSORT / TRIPOD / STARD / PRISMA / CLAIM as fits.

## Sample-size principles

Base on endpoint, effect/event rate, alpha, power, allocation, model complexity, missingness, validation needs — not only EPV rules of thumb.

## Output preference

research question → hypothesis → design → population → endpoints → bias plan → sample-size rationale → analysis plan → validation → reporting framework → evidence gap → key refs

## Progressive disclosure

Only this top-level skill is auto-discovered. Load `bundles/*/MODULE.md` and `references/` as needed. Nested modules are **not** separate skills.
