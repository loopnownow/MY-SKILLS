# Persistence rules

## SAVE (durable in this pack)

| What | Where |
|---|---|
| Submission / portal URLs | `references/submission-urls.csv` (URL fields only) |
| Personal prior outcomes | `references/submission-prior.jsonl` (schema: manuscript_type, target_journal, outcome, date, notes) |
| Policy / workflow / framework formulas | `policy.md`, `recommendation-workflow.md`, `jesi-model.md`, `modules.md` |
| Query-source list (capability, not values) | `query-sources.md` |
| Blacklist names | `blacklist.csv` / `blacklist-names.csv` |
| BMC/Medicine priority whitelist | `whitelist-bmc-medicine.csv` |
| Yearly screening cache (layer membership) | `layer2-*.csv`, `layer3-*.csv`, curated xlsx — rebuilt annually |
| Absorbed methodology (rewrite, not copy) | Fit / Risk / Evidence / Submission Tier logic in modules 04 path (`modules.md`, `jesi-model.md`) |

## DO NOT SAVE into CSV / DB-like persist files

- JIF / 5-year JIF / JIF percentile  
- JCR or JCI quartile  
- Annual publication volume / Total articles  
- CiteScore / SJR / SNIP (and similar yearly bibliometrics)  
- APC, indexing status, review-time values, self-citation rates, author-experience values  

These metrics may appear in **HTML or Markdown delivery reports only**, queried or joined at **run time** from the yearly screening cache or live sources. They must **not** be merged into `submission-urls.csv` or baked into skill text as durable delivery data. Retain **query capability** only (`query-sources.md` / module 03 path).

## Absorb / Query / Delete (ChatGPT 2026-09 + Gemini)

Stable methodology is rewritten into MY-SKILLS; changing journal numbers stay query-only; unsuitable prediction/fixed-scoring logic is deleted. Do **not** install `zero565656/journal-recommender` as a mounted skill.

### ABSORB（改写吸收 / rewrite into 04 decision path）

| Original capability | Final treatment | Destination |
|---|---|---|
| Scope Fit / Article Type Fit / Audience Fit | Rewrite + absorb | Fit / MJF (=MFI) |
| Method Fit | Add/enhance | Fit / MJF |
| Recent-paper similarity | Add/enhance | Fit / MJF (+ query for papers) |
| Challenge / Target / Safety | Rewrite + absorb | Submission Tier (driven by ease × fit × personal × practicality — not IF/CAS alone) |
| Risk Check | Rewrite + absorb | Journal Risk Assessment; **Unknown ≠ Low Risk** |
| Evidence / Confidence | Absorb | Every metric: `value` + `source` + `retrieval_date` + `confidence` |

### QUERY ONLY（03 查询能力 / never bake values into skill or DB）

| Metric / data | Treatment |
|---|---|
| IF / JIF | Query only |
| JCI / JCR / CAS | Query only |
| APC | Query only |
| Indexing | Query only |
| Review time | Query only |
| Annual publication volume | Query only |
| Self-citation | Query only |
| Author-experience values | Query only |

### DELETE（删除 / do not absorb）

| Item | Why |
|---|---|
| CAS prediction from abstract | Unreliable (esp. imaging / clinical / radiomics); never dictate quartile. If needed later, redesign as Manuscript Strength Profile for strategy only |
| Fixed scoring weights | Use dynamic weights from user constraints (speed vs Q1 vs APC); Gemini formulas are **initial defaults only** |
| Fixed LetPub dependency | LetPub is an auxiliary query source, not a hard dependency |
| Fixed output template | Keep useful fields; final table shape follows this pack’s Phase-1/2 + module 04 |
| Monolithic external `SKILL.md` | Dismantle into discovery / query / decision paths — do not retain unchanged |

## Evidence / Confidence QC

Every reported metric should carry:

```text
value | source | retrieval_date | confidence
```

Example: `acceptance_rate: value 18%, source journal_official, date 2026-09, confidence high`.  
Unknown values stay unknown — **do not invent**. Missing risk evidence is **not** “low risk.”

## `submission-urls.csv` schema (URL fields only)

```text
期刊全称,ISO缩写,ISSN,eISSN,投稿网址,来源备注,updated
```

If IF / quartile / volume columns are ever added, remove them.

## Delivery

- User-facing Phase-1/Phase-2: prefer **HTML** (tables may *display* JIF/quartile/volume as runtime fields).  
- After confirming portals: write **submission URLs only** back to `submission-urls.csv`.  
- Personal outcomes: append lines to `submission-prior.jsonl` — never store yearly IF on those lines.
