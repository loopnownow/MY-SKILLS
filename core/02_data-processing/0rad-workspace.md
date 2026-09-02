# 0RAD workspace conventions

**Owner:** `02_data-processing`. Locked across Ying Li lab Grok sessions (through 2026-08-28).

Root: `D:\0Grok\0RAD`. Project folders: `lowercase_UPPERCASE` (`fyh_CAC`, `xlm_LG`). Old names (`CAC_fyh`, `lung_xlm`) are retired.

If the user only opens/`cd`s into a project and names no 01–06 verb, **ask which skill to fire** (`00_orchestrator` → Project open, no skill). Do not start work.

## Where files go

| Kind | Path | Rule |
|------|------|------|
| Scratch / old drafts / one-off scripts | `0del/` (or `0RAD/0del/<project>/`) | Never treat as current results |
| Shared stats library | `modules/` | Entry: `PYTHONPATH=D:\0Grok\0RAD` then `python -m modules.pipeline`. Do not vendor this tree. |
| Ops / manuscript factory | `0scripts/` | Organize / sync / manuscript factory — **not** the stats engine. One-level children only: `organized/` `manuscript/` `sync/` `ssd/` `anjian/`. |
| Reference packs | project `ref/` or `0ref/` | Templates, checklists, locked notes |
| Study/write state (optional) | `ref/project-state.yaml` | Copy from `00_orchestrator/templates/project-state.yaml`. Design + manuscript progress only. **Run keys stay in `settings.ini`.** |
| Current analysis | `<project>/<endpoint>/` or `<project>/<endpoint>/<阳性展示名>_vs_<阴性展示名>/` | One `*-results.html` ↔ one live manuscript. Unpolished: `Manuscript_<结局>_house.docx`. After a polish archive: live `Manuscript_<结局>_polished.docx`, house draft in `0del/<project>/<outcome>/`. Batch scripts scan both via `0scripts/manuscript/ms_paths.py` (skip `0del`; prefer `*_polished.docx` if both exist). Pairwise always nests under the outcome folder; pair folder uses display names. |

| Project-level QC | `<project>/qc.html` | Console「整体 QC」or pipeline start. Combined workbook + imaging QC. Grouping / subgroup → `04_analysis/references/0rad-pipeline-rules.md`. |

Same folder, multiple manuscripts: keep the latest that matches the current HTML; archive the rest to `0del` only if the user asks.

## Named entry points (do not vendor `.py`)

- **Stats:** `python -m modules.pipeline` (`PYTHONPATH=D:\0Grok\0RAD`). Per-project `settings.ini`; algorithms stay in this `modules` copy. `0scripts` does not run the stats engine.
- **STROBE Figure 1:** `figure_strobe_flow.py` is duplicated in `modules/stats` and `0scripts/manuscript`. Canonical after the 2026-08-28 skill update is the figure-engine **POLE** layout (inclusion arrow IN, exclusion arrow OUT, no pipeline row). Point at `python -m modules.stats.figure_strobe_flow`. Do not copy the `.py` into this skill. Layout rules: `05_manuscript/bundles/figure-engine`.
- **Nomogram:** `modules.stats.models.build_nomogram`. Ignore docstrings that still say `python -m modules.nomogram`.

## Tables before any statistic

1. Align clinical rows to the radiomics ID list. Unmatched IDs go to a separate sheet. Do not rename radiomics feature columns after alignment.
2. Clinical categoricals: English labels (`Positive`/`Negative`, `Male`/`Female`). Do not write 0/1 unless the column is a score or a count.
3. Drop columns above the missingness cutoff (lab default **>50%**; user may raise it) **before** imputation.
4. Impute with `04_analysis` `data-impute` (group-stratified; default `mice`; decimal-align). Prefer the project's `modules/utils/u_impute.py`.
5. `exc` sheet: first column = IDs to drop. **Exclude, then analyze.** Building an analysis workbook creates a blank `exc` if missing. Sync: `0scripts/sync/sync_exc_sheet.py`.
6. Columns at or before `record_id` (IDs, names, match-status) do not enter models.

Do not invent values. Ask when a label or ID is ambiguous.

## False classification

- One workbook: `false_classification.xlsx`.
- Required columns include **Group** and **Pattern** (not a separate `all_FN_or_all_FP` sheet).
- Color FN/FP cells. Sync: `0scripts/sync/sync_exclude_and_fc_colors.py` and `batch_rebuild_xlsx.py`.

## Console vs `settings.py`

`{project}.html` / console overlay overrides `settings.py` for that run. Write-back updates `ref/settings.ini`. Command-line without overlay uses `settings.py` only.

`CLIN_ID_COL` may equal `LABEL_COL` (ID is the grouping field). Do not invent a second ID column.

## Coding

Same as `archive/code-refactoring`: CONFIG on top, dry-run for bulk IO, checkpoint resume. Shared library: `D:\0Grok\0RAD\modules`.
