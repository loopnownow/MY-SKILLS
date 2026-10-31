# Annual JCR refresh

Trigger phrases: 更新JCR, 新的影响因子表, 换2027表, 重建推荐库 (keep ZH match keys).

## What the user should send

1. New raw workbook, same role as raw rebuild input `JCR20XX影响因子.xlsx` (do not keep in this pack after rebuild).
2. Whether blacklist / layers / default 10 titles per layer (层2/3/4); optional 层2补 changed. If they say nothing, keep `03_research/base/find-journal/rules/policy.md`.

## What to rebuild

Derived only. Do not hand-edit 22k rows.

- **Curated xlsx SSOT (0doc `mem\`, not in git):** `{jcr2026_xlsx}` (current: `{doc_root}\mem\医学投稿推荐_JCR2026.xlsx`). Mutable workbook lives under `mem\`, not the theme tree.
- **List gates (skill pack):** `data/<YEAR>/` (current: `data/2026/`) — blacklist/graylist/whitelist + `submission-urls.csv` only.
- **Runtime pools (0doc):** `{find_journal_pools}` = `{doc_root}\_library\journals\` — single `index.csv` with a `layer` column, plus `l1-l2-map.csv`; the old `full-pool.csv` / `layer*.csv` / `priority-compact.json` / `publisher-fees.csv` are archived read-only under `journals\archive\<YEAR>\`. Selection-side private files (`whitelist-submitted.csv` / `submission-prior.jsonl`) live in the same folder since 2026-10-31 (the former `_library\jcr\<YEAR>\` level is retired; `index.xlsx` is retired too).
- Rebuild the curated xlsx under `mem\`, rebuild `journals\index.csv` from the raw Clarivate tables, then **discard** the raw file from the skill pack (user keeps a private copy if needed).

When the year rolls (e.g. 2027), create `data/2027/` for list gates, rebuild `{find_journal_pools}\index.csv` with `jcr_year=2027` / `metric_year=2026`, archive the previous table under `journals\archive\2026\`, put the new curated xlsx under `{doc_root}\mem\医学投稿推荐_JCR20XX.xlsx` (update `{jcr2026_xlsx}`), and **append** that year's new submission priors / whitelist rows to `{find_journal_submission}\submission-prior.jsonl` / `whitelist-submitted.csv` (both cumulative; do **not** create a new `jcr\<year>\` folder — retired 2026-10-31).

**Timing:** the rebuild happens in **July**, after Clarivate ships the new JCR edition (the 2026 edition carries 2025 JIF values). Do not refresh mid-year.

## Never merge yearly metrics into URL persist

- Do **not** merge JIF, JCR/JCI quartile, or annual volume into `data/2026/submission-urls.csv`.
- Layer CSVs may hold those fields as screening cache; reports may **display** them at run time; durable delivery persist for portals stays URL-only (`persistence.md`).
- Skill text (`SKILL.md`, `policy.md`) must **not** hardcode IF lists, article counts, or APC numbers.

## Column mapping (check first)

Expected raw sheets: `Journals`, `Category_Quartiles`.

Journals: Journal name, Abbreviated journal, Publisher, Editions, 20XX JIF, JIF quartile, JIF rank, JCI quartile, Total citations, Total articles.

Category_Quartiles: Journal name, ISSN, eISSN, Category, JIF quartile, JCI quartile, JIF percentile, 20XX JIF, 5-year JIF, JCI.

If headers differ, map them. Do not assume the year is still labeled 2025 JIF.

## Rebuild checks

- Blacklist three names still resolve (watch PLoS One vs PLOS ONE).
- Layer 2 max IF < 5; 2补 IF between 5 and 10 inclusive; layer 3 is Q2.
- Blacklist titles absent from layer CSVs.
- SKILL.md `metadata.source_table` and data-year wording updated.
- `policy.md` untouched unless the user changed rules.
- `data/2026/submission-urls.csv` still has URL fields only (no IF/quartile/volume columns).

## What not to bake into SKILL.md

Exact journal lists, APC numbers, article counts, IF values. Those belong in the yearly tables / runtime display, not durable skill prose.
