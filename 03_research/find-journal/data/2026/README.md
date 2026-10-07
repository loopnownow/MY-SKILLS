# Journal datasets (layer / list SSOT)

Annual **screening cache** and list tables for `find-journal`. The curated JCR **xlsx** is not here.

- **Curated xlsx (0doc):** `D:\0Grok\0doc\04-lab-reference\jcr2026\医学投稿推荐_JCR2026.xlsx`
- **Year folder:** `2026/` = current JCR cycle layer CSVs used by the skill.
- **Do not** keep parallel copies under `references/` or `artifacts/`.
- Rules / methods live in `../rules/` and `../SKILL.md`.
- Operational write-back: `submission-urls.csv`, `submission-prior.jsonl` (URL/prior only).
- Alias removals (byte-identical): `secondary-journals.csv` → use `layer3-q2.csv`; `priority-journals.csv` → use `layer2b-q1-if-5to10.csv`.
- Former `artifacts/白名单_*.csv` / `灰名单_*.csv` / `黑名单_默认挂载.csv` were duplicates of English-named files here — deleted; list SSOT is this folder.
