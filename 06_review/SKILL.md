---
name: medical-manuscript-review
description: >
  Personal review/response upper layer. Entry for 审稿, 投稿前预审, 回复审稿人 is always 06.
  May internally call 04/05/02/03. Does not write manuscript body. Literature → 03.
  Figures → 04. Prose polish → 05.
---

# Manuscript Review — personal upper layer

## Purpose

Find defects, write journal-system peer reviews, and draft point-by-point responses.
**Never invent** rescue experiments, missing AUCs, ethics IDs, or unrun analyses.
Do not rewrite the manuscript here — changed sentences go to `05_manuscript`.

**Reviewer response enters through `06_review` only.**

Path A (`落实审稿意见` / revise an existing manuscript) **skips the entire title page**: ethics number, author block, target journal, and whether the paper declares “not generated”. Do not fill, yellow-highlight, or rewrite those fields. From-scratch title page stays in `05_manuscript/personal/Aitor-format.md`.

When reviewing an already-written manuscript, do **not** delete genuine references to hit the Intro 10–15 / Discussion 10–15-new quota; note over-quota only. New-I/D quota and evidence retrieval stay in `05_manuscript` / `03_research`.

## Layer model

**Mounted review/response capability → 06 personal upper layer → 00 Final QC.**

## Personal assets

| Task | Path |
|---|---|
| English peer-review voice | `personal/personal-review-style.md` |
| Response-letter tone (opening default A) | `personal/personal-response-style.md` |
| 毕业论文评阅（中文；不要混进英文 peer review） | `personal/thesis-review.md` |
| 中文刊审稿单 A–F | `personal/chinese-journal-score-sheet.md` |

## Mounted capability ids (generic; not present until mounted)

- `06-review-generic` — mode-2/3, dealbreakers, hard gates, review-report-format, action-mapping, response-audit-gate, checklist export

Until mounted, local generic copies remain under `review-generic/` (see `EXTERNALIZATION_CANDIDATES.md`).

## Modes

- `pre-review` — Blocking / Major / Minor on the user's manuscript (Path A: skip title page; do not cut real refs)
- `peer-review` — English reviewer report for another paper (`personal/personal-review-style.md`)
- `response` — point-by-point letter (`personal/personal-response-style.md`; opening **A**)
- `thesis-review` / Chinese journal score sheet — separate templates; never mix into English peer review

## Internal calls (not entry points)

- Wording / layout → `05_manuscript`
- New statistics → `04_analysis`
- Imaging verification → `02_data-processing`
- Design / literature fact-check → `03_research`

## Not this skill

- 写论著 / 润色 / 去AI / 引言 / 讨论 → `05_manuscript`
- 选题 / 选刊 / 文献检索 → `03_research`
- 出图 → `04_analysis`
