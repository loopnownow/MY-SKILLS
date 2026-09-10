---
name: medical-journal-submit
description: Recommend medical journals from the user's JCR2026 curated pool and format manuscripts to target-journal author instructions. Use when the user asks to 推荐杂志, 投稿, 选刊, JCR/JCI分区, 影响因子, 版面费, AIM, author instructions, or to tidy a medical paper for submission.
metadata:
  type: workflow
  version: "1.15"
  source_table: artifacts/医学投稿推荐_JCR2026.xlsx
  owner: 03_research/Victor
  home: A 03_research/medical-journal-submit (not B 05-write-venue)
  advice_merged: Gemini+ChatGPT 2026-09
---

# Medical Journal Submit

## Owner / routing

- Lives in **A** `03_research/medical-journal-submit/` (Victor).
- Called from A `03_research/literature/journal-selection.md`.
- **Not** B `05-write-venue` (that id is house style only).
- Bai handles Phase-1 checkbox HTML → user export JSON handoff, then portal submit after a journal is chosen; Aitee `05-write-venue` only for formatting to the chosen family.

## Mounted blacklist (always on)

Load `references/blacklist.csv` first. Never list these titles.

- PLoS One / PLOS ONE
- Scientific Reports / SCI REP-UK
- MEDICINE (LWW Baltimore mega-journal; not NEJM; not Nature Medicine)

Copy: `artifacts/黑名单_默认挂载.csv` (same titles as `references/blacklist.csv`).
Name-only mount list: `references/blacklist-names.csv`.

## Every 推荐杂志 request

Read the uploaded manuscript. Output three tables, **10 journals each**, in this default layer order

1. 层2 — Q1 and IF < 5 — Target/主攻 — 10本 — `references/layer2-q1-if-lt5.csv`
2. 层3 — Q2 — Safety偏上/稳妥 — 10本 — `references/layer3-q2.csv`
3. 层4 — **Q3 — 默认给出** — 10本 — `references/layer4-q3.csv`
4. 层2补 — Q1 and 5 ≤ IF ≤ 10 — Challenge — **default OFF**; **ask the user before each skill use** whether to show — `references/layer2b-q1-if-5to10.csv`

Default total **30** titles (10+10+10) unless a layer has fewer acceptable matches. Do not use layer 1 (IF>10) unless the user asks. **Comprehensive / general medical journals** (e.g. Medicine, General & Internal / multidisciplinary clinical) may be recommended when scope match is reasonable — not specialty-only.

Inside each layer rank by

1. **稿件匹配度** (MJF/MFI, highest weight): topic, design, article type, clinical vs basic, specialty vs `医学相关学科` (**MJF = MFI**; display **稿件匹配度**)
2. **BMC/Medicine 白名单优先** (`references/whitelist-bmc-medicine.csv`): among comparable fit, whitelist hits rank above non-whitelist (boost, not auto-fill)
3. **投稿易投指数** (JESI/JEI; see `references/jesi-model.md`). Always compute from **available** metrics (A/R/P + 稿件匹配度); when some rate inputs missing, still compute (skip/renormalize or capacity+MJF fallback) and **mark** incompleteness in-cell (`62.4*` + `缺:…`). Never invent rates; blank rate cells stay blank. Do not use quartile-only / curated 易投指数 as primary. `JEI = f(JDI, Capacity, Reviewability)`
4. **Capacity signal** (log annual volume / 年发文量 as a weak tie-breaker; annual pubs ≠ accepts)

**Dynamic weights:** numeric JESI defaults in `jesi-model.md` are **initial only** and must be overridable when the user prioritizes speed, Q1, APC/OA, etc. Do not copy fixed external Fit Score weights into this pack.

Optional front door: external candidate pool (query mounts) → Difficulty + Fit + Risk → **this pack decides** → Challenge / Target / Safety (see `recommendation-workflow.md`). External recommenders are data providers, not decision makers.

Phase 1 columns for every layer table

勾选 | 期刊全称 | 2025 JIF | 年发文量 | 接收率 | 初筛拒稿率 | 送审率 | 匹配理由 | 稿件匹配度 | 投稿易投指数(可带缺标)

- **Chinese score headers:** MJF/MFI → **稿件匹配度**; JESI → **投稿易投指数**. Do **not** show curated **易投指数**.
- **No 分层/策略 column (v1.11+):** layer/tier already appear in section titles（层2主攻 / 层3(Q2) / 层4(Q3)）. Keep `data-layer` / `data-tier` on checkboxes for export JSON.
- **Removed from Phase-1 display:** 置信度, ISO缩写/ISO, 最佳JIF分区/JIF分区, 最佳JCI分区/JCI分区, 易投指数, 分层/策略.
- **Always display** 接收率 / 初筛拒稿率 / 送审率 (empty/`—` if unknown; never invent). Attach `rates_source` in JSON/title when found. Do **not** persist rates into `submission-urls.csv`.
- JIF / 年发文量 / rates are **display-only runtime fields** in the report (HTML/Markdown). Do **not** persist them into `submission-urls.csv` or other DB-like files (`references/persistence.md`).
- 稿件匹配度: keep from Phase-1 human MJF.
- **投稿易投指数 (partial OK, marked):** always compute from available A（接收率）, R（送审率或 1−初筛拒稿率）, P（年发文量→JCI-C）, and 稿件匹配度.
  - Full (rates available): `JESI = 0.50×(100−JDI) + 0.20×JCI-C + 0.30×稿件匹配度` (A/R/P components as in `references/jesi-model.md`).
  - Partial: skip missing inputs and renormalize, or capacity+MJF fallback when A/R both absent; show in-cell marker e.g. `62.4*` + `缺:接收率,初筛拒稿率` (tooltip OK). Persist `投稿易投指数` + `jesi_missing: [...]` in Phase-1 JSON. **Never invent rates.**
  - **Unknown ≠ Low Risk.**
