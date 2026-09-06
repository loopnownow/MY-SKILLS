---
name: medical-journal-submit
description: Recommend medical journals from the user's JCR2026 curated pool and format manuscripts to target-journal author instructions. Use when the user asks to 推荐杂志, 投稿, 选刊, JCR/JCI分区, 影响因子, 版面费, AIM, author instructions, or to tidy a medical paper for submission.
metadata:
  type: workflow
  version: "1.6"
  source_table: artifacts/医学投稿推荐_JCR2026.xlsx
  owner: 03_research/Victor
  home: A 03_research/medical-journal-submit (not B 05-write-venue)
---

# Medical Journal Submit

## Owner / routing

- Lives in **A** `03_research/medical-journal-submit/` (Victor).
- Called from A `03_research/literature/journal-selection.md`.
- **Not** B `05-write-venue` (that id is house style only).
- Bai handles portal submit after a journal is chosen; Aitee `05-write-venue` only for formatting to the chosen family.


## Mounted blacklist (always on)

Load `references/blacklist.csv` first. Never list these titles.

- PLoS One / PLOS ONE
- Scientific Reports / SCI REP-UK
- MEDICINE (LWW Baltimore mega-journal; not NEJM; not Nature Medicine)

Copy: `artifacts/黑名单_默认挂载.csv` (same titles as `references/blacklist.csv`).
Name-only mount list: `references/blacklist-names.csv`.

## Every 推荐杂志 request

Read the uploaded manuscript. Output three tables, 5 journals each, in this layer order

1. 2 — Q1 and IF < 5 — `references/layer2-q1-if-lt5.csv`
2. 3 — Q2 — `references/layer3-q2.csv`
3. 2补 — Q1 and 5 ≤ IF ≤ 10 — `references/layer2b-q1-if-5to10.csv`

Total 15 titles unless a layer has fewer than 5 acceptable matches. Do not use layer 1 (IF>10) or layer 4 (Q3) unless the user asks.

Inside each layer pick the best 5 by

- 稿件/杂志匹配度 (highest weight): topic, design, article type, clinical vs basic, specialty vs `医学相关学科`
- 年发文量
- 易发程度: 易投指数; large-volume OA families only when scope fits; note unit bans for MDPI/Frontiers if those appear

Phase 1 columns for every layer table

分层 | 期刊全称 | ISO缩写 | 2025 JIF | 最佳JIF分区 | 最佳JCI分区 | 年发文量 | 易投指数 | 匹配理由

No AIM, author instructions, or APC in phase 1. After the three tables, ask the user to circle 备选杂志.

Phase 2 runs only after the user confirms titles. Then look up AIM, instructions, and fees for those titles only.

## Files

1. `references/blacklist.csv`
2. `references/recommendation-workflow.md`
3. `references/category-index.csv`
4. `references/layer2-q1-if-lt5.csv`
5. `references/layer3-q2.csv`
6. `references/layer2b-q1-if-5to10.csv`
7. `references/aim-author-checklist.md` — phase 2 only
8. `artifacts/医学投稿推荐_JCR2026.xlsx` — curated pool (keep). Raw Clarivate `JCR20XX影响因子.xlsx` is build input only; do not store after rebuild.
9. `references/policy.md` — stable rules
10. `references/annual-update.md` — yearly table refresh

## What not to do

- Do not recommend the three mounted blacklist titles.
- Do not collapse the three layers into a single top-5 list.
- Do not query AIM / author instructions / APC before the user confirms 备选杂志.

## Annual refresh

When the user sends a new JCR workbook, follow `references/annual-update.md`. Keep `references/policy.md` unless they also change blacklist, layers, or the 5-per-layer rule.
