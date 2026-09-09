# AGENTS — medical-journal-submit

Authority order: `SKILL.md` → `references/policy.md` → `references/recommendation-workflow.md` → this file.
If this file conflicts with `SKILL.md` / `policy.md`, **follow SKILL/policy** (zip processed pack).

Aligned with **SKILL.md metadata.version 1.14** (Gemini + ChatGPT 2026-09; 10/10/10 + 层4 default + 可荐综合刊).

## When to use

User asks 推荐杂志 / 选刊 / 投稿去哪 / JCR·JCI 分区 / 影响因子分层 / 版面费·AIM（仅备选确认后）.

Owner: **Victor** · A `03_research`. Bai owns 选刊推进 after titles are chosen. Not Aitee `05-write-venue`.

## Every 推荐杂志 run

1. Mount blacklist first (`references/blacklist.csv`): never list PLoS One / Scientific Reports / MEDICINE (LWW Baltimore).
2. Read the manuscript. **Ask before each run** whether to include 层2补 (Challenge); **default OFF**.
   - Always: 层2 — Q1 and IF < 5 — `references/layer2-q1-if-lt5.csv` (Target; **10** journals)
   - Always: 层3 — Q2 — `references/layer3-q2.csv` (Safety偏上/稳妥; **10** journals)
   - Always: 层4 — Q3 — `references/layer4-q3.csv` (**默认给出**; **10** journals)
   - Only if user opts in: 层2补 — Q1 and 5 ≤ IF ≤ 10 — `references/layer2b-q1-if-5to10.csv` (Challenge)
3. Do **not** use layer1 (IF>10) unless the user asks. Comprehensive/general medical journals OK when match is reasonable.
4. Rank inside a layer by: **稿件匹配度** (MJF/MFI, highest) → **投稿易投指数** (JESI/JEI) → capacity signal (年发文量 / log volume as weak tie-breaker). Use **dynamic weights** when user constraints differ (speed / Q1 / APC); no fixed weights as policy. Do not use curated 易投指数 in ranking/JDI.
5. Phase-1 columns: 勾选 | 期刊全称 | 2025 JIF | 年发文量 | 接收率 | 初筛拒稿率 | 送审率 | 匹配理由 | 稿件匹配度 | 投稿易投指数(可带缺标)
   - No 分层/策略 column (layer in section titles; keep data-layer/data-tier on checkboxes). Chinese score headers; always show rate columns (blank/`—` if unknown). Do **not** show 置信度 / ISO / JIF分区 / JCI分区.
   - JESI: always from available A/R/P+MJF; partial scores marked in-cell (`*` + `缺:…`); never invent rates. See `jesi-model.md`.
   - JIF / volume / rates are **display-only**; do **not** persist them into `submission-urls.csv`.
   - **Ask before each run** whether to include 层2补 (Challenge); **default OFF** (层2 + 层3 + 层4 by default).
   - Per-layer default count: **10**. Specialty preferred; **综合/全科刊** allowed when fit is reasonable.
6. No AIM / author instructions / APC in phase 1. Then ask user to circle 备选杂志.
7. Phase 2 only after confirmation — see `references/aim-author-checklist.md`.
8. Pipeline: optional external candidate pool → metrics → fit → JESI → prior (`modules.md`, `jesi-model.md`). External recommender = query provider only.
9. Delivery: HTML for user; write submission URLs only back to `submission-urls.csv`; optional prior lines → `submission-prior.jsonl`.
10. Risk: **Unknown ≠ Low Risk.**

Curated table: `artifacts/医学投稿推荐_JCR2026.xlsx`. Raw Clarivate workbook is rebuild input only. Query sources: `references/query-sources.md`. Persistence absorb/query/delete: `references/persistence.md`.

## Do not

- Recommend the three blacklist titles.
- Collapse default layers into one top-N list.
- Route 选刊 to `05-write-venue`.
- Invent word limits or APC; invent missing risk as “low.”
- Persist annually updated IF / JCR·JCI/CAS / APC / review-time / volume values into CSV/DB-like files — **query capability only**.
- Install external journal-recommender as a mounted skill; copy fixed Fit Score weights or abstract→CAS prediction.

## Display hard rules (v1.14)
- 刊名含 Medicine：层内降权；**no** 「可疑」/红标；LWW MEDICINE still blacklisted.
- Phase-1 HTML：only **投稿易投指数 ≥80** yellow highlight.
