---
name: medical-manuscript-review
description: >
  Peer review, pre-submission audit, reviewer-response letters, and Chinese thesis
  评阅 (separate from English peer review). Use for 审稿, 投稿前预审, 找洞,
  dealbreaker, peer review, 写审稿意见, 模拟审稿, 回复审稿人, 回答审稿人问题,
  response letter, 修回, 落实审稿意见, point-by-point, 毕业论文评阅, 中文刊审稿单.
  English peer review stays polite; do not import Chinese journal-form punch.
  Do not use for 写论著, 润色, 写引言, 写讨论, or figures — those stay in 05_manuscript.
---

# Medical Manuscript Review

## Purpose

Find defects, write journal-system peer reviews, and draft point-by-point responses.
**Never invent** rescue experiments, missing AUCs, ethics IDs, or unrun analyses.
Do not rewrite the manuscript here — changed sentences go to `05_manuscript`.
Path A (`落实审稿意见` / revise an existing manuscript) **skips the entire title page**: ethics number, author block, target journal, and whether the paper declares “not generated”. Do not fill, yellow-highlight, or rewrite those fields. From-scratch title page stays in `05_manuscript` `Aitor-format.md`.
When reviewing an already-written manuscript, do **not** delete genuine references to hit the Intro 10–15 / Discussion 10–15-new quota; note over-quota only. New-I/D quota and evidence retrieval stay in `05_manuscript`.

## Capability map

| Task | Path |
|------|------|
| **Own-manuscript pre-submission audit / 落实审稿意见** | `bundles/manuscript-quality/MODULE.md` path A + `bundles/manuscript-quality/references/mode-2-prereview.md` (skip title page) |
| **Peer review of others' papers** | `bundles/manuscript-quality/MODULE.md` path B + `bundles/manuscript-quality/references/mode-2-prereview.md` |
| **Response to reviewers** | `bundles/manuscript-quality/MODULE.md` path C + `bundles/manuscript-quality/references/mode-3-response.md` |
| Dealbreakers / hard gates | `bundles/manuscript-quality/references/merged/radiology-prereview/` |
| Response action map / audit | `bundles/manuscript-quality/references/merged/radiology-response/` |
| Personal English peer-review voice (Opening → Major → sections) | `bundles/manuscript-quality/references/merged/radiology-prereview/personal-review-style.md` |
| Personal reply tone/phrasing (response letters; **opening default A**, B almost unused) | `bundles/manuscript-quality/references/merged/radiology-response/personal-response-style.md` |
| 毕业论文评阅（院内中文；**不要**混进英文 peer review） | `bundles/manuscript-quality/references/thesis-review.md` |
| 中文刊审稿单 A–F / 1–5 分项（**单独模板**） | `bundles/manuscript-quality/references/chinese-journal-score-sheet.md` |
| Radiology pre-submission notes | `references/radiology/pre-submission.md` |
| Radiology response notes | `references/radiology/response.md` |
| Reporting / citation checklists (read-only) | `05_manuscript` `manuscript-core/references/merged/radiology-reporting/` and `radiology-citation/` |
| Layout / Aitor / sentence polish | `05_manuscript` — do not edit here |

## Modes

- `pre-review` — Blocking / Major / Minor on the user's manuscript (Path A: skip title page; do not cut real refs to hit I/D quota)
- `peer-review` — English reviewer report for another paper (Opening 2–4 sentences → Major → section-wise; voice in `personal-review-style.md`)
- `response` — point-by-point letter + change log (opening **A**; style B almost unused)
- `thesis-review` — 毕业论文 / 学位论文评阅（中文评阅表；**与英文 peer review 分开**）
- Chinese journal A–F score sheets — only `chinese-journal-score-sheet.md`; never mix into English peer review

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
