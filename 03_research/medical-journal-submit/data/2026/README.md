# Journal datasets (SSOT)

Annual curated pool and list tables for `medical-journal-submit`.

- **Year folder:** `2026/` = current JCR cycle used by the skill.
- **Do not** keep parallel copies under `references/` or `artifacts/`.
- Rules / methods live in `../rules/` and `../SKILL.md`.
- Operational write-back: `submission-urls.csv`, `submission-prior.jsonl` (URL/prior only).
- Alias removals (byte-identical): `secondary-journals.csv` → use `layer3-q2.csv`; `priority-journals.csv` → use `layer2b-q1-if-5to10.csv`.
- Former `artifacts/白名单_*.csv` / `灰名单_*.csv` / `黑名单_默认挂载.csv` were duplicates of English-named files here — deleted; SSOT is this folder.
