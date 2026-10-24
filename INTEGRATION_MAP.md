# Integration map (live stub)

Monthly full log is archived. Current roll starts empty after 2026-10-07.

- **Latest archive:** `INTEGRATION_MAP-20261007.md` — lives under `D:\0del\00_orchestrator_reorg_20261017\_medical-research-meta_history\MY-SKILLS_history\` (moved 2026-10-17 with `history/`; not restored in-repo). Parallel copy: `...\grok_history\`.
- **Older archive:** `INTEGRATION_MAP.archive.md` — lives under `D:\0del\00_orchestrator_reorg_20261018\MY-SKILLS_history\` (moved 2026-10-18 QC Batch 3 A1; not restored in-repo).

Append new CHG / decision rows **here** until the next monthly roll, then archive this file into `D:\00db\_lab\_ledgers\<dated-folder>\` (or a successor dated folder) as `INTEGRATION_MAP-YYYYMMDD.md` and replace with a fresh stub. Do not recreate an in-repo `history/` folder for the monthly roll.

> **2026-10-24:** the `D:\0del\00_orchestrator_reorg_2026*` / `D:\0del\my-skills-qc-*` archives named below went to the Recycle Bin when 0del was emptied. Paths are kept as history; restore from the Recycle Bin to read them.

Harvest must not invent a second evolution log file.


## CHG-20261020-deepscan-fix — deep-scan P0/P1 absorb

- Branch `fix/deepscan-p0-p1-20261020` (Asia/Shanghai 2026-10-20), registry `change_id` bumped.
- **Ids**: 66 B-era call-site ids in 29 files → canonical fine ids (04-fig-flow→draw-flowchart ×13, 04-fig-plot→plot-figures ×13, 04-stats-models→meta-analysis ×12, 02-imaging-io→imaging-io ×5, 02-tables→clean-data ×4, 04-stats-power→calc-sample-size ×4, 02-imaging-qc→preprocess-imaging ×3, 02-radiomics-habitat→analyze-stats ×7, 02-lit fixes ×3). Three unmapped names (`04-stats-power`, `03-lit-fulltext`, `03-lit-cite`) added to `legacy_aliases.yaml`.
- **Dead pointers**: `ban-phrases.md` → `vocab/L2/preferred.md` §1c; `report-checks.md` self-row → "Part A of this file"; `guideline-router.md` → `write-venue/radiology-writing/journal-family-writing-style.md`; `mount-review-polish-recipe.md` → `06_review/personal/review.md` §0; `ai_patterns.md` → `vocab/L1/patterns.md`; `retraction-watcher/MODULE.md` → `references/audit-reference.md`; `data-impute` → `clean-data` impute module.
- **mounts-cap**: bytes (624 files) moved to `D:\0del\_by-function\mounts-cap-retired-20261020`; README / lab-paths / lifecycle-cache / NOTICE narratives unified (the three files had disagreed on whether the cache was emptied, deleted, or still present).
- **State claims**: `PROPOSED/MOUNTED` mix removed from README + ARCHITECTURE (registry has 0 PROPOSED); 01 SKILL documents the A-local-pack exception (`base/vocab/`, `base/write-venue/`); `Aitor-format.md` owner → `05_manuscript/personal/`; raw lab paths → `{alias}` in 13 files.
- **Tests**: `PATH_UNIT_ALIAS_KEYS` emptied (no B-era directory exists); new `test_bare_md_cites`, `test_alias_targets_exist`, `test_no_raw_lab_paths`, `test_docs_match_registry_state`, `test_ledger_freshness`; `test_owner_fields` / `test_pre_submit_checks` now run on the runtime tree (relative parts + rglob fallback).
- Sync whitelist post-merge: changed skill bodies + `registry.yaml` + `legacy_aliases.yaml` + `VERSION.txt` + `INTEGRATION_MAP.md` → `{SKILLS}` per skills.md §1b.

## CHG-20261019-scan-fix-p0-p2 — scan fix absorb (PR pending)

- Branch `chore/scan-fix-p0-p2-20261019`: apply SCAN-REPORT P0/P1/P2 (Asia/Shanghai 2026-10-19).
- P0: rewrite live `~/.grok/AGENTS.md` required reads → My rule / network-security / skills (+ optional workspace-layout); replace all bare qc/local-checks cites cites → `05_manuscript/qc/manuscript-local-qc.md`; Aitor-format ban-phrases → `05_manuscript/base/vocab/L1/ban-phrases.md` (+ sci-overrides).
- P1: cross-link qc `reporting-guideline-route` ↔ base `guideline-router` (Gate SSOT vs writing audit; CLAIM/CLEAR footnotes); align Integrity·pre-06 mid-entry G-CIT wording with gates.md; add `nature-reporting-summary.md` stub; add **G-07** QUALITY row; fix manuscript-local-qc / cross-manuscript-qc ownership/move headers; retarget paper-claim-audit / external-principles cites to `references/…` and shrink `ALLOW_MISSING`; NOTICE Archify → `04_analysis/personal/visualization/`.
- P2: mmd `LayerBasease`→`LayerBase`; NOTICE pack 00–07 + ARS topology-inspiration line; bare-relative cite regression in `test_inline_paths_exist.py`.
- Also documents prior same-day merges already on main: Integrity pre-06 + R&R (PR #156), P0 nature-stats/reviewer/figure + K-Dense router, P1 ref-verify/response/venue/data-avail/lit-appraisal (PR #157).
- Sync whitelist post-merge: changed skill bodies + `INTEGRATION_MAP.md` + `VERSION.txt` → `{SKILLS}` per skills.md §1b.

## CHG-20261019-integrity-rereview — Integrity · pre-06 + R&R (PR #156)

- Documented on main via PR #156: `I25` Integrity · pre-06, `I45` / `P06r` re-review lite; mid-entry Need06 OK; gates.md Integrity compositions; runtime-flow(.md/.mmd) nodes.
- No second SSOT: compositions reuse G-FACT / G-CIT / G-LIT + 05/06 qc checklists.

## CHG-20261019-p0-absorb — nature-stats/reviewer/figure + K-Dense reporting router

- P0 absorb already on main (merge path via chore/runtime-flow-integrity + follow-ons): figure-stats-legend / figure-qa-minima; stats-failure-modes / forensic-consistency / technical-concern-coverage / review-release-gates; reporting-guidelines-router.json (K-Dense MIT metadata).

## CHG-20261019-p1-absorb — ref-verify / response / venue / data-avail / lit-appraisal (PR #157)

- P1 absorb already on main (PR #157): refs-verified, venue-compliance-minima / venue-currency, data-code-availability, 07 routing, appraisal-tool-route, doi-crossref-field-audit / lit-pipeline-router pointers. NOTICE covers Yuan1z Apache-2.0 + K-Dense MIT.

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
- F42: `review-isolation` row added to `01_skill-integration/workflows/README.md` (formerly under 00 workflows pointer).
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
