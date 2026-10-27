# SOP: statistics

**Owner:** `00_orchestrator`. Cross-skill only. Modeling / LASSO / ROC / DCA stay in `02_data-processing`.

Use when the user picks this SOP, or says radiomics full pipeline / habitat flow / imaging-to-model (and this SOP was chosen), or directory detection finds imaging/ROI without `*-results.html`.

If `ref/project-state.yaml` is missing, copy `../../00_orchestrator/templates/project-state.yaml` into the project `ref/` and fill only what the user stated. Do not invent ethics or n. Set `pipeline.sop: statistics`.

## Sequence

0. **Session fine-id pick (`00`)** — every independent run needs a fine-id pick. If `session_picked_fine_ids` already covers the fine ids this task needs, reuse the session lock. Otherwise enter 01 and ask which registry live ids to attach. `PROPOSED` is not pickable. Load only the picked ids. Do not auto-load all live ids. Advanced layers are not a fine-id pick. Gate **G0**.
1. **PHI (`N2`)** — before tables or clinical extraction. Unknown PHI → stop. Gate **G-PHI**.
2. **Workspace** — folder names, `exc` first, ID align: `{RULES}/workspace-layout.md`. Table batch stays `02_data-processing` (`clean-data` when picked this run). File check: analysis-ready table exists. Handoff `02`.
3. **Methods / prep (`02_data-processing`)** — live `preprocess-imaging` for ROI/QC (if picked), then live `stats-analysis` / `preprocess-imaging` for IBSI/radiomics/habitat **preparation** (if picked; former radiomics-ml / radiomics-habitat absorb). Advanced MATLAB: `{code_data_processing}\preprocess-imaging\fmri\parallel_preprocess.m`.
4. **Feature matrix (`02_data-processing`)** — extraction / habitat prep. Hand a patient-level table to `02_data-processing`. No feature selection on the full cohort.
5. **Missing-value handling (`02_data-processing`, live `clean-data` when picked) then pipeline (`02_data-processing`)** — drop >50% missing; `python -m modules.pipeline`. `VAL_MODE` and columns only from `settings.ini`.
6. **Stop for numbers** — one `*-results.html` per endpoint. File check + gate **G-STATS**. Do not write a manuscript in this SOP unless the user also picks `sci-manuscript` (node **N3**).

## Do not

- Rebuild DICOM batch / DL packs that are not in this repo.
- Put DCA/nomogram code in `02_data-processing`.
- Re-select features on the test set.
- Route literature through 00 to 03 (never through 05/06).
- Auto-load every registry live id.
- Invent n or AUC when HTML is missing.

## Next

Offer `sci-manuscript` if HTML exists (N3 WRITE). Copy `../../00_orchestrator/templates/handoff.yaml` as `02 → 05` when they accept.
