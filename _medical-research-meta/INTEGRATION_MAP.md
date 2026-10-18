# Integration map (live stub)

Monthly full log is archived. Current roll starts empty after 2026-10-07.

- **Latest archive:** `INTEGRATION_MAP-20261007.md` — lives under `D:\0del\00_orchestrator_reorg_20261017\_medical-research-meta_history\MY-SKILLS_history\` (moved 2026-10-17 with `_medical-research-meta/history/`; not restored in-repo). Parallel copy: `...\grok_history\`.
- **Older archive:** [`INTEGRATION_MAP.archive.md`](INTEGRATION_MAP.archive.md)

Append new CHG / decision rows **here** until the next monthly roll, then archive this file into `D:\0del\00_orchestrator_reorg_20261017\_medical-research-meta_history\` (or a successor dated folder) as `INTEGRATION_MAP-YYYYMMDD.md` and replace with a fresh stub. Do not recreate an in-repo `history/` folder for the monthly roll.

Harvest must not invent a second evolution log file.

## CHG-20261017-001 — meta tidy: 06/07 seats + history path

- `_medical-research-meta/README.md`: add `07_response` row; reviewer response → 07 (Aitee); 06 = review only (Lee).
- `_medical-research-meta/ARCHITECTURE.md` intent tables: same 06/07 seat alignment; root `ARCHITECTURE.md` stays one-line pointer.
- History archive clarified at `D:\0del\00_orchestrator_reorg_20261017\_medical-research-meta_history\` (broken relative `history/` links removed).
- Drop `__pycache__` under `_medical-research-meta`; `.gitignore` already covers it.
- Tests: expectation strings for 06→07 (response path, response-enters-07 phrase, allow top-level `07_response`).
- `VERSION.txt` trimmed to recent Oct-2026 blocks; older → this map / archive / 0del history.

## CHG-20261008-001 — find-journal similar-article check

- User rule 2026-10-08: for each candidate journal, search the last 3–5 years for articles similar to the manuscript title. Cite found articles (title, year, DOI/link) in 匹配理由. None found → lower the tier and write 「近年未见类似文章，已降级」. Never invent articles. A failed search is not a no-hit.
- Canonical: `MY-SKILLS-base/03-research/find-journal/SKILL.md` § Similar-article check (pack v1.16 → v1.17). Pointers: `rules/policy.md`, `rules/recommendation-workflow.md`, `AGENTS.md`.
- Regenerated `docs/` visualization HTML via `04_analysis/personal/visualization/scripts/gen_visualization.py` (outputs were stale on main after #126).
- `skill-harvest/scripts/repo_qc.py` (archived under `D:\0del\00_orchestrator_reorg_20261017\skill-harvest_MY-SKILLS\`): historical map files under the 0del `_medical-research-meta_history` tree count as historical (legacy-active-refs, stale-ids), like this stub and archive. The Oct-7 monthly file is at `D:\0del\00_orchestrator_reorg_20261017\_medical-research-meta_history\MY-SKILLS_history\INTEGRATION_MAP-20261007.md` (in-repo `history/` link removed).

## CHG-20261008-002 — find-journal similar-article check is round 2

- User rule update 2026-10-08: the similar-article search is round 2 of journal selection, not a step before ranking.
- Round 1 ranks by the existing criteria and does not search. Round 2 searches each candidate for similar articles from the last 3–5 years, then lowers a journal with no similar article inside its layer. Cite found articles (title, year, DOI/link). Never invent articles. A failed search is not a no-hit.
- Canonical: `MY-SKILLS-base/03-research/find-journal/SKILL.md` § Similar-article check (pack v1.17 → v1.18). Pointers: `rules/policy.md`, `rules/recommendation-workflow.md`, `AGENTS.md`.
