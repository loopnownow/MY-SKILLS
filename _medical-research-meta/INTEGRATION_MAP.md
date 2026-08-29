# Integration map — MedicalResearch Lean v6

This file records the current architecture, not the historical export tree.

| Source capability | Active home |
|---|---|
| Excel/CSV / 0RAD workspace | `core/01_automation/` |
| Soft-coding / dry-run | `archive/code-refactoring/` |
| Clinical extraction | `archive/clinical-data-extraction/` |
| Ethics form packs | `archive/ethics-application-forms/` |
| MRI/fMRI / radiomics / habitat | `core/02_imaging/bundles/` |
| Clinical translation / reader studies | `archive/clinical-translation/` |
| Study design / radiology frontier | `03_research/bundles/` |
| Clinical statistics / prediction | `04_analysis/bundles/` |
| SCI writing / figures | `05_manuscript/bundles/` |
| Manuscript audit / peer review / reviewer response | `06_review/bundles/` |
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
