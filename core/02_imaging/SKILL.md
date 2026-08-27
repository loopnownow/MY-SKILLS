---
name: medical-imaging-and-radiomics
description: >
  Imaging and radiomics methods (not the stats HTML). Use for 图像, 图像处理,
  DICOM, NIfTI, 分割, 配准, fMRI, IBSI/PyRadiomics, habitat.
  Integrates preprocessing/QC and radiomics-habitat. Radiogenomics design → 03_research.
  Clinical translation / reader studies → clinical-translation. Do not use for 统计, 插补, or 写论著.
  组学 as a whole project → 00_orchestrator.
---

# Medical Imaging and Radiomics (integrated)

## Purpose

Reproducible clinical/research imaging. Priority:

**acquisition metadata → file integrity → preprocessing → QC → features → stats/model → reproducibility**

Statistical modeling itself → hand off to `04_analysis`. Prose → `05_manuscript`. Pre-review / reviewer response → `06_review`.

## Capability map

| Task | Path |
|------|------|
| **Methods design router** | `bundles/imaging-preprocessing-qc/MODULE.md` |
| · annotation | `bundles/imaging-preprocessing-qc/` |
| · radiomics (IBSI) | `bundles/radiomics-habitat/` + `references/radiology/radiomics.md` |
| · bilingual paper reader | `bundles/imaging-preprocessing-qc/` |
| Pipeline coding (habitat, ROI match, ML port) | `bundles/radiomics-habitat/MODULE.md` |
| Habitat / radiomics pipeline scripts | `bundles/radiomics-habitat/scripts/` |
| fMRI SPM/CAT12/DPABI | `bundles/imaging-preprocessing-qc/MODULE.md` |
| Leakage / split scripts | `scripts/radiology-skills/` |
| Manuscript figures / figure standards | `../05_manuscript/bundles/figure-engine/` |
| Radiogenomics design | `03_research` |
| Clinical translation / reader studies | `archive/clinical-translation` |

## General workflow

1. Confirm modality, sequence, scanner, acquisition, design.
2. Validate files and subject IDs.
3. Preprocessing parameters before batch.
4. Versioned software; objective QC.
5. Documented feature definitions; ID-align with clinical data.
6. Hand quantitative features to `04_analysis`.
7. Keep logs and parameter files.

## Radiomics mode

harmonization/resampling → intensity → ROI/VOI → segmentation QC → extraction → reproducibility (ICC) → reduction → modeling → validation.

Check voxel size, interpolation, discretization, bin width, IBSI/PyRadiomics, observer ICC, batch effects.

**Do not** run feature selection on the full dataset before validation.  
Deep design: `bundles/radiomics-habitat/`.

## Pipeline coding conventions (with `code-refactoring`)

1. Fully soft-coded CONFIG at top of file.
2. Modular, independently runnable modules.
3. Fresh heavy comments (especially on ports).
4. Deliver complete scripts; flag R↔Python behavioral caveats.

See `bundles/radiomics-habitat/` and `archive/code-refactoring`.  
0RAD `VAL_MODE` / pairwise / ID rules: `04_analysis/references/0rad-pipeline-rules.md`. Workspace: `01_automation/references/0rad-workspace.md`.

## rs-fMRI / structural MRI modes

rs-fMRI: slice-timing when appropriate, realignment, motion/FD, nuisance, metrics — do not blindly stack every step.  
Lab MATLAB: `bundles/imaging-preprocessing-qc/`.  
Structural/CAT12: segmentation, bias, normalization, VBM, TIV; document transforms.

## Segmentation and registration

Distinguish rigid / affine / nonlinear. Document reference space, direction, interpolation.

## Handoff to analysis

Deliver: subject-level feature table, feature definitions, preprocessing params, QC exclusions, software versions, transform/extraction logs, unresolved imaging limitations.

## Progressive disclosure

Only this top-level skill is auto-discovered. Load `bundles/*/MODULE.md` as needed. Nested modules are **not** separate skills.
