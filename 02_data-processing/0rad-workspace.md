# 0RAD workspace conventions

**Owner:** `02_data-processing`. Locked across Ying Li lab Grok sessions (through 2026-09-06).

Projects: `D:\0Grok\<stage>\<project>` (stage folders `preparing` `polishing` `submitting` `received` `DER`; `preparing` is the old 0RAD root). Code: `D:\0Grok\0scripts`. Project folders: `lowercase_UPPERCASE` (`fyh_CAC`, `xlm_LG`). Old names (`CAC_fyh`, `lung_xlm`) are retired. A folder still named `reseived` is the `received` stage (`study_folder_stage_aliases` in `00_orchestrator/templates/project-state.yaml`). Leave that folder name as written.

If the user only opens/`cd`s into a project and names no 01–06 verb, **ask which skill to fire** (`00_orchestrator` → Project open, no skill). Do not start work.

## Where files go

| Kind | Path | Rule |
|------|------|------|
| Scratch / old drafts / one-off scripts | `0del/` (or `D:\0Grok\0del\<project>\`) | Never treat as current results |
| Shared stats library | `D:\0Grok\0scripts\modules/` (gold) | Entry: `PYTHONPATH=D:\0Grok\0scripts` then `python -m modules.pipeline`. Projects **point at** this tree; do not vendor it and do not keep a second `modules/` inside each project. If the current request does not explicitly ask to change `D:\0Grok\0scripts\modules`, do not modify that library; project HTML only points at it. |
| Ops / tidy / sync | `0scripts/` (besides `modules/`) | Organize / sync / tidy — **not** the stats engine. Children: `tidy/` `stat/` `sync/` `figures/` `docx_revise/` `archive/` (old `organized/` `manuscript/` `anjian/` live under `archive/`). |
| Reference packs | project `ref/` or `0ref/` | Templates, checklists, locked notes |
| Study/write state (optional) | `ref/project-state.yaml` | Copy from `00_orchestrator/templates/project-state.yaml`. Design + manuscript progress only. **Run keys stay in `settings.ini`.** |
| Current analysis | `<project>/<endpoint>/` or `<project>/<endpoint>/<阳性展示名>_vs_<阴性展示名>/` | One `Results{子项目}.html` / `Results{subproject}.html` ↔ one live manuscript. Manuscript numbers come only from that page. Old `{endpoint}-results.html` and `results.html` are still recognized for reading; newly written files use the new name. Unpolished: `Manuscript_<结局>_house.docx`. After a polish archive: live `Manuscript_<结局>_polished.docx`, house draft in `0del/<project>/<outcome>/`. Batch scripts scan both via `0scripts/archive/manuscript/ms_paths.py` (skip `0del`; prefer `*_polished.docx` if both exist). Pairwise always nests under the outcome folder; pair folder uses display names. |

| Project-level QC | `<project>/ref/qc.html` | Main QC is `<project>/ref/qc.html`. External QC is `<project>/ref/qc-ext-*.html` (the filename is never `qc.html`). Console「整体 QC」or pipeline start. Combined workbook + imaging QC. Grouping / subgroup → `04_analysis/personal/0rad-pipeline-rules.md`. |

Same folder, multiple manuscripts: keep the latest that matches the current HTML; archive the rest to `0del` only if the user asks.

## Named entry points (do not vendor `.py`)

- **Stats:** `python -m modules.pipeline` (`PYTHONPATH=D:\0Grok\0scripts`). Per-project `ref/settings.ini` + console HTML; algorithms stay in **gold** `modules`. Other `0scripts` folders do not run the stats engine.
- **STROBE Figure 1:** `figure_strobe_flow.py` is duplicated in `modules/stats` and `0scripts/archive/manuscript`. Drawing code stays local, not in git. Point at `python -m modules.stats.figure_strobe_flow`. Do not copy the `.py` into this skill. Figure 1 is the single study flowchart read from Materials and Methods. Training Cohort and Test Cohort sit on one row. Validation Cohort joins that row only when Methods states an external cohort. Steps are drawn only when Methods names them. Layout rules: `05_manuscript/personal/Aitor-format.md` (Figure 1).
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

## Console vs settings / `sync_modules`

Canonical layout (enforced by `D:\0Grok\0scripts\sync\sync_modules.py`, 2026-09-04):

- Each project keeps **console** (`{project}.html`) + **`ref/settings.ini`** only for run config.
- Algorithms always come from gold `D:\0Grok\0scripts\modules`. Do **not** leave a per-project `modules/` or a lasting `config/settings.py` tree.
- CLI: default dry-run; `--apply` writes; `--check`; `--keys` appends shared knobs (`MODULES_DIR`, `DO_SURVIVAL`, `PAIRWISE_*`, …).
- Typical plan actions: `settings.py` → `ref/settings.ini`, remove project `config/`, refresh console HTML, drop legacy `console.html` / `run.bat` / `strobe-flowchart/`, rename `PBG` → `PNG` when present.

`{project}.html` / console overlay overrides ini for that run; write-back updates `ref/settings.ini`. Command-line without overlay reads ini / migrated settings only.

`CLIN_ID_COL` may equal `LABEL_COL` (ID is the grouping field). Do not invent a second ID column.



## Console UX

- Key bindings and UX details are authoritative in `04_analysis/personal/0rad-pipeline-rules.md` (Console keys); layout rules below.
- Boolean switches share one row with same-zone dropdowns: multi-column, left-aligned — do **not** stack switches as many vertical rows.
- Selected chips sit **above** the “add from data” dropdown.
- Do **not** mark “hot” items with red asterisks or red bold.

## Coding

Same as `code-refactoring/`: CONFIG on top, dry-run for bulk IO, checkpoint resume. Shared library: `D:\0Grok\0scripts\modules`.
