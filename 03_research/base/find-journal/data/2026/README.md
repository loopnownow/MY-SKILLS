# Journal datasets (list gates only)

Annual **list gates** for `find-journal`. Large runtime selection pools live in **0doc**, not in MY-SKILLS.

## In this folder (MY-SKILLS — keep)

- `blacklist.csv` / `blacklist-names.csv` — never recommend
- `graylist.csv` / `graylist-names.csv` — not preferred when better matches exist
- `whitelist-bmc-medicine.csv` — BMC / Medicine pattern boost
- `submission-urls.csv` — portal URL write-back only (no IF/quartile/volume)
- `README.md`, `SUBMISSION_PRIVACY.md`

## Runtime pools (0doc — not in git)

Path: `{find_journal_pools}` = `_library\journals\`

- `index.csv` + `index.xlsx` — **single table** (2026-10-31 t1458u): `layer`, `jcr_year`, `metric_year`, `jif_2025`, `quartile_jif`, `quartile_jci`, `articles`, `l1`, `l2`, `whitelist`, `gate`, `queried_at`
- `l1-l2-map.csv` — 70 WoS disciplines -> `l1`,`l2`
- `archive\2026\` — pre-compression files (`full-pool.csv`, `layer1..layer4`, `category-index.csv`, `priority-compact.json`, `publisher-fees.csv`); read-only history

Layer filter values: `1-Q1且IF大于10` / `2-Q1且IF小于5` / `2补-Q1且IF5到10` / `3-Q2` / `4-Q3`.

**Runtime selection pools live in 0doc; this skill keeps list gates only.** Refresh yearly in July, after the new JCR release.

## Other SSOT

- **Curated xlsx (0doc):** `{jcr2026_xlsx}`
- Advanced prior / 投过 whitelist (0doc, not in git): see `SUBMISSION_PRIVACY.md` and alias `find_journal_submission` in `00_orchestrator/references/lab-paths.yaml`.
- Per-project 选刊/已投名单 -> `<project>/ref/citation/journals.csv` (+ `_notes.md`) — never in MY-SKILLS.
- Rules / methods live in `../../rules/` and `../../SKILL.md`.
- Alias removals (byte-identical): `secondary-journals.csv` → use `layer3-q2.csv`; `priority-journals.csv` → use `layer2b-q1-if-5to10.csv` (both now under 0doc pools).
