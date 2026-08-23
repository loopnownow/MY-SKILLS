---
name: medical-peer-review-and-quality-control
description: >
  Pre-submission audit and reviewer letters for imaging SCI papers. Use for 投稿前预审,
  评阅, 评阅论文, 评审, 审稿, 审阅, 审这篇, 帮我评这篇, 点评稿件, 模拟审稿,
  批判性意见, 25-30条, 补充清单, 回复审稿人.
  Do not use for git/PR/code review (/review). Integrates ly-prereview, ly-response.
---

# Medical Peer Review and Quality Control (integrated)

## Purpose

Find material validity problems and produce **actionable** corrections. Do not rewrite full
prose here (that is `04_writing`). Do **not invent** rescue experiments or metrics.

## Capability map

| Task | Path |
|------|------|
| Own-manuscript pre-submission (Blocking/Major/Minor) | `bundles/ly-prereview/MODULE.md` |
| English peer-review comments for others | `bundles/ly-prereview/` path B |
| Point-by-point response letters | `bundles/ly-response/MODULE.md` |
| Broad structured peer-review methodology | `bundles/peer-review/MODULE.md` |
| Radiology pre-sub / response notes | `references/radiology/` |
| Review checklist (skills_export) | `bundles/ly-prereview/references/review_checklist_export.md` |
| Export paper-writing-review notes | `references/paper-writing-review-NOTES.md` |

## Review hierarchy (priority order)

1. Fatal validity threats  
2. Design / selection bias  
3. Outcome/exposure definition  
4. Confounding / causal interpretation  
5. Statistical / modeling errors  
6. Imaging preprocessing and **leakage**  
7. Validation and reproducibility  
8. Reporting completeness  
9. Presentation and language  

Do not spend most of the review on grammar when design is broken.

## Imaging / prediction dealbreakers (flag first)

- Train/test leakage; feature selection on full data  
- Slice-level split claimed as patient-level external validation  
- No validation while claiming generalizability  
- Untraceable AUC / missing denominators  
- Overstated clinical utility from retrospective single-center AUC  
- Dual-cohort prediction papers missing main model metrics on both sets  

## Modes

### A. Pre-review own manuscript (`ly-prereview`)
Output Blocking / Major / Minor + checklist gaps + citation flags.  
Lab SCI full papers: write **25–30 critical questions** (fact → why → fix). Collect items that would invent ethics, dirty-data handling, endpoint scope, or names as **multiple-choice questions for the user** before `04_writing` revises. Aitor-format is not reviewed here — it lives in `04_writing` `Aitor-format.md`.

### B. Peer review others
Opening + sectioned numbered comments: fact → why problem → what authors should do.

### C. Response to reviewers (`ly-response`)
Stable IDs (R1-1…); map action + manuscript location; **never claim unmade experiments**.

### D. Generic QC
Use peer-review pack stages + radiology checklists.

## Comment format

For each major issue: exact problem · why it matters · principle · concrete fix · needs new analysis vs rewrite.

Separate Major / Minor / Required / Optional.

## QC output envelope

overall validity · highest-priority fixes · analyses to rerun · text-only fixes · residual limitations · next skill (`04_writing` polish or `02_analysis` rerun)

## Progressive disclosure

Only this top-level skill is auto-discovered. Load `bundles/*/MODULE.md` and `references/` as needed for the active mode. Nested modules are **not** separate skills.
