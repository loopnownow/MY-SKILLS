---
name: medical-research-automation-and-coding
description: >
  Lab file batching, Excel/CSV, and 0RAD workspace rules (not Word/PDF/PPTX).
  Use for 批处理, 合并表, 对齐, 英文化, Excel, 0RAD 文件夹, exc, 假分类.
  Soft-coding / dry-run → code-refactoring. 伦理申请 → ethics-application-forms.
  临床提取 → clinical-data-extraction. Methods stay in 04_analysis / 02_imaging.
  Chat harvest → skill-harvest.
---

# Medical Research Automation

## Purpose

Turn repetitive file and table operations into **reproducible, inspectable** workflows.

- Soft-coding / dry-run / checkpoint → `code-refactoring`
- Ethics form packs → `ethics-application-forms`
- Clinical text / HIS extraction → `clinical-data-extraction`
- Statistical methodology → `04_analysis`
- Imaging methodology → `02_imaging`
- Prose → `05_manuscript`
- Pre-review / reviewer response → `06_review`

## Capability map

| Task | Path |
|------|------|
| Excel/CSV | `bundles/xlsx/MODULE.md`（只读该 MODULE；`scripts/office/schemas/*.xsd` 仅供 validate.py，不要读进上下文） |
| **0RAD workspace** (folder names, `0del`/`0scripts`, `exc`, false-classification) | `references/0rad-workspace.md` |
| Word / PDF / PPTX | system `docx` / `pdf` / `pptx` |
| Coding conventions | `archive/code-refactoring` |
| Harvest chats → update core/archive | `../skill-harvest/SKILL.md` |

## Coding workflow

When this skill writes batch/Excel scripts, follow `code-refactoring` (CONFIG on top, dry-run, checkpoint). Do not restate those rules here.

## 0RAD workspace

Lab folder names, `0del` / `0scripts` / `ref`, `exc`-before-stats, false-classification Pattern+color, HTML-overrides-settings, English clinical labels: **`references/0rad-workspace.md`**.

## Data processing checks

Before merging clinical and imaging data: duplicates, missing/unexpected IDs, one-to-many merges, row counts, missingness introduced by merge, output existence.

## Debugging protocol

classify → first informative message → schema/state → minimal repro → fix root cause → rerun → no silent coerce of bad data.

## Language roles

- Python: automation, files, general pipelines
- R: stats modeling when preferred
- MATLAB: legacy imaging toolboxes
- Shell/SQL: orchestration when appropriate

Do not mint a skill per language.

## Final QC

syntax · input assumptions · output existence · row/subject counts · numerical sanity · reproducibility · clear errors

## Progressive disclosure

Nested `xlsx` uses `MODULE.md` (not a separate skill). Word/PDF/PPTX → system `docx`/`pdf`/`pptx`.
