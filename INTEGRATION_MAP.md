# Integration map (live stub)

Monthly full log is archived. Current roll starts empty after 2026-10-07.

- **Latest archive:** `INTEGRATION_MAP-20261007.md` — lives under `D:\0del\00_orchestrator_reorg_20261017\_medical-research-meta_history\MY-SKILLS_history\` (moved 2026-10-17 with `history/`; not restored in-repo). Parallel copy: `...\grok_history\`.
- **Older archive:** `INTEGRATION_MAP.archive.md` — lives under `D:\0del\00_orchestrator_reorg_20261018\MY-SKILLS_history\` (moved 2026-10-18 QC Batch 3 A1; not restored in-repo).

Append new CHG / decision rows **here** until the next monthly roll, then archive this file into `D:\0del\00_orchestrator_reorg_20261017\_medical-research-meta_history\` (or a successor dated folder) as `INTEGRATION_MAP-YYYYMMDD.md` and replace with a fresh stub. Do not recreate an in-repo `history/` folder for the monthly roll.

Harvest must not invent a second evolution log file.


## CHG-20261018-slim-rules-landing — absorb MY-RULES standing policy (PR #154)

- Branch `chore/slim-rules-landing-20261018` merge `4aedd18` (commit `9eadf89`).
- Reverse Rules authority into `ownership-contract` + domain `qc/`; add `handoff-monitor` and `skill-evolution`.
- Extend standing-delivery, workspace A/B, manuscript bans, response hard rules; point SKILL/gates/routing/runtime-flow/mount-recipe.
- Post-merge sync noted in `lifecycle-cache`; new `tests/test_rule_landing.py` + tighten lab-ste path assert.
- Do **not** sync `.grok/skills` (repo policy landing only).

## CHG-20261018-batch3-5 — QC structure + content + regression tests

- A1: `INTEGRATION_MAP.archive.md` moved to `D:\0del\00_orchestrator_reorg_20261018\MY-SKILLS_history\`; live stub points at absolute 0del path.
- Caches (`.pytest_cache` + `__pycache__`) moved to `D:\0del\my-skills-qc-20261018\caches\` (not deleted); pytest uses `-p no:cacheprovider`.
- `.cursorignore` mounts-cap dead entry removed; keep `.gitignore` defense; `00/SKILL.md` wording synced.
- F42: `review-isolation` row added to `00_orchestrator/workflows/README.md`.
- B2: `fill-protocol/MODULE.md` trimmed to principles + paths (missing assets noted).
- D2: design-experiment bilingual pair headers (validation / study-design).
- F46: Absent labels → 归档勿建.
- Dated refs: snapshot notes on ai-radiogenomics-12-24-roadmap + journal-patterns-2023-2026.
- Batch5: four regression tests under `tests/`.
- Do **not** sync `.grok/skills`.

## CHG-20261018-batch2 — QC Batch 2 metadata + old names (F15–F36)

- PR #152 (`fix/qc-batch2-old-names`, merge `71c74f3`, commit `e9a2c2d`).
- Owner paths → `NN_slug/base/`; hyphen B paths → underscore/base; retired fine-ids → §7 map; clear (was B) residue.
- Registry chassis 00–07; review-response specialist_hint Aitee; archived.old_path + historical: true (E1).
- README layout + 07; tests tighten.
- Not A1 archive move / not full B2 fill trim / not D2 merge.
- Do **not** sync `.grok/skills`.

## CHG-20261018-batch1 — QC Batch 1 P0 dead links (F1–F14)

- PR #151 (`fix/qc-batch1-p0-deadlinks`, merge `84a7f8e`, commit `098166a`).
- style_lint mounts-cap fallback removed; sci-manuscript path fixes; presets C1 in-repo paths.
- fill-protocol owners; radiomics/venue-templates live wording; style-tells → base ban-terms.yaml.
- Do **not** sync `.grok/skills`.

## CHG-20261017-001 — meta tidy: 06/07 seats + history path

- `README.md`: add `07_response` row; reviewer response → 07 (Aitee); 06 = review only (Lee).
- `ARCHITECTURE.md` intent tables: same 06/07 seat alignment; root `ARCHITECTURE.md` stays one-line pointer.
- History archive clarified at `D:\0del\00_orchestrator_reorg_20261017\_medical-research-meta_history\` (broken relative `history/` links removed).
- Drop `__pycache__` under repo-root `tests/` (formerly a meta package folder); `.gitignore` already covers it.
- Tests: expectation strings for 06→07 (response path, response-enters-07 phrase, allow top-level `07_response`).
- `VERSION.txt` trimmed to recent Oct-2026 blocks; older → this map / archive / 0del history.

## CHG-20261008-001 — find-journal similar-article check

- User rule 2026-10-08: for each candidate journal, search the last 3–5 years for articles similar to the manuscript title. Cite found articles (title, year, DOI/link) in 匹配理由. None found → lower the tier and write 「近年未见类似文章，已降级」. Never invent articles. A failed search is not a no-hit.
- Canonical: `03_research/base/find-journal/SKILL.md` § Similar-article check (pack v1.16 → v1.17). Pointers: `rules/policy.md`, `rules/recommendation-workflow.md`, `AGENTS.md`.
- Regenerated `docs/` visualization HTML via `04_analysis/personal/visualization/scripts/gen_visualization.py` (outputs were stale on main after #126).
- `skill-harvest/scripts/repo_qc.py` (archived under `D:\0del\00_orchestrator_reorg_20261017\skill-harvest_MY-SKILLS\`): historical map files under the 0del `_medical-research-meta_history` tree count as historical (legacy-active-refs, stale-ids), like this stub and archive. The Oct-7 monthly file is at `D:\0del\00_orchestrator_reorg_20261017\_medical-research-meta_history\MY-SKILLS_history\INTEGRATION_MAP-20261007.md` (in-repo `history/` link removed).

## CHG-20261008-002 — find-journal similar-article check is round 2

- User rule update 2026-10-08: the similar-article search is round 2 of journal selection, not a step before ranking.
- Round 1 ranks by the existing criteria and does not search. Round 2 searches each candidate for similar articles from the last 3–5 years, then lowers a journal with no similar article inside its layer. Cite found articles (title, year, DOI/link). Never invent articles. A failed search is not a no-hit.
- Canonical: `03_research/base/find-journal/SKILL.md` § Similar-article check (pack v1.17 → v1.18). Pointers: `rules/policy.md`, `rules/recommendation-workflow.md`, `AGENTS.md`.
