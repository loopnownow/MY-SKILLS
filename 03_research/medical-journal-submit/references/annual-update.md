# Annual JCR refresh

Trigger phrases: 更新JCR, 新的影响因子表, 换2027表, 重建推荐库.

## What the user should send

1. New raw workbook, same role as raw rebuild input `JCR20XX影响因子.xlsx` (do not keep in this pack after rebuild).
2. Whether blacklist / layers / 默认每层10本（层2/3/4）；层2补可选 changed. If they say nothing, keep `references/policy.md`.

## What to rebuild

Derived only. Do not hand-edit 22k rows.

- `artifacts/医学投稿推荐_JCR20XX.xlsx`
- layer CSVs in this `references/` folder (yearly **screening cache**)
- `category-index.csv`, `full-pool.csv`
- `artifacts/黑名单_默认挂载.csv` (names stay; metrics may change)

Rebuild curated xlsx + layer CSVs from the raw workbook, then **discard** the raw Clarivate file from this pack (user keeps a private copy if needed). Keep the curated xlsx + derived CSVs.

## Never merge yearly metrics into URL persist

- Do **not** merge JIF, JCR/JCI quartile, or annual volume into `submission-urls.csv`.
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
- `submission-urls.csv` still has URL fields only (no IF/quartile/volume columns).

## What not to bake into SKILL.md

Exact journal lists, APC numbers, article counts, IF values. Those belong in the yearly tables / runtime display, not durable skill prose.
