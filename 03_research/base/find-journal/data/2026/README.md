# Journal datasets (list gates only)

Annual **list gates** for `find-journal`. Large runtime selection pools live in **0doc**, not in MY-SKILLS.

## In this folder (MY-SKILLS — keep)

- `blacklist.csv` / `blacklist-names.csv` — never recommend
- `graylist.csv` / `graylist-names.csv` — not preferred when better matches exist
- `whitelist-bmc-medicine.csv` — BMC / Medicine pattern boost
- `submission-urls.csv` — portal URL write-back only (no IF/quartile/volume)
- `README.md`, `SUBMISSION_PRIVACY.md`

## Runtime pools (0doc — not in git)

Path: `D:\0Grok\0doc\04-lab-reference\find-journal\data\2026`

(alias: `{doc_root}\04-lab-reference\find-journal\data\2026`)

- `full-pool.csv`, `category-index.csv`
- `layer1-q1-if-gt10.csv`, `layer2-q1-if-lt5.csv`, `layer2-q1-if-lt10.csv`, `layer2b-q1-if-5to10.csv`
- `layer3-q2.csv`, `layer4-q3.csv`
- `priority-compact.json`, `publisher-fees.csv`

**Runtime selection pools live in 0doc; this skill keeps list gates only.**

## Other SSOT

- **Curated xlsx (0doc):** `{jcr2026_xlsx}`
- Personal prior / 投过 whitelist (0doc, not in git): see `SUBMISSION_PRIVACY.md` and alias `find_journal_submission` in `00_orchestrator/references/lab-paths.yaml`.
- Per-project 选刊/已投名单 → `<project>/ref/` (e.g. `journals-submitted.md`) — never in MY-SKILLS.
- Rules / methods live in `../rules/` and `../SKILL.md`.
- Alias removals (byte-identical): `secondary-journals.csv` → use `layer3-q2.csv`; `priority-journals.csv` → use `layer2b-q1-if-5to10.csv` (both now under 0doc pools).