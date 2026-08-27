# SOP: radiomics-study

**Owner:** `00_orchestrator`. Cross-skill only. Modeling / LASSO / ROC / DCA stay in `04_analysis`.

Use when the user picks this SOP, or says 组学全线 / habitat 流程 / 从图像到模型（且选了本 SOP）。

If `ref/project-state.yaml` is missing, copy `../templates/project-state.yaml` into the project `ref/` and fill only what the user stated. Do not invent ethics or n.

## Sequence

1. **Workspace (01_automation)** — folder names, `exc` first, ID align. `0rad-workspace.md`.
2. **Methods design (02_imaging)** — `imaging-preprocessing-qc` for ROI/QC, then `radiomics-habitat` for IBSI/radiomics/habitat.
3. **Feature matrix (02_imaging toolkit)** — extraction / habitat scripts. Hand a patient-level table to `04_analysis`. No feature selection on the full cohort.
4. **Impute + pipeline (04_analysis)** — drop >50% missing; `u_impute`; `python -m modules.pipeline`. `VAL_MODE` and columns only from `settings.ini`.
5. **Stop for numbers** — one `*-results.html` per endpoint. Do not write a manuscript in this SOP unless the user also picks `sci-manuscript`.

## Do not

- Restore archived DICOM batch / DL packs.
- Put DCA/nomogram code in `02_imaging`.
- Re-select features on the test set.

## Next

Offer `sci-manuscript` if HTML exists.
