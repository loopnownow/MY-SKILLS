# Multi-Parametric Habitat Radiomics

Two **mutually exclusive** live trees. Do not vendor `.py` / NIfTI / CSV into this skill; point at
the trees and call the functions below.

| Tree | Role | CLI |
|---|---|---|
| `D:\0Grok\0RAD\0scripts\habitat_pipeline` | Multiparametric **single timepoint** | `python pipeline.py --data <csv> --labels <csv>` |
| `D:\0Grok\0RAD\0scripts\delta_habitat_pipeline` | Longitudinal **delta** | `python pipeline.py --data <csv> --labels <csv> --delta_t <days>` |

Shared module names (`config.py`, `data_loader.py`, `preprocessing.py`, `registration.py`,
`habitat.py`, `radiomics.py`, `pipeline.py`) do **not** make the flows interchangeable. Habitat
IDs and downstream columns are not comparable across the two paradigms.

Engine for Habitat×sequence (or Habitat×timepoint) features: **Pictologics**
`RadiomicsPipeline` — see `feature-extraction.md`. Not PyRadiomics.

## Flow 1 — `habitat_pipeline` (single timepoint, multi-sequence)

`python pipeline.py --data … --labels …` → `run_pipeline`.

1. **Align** — `align_patient_sequences`: per-sequence `preprocess_sequence` (via
   `resolve_preproc_settings`), then `register_all_sequences` of non-reference series onto the
   `is_reference` sequence (ROI lives in reference space).
2. **Full-cohort model** — `CohortHabitatModel` (`HABITAT["cohort_mode"]` True, recommended):
   pool voxel/superpixel features, fit one Scaler→PCA→KMeans, `predict` per patient.
   `HABITAT["cohort_mode"]` False skips the global model: each patient runs local `optimize_k` /
   `build_habitats`. **Without the global model, habitat IDs are not comparable across patients.**
3. **Pictologics** — `process_patient_habitat_and_radiomics` →
   `extract_features_all_habitats` / `extract_features_single_habitat_sequence`
   (Habitat × sequence).
4. **Selection** — `run_cohort_aggregation` → `aggregate_cohort_features` → train-only
   `select_features` (when `--labels` is present).

Voxel-fusion channels (`VOXEL_FEATURES` / `compute_voxel_feature_maps` /
`compute_parametric_maps`):

| Channel | Config switch | Notes |
|---|---|---|
| Intensity | `use_intensity` | Raw intensities; `intensity_sequences` `"all"` or a list |
| Parametric maps | `use_parametric_map` | Rules in `PARAMETRIC_MAPS` (`direct` / `absolute_change` / `relative_change` / `ratio`) |
| Local texture | `use_local_texture` | Window mean / variance / entropy |
| Gradient | `use_gradient` | First-order gradient magnitude |
| LoG / wavelet | `use_log` / `use_wavelet` | Optional; default off / off in this tree |
| Superpixel | `HABITAT["use_superpixel"]` | Optional SLIC (`compute_superpixel_segmentation`, `aggregate_by_superpixel`); default False |

Registration QC in this tree is **soft mutual information** (`REGISTRATION["qc_metric"]` =
`mattes_mutual_information`, `qc_hard_fail` False). Non-reference series usually have no ROI, so
Dice/Hausdorff is not the gate. See Registration QC below.

## Flow 2 — `delta_habitat_pipeline` (longitudinal)

`python pipeline.py --data … --labels … --delta_t …` → `run_pipeline` / `process_single_patient`.
`--delta_t` (days) enables `delta_rate_` columns in `compute_delta_features`.

**Cluster baseline ONLY.** `build_habitats` / `CohortHabitatModel` run on **pre** (`t1`) image +
ROI. Post habitats come from `registration.propagate_masks` (ANTs forward transform of baseline
habitat masks onto the registered post image). **Never re-cluster post.**

`propagate_masks` is the source of truth for post habitat identity. HTML / comments that say
"remove mask propagation" / "方案 A，删除传播" are **wrong** — do not follow them (see
`roi-processing.md`).

