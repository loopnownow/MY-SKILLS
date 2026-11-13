# Longitudinal delta-habitat radiomics

Recipe for a tumour imaged at two or more timepoints when sub-regions (habitats) must correspond
across timepoints so that per-habitat ROI features can be differenced (Δ). Image I/O and mask
geometry rules stay in [MODULE.md](../MODULE.md) and
[mask-geometry.md](mask-geometry.md); this file covers registration, habitat definition and
propagation.

## 1 Seven stages

1. Preprocess — one target grid, intensity normalisation.
2. Non-rigid registration of the follow-up onto the baseline.
3. Voxel-level feature map (baseline only).
4. Habitat partition (clustering at baseline).
5. Mask and habitat-label propagation to the follow-up.
6. ROI-level feature extraction at each timepoint.
7. Δ features → model / validation.

The order is the contract: habitats are defined once, at baseline, and propagated. Do not re-define
them per timepoint (§7).

## 2 Resampling and intensity

- One grid for the whole study: **1×1×1 mm³**, B-Spline interpolation. Voxel-size differences alone
  can move the same tumour's GLCM entropy by >20%, so a mixed grid makes Δ meaningless.
- MRI: N4 bias correction is mandatory. CT: intensities are absolute HU and N4 is normally skipped,
  because it destroys the HU meaning.
- Record software, version, interpolation and target grid; the geometry gate runs before any feature.

## 3 Registration

- Register the **original grayscale** images, optionally weighted by the ROI mask. Registering only
  the ROI mask is a hard error: a binary mask has poor gradient support, the deformation field goes
  wrong, and DSC can look acceptable at the surface while the interior is misaligned.
- Two stages: affine (12 DOF, mutual information) to millimetre level, then deformable (B-Spline or
  ANTs SyN). B-Spline control points 6–10, about 15–25 mm spacing — finer is more precise but
  over-fits the deformation.
- Four gates per pair:
  - DSC >0.85 pass, <0.75 fail.
  - Hausdorff distance <5 mm.
  - Jacobian determinant >0 everywhere (≤0 means folding / broken topology).
  - Checkerboard or overlay visual check.

## 4 Voxel-level feature maps (baseline only)

- 3–5 voxel windows: local mean / variance / entropy.
- Laplacian-of-Gaussian, σ = 1 mm and 3 mm.
- 3D wavelet sub-band energy.
- Multimodal channels (SUV / ADC / Ktrans).
- Per-dimension Z-score with training-set parameters.
- More than 5 channels: PCA, keep cumulative explained variance ≥95%.

Voxel-level feature maps are **not** IBSI-compliant; ROI-level features are. Never report one as the
other.

## 5 Habitat partition

- K is not fixed a priori. Candidate range 2–8.
- Choose K by agreement of at least 3 methods — elbow, silhouette, gap statistic, consensus
  clustering; the chosen K is typically 3–5.
- Record K, seed, distance metric, feature set, and Z-score parameters.

## 6 Propagation

- Nearest neighbour only for categorical habitat labels; linear interpolation produces fractional
  labels (0.4 / 1.6) that are not habitats.
- After propagation: per-habitat volume change <30%, inter-habitat DSC <0.1, visual overlay.
- A volume change >30% or inter-habitat DSC ≥0.1 means registration failure or unstable habitats.
  Fix it; do not compute Δ on top of it.

## 7 Δ-feature strategy

| Strategy | What it does | Use |
|---|---|---|
| A — independent clustering per timepoint | "habitat 1" at t1 and t2 are different tissue, so Δ has no biological meaning | not usable for Δ |
| B — joint clustering on concatenated timepoints | one common space, but timepoints influence each other | acceptable, weaker |
| C — define at baseline, propagate | Δ is per matched habitat | recommended |

## 8 QC checklist (all must pass)

1. Four registration gates passed on every pair.
2. K chosen by ≥3 agreeing methods; ARI between methods >0.8.
3. No single habitat covers >80% of voxels; every habitat has >100 voxels.
4. ComBat (scanner / centre) fitted inside the training set only.
5. ICC >0.75 on the reproducibility subset, training only.
6. ROI features extracted with identical settings at both timepoints.
7. Δ computed between the same habitat index at both timepoints.
8. Z-score / normalisation parameters taken from training only.
9. |Δ%| >500% triggers a denominator check (zero or near-zero baseline value).
10. Every Δ row traceable to its pair of source rows (no averaged or re-derived values).

## 9 Handoffs

ROI features and the Δ table → `stats-analysis` (habitat clustering code lives there); modelling and
calibration → `model-evaluation`. This file defines the imaging steps only.
