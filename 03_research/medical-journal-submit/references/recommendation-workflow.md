# Recommendation workflow

## Mounted blacklist

PLoS One, Scientific Reports, MEDICINE (LWW Baltimore). Never recommend.

## Mounted whitelist (priority)

`whitelist-bmc-medicine.csv`: titles/ISO containing **BMC** or **Medicine** (case-insensitive). Priority boost inside layer after MJF. Never include LWW MEDICINE.

## Decision flow (ChatGPT architecture mapped to this pack)

External tools supply **candidates and current evidence**; MY-SKILLS owns the decision.

```text
[Optional] External journal-recommender / query mounts
        → Candidate journal pool + current metadata
        → Journal Difficulty (JDI) + Manuscript Fit (MJF) + Risk
        → MY-SKILLS decision (modules.md / jesi-model.md)
        → Challenge / Target / Safety / Not recommended
```

| Step | Owner | Pack mapping |
|---|---|---|
| Candidate pool + live metrics | 03 query mounts (`query-sources.md`) | Layer CSVs = yearly screening pool; live APIs for rates/APC/AIM |
| Difficulty + Capacity | 04 `jesi-calculator` / JDI · JCI-C · JEI | `jesi-model.md` |
| Fit | 04 `manuscript-fit-analyzer` / **MJF (=MFI)** | Scope, methods, recent papers |
| Risk | 04 Risk Assessment | **Unknown ≠ Low Risk** |
| Personal prior | 04 `submission-prior-logger` / **PAI** | `submission-prior.jsonl` |
| Final tier + layer tables | 04 decision + this workflow | Challenge / Target / Safety → layers below |

Do **not** let an external Fit Score or fixed-weight template pick the final list.

## Every paper: default three layers, **ten** each (+ optional 层2补)

Order of tables (v1.15)

1. 层2 — Q1, IF<5 — **10本** → primary **主攻 / Target** band
2. 层3 — Q2 — **10本** → **Safety偏上/稳妥** band
3. 层4 — Q3 — **10本** → **默认给出** (broader Q3 pool)
4. 层2补 — Q1, 5≤IF≤10 — **10本 if opted in** → **冲刺 / Challenge**; **ask before each use**; **default OFF**

Note: default table order is 层2 → 层3 → 层4. 层2补 is Challenge/optional stretch. **Comprehensive/general medical journals** may be listed when manuscript fit is reasonable (not specialty-only).

Tier labels must be driven by **Journal Ease (JEI/JESI) × MJF × PAI × Practicality − Risk**, not IF/CAS alone.

Score inside a layer by **稿件匹配度** (MJF/MFI, highest) → **BMC/Medicine whitelist boost** (`whitelist-bmc-medicine.csv`) → **投稿易投指数** (JESI) → capacity signal. Do not use curated 易投指数. Use **dynamic weights** when the user states constraints (speed / Q1 / APC).

## Four-module pipeline

```text
sci-metrics-retriever → manuscript-fit-analyzer → jesi-calculator → submission-prior-logger
```

Details: `modules.md`, formulas: `jesi-model.md`, sources: `query-sources.md`, persist: `persistence.md`.

## Two phases

**Phase 1:** tables for 层2 + 层3 + 层4 (**10 rows each** by default); **ask before each run** whether to add 层2补 (**default OFF**); columns: 勾选 | 期刊全称 | 2025 JIF | 年发文量 | 接收率 | 初筛拒稿率 | 送审率 | 匹配理由 | 稿件匹配度 | 投稿易投指数(可带缺标). No 分层/策略 column (titles carry layer; checkboxes keep data-layer/data-tier). Always show rate columns (blank if unknown). JESI always from available metrics; mark partial with in-cell `*` + `缺:…` (`jesi-model.md`). No curated 易投指数. No 置信度/ISO/JIF分区/JCI分区 columns. Comprehensive/general medical titles OK when match is reasonable. No live AIM/fee lookup. Prefer HTML delivery. Do not write yearly metrics/rates into `submission-urls.csv`.

**Phase 2:** only confirmed titles — AIM, author instructions, APC (`aim-author-checklist.md`). Persist new portal URLs to `submission-urls.csv` (URL fields only). Optionally log outcomes later to `submission-prior.jsonl`.

## Phase-1 HTML marks (v1.15)
- Yellow highlight **only** when 投稿易投指数 ≥ 80.
- BMC/Medicine **whitelist priority** (`whitelist-bmc-medicine.csv`); **do not** mark 可疑 / red; LWW MEDICINE stays blacklisted.
- Mounted whitelist after blacklist on every Phase-1 run.
