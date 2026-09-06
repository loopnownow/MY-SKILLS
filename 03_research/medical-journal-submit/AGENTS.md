# AGENTS — medical-journal-submit

Authority order: `SKILL.md` → `references/policy.md` → `references/recommendation-workflow.md` → this file.
If this file conflicts with `SKILL.md` / `policy.md`, **follow SKILL/policy** (zip processed pack).

## When to use

User asks 推荐杂志 / 选刊 / 投稿去哪 / JCR·JCI 分区 / 影响因子分层 / 版面费·AIM（仅备选确认后）.

Owner: **Victor** · A `03_research`. Not Aitee `05-write-venue`. Not Bai until titles are chosen.

## Every 推荐杂志 run

1. Mount blacklist first (`references/blacklist.csv`): never list PLoS One / Scientific Reports / MEDICINE (LWW Baltimore).
2. Read the manuscript. Output **three** tables, **5** journals each, in this order:
   - 层2 — Q1 and IF < 5 — `references/layer2-q1-if-lt5.csv`
   - 层3 — Q2 — `references/layer3-q2.csv`
   - 层2补 — Q1 and 5 ≤ IF ≤ 10 — `references/layer2b-q1-if-5to10.csv`
3. Do **not** use layer1 (IF>10) or layer4 (Q3) unless the user asks.
4. Rank inside a layer by: 匹配度 (highest) → 年发文量 → 易投指数.
5. Phase-1 columns only: 分层 | 期刊全称 | ISO缩写 | 2025 JIF | 最佳JIF分区 | 最佳JCI分区 | 年发文量 | 易投指数 | 匹配理由
6. No AIM / author instructions / APC in phase 1. Then ask user to circle 备选杂志.
7. Phase 2 only after confirmation — see `references/aim-author-checklist.md`.

Curated table: `artifacts/医学投稿推荐_JCR2026.xlsx`. Raw Clarivate workbook is rebuild input only.

## Do not

- Recommend the three blacklist titles.
- Collapse three layers into one top-5.
- Route 选刊 to `05-write-venue`.
- Invent word limits or APC.
