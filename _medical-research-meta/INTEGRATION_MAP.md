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
change: Deleted HIS login automation from clinical-data-extraction (HIS clients stay on the hospital machine, never in git). Aligned ARCHITECTURE.md and _medical-research-meta/ARCHITECTURE.md (depth ≤4, default B, ethics in 03, 30-id menu, backups PROPOSED, no live 04-figure-engine). Workflows ask session-mount pick; Figure 1 uses 04-fig-flow, plots 04-fig-plot; de-AI path is 05_manuscript/personal/forbidden-phrases.md. Fast routing: 选刊 → 05-write-venue, 样本量 → 04-stats-power. Deleted stale SKILLS_map.html. VERSION/READMEs/harvest/tests updated for this batch. Do not rewrite git history.
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
