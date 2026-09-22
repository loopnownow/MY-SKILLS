# Integration map — MedicalResearch Lean v6

This file records the current architecture, not the historical export tree.

| Source capability | Active home |
|---|---|
| Skill discovery / mount | `01_skill-discovery-integration/` |
| Excel/CSV / 0RAD workspace | `02_data-processing/` |
| Soft-coding / dry-run | `02_data-processing/code-refactoring/` |
| Clinical extraction | `02_data-processing/clinical-data-extraction/` |
| Ethics form packs | `03_research/ethics-application-forms/` |
| MRI/fMRI / radiomics / habitat prep | `02_data-processing/` |
| Clinical translation / reader-study design | `03_research/clinical-translation/` |
| Study design / literature / radiology frontier / 选刊 | `03_research/` |
| Clinical statistics / prediction / figures | `04_analysis/` |
| SCI writing | `05_manuscript/` |
| Manuscript audit / peer review / reviewer response | `06_review/` |
| Skill lifecycle governance | `skill-harvest/` |

Historical export paths are intentionally not retained in the active map.

## Swap 2026-08-25 (user)

Replaced live `~\.grok\skills` with `skills-lean-v6.zip`. Pre-v6 tree archived at `D:\0Grok\0RAD\0scripts\skills_live_v1.3.1_20260825.zip`. Runtime XSD zip + extract: `D:\0Grok\0RAD\0scripts\skills-runtime-assets-v3.zip` and `D:\0Grok\0RAD\0scripts\runtime-assets\`.

Active top-level: `00_orchestrator` … `06_review` + `skill-harvest` + `_medical-research-meta`. Review/response lives under `06_review/bundles/manuscript-quality`. Coding/Office under `01_automation`.

## Split 2026-08-25 (user)

```text
change_id: split-04-review-06
date: 2026-08-25
skill: 05_manuscript → 05_manuscript + 06_review
from_version: Lean v6
to_version: Lean v6.1
problem: 04 mixed SCI 论著 writing with 评阅/回审; review triggers were buried and collided with writing.
change: Promoted `manuscript-quality` (pre-review, peer review, response) to top-level `06_review`. `05_manuscript` keeps manuscript-core + figure-engine.
expected_benefit: Distinct auto-invoke for 写论著 vs 评阅/回复审稿人; smaller 04 context on writing tasks.
observed_evidence: pending first live use
metric_summary: n/a
boundary_effect: Authorized 00–06 domain set. Do not add 07.
decision: observe
next_action: watch routing accuracy on 润色 vs 审稿 vs 回复审稿人
```

## Renumber 2026-08-25 (user)

```text
change_id: renumber-01-to-06
date: 2026-08-25
skill: 00–06 domain folders
from_version: Lean v6.1
to_version: Lean v6.2
problem: Folder numbers did not match the user's preferred order after the 04/06 writing–review split.
change: Renamed live folders to 01_automation, 02_imaging, 03_research, 04_analysis, 05_manuscript, 06_review. 00_orchestrator and skill-harvest unchanged. Task pipeline order is still research → imaging → analysis → manuscript → review.
expected_benefit: Directory numbers match the user's map; fewer routing mistakes from stale 01=research / 05=automation memory.
observed_evidence: pending first live use
metric_summary: n/a
boundary_effect: Same six business skills; numbers only. Do not add 07.
decision: observe
next_action: confirm auto-discovery after reload
```

## Core/archive split 2026-08-25 (user)

```text
change_id: core-archive-split
date: 2026-08-25
skill: layout
from_version: Lean v6.2
to_version: Lean v6.3
problem: Nested packs were either bloating 01/02 or needed their own triggers.
change: Moved 00–06 + harvest into skills/core/. Promoted ethics-application-forms, code-refactoring, clinical-data-extraction, clinical-translation to skills/archive/ as standalone SKILL.md. Deleted markitdown, tool-environment-setup, imaging-omics-ml. Kept data-impute and figure-engine nested.
expected_benefit: Distinct auto-invoke for 软编码 / 填伦理 / 提取 / 转化; smaller 01 and 02.
observed_evidence: pending first live use
metric_summary: n/a
boundary_effect: Archive skills are extra homes, not 07_. data-impute and figure-engine remain modules.
decision: observe
next_action: watch routing on 软编码 vs 批处理, 转化 vs 02_imaging
```
## Forbidden-word policy reversal + corpus phrase bank spot-check + diff-harvest tool 2026-08-29 (user)

```text
CHG-20260921-002 | 01+03 | Regen MOUNTED_SKILLS 10+55; README 55 fine; flatten journal-format publisher-notes to medical-journal-submit/references/; qualify bare submission-urls.csv refs.
CHG-20260921-001 | 01 | Fix registry.yaml: move P1 candidates before reference_only:[]; valid YAML; fine menu 55; regenerate MOUNTED_SKILLS; stub_in_b rename; scrub 52/30-id residue.
CHG-20260920-001 | 00 | Absorb the SlopMonster *mechanism* (pattern-group score + non-zero exit) as G-05 sub-check `style-lint`.
Absorbed: scoring/exit-code loop, section scoping, fail-closed input guards, paired must-hit/must-stay-clean test discipline.
Not absorbed: rival-model cleanse (owner: no manuscript text to other models), CI workflow, marketing rules,
"invented proof" regex (-> G-FACT), rewrite pass 3 (conflicts with house style). CONFIG in style_lint.py is machine SSOT for lint vocab; 05 personal lists remain rewrite guidance (dedupe follow-up). Source: ItsssssJack/SlopMonster (MIT).
change_id: CHG-20260829-001
date: 2026-08-29
skill: 05_manuscript
mode: manuscript-core
from_version: n/a
to_version: n/a
change_class: fix + extend + toolize
problem: (1) User made an explicit editorial decision to ban novel/notably/interestingly/importantly, reversing the prior corpus-verified "not banned" status in forbidden-phrases.md and corpus-phrase-bank.md §8. (2) A separate 50-manuscript spot-check surfaced 4 candidate patterns not yet present in the 389-draft corpus-phrase-bank.md. (3) A standalone JSON-ledger evolution engine would have duplicated skill-harvest's governance role.
change: (1) forbidden-phrases.md and corpus-phrase-bank.md §8 updated to Forbidden; prior "not banned" reasoning kept in <details> as historical record, not deleted. (2) Added §2 "[This/Our] study showed that…" and new §2b (gap-statement / novelty-claim openers) to corpus-phrase-bank.md, explicitly marked as a provisional 50-draft spot-check sample, smaller than the section's existing 96-draft baseline — not yet confirmed at the 389-draft scale. Declined TIPS/DIT-cluster-only candidates. (3) Ported diff-based capability into core/05_manuscript/bundles/manuscript-core/scripts/diff_harvest.py. The script appends one row per run to data/diff-evidence-log.csv and never auto-writes corpus-phrase-bank.md or forbidden-phrases.md.
expected_benefit: Forbidden-word policy matches current user intent without silently losing the prior evidence trail. Corpus phrase bank gains a small, honestly-labeled increment rather than a false-confidence merge. Diff-based editing evidence accumulates in the owning skill instead of a parallel ungoverned system.
observed_evidence: n/a (first use)
metric_summary: n/a (first use)
boundary_effect: No new top-level skill created. skill-harvest untouched; its governance role was followed, not duplicated.
decision: keep (policy + phrase-bank edits), observe (diff_harvest.py)
next_action: run diff_harvest.py against real AI-draft/human-final pairs; if data/diff-evidence-log.csv shows recurring new candidates across multiple manuscripts, fold them into the next full corpus-phrase-bank.md re-harvest rather than adding them ad hoc.
```
## Harvest 2026-08-30 — 05_manuscript (user)

```text
change_id: CHG-20260902-001
date: 2026-09-02
skill: 05_manuscript
mode: manuscript-core
from_version: n/a
to_version: n/a
change_class: fix + policy
problem: Harvest 2026-08-30 (author A): Track Changes author; yellow empty slots; I/D quota vs already-written refs; body was-not-tested / validation-set stock; Vancouver reorder on revision; COMMENTARY anti-reading voice; elucidat*; adverb load.
change: (C2-B) Word Track Changes/comments author A, never Grok. Hunt under core/05_manuscript found no python/json default revision author (only path strings D:\0Grok\…, left unchanged); rule written in Aitor-format.md. (C4-C) Cancel yellow-highlight empty slots forever; missing method/product facts go in Word comments only, never body, never yellow fills; new writing and revision; do not fabricate. (C6-B) Writing new I/D still 10–15 / 10–15-new; checking an already-written manuscript: do not delete genuine refs to hit quota, note over-quota only. (C9-B) Body never contains was not tested / 未测 / 未完成; incomplete work → comments; Aitor “A validation set is required” and “No validation set was available” moved out of body/Conclusion/Limitations into comments-only. (C10-C) Revising existing MS: reorder in-text Vancouver numbers to appearance order vs the reference list; duplicate list entries → already-verified substitute (author A); this exception only — no general substitutes-in-comments rule. (C13-B) Ban COMMENTARY anti-reading phrasing in body (they should not be summarized as; is not reported as; should not be read as; given this extent; should not be described as; rhetorical rather than / but not by); observational contrast may still use associated with; do not blanket-ban factual rather than / but not by (e.g. but not by sex). (C14-C) Ban elucidat*; purpose/aim → exploring; mechanism-unknown → remain unclear (not explain/clarify); deleted template “has not been fully elucidated”. Adverb: new writing and polish reduce adverb use; do not ban statistical significantly (p-value language).
expected_benefit: House DOCX marks and honesty boundaries match author A’s harvest; de-AI stops commentary/elucidate/adverb slop without breaking factual contrast or p-value English.
observed_evidence: n/a (first use)
metric_summary: n/a
boundary_effect: 05_manuscript / manuscript-core only. 06_review and 00_orchestrator untouched. KEEP not in this PR: C1 polish-before-review order; C5 figure-vs-caption; C7 substitutes-only-in-comments as general rule; C8 _revised.docx layout; C11 uncited figures as Major; C12 Table 1 vs literature range; no 00_orchestrator pointer.
decision: keep
next_action: live full-paper write/polish; confirm Word comments author A and no yellow slots
```

## Harvest 2026-08-30 — 06_review (user)

```text
change_id: CHG-20260902-002
date: 2026-09-02
skill: 06_review
mode: manuscript-quality
from_version: n/a
to_version: n/a
change_class: fix + policy
problem: Harvest 2026-08-30 (author A, choice B): Path A review-implementation was filling title-page slots; reviewing already-written I/D was deleting genuine refs to hit 10–15 / 10–15-new.
change: (C3-B) Path A (落实审稿意见 / revise existing MS) skips the entire title page: ethics number, author block, target journal, and whether the paper declares “not generated”. Do not fill, yellow-highlight, or rewrite those fields. From-scratch title page remains 05 Aitor-format (pointer only). (C6-B) Reviewing an already-written manuscript: do not delete genuine refs to hit Intro 10–15 / Discussion 10–15-new; note over-quota only. New-I/D quota stays in 05 (companion PR #11); 06 points at 05 evidence, does not duplicate retrieval.
expected_benefit: Review implementation no longer overwrites title-page identity fields; already-written citations are preserved with an over-quota note instead of destructive quota trimming.
observed_evidence: n/a (first use)
metric_summary: n/a
boundary_effect: 06_review / manuscript-quality only. 05_manuscript and 00_orchestrator untouched except this append. KEEP not in this PR: C1; C5 figure-vs-caption; C7; C8; C11 uncited figures as Major; C12 Table 1 vs literature range; no 00_orchestrator pointer; no 05 body/de-AI rules.
decision: keep
next_action: live Path A 落实审稿意见; confirm title page unchanged and over-quota notes instead of ref deletion
```

## Framework / capabilities split 2026-09-02 (user)

```text
change_id: CHG-20260902-003
date: 2026-09-02
skill: layout (A framework vs B capabilities)
from_version: Lean v6.3 + harvest CHG-20260902-001/002
to_version: framework-a-20260902
change_class: architecture split
problem: One repo mixed orchestrator/personal lab rules with mountable generic capabilities; 01 was Excel; 05 nested figure-engine; core trees exceeded three directory levels (`bundles/`, `merged/`, `evolution/proposals/`).
change: Split A (this repo: framework + personal) from B (MY-SKILLS-capabilities). Locked C1–C5 and M01–M34. 01 = Skill Discovery & Integration (not Excel). 02_imaging → 02_data-processing (raw→analysis-ready; Excel/0RAD here; no modeling). Literature → 03 only; figures → 04; reviewer response → 06 only. Flatten A core to ≤3 directories. Registry mounts: [] with PROPOSED default-candidate Imbad0202/academic-research-skills and backup Aperivue/medsci-skills. Never auto-mount. Journal-style files (C4) go to B only. radiology-stats stays in A/04. Freeze tag pre-split-2026-09-02 on origin/main. Specialist bot profiles unchanged.
expected_benefit: A stays a personal orchestrator; B is a mountable capability pack; routing matches lab intent; depth limit is enforceable.
observed_evidence: n/a (first use)
metric_summary: n/a
boundary_effect: No bot profile edits (C5). Archive four packs not migrated. Do not delete A generic 03/05/06 copies until a mount covers them. Do not merge this PR automatically.
decision: keep
next_action: user reviews PR; mount only after explicit approval; then delete matching EXTERNALIZATION_CANDIDATES rows
```

## Rehome archive packs + lift skills to repo root 2026-09-02 (user)

```text
change_id: CHG-20260902-004
date: 2026-09-02
skill: layout (A root lift + archive rehome; B classified folders)
from_version: framework-a-20260902
to_version: rehome-archive-root-20260902
change_class: architecture
problem: Skills still lived under core/; four packs remained archive standalones; A depth counted core as a directory; B mountable pack was a flat list of 02-xlsx / 03-design ids rather than domain folders.
change: Lifted A 00–06 + skill-harvest (and MOUNTED_SKILLS.md / EXTERNALIZATION_CANDIDATES.md) from core/ to repo root. Flattened four archive packs into domain skills at ≤3 directories: clinical-data-extraction, code-refactoring, ethics-application-forms → 02_data-processing/<pack>/ (files hoisted; ethics forms temporary parking, true home remains 03 ethics design); clinical-translation → 03_research/clinical-translation/ as personal translational DESIGN (not 02, not 04). archive/ kept with README only. Routing: Excel/extraction/ethics-forms(temp)/coding-principles → 02; translational/reader-study design → 03; no archive-as-standalone routes. B reorganized into 02-data-processing/ 03-research/ 04-analysis/ 05-manuscript/ 06-review/ domain folders; ids unchanged. 01 registry unchanged (ARS default candidate, MedSci backup, mounts []). Specialist bot profiles unchanged.
expected_benefit: Discoverable skills at repo root; archive packs have domain homes; A depth rule is skill + optional folder + file; B layout matches A domains for mounting.
observed_evidence: n/a (first use)
metric_summary: n/a
boundary_effect: No bot profile edits. Do not merge this PR automatically. Do not copy A personal files into B.
decision: keep
next_action: user reviews PRs; mount only after explicit approval
```

## Classify A extra layer 2026-09-02 (user)

```text
change_id: CHG-20260902-005
date: 2026-09-02
skill: layout (A classification using extra directory)
from_version: rehome-archive-root-20260902
to_version: classify-extra-layer-20260902
change_class: architecture
problem: After lifting core/, skills sat at repo root but personal and generic files still mixed at skill root; 02 packs had scripts hoisted beside SKILL.md. User allowed one extra folder for classification.
change: Restored 02 pack scripts/references. Classified 03 into personal/design/frontier/literature (+ clinical-translation/references). 04 personal/ + radiology-stats/references. 05 personal/ vs writing-generic/. 06 personal/ vs review-generic/. Depth rule is now ≤4 path parts (`skill/category/scripts|references/file`). Tests, SKILL.md maps, EXTERNALIZATION_CANDIDATES updated. B already classified; not copied. Bots unchanged.
expected_benefit: Personal vs generic files are navigable; scripts sit in scripts/; A still cannot grow a fifth folder.
observed_evidence: n/a (first use)
metric_summary: n/a
boundary_effect: No bot profile edits. Do not merge this PR automatically. Do not copy A personal files into B. Do not delete writing-generic/review-generic until a mount covers them.
decision: keep
next_action: user reviews PR; merge only when named
```

## Relocate generics to B + ethics to 03 + merge 04 personal 2026-09-02 (user)

```text
change_id: CHG-20260902-006
date: 2026-09-02
skill: layout (A relocate; B ingest)
from_version: classify-extra-layer-20260902
to_version: relocate-20260902
change_class: architecture
problem: User named remaining A generic folders that belong in B, ethics forms still parked in 02, and 04 split across radiology-stats vs personal.
change: Moved 05 de-ai + writing-generic and 06 review-generic into B (ids 05-de-ai, 05-writing-generic, 06-review-generic). A copies deleted. Ethics-application-forms git-moved 02 → 03_research. Merged 04 radiology-stats into 04_analysis/personal (hoisted references). Registry still mounts: []. No auto-mount. Bots unchanged.
expected_benefit: A is personal/orchestrator only for 05/06 generics; ethics fill lives with 03; 04 lab stats are one folder.
observed_evidence: n/a
metric_summary: n/a
boundary_effect: Do not merge until named. Do not copy 04 personal or 03 ethics forms into B. Do not auto-mount.
decision: keep
next_action: user reviews PRs
```

## Return de-ai to A personal 2026-09-02 (user)

```text
change_id: CHG-20260902-007
date: 2026-09-02
skill: 05_manuscript
change_class: architecture
problem: de-ai is personal Ying Li voice; user asked it back from B and merged into 05 personal.
change: Copied B 05-manuscript/de-ai files into 05_manuscript/personal/ (README → de-ai.md). Removed B pack and id 05-de-ai. 05 SKILL.md points at personal/forbidden-phrases.md. writing-generic stays B-only. mounts still [].
decision: keep
next_action: user reviews PRs; do not merge until named
```

## 01 mount pointers default B 2026-09-02 (user)

```text
change_id: CHG-20260902-008
date: 2026-09-02
skill: 01_skill-discovery-integration
change_class: policy
problem: Mount id tables were duplicated on domain SKILL.md files; default candidate was ARS; empty mounts had no protocol.
change: Canonical pointers only in 01 (`registry.yaml` + `MOUNTED_SKILLS.md`). Default source B (all current B packs MOUNTED except de-ai, which is A personal). Empty mount → notify, re-search, confirm; no silent ARS/MedSci fallback. ARS/MedSci remain PROPOSED backups. Root MOUNTED_SKILLS.md is a stub.
decision: keep
next_action: user reviews PR; do not merge until named
```

## 01 mounts.html + per-source yaml 2026-09-03 (user)

```text
change_id: CHG-20260903-001
date: 2026-09-03
skill: 01_skill-discovery-integration
change_class: interface board
problem: Mount pointers were yaml/md only; user asked for an HTML board of sources, available skills, A hook, and interface status, plus a recommendation on one-file-per-mount vs one-file-for-all.
change: Added 01/mounts.html (human board). One yaml per external source under 01/sources/ (B default; ARS/MedSci proposed). registry.yaml remains canonical index. Recommended against one file per skill id and against mixing sources. 03 literature/design/frontier marked dual-track. de-ai not listed as a B mount.
decision: keep
next_action: user reviews PR; do not merge until named
```

## 01 mounts.html preset pages 2026-09-03 (user)

```text
change_id: CHG-20260903-002
date: 2026-09-03
skill: 01_skill-discovery-integration
change_class: interface board
problem: Single mounts.html mixed all sources. User asked for multi-page presets: each page one fixed mount set, with source, A-hook, and empty mounts if that set is used alone.
change: mounts.html is the index. mounts-b.html (current default, 0 empty), mounts-ars.html and mounts-medsci.html (12/12 empty vs A ids). Shared mounts.css. File counts taken from B main 2026-09-03.
decision: keep
next_action: user reviews PR; do not merge until named
```

## 01 ARS/MedSci preset maps 2026-09-03 (user)

```text
change_id: CHG-20260903-003
date: 2026-09-03
skill: 01_skill-discovery-integration
change_class: interface board
problem: Backup preset pages listed all 12 A ids as unmapped/empty, so using ARS or MedSci still required a live repo search.
change: Scanned Imbad0202/academic-research-skills@9443623 and Aperivue/medsci-skills@912f7e8. Wrote A-id → path maps into sources/ars.proposed.yaml and sources/medsci.proposed.yaml. ARS maps 03-literature, 03-design (partial), 05-writing-generic, 06-review-generic; 8 empty. MedSci maps all 12 (4 partial); 0 empty. Mapping ≠ mount; both stay PROPOSED backups. Default remains B.
decision: keep
next_action: user reviews PR; do not merge until named
```

## 01 mounts folder + unmapped extras 2026-09-03 (user)

```text
change_id: CHG-20260903-004
date: 2026-09-03
skill: 01_skill-discovery-integration
change_class: interface board
problem: Backup skills that exist but have no A mount id were only mentioned as extras; HTML pages sat next to yaml in 01.
change: Moved all mounts HTML/CSS into 01/mounts/. Added unmapped.html listing ARS academic-pipeline and 19 MedSci skills with no A mount id (12 expansion / 7 analog). Wrote unmapped: tables into sources/ars.proposed.yaml and sources/medsci.proposed.yaml. Mapping ≠ mount. Default remains B.
decision: keep
next_action: user reviews PR; do not merge until named
```

## 04/05 MedSci interfaces; drop unmapped.html 2026-09-03 (user)

```text
change_id: CHG-20260903-005
date: 2026-09-03
skill: 01_skill-discovery-integration + 04_analysis + 05_manuscript
change_class: interface
problem: User asked for A 04/05 interfaces to MedSci explainability and humanize. unmapped.html duplicated the extras already listed on ARS/MedSci pages.
change: Added mount ids 04-explainability and 05-humanize (source MedSci, MOUNTED). Personal de-AI stays in A; 05-de-ai is not revived. Deleted mounts/unmapped.html. Default source remains B for the other 12 ids. CHG-20260903-005.
decision: keep
next_action: user reviews PR; do not merge until named
```

## 01 mounts HTML → markdown 2026-09-03 (user)

```text
change_id: CHG-20260903-006
date: 2026-09-03
skill: 01_skill-discovery-integration
change_class: interface board
problem: mounts/ was HTML + CSS; user asked for markdown and to drop extra files.
change: Replaced mounts.html / mounts-b.html / mounts-ars.html / mounts-medsci.html / mounts.css with README.md, b.md, ars.md, medsci.md. Content unchanged. yaml remains machine truth.
decision: keep
next_action: user reviews PR; do not merge until named
```

## 01 Scientific Agent Skills preset 2026-09-03 (user)

```text
change_id: CHG-20260903-007
date: 2026-09-03
skill: 01_skill-discovery-integration
change_class: interface board
problem: User asked for a mounts page for K-Dense-AI/scientific-agent-skills.
change: Scanned @1e5eeff (v2.66.0). Added sources/scientific-agent-skills.proposed.yaml and mounts/scientific.md. 12/14 A ids mapped (5 partial); empty 02-radiomics-habitat and 05-humanize. Remainder grouped by domain, not listed skill-by-skill. Status PROPOSED. Default remains B. CHG-20260903-007.
decision: keep
next_action: user reviews PR; do not merge until named
```

## Coarse ids reclassified to Scientific jobs 2026-09-03 (user)

```text
change_id: CHG-20260903-008
date: 2026-09-03
skill: 01_skill-discovery-integration
change_class: interface
problem: User asked to reclassify coarse A ids to match K-Dense-AI/scientific-agent-skills jobs, not keep 03-literature/design/frontier umbrellas.
change: Retired 03-literature, 03-design, 03-frontier, 04-stats-generic, 05-writing-generic, 06-review-generic. New coarse ids: 03-lit-search/review/cite, 03-design-experiment/grant, 03-frontier-ideate/hypothesize, 04-stats-guide/power/models, 05-write-manuscript/venue, 06-review-peer/critique. B folders unchanged; several A ids share one B path. 22 ids total. Default still B. Mapping ≠ mount.
decision: keep
next_action: user reviews PR; do not merge until named
```

## B folders 1:1 with coarse ids 2026-09-03 (user)

```text
change_id: CHG-20260903-009
date: 2026-09-03
skill: 01_skill-discovery-integration
change_class: interface
problem: After coarse-id reclass, B still shared umbrella folders; user asked to split B to match A, then remount ARS/MedSci.
change: B packs are 1:1 with A ids (except MedSci-only 04-explainability / 05-humanize). journal-selection moved to write-venue; doi_to_bibtex to lit-cite; design-grant is a stub MODULE. ARS/MedSci boards re-adapted with a B-path column. MedSci find-journal/add-journal moved from 03-lit-cite to 05-write-venue. Default still B. Mapping ≠ mount.
decision: keep
next_action: user reviews B PR then A PR; do not merge until named
```

## 02 media-type coarse ids 2026-09-03 (user)

```text
change_id: CHG-20260903-010
date: 2026-09-03
skill: 02_data-processing
change_class: interface
problem: User asked to split 02 coarse ids so clinical tables, CT/MRI volumes, pictures, and fMRI are visually distinct.
change: Retired 02-xlsx, 02-imaging-qc, 02-impute, 02-generic-docs. New ids: 02-tables (xlsx+impute), 02-imaging (CT/MRI DICOM/NIfTI/NII), 02-pictures (TIFF/PNG/JPG/PDF-as-image), 02-fmri (DICOM/NIfTI). Kept 02-radiomics-habitat. B stubs for pictures/fmri. ARS still empty on all 02. MedSci empty on pictures/fmri. Scientific empty on fmri (+ habitat, humanize). Default still B. Mapping ≠ mount.
decision: keep
next_action: user reviews PRs; do not merge until named
```

## P0+P1 fine split of coarse ids 2026-09-03 (user)

```text
change_id: CHG-20260903-011
date: 2026-09-03
skill: 01_skill-discovery-integration
change_class: interface
problem: User asked to split both P0 and P1 coarse ids for finer external mounts.
change: 30 ids. New: 03-lit-fulltext, 03-design-protocol, 04-model-eval, 04-fig-flow, 04-fig-plot (retired 04-figure-engine), 05-write-reporting, 05-write-polish, 06-review-response, 02-imaging-io, 02-imaging-qc (retired 02-imaging umbrella). Default still B. Mapping ≠ mount. clinical-reports / present-paper not in 05.
decision: keep
next_action: user reviews PRs; do not merge until named
```

## Session mount pick each run 2026-09-03 (user)

```text
change_id: CHG-20260903-012
date: 2026-09-03
skill: 01_skill-discovery-integration
change_class: interface
problem: User asked that every MY-SKILLS run prompt which packs to mount and let them choose.
change: session_mount: ask-each-run. Registry MOUNTED = available menu. 00 and 02-06 must not load packs until 01 asks (task-scoped candidate ids, multi-select, default B except 04-explainability/05-humanize). Unpicked unloaded. Source-wide switch still needs confirm. Personal layers are not a mount pick.
decision: keep
next_action: user reviews PR; do not merge until named
```

## Audit 2026-09-03 (user)

```text
change_id: CHG-20260903-013
date: 2026-09-03
skill: A framework (security + docs/SOP)
author: Aitor
change_class: fix + policy
problem: HIS login client with hospital-host credentials lived in A; root vs meta architecture disagreed (depth, default source, ethics home, empty mounts); workflows auto-loaded packs and mis-routed Figure 1 / de-AI; retired coarse ids still appeared as live routes; 选刊/样本量 fast routes were wrong.
change: Deleted HIS login automation from clinical-data-extraction (HIS clients stay on the hospital machine, never in git). Aligned ARCHITECTURE.md and _medical-research-meta/ARCHITECTURE.md (depth ≤4, default B, ethics in 03, 10 coarse + 55 fine menu, backups PROPOSED, no live 04-figure-engine). Workflows ask session-mount pick; Figure 1 uses 04-fig-flow, plots 04-fig-plot; de-AI path is 05_manuscript/personal/forbidden-phrases.md. Fast routing: 选刊 → 05-write-venue, 样本量 → 04-stats-power. Deleted stale SKILLS_map.html. VERSION/READMEs/harvest/tests updated for this batch. Do not rewrite git history.
decision: keep
next_action: user reviews PR; do not merge until named
```

## 选刊 back to 03 2026-09-03 (user)

```text
change_id: CHG-20260903-014
date: 2026-09-03
skill: A framework (routing)
author: Aitor
change_class: policy
problem: Audit CHG-20260903-013 routed 选刊 to 05-write-venue; user policy is 选刊 lives in 03, not 05.
change: Reverted 选刊→05-write-venue routing everywhere in A. Journal choice / 选刊 / where to submit → 03_research (literature/journal-selection.md; evidence via 03-lit-search / literature layer). 05-write-venue remains a mount id for journal templates / house style while writing, never “where to submit”. 选题 stays 03-frontier-ideate. 样本量 stays 04-stats-power. Tests updated to 选刊→03. Do not delete 05-write-venue; do not move B files.
decision: keep
next_action: user reviews PR; do not merge until named
```

## 00 QC closed loop 2026-09-03 (user)

```text
change_id: CHG-20260903-015
date: 2026-09-03
skill: 00_orchestrator
author: Aitor
change_class: policy
problem: Architecture and personal layers were in place; 00 still had four-sentence Final QC and two unwired SOPs.
change: Pipeline scheduling is intent classify + skill chain + QC closed loop. Directory detection as entry; four decision nodes (SOP / PHI / WRITE / PREVIEW); post-skill file checks; integrity gates G0/G-PHI/G-04/G-05/G-06 mapped to lab failure modes; handoff.yaml; project-state pipeline/qc/defects; local recovery max 3 then unresolved. radiomics-study offers sci-manuscript when HTML exists. Do not mount ARS academic-pipeline or MedSci orchestrate. Do not add --e2e skip of session mount pick or PHI. 选刊 stays 03.
decision: keep
next_action: user reviews PR; do not merge until named
```

## mounts-cap local cache 2026-09-03 (user)

```text
change_id: CHG-20260903-016
date: 2026-09-03
skill: 01_skill-discovery-integration
author: Aitor
change_class: interface
problem: B and backup plugins had no A-local cache; fetching a backup meant guessing a whole clone.
change: Added repo-root mounts-cap/ (README, INDEX, fetch.py). Pack trees gitignored. B = full tree (legacy sibling MY-SKILLS-capabilities still accepted). ARS/MedSci/Scientific = only the path(s) of ids picked this run. Download ≠ mount. Session pick and empty-mount unchanged. Do not vendor packs into A git.
decision: keep
next_action: user reviews PR; do not merge until named
```

## 00/05/06 interact + review template 2026-09-04 (user)

```text
change_id: CHG-20260904-001
date: 2026-09-04
skill: 00_orchestrator + 05_manuscript + 06_review
author: Aitor
change_class: policy
problem: User wanted interactive 00 (plan first, execute-QC-execute), sentence-level edits, tagged comments with user-final decisions on mount vs lab conflicts, lit-verify dual plans, and personal English review rearranged to an 8-section Major/Minor template.
change: 00 plan card + G-LIT; 05 internal-call table + edit-unit/comments; 06 layout/comment/conflict rules; personal-review-style.md rewritten to Title…Figures template while keeping corpus themes; response-style §9. Mount conflicts → comment with edit plan; user decides. Do not silent-apply mounts.
decision: keep
next_action: user reviews PR; do not merge until named
```

## Comment attribution + fetch harden 2026-09-04 (user)

```text
change_id: CHG-20260904-002
date: 2026-09-04
skill: 06_review + 00_orchestrator + 05_manuscript + mounts-cap
author: Aitor
change_class: policy + tool
problem: Three same-day harvests (lxf_RC / wyy_SCD / tyt_SDC) showed mount-driven comments labeled only [A:personal]; fetch parallel ensure clobbered STATE; Contents API 403 on large trees.
change: P0 in personal-review-style §0 — author field A ≠ source prefix; mount sources must appear in prefix (dual-tag OK). 00 pointer + G-06 fail if mounted non-personal source has zero matching prefixes. Refs: duplicate DOI/title = Major; no number migration on swap. 05: scan max [n] before new cite. fetch.py: zip-first for backups, merge STATE under lock, API 403 falls through to zip.
decision: keep
next_action: user reviews PR; do not merge until named
```

## Remove archive stub + B under mounts-cap 2026-09-04 (user)

```text
change_id: CHG-20260904-003
date: 2026-09-04
skill: layout + mounts-cap
author: Aitor
change_class: layout
problem: archive/ only held README after packs were rehomed; B still lived as a sibling of A instead of mounts-cap/b/.
change: Deleted archive/. Docs/tests no longer require it. Canonical local B is mounts-cap/b/; fetch.py migrate-b moves leftover sibling MY-SKILLS-capabilities/. Pack bytes stay gitignored.
decision: keep
next_action: user reviews PR; do not merge until named
```

## OpenClaw Medical Skills PROPOSED board 2026-09-06 (user)

```text
change_id: CHG-20260906-001
date: 2026-09-06
skill: 01_skill-discovery-integration + mounts-cap + 00/06 attribution
author: Aitor
change_class: policy
problem: User approved adding FreedomIntelligence/OpenClaw-Medical-Skills as a 01 backup interface (same format as MedSci/Scientific), after a ChatGPT share proposed 7 ocms-* mount ids.
change: PROPOSED board mounts/openclaw.md + sources/openclaw-medical-skills.proposed.yaml @b1f9b6e; registry proposals entry; fetch/INDEX dir openclaw; session pick/换源 includes OpenClaw; attribution/G-06 prefix [OpenClaw:…]. Mapped 23/30 (7 empty). No new coarse ids; no ocms-*; no writing-only OpenClaw mount; clinical-reports excluded from 05; on-demand paths only.
decision: keep
next_action: user reviews PR; do not merge until named
```

## Evidence Request protocol 2026-09-06 (user)

```text
change_id: CHG-20260906-002
date: 2026-09-06
skill: 05_manuscript/personal + 00 G-LIT
author: Aitor
change_class: policy
problem: User agreed mounts should raise reverse lit-fill gaps, 03 searches, and A 05 personal owns final evidence QC — rejecting B05-as-personal-orchestrator and permanent A05 three-pack sub-dispatch.
change: Thin protocol 05_manuscript/personal/evidence-request.md (card fields; Accept/Weaken/Delete; roles). Pointers in 05 SKILL, intro-discussion-evidence, 00 G-LIT/gates. No B layout change; no new coarse ids.
decision: keep
next_action: user reviews PR; do not merge until named
```

## Review Resolution protocol 2026-09-06 (user)

```text
change_id: CHG-20260906-003
date: 2026-09-06
skill: 06_review/personal + 00 G-06
author: Aitor
change_class: policy
problem: User agreed ChatGPT A06/B06 redesign should keep swappable mount engines and structured resolution status, but reject B06-as-intelligence-core and A06-as-permanent three-pack dispatcher.
change: Thin protocol 06_review/personal/review-resolution.md (issue card; Resolved/Partial/Unresolved/New; A 06 judges). Pointers in 06 SKILL, response-style, G-06. No B layout change; no new coarse ids.
decision: keep
next_action: user reviews PR; do not merge until named
```

## AIPOCH Medical Research Skills PROPOSED board 2026-09-06 (user)

```text
change_id: CHG-20260906-006
date: 2026-09-06
skill: 01_skill-discovery-integration
author: Aitor
change_class: policy
problem: User asked to continue after ChatGPT share on aipoch/medical-research-skills — treat as capability source, not a new MY-SKILLS layer.
change: PROPOSED board mounts/aipoch.md + sources/aipoch-medical-research-skills.proposed.yaml @f5ef65b; registry proposals; fetch/INDEX dir aipoch; session pick/换源 includes AIPOCH; attribution/G-06 prefix [AIPOCH:…]. Mapped 25/30 (5 empty). No new coarse ids; no aipoch-*; writing/review as workers only; lab-ops/education EXCLUDE; meta-skills cannot steal 00.
decision: keep
next_action: user reviews PR; do not merge until named
```

## Medical journal submit personal pack 2026-09-06 (user)

```text
change_id: CHG-20260906-007
date: 2026-09-06
skill: 03_research/medical-journal-submit
author: Aitor
change_class: capability
problem: User provided medical-journal-submit zip (JCR2026 curated荐刊); agreed A/03 Victor home; keep curated xlsx not raw Clarivate; fix B write-venue journal-selection.md mis-home; AGENTS.md must follow SKILL/policy.
change: Add A 03_research/medical-journal-submit (SKILL+AGENTS+references+artifacts/医学投稿推荐_JCR2026.xlsx). Wire literature/journal-selection + 03 SKILL/intake. Companion B PR deletes write-venue/journal-selection.md and points to A pack.
decision: keep
next_action: user reviews PRs; do not merge until named
```

## Harvest-QC + G-FACT 2026-09-06 (user)

```text
change_id: CHG-20260906-008
date: 2026-09-06
skill: 00_orchestrator + skill-harvest/qc
author: Aitor
change_class: policy
problem: ChatGPT share proposed compact QC + harvest evolution; user agreed Aitor rewrite (no 07_QC, no Q0–Q6 takeover, passive evolution HTML only on ask).
change: Add G-FACT consistency gate + transversal map in gates.md; skill-harvest/qc/SKILL.md+rules.md; data/qc-events/; templates/qc-evolution.html; wire harvest SKILL + ARCHITECTURE.
decision: keep
next_action: merge when named; sync local A
```


## Harvest-QC repository-wide audit hardening 2026-09-06 (user)

```text
change_id: CHG-20260906-009
date: 2026-09-06
skill: skill-harvest/qc + _medical-research-meta
author: Aitor
change_class: qc-fix + tooling
problem: Repository-wide QC identified broken relative Markdown links, stale active-path wording, a Git-only invariant that failed on exported ZIPs, and no single repo-wide Harvest-QC scanner.
change: Added skill-harvest/scripts/repo_qc.py with deterministic repository-wide checks; added skill-harvest/qc/repo-qc.md and JSON/Markdown report outputs; repaired broken internal links and active-path wording; made the mounts-cap cache invariant skip cleanly outside a Git checkout while retaining the Git-tracked check inside Git; added QC tests for local links and the scanner.
expected_benefit: One reproducible QC entry point for structure, frontmatter, routing, mounts, stale references, local links, meta/version consistency, and test status without granting auto-modification authority.
observed_evidence: static full-repo scan + local unittest run after repair
metric_summary: 0 broken local Markdown links; deterministic QC PASS; unit tests pass outside Git checkout
boundary_effect: skill-harvest observes and reports; 00–06 remain domain owners; no new top-level skill; no automatic evolution
decision: keep
next_action: run repo_qc.py after structural changes (do not commit generated data/repo-qc.*); record evolution only when the user explicitly asks
```

## CHG-20260907-001 — Nature PROPOSED board
date: 2026-09-07
problem: User provided Nature Skills zip and asked for a PROPOSED mount pointer board (backup candidate), same pattern as OpenClaw/AIPOCH.
change: PROPOSED board mounts/nature.md + sources/nature-skills.proposed.yaml @287ee37; registry proposals entry; fetch/INDEX dir nature; session pick/换源 includes Nature; attribution/G-06 prefix [Nature:…]. Mapped 13/30 (17 empty). Uniquely fills 03-lit-fulltext and 06-review-response vs Scientific/OpenClaw empty. No new coarse ids; no nature-* coarse IDs; writing/polish overlaps A personal de-AI (personal wins); PPT/patent/lab systems stay unmapped_groups. Third-party package disclaimer (not Springer Nature official). Node 22+ and authenticated Chrome required for nature-downloader / nature-image2ppt. Default 06-review-response remains B. Mapping is not a mount.

## CHG-20260907-002 — table-qc + stats-consistency
date: 2026-09-07
problem: Harvest Gemini share into skill-library and thin-patch A with PR.
change: Add 02 table-qc references and 04 personal stats-consistency plus checklist. Wire 02/04 SKILL tables. No vendored scripts; not code-refactoring; not skill-harvest/qc.

## CHG-20260908-001 — review hybrid presets + mount score rubric
date: 2026-09-08
problem: User wants hybrid mount as default session recipe (Nature-primary), swappable detail skills, human score tables separate from QC standards in skill-harvest/qc.
change: Add mounts/presets.md + presets/review-hybrid.yaml; wire 01 session pick to pre-check review-hybrid-default for review tasks; add skill-harvest/qc/mount-score-rubric.md and pointers in qc SKILL/rules. Do not flip PROPOSED sources to MOUNTED; ARS/Grok out of default.

## CHG-20260908-002 — code-refactoring QC + complexity ladder
date: 2026-09-08
problem: User said 更新 code-refactoring: merge modules deep code QC and Ponytail-stable ladder absorbs from skill-library.
change: Extend code-refactoring SKILL + references/code-qc.md + references/complexity-ladder.md. No 01 mount, no B coarse id, no skill-harvest/qc mix-in, Medical axis pointers to 04 only.

## CHG-20260908-003 — skill-level mount attribution
date: 2026-09-08
problem: Hybrid mount and scorecards were treated as whole sources because comments lacked pack-skill tags.
change: Require [Source:pack-skill] prefixes (06 style + G-06); presets review-hybrid.yaml gains skills: + narrowed paths; 01 session lines show 粗ID·源·skill; qc mount-score-rubric primary key is source/skill.

## CHG-20260909-001 — journal-selection / medical-journal-submit align
date: 2026-09-09
problem: User (via Bai notes) finalized Phase-1 选刊 display/defaults; pack still had Medicine red-mark and 5-per-layer remnants in places.
change: Align SKILL/AGENTS/policy/workflow/journal-selection/annual-update to v1.14 rules (10+10+10, 层2补 ask-off, JESI≥80 yellow only, Medicine deprioritize no 可疑/red, persist URLs only).

## CHG-20260910-002 — BMC/Medicine whitelist priority
date: 2026-09-10
problem: User wants BMC/Medicine titles preferred in Phase-1 (except LWW MEDICINE blacklist).
change: medical-journal-submit v1.15 + whitelist-bmc-medicine.csv (~486); rank after 稿件匹配度; drop Medicine demote; no 可疑/red.

## CHG-20260910-003 — Phase-2 选刊短表交付
date: 2026-09-10
problem: User (via Victor) locked Phase-2 HTML short-table columns and full-URL display; no ISO/OA/置信/APC/分刊详情.
change: medical-journal-submit v1.16 + aim-author-checklist/workflow/AGENTS/journal-selection; wording 默认挂载 B 包/本仓 not 空挂.

## CHG-20260910-001 — HTML visual design standing rules
date: 2026-09-10
problem: User wants HTML Visual Design Principles applied whenever editing/generating .html; not a full-repo audit; do not vendor lab console/starter HTML into MY-SKILLS.
change: Add 00_orchestrator/references/html-visual-design.md; wire 00 SKILL only.

## CHG-20260912-001 — 04 0RAD clinical/manual + console gates
date: 2026-09-12
problem: Live modules (2026-09-12) switched Clinical to manual FORCE_MODEL and gated external/advanced/exclude; skills still said AIC backward / candidate pool.
change: Update 0rad-pipeline-rules + SKILL/MODULE/high-dimensional-omics from skill-library extracts/04_analysis/modules-delta-20260912.md; no modules .py in repo.

## CHG-20260913-001 — v4 mount registry (10+52 hybrid)
date: 2026-09-13
problem: User accepted option B — replace 30 coarse-id mount menu with 10 welded stage buckets + 52 fine session-pick ids; integrate B_updates; archive unused mounts; ban OpenClaw as atomic source.
change: registry.yaml v4 (backup registry.v3.30.yaml); mounts/MIGRATION_v3_to_v4.md; boards/SKILL/MOUNTED_SKILLS/presets; B new skills + cross-pack stubs + external-principles; tests adapted; A folders not renamed to Chinese.
decision: open PR only (no merge until 合并)
next_action: user review PR; confirm Nature LICENSE; optional move 样本量 coarse to 统计分析

## CHG-20260913-002 — Claude repo audit: stale pointers, YAML bug, dedup, coarse→fine wiring
date: 2026-09-13
problem: Full-repo scan requested (旧的指针/错误/精简机会 + 00→02-06 粗ID→细ID 分派机制点评). Found: root README.md and _medical-research-meta/README.md still described the pre-v4 "30 coarse ids" menu (untested drift, ArchitectureSsot test only covered the two ARCHITECTURE.md files); registry.yaml line 238 had a real YAML syntax error (unquoted colon inside a `note:` scalar — the "canonical machine index" was never actually parseable by a standard YAML loader); root `MY-SKILLS-capabilities/` was a byte-identical duplicate of `mounts-cap/b/` (should only exist as the gitignored local cache, B is a separate repo); `registry.v3.30.yaml` / `registry_v4.audit.yaml` cluttered 01's root next to the live `registry.yaml`; MOUNTED_SKILLS.md was a hand-copied table with no drift protection; G0 gate had no concrete field to check "only picked ids loaded" against; `test_no_legacy_manuscript_paths` false-positived on a coincidental substring in an upstream Nature template filename (`01_research_canon.md`); find-journal/grant-builder's a_domain override wasn't a declared rule anywhere.
change: Fixed both READMEs to v4 wording; quoted the bad YAML scalar; verified all other *.yaml parse cleanly; deleted duplicate root `MY-SKILLS-capabilities/` (mounts-cap/b/ is now the sole local copy); moved the two old registries into new `01_skill-discovery-integration/_history/` (updated 8 cross-references); added `01_skill-discovery-integration/scripts/gen_mounted_skills.py` to generate MOUNTED_SKILLS.md from registry.yaml (verified zero data drift on first run); added `mounted_fine_ids` / `mounts.session_picked_fine_ids` fields to handoff.yaml / project-state.yaml and wired G0 in gates.md to check them; added `a_domain_override_policy` to registry.yaml meta; scoped `test_no_legacy_manuscript_paths` to skip `mounts-cap/` (third-party verbatim content); added `ReadmeSsot` and `MountedSkillsGenerated` tests to close both drift blind spots; rewrote `EXTERNALIZATION_CANDIDATES.md`'s 03-research section into a file-level retirement table (was a blanket folder-level note) and flagged `literature/journal-selection.md` as a permanent home, not a duplicate — left the actual deletion of the retirement-candidate files for user confirmation per fine-id usage.
not_done: 03_research/design|frontier|literature retirement-candidate files not deleted (needs Aitor's per-fine-id usage confirmation, see EXTERNALIZATION_CANDIDATES.md). B-repo (`MY-SKILLS-capabilities`) has 13 broken relative links under `cross-pack/*/MODULE.md` (missing `references/*.md` / `manifest.yaml`) — out of scope for this (A) repo, flagged for a separate PR against B.
decision: local edits only, no GitHub push (no git credentials in this session) — delivered as a zip for manual sync.
next_action: user reviews the zip, syncs to `loopnownow/MY-SKILLS` manually or via their own git access; confirm/action the EXTERNALIZATION_CANDIDATES.md retirement table; consider filing the B-repo broken-links issue separately.

## CHG-20260913-003 — 03 dual-track retirement executed; correction to CHG-20260913-002's mapping
date: 2026-09-13
problem: User approved (1) executing the file-level retirement table from CHG-20260913-002, and (2) filing a fix for B's 13 broken cross-pack links. Before deleting, verified each file individually instead of trusting the earlier coarse mapping — found it was wrong in two places: `journal-patterns-2023-2026.md` was mapped to a "safe duplicate", but B's same-named file under `05-manuscript/write-venue/` is a deliberately narrowed rewrite ("not a 选刊 SOP") that dropped the journal-tier table and Red Lines section — not equivalent, must stay in A. Also `literature.md`/`sources.md`/`public-datasets.md` (B: `lit-search/`) and `evidence-layer.md`/`idea-to-question.md` (B: `frontier-hypothesize/`) point at real B content that has **no fine id in registry.yaml at all** (not PROPOSED, not MOUNTED) — deleting the A copies would make that content unreachable via session pick.
change: Diffed all 13 originally-flagged files byte-for-byte against their B counterpart. Deleted the 12 confirmed pure duplicates (7 under `design/`, 4 under `frontier/`, 1 under `literature/` — all diffs were legacy-pointer-name updates only, e.g. `radiology-stats` → `04-stats-guide`, no content lost). Kept `journal-patterns-2023-2026.md`, `radiology-design.md`, `radiology-frontier.md`, `evidence-layer.md`, `idea-to-question.md`, `literature.md`, `sources.md`, `public-datasets.md`, `journal-selection.md` with reasons recorded in `EXTERNALIZATION_CANDIDATES.md`. No other doc referenced the deleted paths (grep-verified) except `EXTERNALIZATION_CANDIDATES.md` itself, which was rewritten.
finding: B has two folders with real content and zero live mount points: `03-research/lit-search/` and `03-research/frontier-hypothesize/`. Not fixed here (mounting requires explicit user approval per registry.yaml's own rule) — flagged as a follow-up recommendation in `EXTERNALIZATION_CANDIDATES.md`.
decision: file-level cleanup executed; registry.yaml mount additions NOT executed (needs explicit approval, out of scope for a cleanup pass).
next_action: user decides whether to add `lit-search` / `frontier-hypothesize` fine ids to registry.yaml, or accept `literature.md`/`sources.md`/`public-datasets.md`/`evidence-layer.md`/`idea-to-question.md` as permanent A content instead of "temporary duplicates".

## CHG-20260913-003B — External skill triage: no-ai-slop dropped, vivid-figures license-blocked (palette-only original substitute), mattpocock grill/loop absorbed, repo-map.html activated
date: 2026-09-13
note: numbered 003B — collides with the existing CHG-20260913-003 above (03 dual-track retirement) because this entry was written without checking whether 003 was already taken. Kept both entries as-is (content is accurate) rather than renumbering everything downstream that already cites CHG-004/005/etc.
problem: User asked to integrate 4 external repos (archify, mattpocock/skills, no-ai-slop, vivid-figures-skill) evaluated in CHG-20260913-002-adjacent triage. Findings: no-ai-slop's blanket "always active voice" rule would regress the already-established Methods-section passive-voice exception, and 21/23 of its banned words already exist in `ai-isms-checklist.md` — low marginal value. vivid-figures-skill carries a custom "Personal Non-Commercial, no derivative works, no redistribution" license (not MIT) — copying or rewriting its palettes/figure-planning content, even a 10-of-108 subset, is a derivative work its license explicitly forbids. Its figure-planning content (data/statistical/technical diagrams) is also already superseded by the mounted `04-fig-plot` (12 reference files, radiology-specific) — no gap to fill there regardless of license. mattpocock/skills (MIT) has a "grilling"/"grill-me"/"loop-me" mechanic (batched clarify-round questions, each with a recommended default, "push the checkpoint right") worth adopting for 00's Plan card, condensed heavily per user request. archify not evaluated further this round (user did not act on it).
change: (1) no-ai-slop: dropped, no changes. (2) vivid-figures-skill: declined to copy/adapt its licensed content (explained the license conflict rather than proceeding); instead added an original, openly-sourced "发表用扩展色板" 10-palette table to `04_analysis/personal/lab-palettes.md` (ColorBrewer / matplotlib viridis family / Paul Tol / Crameri batlow / ggsci — all open licenses, none derived from vivid-figures-skill's specific hex values or naming) covering categorical/sequential/diverging/grayscale-safe/journal-style gaps not already in `lab-palettes.md` or mounted `04-fig-plot/color-systems.md`. (3) Condensed mattpocock's grilling/loop-me Q&A discipline into `00_orchestrator/SKILL.md`'s "Plan card" section as a single paragraph (batched numbered questions + recommended defaults + find-facts-yourself + push-checkpoint-late), scoped as the one exception to the existing "ask one question, never two" rule, only for multi-node/new-capability entry points. (4) Activated the previously-dormant "full-repo architecture audit" hook in `html-visual-design.md`: added `00_orchestrator/scripts/gen_repo_map.py`, generating `00_orchestrator/repo-map.html` (offline, no-CDN, filterable index of registry.yaml's 10 coarse / 48 mounted fine ids) — same generate-from-source-of-truth pattern as `gen_mounted_skills.py`. Added `RepoMapGenerated` test (anti-drift, mirrors `MountedSkillsGenerated`).
not_done: archify not integrated (user didn't confirm a concrete need for software/pipeline architecture diagrams; stays unevaluated-in-registry). vivid-figures-skill's figure-planning text not touched at all (license + redundant with 04-fig-plot).
decision: license conflicts are hard stops, not negotiable via scope reduction (10 vs 108 palettes does not change derivative-work status) — declined the literal ask, delivered the underlying need (curated publication palettes) via original, openly-licensed sourcing instead.
next_action: user reviews repo-map.html and the new palette table; if archify's architecture-diagram capability becomes actually needed, re-open as a PROPOSED registry candidate under 数据处理.

## CHG-20260913-004 — figure-claim-planning absorbed; grilling promoted to a standalone sub-skill
date: 2026-09-13
problem: User asked to (1) rewrite the four generic principles distilled from vivid-figures-skill (claim-driven chart selection, pre-registered figure-evidence manifest, 3-round per-figure repair cap, style/palette decoupling) as original content in the lab's own voice, and (2) promote the condensed grilling mechanic (added to 00's Plan card in CHG-20260913-003) into a standalone, directly-triggerable skill usable for any underspecified build/implementation request, not just 00's multi-node dispatch — with two modes (grill-me / grill-with-docs).
change: Added `04_analysis/personal/figure-claim-planning.md` — original content reframed entirely around the lab's own analysis types (paired ROC + DeLong p, calibration plots, KM/log-rank, LASSO path, ICC) and existing gate ids (G-FACT/G-04 reused, not duplicated, for a pre-figure evidence manifest; the existing gates.md 3-round cap reused, not re-defined, for per-figure render QC). Wired into `04_analysis/SKILL.md` (Personal layer table + Workflow step 5). Added `00_orchestrator/grilling/SKILL.md` (new sub-skill, 3 path parts, within `test_core_max_four_path_parts`) with `grill-me` (direct batched Q&A) and `grill-with-docs` (research repo/docs/web first, then ask) modes. Updated `00_orchestrator/SKILL.md`'s Plan card to reference `grilling/SKILL.md` instead of re-stating the mechanism inline (one fact, one home — Plan card is now just grilling's application at the multi-node dispatch point). Added a Fast routing entry for `grill-me`/`grill-with-docs`/盘问/烤透需求 keywords.
not_done: archify still not integrated — instead extended `00_orchestrator/scripts/gen_repo_map.py` (CHG-20260913-003) with a hand-authored native SVG of 00's full-project SOP flow, avoiding a Node.js dependency for a single static diagram.
decision: kept the vivid-figures-skill-derived principles at the "engineering idea" level, rewritten from scratch in lab-specific terms and cross-referenced to already-existing gates rather than introduced as new parallel rules — avoids both the license issue and rule duplication.
next_action: none pending from this round; user to review figure-claim-planning.md against actual upcoming manuscripts and grilling/SKILL.md the next time a build request is underspecified.

## CHG-20260913-005 — 01 gets a formal GitHub discovery workflow (search → checklist → recommend → grill-me confirm)
date: 2026-09-13
problem: 01's "new capability" path was thin ("network first, then ask for a local path") — every actual GitHub-skill evaluation this session (archify, mattpocock/skills, no-ai-slop, vivid-figures-skill) was done ad hoc by hand, with no repeatable procedure baked into the skill itself. User asked to formalize: 01 should search GitHub, compare candidates, and decide mount-vs-absorb itself — but must ask (not 00, not silently) before actually executing.
change: Added a "GitHub discovery workflow" section to `01_skill-discovery-integration/SKILL.md`: (1) search 3-6 candidates, don't stop at one; (2) shallow-clone and read SKILL.md/README/LICENSE; (3) a 4-step ordered checklist — license hard-gate (permissive-license required, "just take a subset" does not change derivative-work status), domain fit (skip out-of-scope general software-eng content unless the user names a concrete need), overlap check (≥~80% already covered elsewhere → low marginal value, don't mount/absorb wholesale), granularity (must map to one clean fine id; oversized/heavy-runtime candidates default to a native lightweight alternative instead) — each step cites this session's own precedent (vivid-figures-skill / mattpocock / no-ai-slop / archify respectively) as a worked example; (4) output a recommendation table, never execute directly; (5) hand the table to `grilling` (`grill-me` mode) as one batched round with recommended actions, wait for per-row confirmation; (6) only then write `sources/<name>.proposed.yaml` (mount path) or rewrite into `personal/` (absorb path) or do nothing (skip path). Updated 00_orchestrator/SKILL.md's "New capability" routing line to name this workflow explicitly instead of the vague "network first" phrasing.
not_done: nothing pending.
decision: 01 owns search+comparison+recommendation (matches its existing charter "resolves where a capability comes from"); 00 only routes into it; grilling (not 00, not 01 alone) is the confirmation gate before any file gets written — reuses the sub-skill added in CHG-20260913-004 rather than defining a second ask-before-acting mechanism.
next_action: none pending; next external-skill evaluation should visibly follow this section's 6 steps.

## CHG-20260913-006 — Final A+B scan: humanize MOUNTED-but-empty fixed; nature PROPOSED stubs clarified (not a bug)
date: 2026-09-13
problem: Full re-scan of both A and B requested. Cross-checked every `MOUNTED` fine id in registry.yaml against actual bytes in `mounts-cap/`. Found `humanize` (source `med-sci-skills`) declared `MOUNTED` with zero bytes at `mounts-cap/medsci/skills/humanize/` — a real violation of the repo's own rule ("do not claim MOUNTED if bytes absent"), likely a leftover from before this fine id was fetched. Verified the content genuinely exists upstream (`Aperivue/medsci-skills@fb6e78d`, 15 files) via a throwaway shallow clone. Separately, re-examined the earlier "13 broken links" claim (CHG-20260913-002/003): that number was from the A-repo LocalLinkHygiene test run *before* the duplicate root `MY-SKILLS-capabilities/` was deleted — the real broken-link source was that duplicate, already fixed. The actual B-side pattern (4 `nature-*` PROPOSED cross-pack MODULE.md router stubs referencing a `manifest.yaml`/`static/`/`../nature-shared/` that aren't fetched) is by design — PROPOSED status means preview-only, no bulk download until APPROVED — verified the full dependency tree exists upstream (`Yuan1z0825/nature-skills`) but correctly wasn't pulled. That prior "13 broken links, out of scope for B" framing was itself imprecise and is corrected here.
change: Fetched `skills/humanize/` from `Aperivue/medsci-skills` into `mounts-cap/medsci/skills/humanize/` (15 files) and recorded it in `mounts-cap/STATE.yaml` under `med-sci-skills`. Re-ran a full MOUNTED-vs-disk audit across all 33 MOUNTED fine ids — zero gaps remain. Added a one-line clarifying comment to the 4 affected `nature-*` cross-pack `MODULE.md` files (`nature-polishing`, `nature-academic-search`, `nature-data`, `nature-proposal-writer`) noting the missing manifest/static/shared files are an intentional PROPOSED-stage gap, not a defect, and must be fully fetched before any of the four is promoted to MOUNTED. Cross-checked B's own `CHANGELOG.md` self-noted TODO ("root SKILL.md/README.md still list 28 ids") — already resolved, no stale "28" text found; false alarm, no action. Verified all 32 directories in B's actual tree are referenced by some fine id in A's `registry.yaml` — no orphaned B content.
not_done: nothing pending from this scan.
decision: treat "MOUNTED claims bytes present" as a hard, checkable invariant, not just a written rule — worth scripting as a permanent test (see next_action) rather than relying on manual audits like this one.
next_action: none — implemented immediately: added `MountedBytesPresent` test to `_medical-research-meta/tests/test_audit_invariants.py` (50 tests total now), running the exact MOUNTED-vs-disk check this session did by hand on every future run.

## CHG-20260913-007 — 03_research local-file retirement confirmed + broken cross-refs fixed (self-correction)
date: 2026-09-13
problem: User said "替换本地细ID" (go ahead with the CHG-006-flagged retirement of `03_research/design|frontier|literature` duplicates). Investigating current state, Claude found `design/`/`frontier/` had fewer files than expected and momentarily misdiagnosed this as accidental data loss from earlier in the session; restored all files from the original upload. Re-reading `EXTERNALIZATION_CANDIDATES.md` (which already had a detailed, verified retirement analysis — more precise than the file-level table from CHG-002/006 — checking each B counterpart's actual registry mount status, not just filename matches) revealed the "missing" files were in fact **already correctly retired** in earlier work this session: `design/study-design.md`, `study-blueprints.md`, `feasibility-triage.md`, `validation.md`, `validation-strategy.md`, `endpoints-and-estimands.md`, `ai-radiogenomics-12-24-roadmap.md` (7 files) and `frontier/frontier.md`, `frontier-themes.md`, `frontier-patterns-2023-2026.md`, `ai-radiogenomics-frontier-map.md` (4 files) are genuine 1:1 duplicates of mounted `design-study`/`find-cohort-gap`; `design/radiology-design.md`, `frontier/radiology-frontier.md`, `frontier/evidence-layer.md`, `frontier/idea-to-question.md` were deliberately kept (no B fine id mounts their B counterpart, or no B counterpart exists at all — see `EXTERNALIZATION_CANDIDATES.md` for the per-file reasoning). Claude's restoration briefly undid this correct work; re-deleted the 11 correctly-retired files and kept only the 4 that should remain.
change: Re-confirmed final state: `design/` has only `radiology-design.md`; `frontier/` has `evidence-layer.md`, `idea-to-question.md`, `radiology-frontier.md`; `literature/` has all 5 non-duplicate files (`literature-evidence-2023-2026.md` stays retired, confirmed byte-for-byte duplicate of mounted `ma-scout` earlier in CHG-006/007). Fixed a real consequence of the retirement that `LocalLinkHygiene` caught: `radiology-design.md` and `radiology-frontier.md` had internal markdown links to sibling files that no longer exist locally (`feasibility-triage.md`, `study-blueprints.md`, `validation-strategy.md`, `endpoints-and-estimands.md`, `ai-radiogenomics-12-24-roadmap.md`, `frontier-themes.md`, `ai-radiogenomics-frontier-map.md`) — converted these from clickable relative links to plain `mounted design-study → references/x.md` / `mounted find-cohort-gap → references/x.md` text references, since mounted paths are fetched on demand and aren't stable local link targets. Updated `03_research/SKILL.md`'s two summary lines to accurately describe partial (not full-folder) retirement.
not_done: nothing pending.
decision: trust and preserve prior verified work in `EXTERNALIZATION_CANDIDATES.md` over a shallower fresh re-derivation — the existing per-file analysis (checking actual registry mount status per B counterpart, not just filename match) was more rigorous than what CHG-002/006 had produced, and is the version that should stand.
next_action: none pending from this item.

## CHG-20260913-008 — OpenClaw held at hard-block; AIPOCH real-content audit promotes 2, rejects 1
date: 2026-09-13
problem: User asked for OpenClaw and AIPOCH fine-id mount planning. OpenClaw is governed by an existing hard rule (`openclaw_policy: never-mount-as-atomic-source`, `sources/openclaw-medical-skills.proposed.yaml` notes "README badges say MIT; root LICENSE file missing at scan") from a prior audit — declined to produce a mount plan for it, consistent with that standing decision. AIPOCH already had 3 fine ids sitting at PROPOSED in `registry.yaml` from an earlier scan (`retraction-watcher`, `clinic-research-design`, `response-tone-polisher`) that had never been promoted or rejected. Read the actual upstream content (`aipoch/medical-research-skills@63c61d3`) for all three rather than trusting the scan's metadata notes or the package's own `eval_report_*.json` self-audits.
change: `retraction-watcher` (732-line script checking DOI/PMID against Retraction Watch, Crossref, PubMed; no overlap with `verify-refs`/`manage-refs`) and `response-tone-polisher` (652-line script softening reviewer-response tone; no overlap with `revise`) promoted PROPOSED→MOUNTED after user confirmation (via `ask_user_input_v0`, three separate decisions). Both had a stale `path:` in `registry.yaml` (`skills/x/`) that didn't match the real repo layout (`scientific-skills/<Category>/x/`) — corrected. Fetched only those two specific skill folders (not their parent category directories) into `mounts-cap/aipoch/`, recorded in `mounts-cap/STATE.yaml`. `clinic-research-design` rejected and removed from `registry.yaml` entirely: its `SKILL.md` documents `scripts/main.py` plus 4 calculator scripts that do not exist anywhere in the actual package, yet its own `eval_report_clinic-research-design_result.json` marks every gate (`skill_veto`, `research_veto`, contract, stability, determinism, security) as PASS — that self-eval is not a trustworthy signal for any other AIPOCH candidate either, noted in `sources/aipoch-medical-research-skills.proposed.yaml`. Updated `meta.fine_id_count_canonical` (52→51) and the mount count (48→47) everywhere it was written down: `registry.yaml` meta comment, `01_skill-discovery-integration/SKILL.md`, `_medical-research-meta/README.md`, and the hardcoded `48` in `test_registry_matches_mounted_skills_v4` (now 47). Regenerated `MOUNTED_SKILLS.md` and `repo-map.html` from the updated registry.
not_done: nothing pending — the other ~24 AIPOCH-scanned a_hook groups stay unpromoted per the original 2026-09-06 scan's own notes (mostly "coverage: partial" or "already covered — 0RAD/B wins"); no new evidence surfaced this session to revisit those.
decision: applied the GitHub discovery workflow (CHG-005) end to end for the first time on a real case: read actual files rather than trusting metadata/self-eval, corrected a stale path as part of promotion (not left for a future audit to find), and gated the registry.yaml write behind explicit per-item user confirmation rather than presenting the recommendation table and proceeding unprompted.
next_action: none pending.

## CHG-20260913-009 — verify-refs/manage-refs/lit-sync swapped from thin B stub to Scientific citation-management/pyzotero
date: 2026-09-13
problem: CHG-20260913-008's OpenClaw-vs-mounted comparison found the current `03-research/lit-cite/` (B, shared by `verify-refs`/`manage-refs`/`lit-sync`) is a 13-line DOI→BibTeX stub — the thinnest content in the entire citation stack — while `lit-cite/MODULE.md` itself already named Scientific's `citation-management`/`pyzotero` as the intended backup for exactly this gap. User asked to execute the swap (OpenClaw itself stays untouched — hard-blocked, not reconsidered).
change: `verify-refs` and `manage-refs` re-sourced to `scientific-agent-skills`, path `skills/citation-management/` (346-line SKILL.md, `citation_validation.md`/`validate_citations.py` for verify, `bibtex_formatting.md`/`format_bibtex.py` for formatting) — kept `path_shared: true` since both still share one folder. `lit-sync` re-sourced to the same package's `skills/pyzotero/` (154-line SKILL.md, real Zotero API — auth/read/full-text/exports/saved-searches), matching its actual "Zotero+Obsidian sync" purpose better than the old shared stub. Confirmed MIT via `LICENSE.md` in a fresh clone before fetching. Fetched only these two specific folders (not their parent `skills/` tree) into `mounts-cap/scientific/skills/`, recorded in `mounts-cap/STATE.yaml`. Updated the three human boards that had gone stale: removed the 3 rows from `mounts/b.md` (no longer B), added them to `mounts/scientific.md` with the new MOUNTED status, and fixed `mounts/hybrid-mount-pointers.md` (source column MedSci→Scientific, marker ✅→🟢, plus added a 🟢 legend entry distinct from 🔵 since 🔵 means "mostly PROPOSED" and these are now confirmed MOUNTED cross-pack). While in that file, also synced the two AIPOCH promotions from CHG-008 (🔵→🟢 for `retraction-watcher`/`response-tone-polisher`) and removed the leftover `clinic-research-design` row and its mention in `mounts/aipoch.md`, which CHG-008 had rejected but never fully scrubbed from the human boards. Regenerated `MOUNTED_SKILLS.md` and `repo-map.html`. Also fixed fill-protocol registry: removed erroneous `stustub_in_b`/`atomic_package: AIPOCH` pointing at declined clinic-research-design; fill-protocol stays MedSci `03-research/fill-protocol/`.
not_done: noticed `mounts-cap/scientific/skills/peer-review/` sitting on disk with no corresponding `STATE.yaml` entry and no registry.yaml mount pointing at it (the live `peer-review` fine id sources from B, not Scientific) — an orphaned prior fetch, harmless (gitignored cache) but unused; left alone, not in scope of this change.
decision: swapped the source, not just supplemented it — `lit-cite`'s own content stays as B's thin stub (still exists, untouched) but is no longer what these 3 fine ids point to, avoiding two competing "citation" answers under one coarse bucket.
next_action: none pending.

## CHG-20260913-010 — mounts-cap orphan cleanup: OpenClaw, ARS, and a stray Scientific folder
date: 2026-09-13
problem: User asked whether B still needs organizing. A fresh size/reference audit of the whole `mounts-cap/` cache (not just the B tree) found three fully-fetched, zero-reference orphans: (1) `mounts-cap/openclaw/` — 10 full skill folders (616K) cached with no fine id in `registry.yaml` ever sourcing from `openclaw-medical-skills`, despite the hard rule that OpenClaw must never be an atomic mount source — leftover from the original 2026-09-06 license-risk audit, never cleaned up after the block was decided; (2) `mounts-cap/ars/academic-paper-reviewer/` (676K) — fetched once to evaluate `06-review-peer` against the already-MOUNTED B/MedSci version, never promoted, no registry reference, violating the "never bulk-cache without a pick" policy in spirit; (3) `mounts-cap/scientific/skills/peer-review/` — a stray folder noted but left alone in CHG-20260913-009, now confirmed to have zero registry reference and zero `STATE.yaml` entry.
change: Deleted all three (`mounts-cap/openclaw/`, `mounts-cap/ars/`, `mounts-cap/scientific/skills/peer-review/`) and their corresponding `STATE.yaml` blocks (`openclaw-medical-skills:`, `academic-research-skills:`). `mounts-cap/` shrank from ~8.9M to 7.5M. Left `mounts-cap/scientific/skills/scholar-evaluation/` alone even though no fine id's `path` includes it directly — it's grouped with the live PROPOSED `scientific-critical-thinking` in the source scan and small enough not to warrant the same treatment; noted here rather than silently ignored.
not_done: nothing pending. B proper (`mounts-cap/b/`) was re-checked for junk files (`__pycache__`, `.pyc`, `.DS_Store`) and obvious internal duplication — none found; it's policy `full-tree` by design (`INDEX.yaml`), so it doesn't have an "orphan" concept the way on-demand sources do.
decision: "on-demand, no bulk caching until picked" is being treated as a checkable invariant like the MOUNTED-bytes-present one — evaluation clones (used throughout this session for archify/mattpocock/no-ai-slop/vivid-figures-skill/AIPOCH/Scientific/OpenClaw) belong in a throwaway location outside `mounts-cap/`, never copied in unless and until something is actually picked. OpenClaw's and ARS's cached bytes were evidence that this wasn't consistently followed by prior sessions.
next_action: none pending.

## CHG-20260914-001 — Nature Apache-2.0 verified; REFERENCE quartet → MOUNTED; Lee 06 WHE harvest
date: 2026-09-14
problem: User confirmed (1) Nature upstream LICENSE is Apache-2.0 (Yuan1z0825/nature-skills @287ee37) — clear standing「需核实」block; (2) former reference_only quartet (scientific-visualization / nature-figure / nature-reviewer / nature-response) become formal fine IDs at MOUNTED; (3) Lee WHE harvest A/B/C into 06 personal + B review-peer checklist.
change: Cleared all Nature `license_flag: 需核实` → `Apache-2.0 verified 2026-09-14` (third-party note retained); promoted quartet into `mounts:` MOUNTED with package paths and emptied `reference_only: []`; updated nature.md / hybrid-mount-pointers; added `06_review/personal` §0.1 locators + `word-edit-rules.md` (linked from 06 SKILL); companion B checklist `ai-public-data-imaging-checklist.md`. fine_id_count remains 51 (51 mounts, 0 reference_only).
decision: Nature MOUNTED only when local mounts-cap bytes present; still never OpenClaw.
next_action: user reviews PRs; do not whole-zip overwrite local .grok/skills.

## CHG-20260921-003 — Word format freeze + paragraph spec
date: 2026-09-21
skill: 05_manuscript/personal/Aitor-format.md + 06_review/personal/word-edit-rules.md
problem: User forbade changing Word format on revision; asked skills to use justified, LTR, space 0/0, TNR 12, line spacing 1.5.
change: Existing `.docx` edits are wording only. Canonical paragraph metrics in Aitor-format; word-edit-rules owns the freeze. Dropped applying first-line 0.74 cm on revision.
decision: keep
next_action: live polish; confirm no restyle of user Word files.

## CHG-20260921-004 — Word user-wording wins
date: 2026-09-21
skill: 06_review/personal/word-edit-rules.md
problem: User required: if Word text differs from the last agent sentence, treat it as the user’s edit; ask before changing; never restore. HTML/PDF/scripts excluded.
change: Home rule in word-edit-rules; pointers in 05 SKILL, Aitor-format, 06 SKILL.
decision: keep

## CHG-20260921-005 — harvest this-session standing rules
date: 2026-09-21
problem: User asked to fold remaining chat rules into skills.
change: (1) `ref/manuscript-revision.md` after 05/06 Word pass; skip re-polish of logged sections. (2) Session pick defaults hybrid; writing pre-checks W2; empty path tell user. (3) Figure 1: Training/Test; downsample ≠ eligibility; PDF TNR 12; underpowered external stays in comments. Aitor wins over fig-flow Validation Cohort in personal files.
skipped: locked AUCs, lxf_js n, Bengbu, title vs mixed-regimen, RadScore 0.000000 (project). Word format freeze and user-wording already in skills.
decision: keep

## CHG-20260921-006 — ban labeled + locked (AI tells)
date: 2026-09-21
skill: 05_manuscript/personal/forbidden-phrases.md (+ ai-isms-checklist, Aitor-format, polisher wording)
problem: User editorial bans: *labeled*/*labelled* and *locked* are AI-ish; do not use in SCI prose or house-rule wording.
change: Hard-ban Prefer labeled→classified as/assigned to/named (abstract parts: headed …); locked→fixed/decided/settled/finalized. Rephrased ai-isms abstract line; Aitor-format “locked tables/choices/threshold” → fixed/decided; polisher “locked paragraphs” → settled. Historical CHG text left as-is.
decision: keep
next_action: same PR as CHG-003/004/005; delete leftover deep publisher-notes path.

## CHG-20260921-007 — ban raw 0/1 outcome coding in prose
date: 2026-09-21
skill: 05_manuscript/personal/Aitor-format.md (+ polisher-sections)
problem: User: manuscript must not show pre-stats raw coding such as Positive = 1, Negative = 0.
change: Outcomes + ban list + checklist: clinical names only; 0/1 encoding stays in the analysis dataset. Polisher Methods pointer.
decision: keep
next_action: include in same PR as CHG-003–006 when PR path is available.

## CHG-20260921-008 — ban dataset-build eligibility narration
date: 2026-09-21
skill: 05_manuscript/personal/Aitor-format.md
problem: User forbids Methods prose that narrates data-prep filters as eligibility (e.g. complete binary outcome label + complete feature row; predefined exclusion list removed).
change: Patients + Banned voice + de-pipeline table: clinical inclusion/exclusion only; row-completeness / feature-matrix filters stay in the analysis pipeline.
decision: keep
next_action: same PR as CHG-003–007.

## CHG-20260921-009 — unused recorded variables → Word comments
date: 2026-09-21
skill: 05_manuscript/personal/Aitor-format.md
problem: User: things not done / not included must not appear in prose (e.g. Treatment type and chemotherapy agent were recorded but were not included as candidate predictors).
change: Model building + Banned voice + reporting defaults: unused recorded predictors → Word comment only (author A).
decision: keep
next_action: same PR as CHG-003–008.

## CHG-20260921-010 — do not re-elaborate sample size
date: 2026-09-21
skill: 05_manuscript/personal/Aitor-format.md
problem: User: writing must not keep restating / emphasizing sample-size narration.
change: Sample-size / power / adequacy once in Methods (Study design); Patients *n* and tables elsewhere; ban repeated essays in Abstract/Results/Discussion/Highlights/Limitations.
decision: keep
next_action: PR when user asks.

## CHG-20260921-011 — decimal places (Table 1 vs P/AUC/NRI)
date: 2026-09-21
skill: 05_manuscript/personal/Aitor-format.md + 04_analysis/personal/stats-checklist.md
problem: User fixed display precision: Table 1 keep 1–2 decimals; P, AUC and related, NRI/IDI, correlation keep 3 decimals.
change: House decimal rule in Aitor-format Results/Table 1 + stats-checklist.
decision: keep
next_action: PR with CHG-010 when user asks.

## CHG-20260922-001 — absorb Code QC Core into code-refactoring
date: 2026-09-22
skill: 02_data-processing/code-refactoring/references/code-qc.md (+ SKILL.md, 00 gates G-CODE)
problem: awesome-copilot-style Code QC Core absorb plan approved; must land inside existing code-refactoring Deep QC home — not a parallel `02/code-qc.md` or new dirs.
change: Extended `code-qc.md` with Existing Pattern First, Data Safety (PHI/PII/secrets/raw overwrite/output pollution; keep CORS/project-scoped), Reproducibility, Preflight→Verdict flow, Critical/Required/Optional ↔ P0–P3 aliases, Boundary as P2 add-on (Architecture kept full), findings/QUESTION rules; SKILL.md capability cross-refs; minimal `G-CODE` row + transversal Code map in `00_orchestrator/gates.md`. No parallel 02 root file; no new mount; no 04 / skill-harvest QC edits; no modules vendor.
decision: keep
next_action: PR open; do not merge until asked; sync only changed files to local Windows `.grok/skills` (no robocopy /MIR on mounts-cap).