- **层4 (Q3):** included **by default** (10本).
- **层2补 (Challenge):** ask the user **before each run** whether to include 层2补; **default OFF** (show 层2 + 层3 + 层4 unless user opts in to Challenge).
- **综合刊：** when fit is reasonable, general/comprehensive medical titles are allowed alongside specialty journals.
- No AIM, author instructions, or APC in phase 1. After the tables, ask the user to circle 备选杂志.

Phase 2 runs only after the user confirms titles. Then look up AIM, instructions, and fees for those titles only.

## Modules (within pack)

Logical pipeline (not separate top-level skills yet): `references/modules.md`

`sci-metrics-retriever` → `manuscript-fit-analyzer` → `jesi-calculator` → `submission-prior-logger`

Indices: **JDI**, **JEI/JESI**, **MJF (=MFI)**, **PAI**, **JCI-C** (capacity).

## Delivery

- Prefer **HTML** for the user-facing recommendation.
- Write **submission URLs only** back to `references/submission-urls.csv` (schema: 期刊全称, ISO缩写, ISSN, eISSN, 投稿网址, 来源备注, updated).
- Annually updated metrics (JCR quartile, IF, annual volume, APC, review time, …) must **not** be persisted as durable delivery data — **query capability only**.
- Personal outcomes → append `references/submission-prior.jsonl` (no IF/quartile fields).

## Files

1. `references/blacklist.csv`
2. `references/recommendation-workflow.md`
3. `references/category-index.csv`
4. `references/layer2-q1-if-lt5.csv`
5. `references/layer3-q2.csv`
6. `references/layer4-q3.csv` — default Q3 layer
7. `references/layer2b-q1-if-5to10.csv` — Challenge; ask-first default OFF
8. `references/aim-author-checklist.md` — phase 2 only
9. `artifacts/医学投稿推荐_JCR2026.xlsx` — curated pool (keep). Raw Clarivate `JCR20XX影响因子.xlsx` is build input only; do not store after rebuild.
10. `references/policy.md` — stable rules
11. `references/annual-update.md` — yearly table refresh
12. `references/query-sources.md` — evolvable query sources (OpenAlex/Crossref/EuropePMC/journal sites/JCR primary; LetPub auxiliary)
13. `references/jesi-model.md` — JESI / JEI / JDI / JCI-C / MJF
14. `references/persistence.md` — absorb / query / delete + what to save
15. `references/modules.md` — four logical modules + naming
16. `references/whitelist-bmc-medicine.csv` — BMC / Medicine priority whitelist (LWW MEDICINE excluded)
17. `references/submission-urls.csv` — URL fields only
18. `references/submission-prior.jsonl` — personal prior log (schema only until outcomes exist)

## BMC / Medicine 白名单（优先推荐）

Load `references/whitelist-bmc-medicine.csv` (copy: `artifacts/白名单_BMC_Medicine.csv`). Membership (case-insensitive): title or ISO contains **BMC**, or title/ISO contains **Medicine**. **Exclude** mounted blacklist **MEDICINE (LWW Baltimore)** — never whitelist it.

User rule 2026-09-10: whitelist hits are **priority recommend** inside each layer (after 稿件匹配度). Do **not** label 「可疑」 and do **not** use a red HTML mark. This **replaces** the former v1.14 「刊名含 Medicine 层内降权」 rule.

Whitelist is a boost, not auto-fill: still require reasonable scope match; still never recommend blacklist titles.


## Phase-1 HTML highlight

Highlight **only** cells/rows where **投稿易投指数 ≥ 80** (yellow background). No other mandatory color marks in the checkbox table.

## What not to do

- Do not recommend the three mounted blacklist titles.
- Do not collapse the default layers into a single top-N list; keep 层2 / 层3 / 层4 tables separate (10 each).
- Do not query AIM / author instructions / APC before the user confirms 备选杂志.
- Do not merge yearly IF / quartile / volume / APC into `submission-urls.csv` or skill text as durable lists.
- Do not install `zero565656/journal-recommender` (or similar) as a mounted skill; do not copy its fixed Fit Score weights or abstract→CAS prediction.
- Do not treat Unknown risk as Low Risk.

## Advice provenance

Merged **Gemini + ChatGPT** private advice (2026-09). Absorb/query/delete table: `references/persistence.md`. Extracts: `skill-library/extracts/03_research/jesi-gemini-2026-09.md`, `jesi-chatgpt-2026-09.md`.

## Annual refresh

When the user sends a new JCR workbook, follow `references/annual-update.md`. Keep `references/policy.md` unless they also change blacklist, layers, or the 10-per-layer / layer-order rules.
