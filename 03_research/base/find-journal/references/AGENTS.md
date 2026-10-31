# AGENTS - find-journal

Authority order: `SKILL.md` -> `03_research/base/find-journal/rules/policy.md` -> `03_research/base/find-journal/rules/recommendation-workflow.md` -> this file.
If this file conflicts with `SKILL.md` / `policy.md`, **follow SKILL/policy**.

Aligned with **SKILL.md metadata.version 1.18** (10/10/10 + layer-4 default + general journals allowed).
2026-10-31 (t1458u): runtime pools collapsed to one table; per-project journal notes live in `ref/citation`.

## Data locations (single source)

- List gates: `data/2026/` (blacklist / graylist / whitelist-bmc-medicine / submission-urls) - in this pack.
- Runtime selection pools: `{find_journal_pools}` = `{doc_library_journals}` - `index.csv` (`layer`, `jif_2025`, `jcr_year`, `l1`, `l2`, `whitelist`, `queried_at`), `index.xlsx`, `l1-l2-map.csv`; archive under `journals\archive\<year>\`.
- Submitted / 选刊 whitelist + priors: `{find_journal_submission}` = `{doc_library_jcr}\<year>\submission\` (now 2026).
- Curated xlsx: `{jcr2026_xlsx}` (0doc `mem\`, not in git).
- Per-project candidates: `<project>/ref/citation/journals.csv` + `_notes.md`.
- Ethics approvals (batch numbers / validity) are outside this pack: `{doc_ethics_approvals}` + `{doc_ethics_index}`.

## When to use

User asks for journal recommendation (推荐杂志) / 选刊 / where to submit / JCR-JCI quartile / IF layers / APC-AIM (only after shortlist confirmed).

Owner: **Victor** - `03_research`. Bai owns 选刊 advancement after titles are chosen. Journal selection routes through 03 `find-journal`; formatting through `05_manuscript/base/write-paper/`.

## Every journal-recommendation run

1. Blacklist first (`data/2026/blacklist.csv`): never list PLoS One / Scientific Reports / MEDICINE (LWW Baltimore).
2. Read the manuscript. **Ask before each run** whether to include 层2补 (Challenge); **default OFF**.
   - 层2 - Q1 and IF < 5 - `{find_journal_pools}\index.csv` where `layer=2-Q1且IF小于5` (Target; 10 journals)
   - 层3 - Q2 - `layer=3-Q2` (safer/steady; 10 journals)
   - 层4 - Q3 - `layer=4-Q3` (**default on**; 10 journals)
   - 层2补 - Q1 and 5 <= IF <= 10 - `layer=2补-Q1且IF5到10` (Challenge; opt-in only)
3. Do **not** use layer 1 (IF>10) unless the user asks. Comprehensive / general medical journals OK when match is reasonable.
4. Rank inside a layer by: 稿件匹配度 (MJF/MFI, highest) -> BMC/Medicine whitelist -> 投稿易投指数 (JESI/JEI) -> capacity signal (年发文量, weak tie-breaker). Use dynamic weights when user constraints differ (speed / Q1 / APC); no fixed weights as policy. Do not use curated 易投指数 in ranking/JDI.
   - Similar-article check, round 2: round 1 ranks first and does not search. In round 2, no similar article in the last 3-5 years -> lower it inside its layer; write 「近年未见类似文章，已降级」. Full rule: `SKILL.md` section Similar-article check.
5. Phase-1 columns: 勾选 | 期刊全称 | 2025 JIF | 年发文量 | 接收率 | 初筛拒稿率 | 送审率 | 匹配理由 | 稿件匹配度 | 投稿易投指数(可带缺标)
   - No 分层/策略 column (layer in section titles; keep data-layer/data-tier on checkboxes). Chinese score headers; always show rate columns (blank/`-` if unknown). Do **not** show 置信度 / ISO / JIF分区 / JCI分区.
   - JESI: always from available A/R/P + MJF; partial scores marked in-cell (`*` + `缺:...`); never invent rates. See `jesi-model.md`.
   - JIF / volume / rates are display-only; never persist them into `data/2026/submission-urls.csv`.
   - Per-layer default count: 10. Specialty preferred; 综合/全科刊 allowed when fit is reasonable.
6. No AIM / author instructions / APC in phase 1. Then ask the user to circle 备选杂志.
7. Phase 2 only after confirmation - see `03_research/base/find-journal/rules/aim-author-checklist.md`.
   - User HTML short table: 期刊全称 | JCR分区 | 影响因子 | 年发文量 | 投稿网址/作者须知.
   - Show full URLs (not bare 「投稿须知」). Short table omits ISO, OA, 置信, 分刊详情, APC.
   - Quartile/IF/volume display-only; portal URLs -> `data/2026/submission-urls.csv`.
8. Pipeline: optional external candidate pool -> metrics -> fit -> JESI -> prior (`modules.md`, `jesi-model.md`). External recommender = query provider only.
9. Delivery: HTML for the user; write submission URLs only back to `data/2026/submission-urls.csv`; optional prior lines -> `{find_journal_submission}\submission-prior.jsonl`.
10. Risk: **Unknown != Low Risk.**

## Display hard rules (v1.16)

- BMC/Medicine whitelist priority (`data/2026/whitelist-bmc-medicine.csv`); no 「可疑」/红标; LWW MEDICINE stays blacklisted.
- Phase-1 HTML: only 投稿易投指数 >= 80 gets yellow highlight.

## Do not

- Recommend the three blacklist titles.
- Collapse default layers into one top-N list.
- Route formatting / house style to `write-paper` (选刊走 03 `find-journal`).
- Invent word limits or APC; invent missing risk as "low".
- Persist annually updated IF / JCR-JCI-CAS / APC / review-time / volume into CSV/DB-like files. The yearly screening cache `journals\index.csv` is the single approved exception: rebuilt yearly, never hand-edited.
- Install an external journal-recommender as a live skill; copy fixed Fit Score weights or abstract->CAS prediction.
- Scatter journal notes as `.md` / `.json` / `.html` inside a project's `ref/`; merge into `ref/citation/_notes.md` and archive originals under `ref/tmp/`.

## Wording

- Say 本仓, never 「空挂」.

## Journal format compliance (nested)

Not a registry fine id. After 备选杂志 are chosen, invoke `03_research/base/find-journal/journal-format-compliance/SKILL.md` by path/keyword. Parent owns 选刊; nested pack owns guideline plan + Track Changes. See `SKILL.md` section Journal format compliance.