`load_patient_pairs` expects **1 pre + 1 post**, each with an ROI. Global model still recommended:
without `CohortHabitatModel`, habitat IDs are not comparable across patients. Validation reuse:
`utility/validate_delta_habitat.py` (`apply_global_habitat`, `propagate_masks_val`).

Delta features: `compute_delta_features` then `aggregate_delta_features`. Absolute / relative
(and rate if `--delta_t`) — no Z-score at this step (`leakage-audit.md`).

Registration QC in this tree is **hard Dice + Hausdorff** (`compute_registration_qc` after
`register_images`). Follow the **live config value**, not the comment.

## K selection (both trees)

`habitat.optimize_k` combines:

- Elbow (`_elbow_optimal_k`)
- Silhouette (`_silhouette_optimal_k`)
- Consensus ARI (`_consensus_optimal_k`)

Stability gate: `HABITAT["ari_threshold"]` (live default `0.70`). Candidate range is
`HABITAT["k_range"]`. Do not hard-code K in function bodies.

## Function map (names only)

**habitat_pipeline:** `load_patient_data`; `preprocess_sequence`, `resolve_preproc_settings`;
`register_all_sequences`, `compute_registration_qc`; `CohortHabitatModel`,
`compute_parametric_maps`, `compute_voxel_feature_maps`, `compute_superpixel_segmentation`,
`optimize_k`, `build_habitats`, `build_habitat_masks`; `sitk_to_pictologics`,
`extract_features_single_habitat_sequence`, `extract_features_all_habitats`,
`aggregate_cohort_features`, `select_features`; `align_patient_sequences`,
`process_patient_habitat_and_radiomics`, `run_pipeline`, `run_cohort_aggregation`.

**delta_habitat_pipeline:** `load_patient_pairs`; `preprocess`; `register_images`,
`compute_registration_qc`, `propagate_masks`; `CohortHabitatModel`,
`compute_voxel_feature_maps`, `optimize_k`, `build_habitats`; `sitk_to_pictologics`,
`extract_features_single_habitat`, `extract_features_all_habitats`, `compute_delta_features`,
`aggregate_delta_features`, `select_features`; `process_single_patient`, `run_pipeline`,
`run_cohort_aggregation`.

Filename matching helper (habitat tree only): `utility/match_img_ior_updated.py` — **filename**
pairing, not HIS (`roi-processing.md`).

Do **not** treat `utility/LASSO.py` as the stats library (`selection-modelling.md`).

## Registration QC (follow code, flag comments)

| Tree | QC | Live gate | Comment to flag |
|---|---|---|---|
| `habitat_pipeline` | **Soft MI** inside the reference ROI | `qc_metric` = `mattes_mutual_information`; `qc_min_similarity` = `0.10`; `qc_hard_fail` = **False** (warn, do not skip) | Soft by design — no second mask |
| `delta_habitat_pipeline` | **Hard Dice + Hausdorff** | `REGISTRATION["qc_dice_threshold"]` = **`0.10`**; `qc_hausdorff_threshold` = `5.0` mm | Comments / docstring still say Dice ≥ **0.85**. **Follow the live `0.10`.** Flag the stale 0.85 comment when editing. |

## Known pitfalls

1. Mixing the two trees (delta clustering on post; single-timepoint MI QC copied into delta).
2. Re-clustering post instead of `propagate_masks`.
3. `cohort_mode` False then treating habitat IDs as cohort-wide labels.
4. Habitat cluster count not read from `HABITAT["k_range"]` / `optimize_k`.
5. Feature extraction on whole-tumor mask after a per-habitat refactor (or the reverse).
6. Normalisation applied before vs after registration inconsistently.
7. Trusting HTML that says "remove mask propagation".
8. Calling the extractor PyRadiomics.

## Documentation deliverables

If the user asks for supporting documentation (not just code), prior work in this domain has included:
a technical operations manual, a validation script + report, a bug-fix log, and a merged HTML user
manual. Offer these as optional add-ons rather than assuming they're wanted for every request.
