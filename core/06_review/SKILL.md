---
name: medical-manuscript-review
description: >
  Peer review, pre-submission audit, and reviewer-response letters. Use for 评阅,
  审稿, 投稿前预审, 找洞, dealbreaker, peer review, 写审稿意见, 模拟审稿, 回复审稿人,
  回答审稿人问题, response letter, reviewer response, 修回, point-by-point.
  Do not use for 写论著, 润色, 写引言, 写讨论, or figures — those stay in 05_manuscript.
---

# Medical Manuscript Review

## Purpose

Find defects, write journal-system peer reviews, and draft point-by-point responses.
**Never invent** rescue experiments, missing AUCs, ethics IDs, or unrun analyses.
Do not rewrite the manuscript here — changed sentences go to `05_manuscript`.

## Capability map

| Task | Path |
|------|------|
| **Own-manuscript pre-submission audit** | `bundles/manuscript-quality/MODULE.md` path A + `bundles/manuscript-quality/references/mode-2-prereview.md` |
| **Peer review of others' papers** | `bundles/manuscript-quality/MODULE.md` path B + `bundles/manuscript-quality/references/mode-2-prereview.md` |
| **Response to reviewers** | `bundles/manuscript-quality/MODULE.md` path C + `bundles/manuscript-quality/references/mode-3-response.md` |
| Dealbreakers / hard gates | `bundles/manuscript-quality/references/merged/radiology-prereview/` |
| Response action map / audit | `bundles/manuscript-quality/references/merged/radiology-response/` |
| Radiology pre-submission notes | `references/radiology/pre-submission.md` |
| Radiology response notes | `references/radiology/response.md` |
| Reporting / citation checklists (read-only) | `05_manuscript` `manuscript-core/references/merged/radiology-reporting/` and `radiology-citation/` |
| Layout / Aitor / sentence polish | `05_manuscript` — do not edit here |

## Modes

- `pre-review` — Blocking / Major / Minor on the user's manuscript
- `peer-review` — English reviewer report for another paper
- `response` — point-by-point letter + change log

Load `bundles/manuscript-quality/MODULE.md`, then only the matching mode file.

## Not this skill

- 写论著 / 润色 / 去AI / 引言 / 讨论 / 配图 → `05_manuscript`
- 选题 / 选刊 → `03_research`
- 新统计或补做分析 → `04_analysis`
- 图像方法核验 → `02_imaging`

## Handoff

After pre-review: `05_manuscript` implements wording and layout fixes.
After a response letter: `05_manuscript` polishes changed sentences. Call `04_analysis` or `02_imaging` only when the comment requires new analysis or imaging verification.

## Progressive disclosure

Only this top-level skill is auto-discovered. Execution lives under `manuscript-quality`. Nested modules are not separate skills.
