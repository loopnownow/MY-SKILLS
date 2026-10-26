# Integration map (live stub)

Monthly full log is archived. The live roll below is newest-first; entries dated before 2026-10-07 live in the archived roll.

> **Two ledgers, by design (2026-10-25):** `VERSION.txt` keeps the one-line release summary for Oct-2026; this map keeps the structured detail. `tests/test_ledger_assurance.py` requires the registry `change_id` in both files, so the overlap is intended — do not collapse either one.

- **Latest archive:** `INTEGRATION_MAP-20261007.md` — lives under `D:\0del\00_orchestrator_reorg_20261017\_medical-research-meta_history\MY-SKILLS_history\` (moved 2026-10-17 with `history/`; not restored in-repo). Parallel copy: `...\grok_history\`.
- **Older archive:** `INTEGRATION_MAP.archive.md` — lives under `D:\0del\00_orchestrator_reorg_20261018\MY-SKILLS_history\` (moved 2026-10-18 QC Batch 3 A1; not restored in-repo).

Append new CHG / decision rows **here** until the next monthly roll, then archive this file into `D:\00db\_lab\_ledgers\<dated-folder>\` (or a successor dated folder) as `INTEGRATION_MAP-YYYYMMDD.md` and replace with a fresh stub. Do not recreate an in-repo `history/` folder for the monthly roll.

> **2026-10-24:** the `D:\0del\00_orchestrator_reorg_2026*` / `D:\0del\my-skills-qc-*` archives named below went to the Recycle Bin when 0del was emptied. Paths are kept as history; restore from the Recycle Bin to read them.

Harvest must not invent a second evolution log file.


## CHG-20261025-fine-id-stats-analysis (2026-10-25)

- Canonical fine-id rename: `analyze-stats` → `stats-analysis`.
- Pack path: `02_data-processing/base/stats-analysis/`; digest: `02_data-processing/personal/analysis/stats-analysis-digest.md`.
- `legacy_aliases.yaml`: `analyze-stats` → `stats-analysis`; former targets (`radiomics-ml`, `02-radiomics-habitat`) now resolve to `stats-analysis`.
- Coarse alias key `stats-analysis` → `02_data-processing` unchanged (seat map).
- `_code` pointer seat remains `stats-analysis`; `analyze-stats` folder stays retired alias.

## CHG-20261025-lab-paths-p0 (2026-10-25)

- **lab-paths.yaml** version 5 → 6.
- `{code_figures}` → `D:\0Grok\0doc\_code\02-data-processing\draw-flowchart` (confirmed on disk; former `04-analysis\draw-flowchart` gone with 04 merge).
- `{code_06_review}` **retired** — no `_code\06-review`; review seat is `{skills_git}\06_review` only. Alias removed (no live cites).
- `{doc_lab_ste}` → `D:\0del\_by-project\skill-harvest-sources-20261024\sources\library-methods-20261023\lab-ste` (full SPEC/`config.yaml`; **not** `_library\lab-ref-ranges`). Live method SSOT remains `05_manuscript/base/vocab/L3/`.
- `{doc_grants}` → `...\library-ftp-20261023\grants` (same durable tree). Word originals also under `{doc_word_archive}\03-research\grants`. Digests stay in `03_research/personal/references/`.
- `{doc_fill_protocol}` → `...\library-methods-20261023\study-design\fill-protocol`. Live Jinshan notes: `03_research/personal/fill-protocol`; scripts: `{code_fill_protocol}`; PHI blanks: `{doc_ethics}`.
- Prose: `05_manuscript/base/vocab/L3/lab-ste.md` "Live library" → park + method SSOT wording.

## CHG-20261025-stats-path-github (2026-10-25)

- **Stats SSOT:** `{code_stats}` / `{code_modules}` / `{code_model_validation}` → `D:\0Grok\0doc\GitHub\stats-analysis` (and `modules` / `model-validation`).
- Former `_code\04-analysis\stats-analysis` tree is gone; `{code_modules_master}` equals `{code_modules}`.
- Prose: `02_data-processing/personal/analysis/stats-analysis-digest.md`, `route.md`.
- MY-RULES `workspace-layout.md` already points at the GitHub tree (same change).

## CHG-20261025-vocab-fine-id — `mount` vocabulary retired, the registry key is `fine_ids`

- **Keys:** `registry.yaml` `mounts:` → `fine_ids:`, `empty_mount` → `empty_fine_ids`,
  `session_mount` → `session_fine_id_pick`; `templates/handoff.yaml` `mounted_fine_ids` →
  `live_fine_ids`, `mount_provenance` → `fine_id_provenance`.
- **Status:** row status `MOUNTED` → `LIVE`; `fine_id_count_canonical` still equals `len(fine_ids)`.
- **Prose:** "mounted pack" → "live pack", "mount decision" → "fine-id pick", "Mount vs lab" →
  "Assistant vs lab"; `mount-review-polish-recipe.md` (retired) → `fine-id-review-polish-recipe.md`
  (git mv, links follow).
- **Site:** the generator writes `fine_ids/index.html`; old `mounts/` URLs are gone (accepted cost).
- **Guards:** `STATUS_TOKENS` guards `LIVE|PROPOSED|ARCHIVED`; the retired-vocabulary regex drops the
  obsolete `B mount` form; test names follow the new vocabulary.
- **Kept as history:** dated ledger entries, `mount_status` frontmatter in two absorbed packs, and the
  retired `MOUNTED_SKILLS.md` filename.
- Suite stays 174. No push, no merge.

## CHG-20261025-qc-dead-pointer-cleanup — dead pointers, orphan scripts, vacuous assertions

- **Deletions:** `plot-figures/scripts/plot_template.py`, `plot-figures/scripts/style_configurator.py`
  and `visualization/scripts/gen_repo_map.py` were cited nowhere (no pack doc, no test); bytes
  quarantined outside the repo. Tracked tree 481 → 478.
- **Three docs kept:** `03_research/personal/references/grant-fulltext-skeleton.md`,
  `lab-ref-method-digest.md` and `0doc-response-structure-pointer.md` are cited from `0doc`
  (its `_library` INDEX + README, the root CURRENT pointer, and the skill-harvest plan), so they
  stay and are now registered in `03_research/personal/route.md`.
- **Pointer fix:** `simulate-reviewers/manifest.yaml` marks the `../nature-shared/core/` sweep
  `external: true` instead of leaving a path that does not resolve in-repo.
- **Tests:** new `PackReferentialIntegrity` (2) fails on an uncited pack `scripts/*.py` or
  `examples/*`; `test_lab_paths` split into key-format + skip-guarded existence; `test_seat_packs`
  pins the 00–07 layer bound and the live-`0result` ban; `test_frontmatter` drops a commented
  workflow row; `07_response/base/tighten-response/MODULE.md` registers its three worked examples.
- **Drift:** README test command carries `-B`; this file's header no longer claims an empty roll.
- Suite 172 → 174. No push, no merge.

## CHG-20261025-seat-coarse-merge-01 — coarse id = execution seat; 01 folded into 00

- **Seat ids as coarse ids:** `coarse_ids` is now exactly the five execution seats —
  `02_data-processing`, `03_research`, `05_manuscript`, `06_review`, `07_response`;
  `coarse_id_count` 9 → 5. The retired buckets (`lit-retrieval`, `topic-explore`,
  `study-design`, `manuscript-body`, `data-processing`, `stats-analysis`, `figures`,
  `manuscript-review`, `review-response`) survive only as `coarse_aliases` targets.
- **Mounts lose `coarse`:** all 25 live rows drop the field (only one assertion in
  `tests/test_registry_contract.py` read it). Bucket = `a_domain`, and
  `SeatBuckets.test_mount_owner_dir_matches_a_domain` keeps path and owner aligned.
- **No override policy:** `a_domain_override_policy` deleted. `find-journal` and
  `grant-builder` are plain `03_research`; both notes lost their override wording.
  `fill-protocol` stays `03_research`.
- **01 retired in place:** `registry.yaml`, `legacy_aliases.yaml`, `references/id-rules.md`,
  `00_orchestrator/references/session-pick.md`, `00_orchestrator/references/hard-rules.md`, `00_orchestrator/references/lifecycle-cache.md`,
  `00_orchestrator/references/text-harvest-by-fine-id.md`, `references/capability-contract.example.yaml` and
  `workflows/` (5 SOPs + README) moved into `00_orchestrator/` with `git mv`; the 01 `SKILL.md`
  became §0 "Index & registry" of `00_orchestrator/SKILL.md`. The duplicate pointer
  `01/references/base-vs-personal-top-loops.md` was retired, not migrated — the same file
  already lived in `00_orchestrator/references/`. Archive copy of the whole 01 tree:
  `D:\0del\_by-project\MY-SKILLS-01-merge-20261025\`.
- **Guards:** `WORKFLOW_HOME` = `00_orchestrator/workflows`; the forbidden list is now
  `01_skill-integration/workflows` + `03_research/workflows`. `test_doc_structure.test_mounts_board`
  asserts registry / aliases / workflows under 00 plus the absence of the 01 folder;
  `test_seat_packs` reads 00 for the seat rule and `skill-evolution.md` for the MY-RULES gate.
- **Suite:** 168 → 172 (4 new `SeatBuckets` assertions).

## CHG-20261025-dedupe-ssot-pass — duplication pass after the deep-QC roll

- **Layer model (02/03/05/06/07):** the pasted `**QC standards:** live in `qc/` …` sentence,
  identical in all five `SKILL.md`, is now one 152-char pointer to
  `00_orchestrator/references/base-vs-personal-top-loops.md` + `gates.md`, with each seat's
  own `<seat>/qc/README.md` named. Seat-specific residue kept (02 personal protocols, 03
  `verify-refs` / `retraction-watcher`, 06/07 envelope lines).
- **03 personal design:** `radiology-design.md` no longer restates the `design-study`
  `## Workflow` (8 steps) and `## Output contract` (7 items) — both were verbatim in
  `03_research/base/design-study/MODULE.md`, and the file's own header already named base as
  the single source. Only the two seat deltas survive (sample size → `02`, `Method options`
  → `05` `check-reporting`).
- **A/B residue:** 49 `A <seat path>` prefixes removed across 31 files — the form the previous
  pass's regex never matched, since it looked only for `` A `base/` ``. `[B:humanize]` →
  `[base:humanize]`; `Voice A/B` and comment author `A` untouched.
- **Former ids:** `radiomics-ml` / `architecture-zoo` call sites now name the live ids
  (`stats-analysis`, `design-study`). Alias/retirement notes stay in `legacy_aliases.yaml`,
  `02_data-processing/base/stats-analysis/SKILL.md`, `03_research/base/design-study/MODULE.md`
  and the `02` absorbed line.
- **Kept on purpose:** `call/require 03 citation-verify — do not self-certify lit` stays
  verbatim in its 8 files; `tests/test_seat_packs.py` pins it as a safety rule.
- **Measured after:** cross-file paragraph groups ≥120 chars = 4 (none ≥200, so the mirror
  guard keeps headroom); `A <seat>` = 0; `[B:...]` = 0; `QC standards:` = 1 (the SSOT).
  Suite 168 OK.


## CHG-20261025-deep-qc-remediation — six-batch remediation after deep QC

- **Tests:** revived the dead cross-file paragraph-dedupe guard, deduped
  `06_review` / `07_response` `disclaimer-comment-only.md` to AL-5, and merged the
  33-file suite into 12 contract-domain modules with `tests/support.py`
  (162 assertions kept, none dropped). New guards: single-H1, qc README↔dir,
  03 route index, retired A/B vocabulary, institutional contact data, LF/trailing
  whitespace. Suite 162 → 168.
- **Docs:** six broken relative pointers fixed; every markdown file now has one H1
  (frontmatter residue dropped, 30 section H1s demoted); table pipes escaped;
  qc READMEs and the 03 route index completed; `ownership-contract.md` self-reference
  and duplicate seat removed; `05_manuscript/SKILL.md` duplicate `humanize` bullet merged.
- **Vocabulary:** retired A/B workspace vocabulary purged (seat ids `A0N`,
  `Work-A`/`Work-B`, `` A `base/` ``, `[A:...]`/`[B:...]` tags, A/B headings) while
  `Voice A/B` and comment author `A` stay.
- **Privacy:** institutional email/phone removed from `fill-protocol/` digests
  (values live in the local ethics record); guard added.
- **Hygiene:** `.gitignore` + `.gitattributes` (`eol=lf`); 283 files normalized to LF,
  1856 trailing-whitespace lines removed; ledger `change_id` equals the newest entry.
- **Batches:** B1 guard+AL-5 · B2 pointers/H1/tables · B3 test restructure ·
  B4 index/contract · B5 A/B + privacy · B6 hygiene.


## CHG-20261025-merge-04-into-02 — 04 absorbed into 02, gate `G-04` → `G-STATS`

- Absorbed `04_analysis` into `02_data-processing` (one top-level skill `02`; `04_analysis` retired). 6 base packs (`stats-analysis`, `meta-analysis`, `model-evaluation`, `calc-sample-size`, `draw-flowchart`, `plot-figures`) → `02_data-processing/base/`; the rest of `04_analysis/personal/**` → `02_data-processing/personal/analysis/**`, except the visualization pack → `02_data-processing/personal/visualization/` (its `scripts/` would otherwise sit six path parts deep, over the five-part ceiling); 5 `04_analysis/qc/*.md` → `02_data-processing/qc/`.
- Gate `G-04` renamed **`G-STATS`** everywhere; no `G-04` alias kept. `02_data-processing/SKILL.md` now carries the layer model (`G-PHI` / `G-CODE` / `G-FACT` / `G-STATS`) plus the imaging hard rules that used to live in `04_analysis/SKILL.md`.
- Registry: `path` / `a_domain` for the 6 moved packs → `02_data-processing`; fine id and coarse counts unchanged.
- Seat token `04` collapsed into `02` across live docs (`02→04→05→06` reads `02→05→06`; `02 or 04` → `02`; `02/04/05` → `02/05`). `runtime-flow.mmd` node ids `Need04` / `P04` / `GF04` / `GA04` → `NeedStats` / `PStats` / `GFStats` / `GAStats`.
- `legacy_aliases.yaml` keeps the historical call-site keys (`04-fig-flow`, `04-fig-plot`, `04-stats-models`, `04-stats-power`, `04-model-eval`); they are retired ids, not live seats.
- Tests: gate strings → `G-STATS`; `SKILL_DIRS` / `TOPS` lists drop `04_analysis`; new regression guard fails if `04_analysis` reappears in tracked files.
- Sync whitelist post-merge: changed skill bodies + `registry.yaml` + `VERSION.txt` + `INTEGRATION_MAP.md` → `{SKILLS}` per skills.md §1b.

## CHG-20261025-merge-language-polish-coarse — coarse merge

- Coarse `language-polish` (single member: `humanize`) merged into `manuscript-body`; the `humanize` mount now carries `coarse: manuscript-body`.
- `coarse_id_count` 10 → 9; fine ids unchanged at 25. No specialist or a_domain change (both groups were Aitee / `05_manuscript`).
- `legacy_aliases.yaml` `coarse_aliases`: label `Language polish` retargeted, and id form `language-polish: manuscript-body` added.
- No live document enumerated coarse groups by name, so no prose sync beyond this ledger.

## CHG-20261025-absorb-polish-language — language lint into humanize

- Absorbed `05_manuscript/base/polish-language/` into `05_manuscript/base/humanize/` (humanize wins).
- Kept: `references/stat-reporting.md` (house-style authority stays `05_manuscript/base/write-paper/radiology-polishing/radiology-house-style.md`), `references/style-guardrails.md`. The lint table moved into humanize `MODULE.md` as `## Language lint (report-only)`. Source `MODULE.md` + pointer `SKILL.md` removed with the directory.
- Retired id: `legacy_aliases.yaml` `polish-language` → `humanize`; alias keys `nature-polishing` / `polish-latex` retargeted. Dropped the MOUNTED row. Canonical count 25.
- Coarse `language-polish` keeps one fine id (`humanize`). Call sites that hand language work to `polish-language` now point at `humanize`.

## CHG-20261025-absorb-tone-polisher — tone polish into tighten-response

- Absorbed `07_response/base/response-tone-polisher/` into `07_response/base/tighten-response/` (tighten-response wins on conflict; stance SSOT is `references/tone-and-stance.md`).
- Kept: `references/tone_patterns.md`, `references/polite_expressions.json`, `scripts/tone_polish_main.py` (renamed from `scripts/main.py`).
- On-demand mode `tone-polish`. Point-by-point structure stays `revise`. 选刊 stays in 03 `find-journal`. `check-reporting` was not moved.
- Retired id: `legacy_aliases.yaml` `response-tone-polisher` → `tighten-response` (cross-pack AIPOCH key retargeted). Dropped the MOUNTED row. Directory deleted. Canonical count 26.
- Fast routing forbids the retired path `07_response/base/response-tone-polisher/`.
- MIT attribution stays in `07_response/base/tighten-response/LICENSE_NOTE.txt`.

## CHG-20261025-absorb-write-venue — venue shape into write-paper

- Absorbed `05_manuscript/base/write-venue/` into `05_manuscript/base/write-paper/` (write-paper wins on conflict; no same-named file overlap).
- Kept: `05_manuscript/base/write-paper/radiology-writing/journal-family-writing-style.md`, `05_manuscript/base/write-paper/radiology-writing/nature-family-shape.md`, `05_manuscript/base/write-paper/radiology-polishing/radiology-house-style.md`, `05_manuscript/base/write-paper/radiology-polishing/venue-voice-and-house-style.md`, `05_manuscript/base/write-paper/references/journal-patterns-2023-2026.md`.
- Venue-shape is in-skill on `write-paper`. 选刊 stays in 03 `find-journal`. `check-reporting` was not moved.
- Retired id: `legacy_aliases.yaml` `write-venue` → `write-paper`. Dropped the `local_packs` row. Directory deleted.
- Policy cites point at `05_manuscript/base/write-paper/`.

## CHG-20261025-inrepo-index — in-repo index only

- Registry `change_id` is `CHG-20261025-inrepo-index`. Source-menu keys are gone. Live rows stay `source: my-skills` under `NN_slug/base/`.
- Deleted root `.cursorignore`, `.gitattributes`, `.gitignore`, and `pytest.ini`.
- Deleted the non-base pointer under `01_skill-integration/references/`.
- README describes seats `00`–`07`. Visualization reads the in-repo registry only.
- Deleted `02_data-processing/personal/workspace.md` and `02_data-processing/personal/coding-qc.md`. Folder layout cites `{RULES}/workspace-layout.md`. `02_data-processing/qc/coding-qc.md` stays.
- Tests: assertions that required the deleted files or source-menu keys were rewritten or dropped. Command: `python -m unittest discover -s tests`.

## CHG-20261024-registry-thin — thin registry (live mounts only)

- Drop `archived:` section + historical meta essays from `01_skill-integration/registry.yaml`.
- Live SSOT: 27 MOUNTED mounts + coarse_ids + local_packs + session/empty/ars policy.
- `legacy_aliases.yaml` absorbs retired-id resolution (orphan chains retargeted to live mounts).
- Tests: alias targets / retired-ids / docs-match / module_headers / mirrors / audit mounts regex.

## CHG-20261020-deepscan-fix — deep-scan P0/P1 absorb

- Branch `fix/deepscan-p0-p1-20261020` (Asia/Shanghai 2026-10-20), registry `change_id` bumped.
- **Ids**: 66 B-era call-site ids in 29 files → canonical fine ids (04-fig-flow→draw-flowchart ×13, 04-fig-plot→plot-figures ×13, 04-stats-models→meta-analysis ×12, 02-imaging-io→imaging-io ×5, 02-tables→clean-data ×4, 04-stats-power→calc-sample-size ×4, 02-imaging-qc→preprocess-imaging ×3, 02-radiomics-habitat→stats-analysis ×7, 02-lit fixes ×3). Three unmapped names (`04-stats-power`, `03-lit-fulltext`, `03-lit-cite`) added to `legacy_aliases.yaml`.
- **Dead pointers**: `ban-phrases.md` → `vocab/L2/preferred.md` §1c; `report-checks.md` self-row → "Part A of this file"; `guideline-router.md` → `write-venue/radiology-writing/journal-family-writing-style.md`; `mount-review-polish-recipe.md` (retired; renamed `fine-id-review-polish-recipe.md` on 2026-10-25) → `06_review/personal/review.md` §0; `ai_patterns.md` → `vocab/L1/patterns.md`; `retraction-watcher/MODULE.md` → `references/audit-reference.md`; `data-impute` → `clean-data` impute module.
- **pack-cache**: bytes (624 files) moved to `D:\0del\_by-function\pack-cache-retired-20261020`; README / lab-paths / lifecycle-cache / NOTICE narratives unified (the three files had disagreed on whether the cache was emptied, deleted, or still present).
- **State claims**: `PROPOSED/MOUNTED` mix removed from README + ARCHITECTURE (registry has 0 PROPOSED); 01 SKILL documents the A-local-pack exception (`base/vocab/`, `base/write-venue/`); `Aitor-format.md` owner → `05_manuscript/personal/`; raw lab paths → `{alias}` in 13 files.
- **Tests**: `PATH_UNIT_ALIAS_KEYS` emptied (no B-era directory exists); new `test_bare_md_cites`, `test_alias_targets_exist`, `test_no_raw_lab_paths`, `test_docs_match_registry_state`, `test_ledger_freshness`; `test_owner_fields` / `test_pre_submit_checks` now run on the runtime tree (relative parts + rglob fallback).
- Sync whitelist post-merge: changed skill bodies + `registry.yaml` + `legacy_aliases.yaml` + `VERSION.txt` + `INTEGRATION_MAP.md` → `{SKILLS}` per skills.md §1b.

## CHG-20261019-scan-fix-p0-p2 — scan fix absorb (PR pending)

- Branch `chore/scan-fix-p0-p2-20261019`: apply SCAN-REPORT P0/P1/P2 (Asia/Shanghai 2026-10-19).
- P0: rewrite live `~/.grok/AGENTS.md` required reads → My rule / network-security / skills (+ optional workspace-layout); replace all bare qc/local-checks cites cites → `05_manuscript/qc/manuscript-local-qc.md`; Aitor-format ban-phrases → `05_manuscript/base/vocab/L1/ban-phrases.md` (+ sci-overrides).
- P1: cross-link qc `reporting-guideline-route` ↔ base `guideline-router` (Gate SSOT vs writing audit; CLAIM/CLEAR footnotes); align Integrity·pre-06 mid-entry G-CIT wording with gates.md; add `nature-reporting-summary.md` stub; add **G-07** QUALITY row; fix manuscript-local-qc / cross-manuscript-qc ownership/move headers; retarget paper-claim-audit / external-principles cites to `references/…` and shrink `ALLOW_MISSING`; NOTICE Archify → `02_data-processing/personal/visualization/`.
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
- `.cursorignore` pack-cache dead entry removed; keep `.gitignore` defense; `00/SKILL.md` wording synced.
- F42: `review-isolation` row added to `01_skill-integration/workflows/README.md` (formerly under 00 workflows pointer).
- B2: `03_research/base/fill-protocol/MODULE.md` trimmed to principles + paths (missing assets noted).
- D2: design-experiment bilingual pair headers (validation / study-design).
- F46: Absent labels → archived — do not recreate.
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
- style_lint pack-cache fallback removed; sci-manuscript path fixes; presets C1 in-repo paths.
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

- User rule 2026-10-08: for each candidate journal, search the last 3–5 years for articles similar to the manuscript title. Cite found articles (title, year, DOI/link) in match rationale. None found → lower the tier and write 「no similar articles in recent years — demoted」. Never invent articles. A failed search is not a no-hit.
- Canonical: `03_research/base/find-journal/SKILL.md` § Similar-article check (pack v1.16 → v1.17). Pointers: `03_research/base/find-journal/rules/policy.md`, `03_research/base/find-journal/rules/recommendation-workflow.md`, `AGENTS.md`.
- Regenerated `docs/` visualization HTML via `02_data-processing/personal/visualization/scripts/gen_visualization.py` (outputs were stale on main after #126).
- `skill-harvest/scripts/repo_qc.py` (archived under `D:\0del\00_orchestrator_reorg_20261017\skill-harvest_MY-SKILLS\`): historical map files under the 0del `_medical-research-meta_history` tree count as historical (legacy-active-refs, stale-ids), like this stub and archive. The Oct-7 monthly file is at `D:\0del\00_orchestrator_reorg_20261017\_medical-research-meta_history\MY-SKILLS_history\INTEGRATION_MAP-20261007.md` (in-repo `history/` link removed).

## CHG-20261008-002 — find-journal similar-article check is round 2

- User rule update 2026-10-08: the similar-article search is round 2 of journal selection, not a step before ranking.
- Round 1 ranks by the existing criteria and does not search. Round 2 searches each candidate for similar articles from the last 3–5 years, then lowers a journal with no similar article inside its layer. Cite found articles (title, year, DOI/link). Never invent articles. A failed search is not a no-hit.
- Canonical: `03_research/base/find-journal/SKILL.md` § Similar-article check (pack v1.17 → v1.18). Pointers: `03_research/base/find-journal/rules/policy.md`, `03_research/base/find-journal/rules/recommendation-workflow.md`, `AGENTS.md`.
