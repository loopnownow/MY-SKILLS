# Integration map (live stub)

Monthly full log is archived. Current roll starts empty after 2026-10-07.

- **Latest archive:** [`history/INTEGRATION_MAP-20261007.md`](history/INTEGRATION_MAP-20261007.md)
- **Older archive:** [`INTEGRATION_MAP.archive.md`](INTEGRATION_MAP.archive.md)

Append new CHG / decision rows **here** until the next monthly roll, then move this file into `history/INTEGRATION_MAP-YYYYMMDD.md` and replace with a fresh stub.

Harvest must not invent a second evolution log file.

## CHG-20261008-001 — find-journal similar-article check

- User rule 2026-10-08: for each candidate journal, search the last 3–5 years for articles similar to the manuscript title. Cite found articles (title, year, DOI/link) in 匹配理由. None found → lower the tier and write 「近年未见类似文章，已降级」. Never invent articles. A failed search is not a no-hit.
- Canonical: `03_research/find-journal/SKILL.md` § Similar-article check (pack v1.16 → v1.17). Pointers: `rules/policy.md`, `rules/recommendation-workflow.md`, `AGENTS.md`.
- Regenerated `docs/` visualization HTML via `00_orchestrator/scripts/gen_visualization.py` (outputs were stale on main after #126).
- `skill-harvest/scripts/repo_qc.py`: files under `_medical-research-meta/history/` count as historical (legacy-active-refs, stale-ids), like the stub and archive. `history/INTEGRATION_MAP-20261007.md` archive link repointed to `../INTEGRATION_MAP.archive.md` (broken since the monthly roll in #124).
