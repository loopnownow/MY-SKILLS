# Feature extraction

Produce a documented, versioned feature matrix that another lab could regenerate.

**Engine (these trees):** Pictologics `RadiomicsPipeline` with `load_standard=True` and
`RADIOMICS["config_names"] = ["standard_fbn_32", "standard_fbs_16"]`.

- `standard_fbn_32` — IBSI fixed bin **number**, 32 bins (typical MRI / already-normalised).
- `standard_fbs_16` — IBSI fixed bin **size**, bin width = range / 16 (typical HU-windowed CT).

The two configs are **complementary**; both trees run them together. Conversion is
`sitk_to_pictologics` then `pipeline.run(...)`.

**Must not** describe this engine as PyRadiomics, and **must not** route extraction through
`0scripts/organized/radiomics_ops.py`.

## sitk_to_pictologics (Spacing / Origin axes flip)

SimpleITK `GetArrayFromImage` is `(Z, Y, X)`. Pictologics `Image.array` is also `(Z, Y, X)` —
**no array transpose**. Spacing and Origin are the opposite axis order, so flip them:

```text
spacing_zyx = tuple(reversed(sitk_image.GetSpacing()))
origin_zyx  = tuple(reversed(sitk_image.GetOrigin()))
```

Pictologics modality field wants `"MR"` not `"MRI"` (habitat tree maps this inside
`sitk_to_pictologics`).

## Two column-name formulas (keep separate)

Do **not** unify these. Habitat×sequence fusion and delta flattening use different prefixes on
purpose.

### 1) `habitat_pipeline` (`extract_features_single_habitat_sequence` → `aggregate_cohort_features`)

Per Habitat × sequence extraction **does not** put `h{idx}_` on the column (that prefix used to
make same-patient habitat rows mis-align into NaNs):

```text
{sequence}_{config_name}_{feature_name}
# e.g. CT_arterial_standard_fbn_32_intensity_mean
```

`aggregate_cohort_features` flattens Habitat rows to one patient row by prefixing **once**:

```text
h{H}_{sequence}_{config_name}_{feature_name}
# e.g. h0_CT_arterial_standard_fbn_32_intensity_mean
```

### 2) `delta_habitat_pipeline` (`extract_features_single_habitat` → `compute_delta_features` → `aggregate_delta_features`)

Per-habitat extraction **does** prefix habitat id:

```text
h{habitat_idx}_{config_name}_{feature_name}
# e.g. h0_standard_fbn_32_intensity_mean
```

Delta columns (`DELTA["compute_absolute"]` / `compute_relative`; rate if `--delta_t`):

```text
delta_abs_{name}
delta_pct_{name}
delta_rate_{name}
```

Cohort flatten:

```text
h{H}_{delta_feature_name}
# e.g. h0_delta_abs_h0_standard_fbn_32_intensity_mean
```

Relative change uses `(|f_pre| + DELTA["epsilon"])` in the denominator. Habitat correspondence
across timepoints is `propagate_masks`, not a second clustering.

## Feature families (IBSI nomenclature)

| Family | Captures |
|---|---|
| **First-order / intensity** | Histogram statistics (mean, entropy, skewness, kurtosis) |
| **Shape (2D/3D)** | Volume, surface area, sphericity, elongation — independent of intensity |
| **GLCM** | Gray-level co-occurrence (texture) |
| **GLRLM / GLSZM / GLDM / NGTDM** | Run-length, size-zone, dependence, neighbouring-tone-difference textures |
| **Filtered (LoG/wavelet/…)** | Any family computed on transformed images |

Pin `RADIOMICS["config_names"]`, software + Pictologics version, and the live tree path. Share
those with CLEAR.

## Aggregation

- 3D extraction inside each habitat mask; skip / error when voxel count `< HABITAT["min_voxels"]`.
- Per-region labels must stay traceable via the formulas above — do not invent a third scheme.

## Output: the feature matrix

- Rows = patients after cohort flatten; columns = features with the tree-specific names.
- Carry IDs that map to the data dictionary (→ radiology-data).
- Version it; record which tree (`habitat_pipeline` vs `delta_habitat_pipeline`) produced it.

## Delta / longitudinal radiomics

When the question is **change**, use **flow 2** (`delta_habitat_pipeline`), not an after-the-fact
subtraction on flow-1 tables:

- Identical Pictologics configs at pre and post (`standard_fbn_32` + `standard_fbs_16`).
- Cluster **baseline only**; `propagate_masks` to post; never re-cluster post
  (`habitat-radiomics.md`).
- `compute_delta_features`: absolute `f_post - f_pre`, relative percent, optional per-day rate.
  **No Z-score here** (`leakage-audit.md`).
- Relative change is undefined near zero-valued baseline features — epsilon is already in
  `DELTA["epsilon"]`; still flag infinities if they appear.
- Selection stays inside training (`select_features` / `selection-modelling.md`).

## Test–retest / phantom repeatability

ICC is **not** implemented in either habitat tree. Point to `modules/utils/u_icc.py` (clinical
pipeline), not a habitat-local ICC helper (`leakage-audit.md`).

`../../imaging-preprocessing-qc/references/reproducibility-qc.md` covers **segmentation**
reproducibility. Phantom / test–retest of the **feature value** is the complementary check.

- Drop low-repeatability features **before** selection/modelling, inside training only.
- This is a scored RQS/RQS 2.0 item — reporting "not performed, and why" is stronger than silence
  (→ `../../../../05_manuscript/bundles/manuscript-core/references/merged/radiology-reporting/clear-metrics-rqs.md`).

## Reporting sentence

*"For each habitat, IBSI-complementary features were extracted with Pictologics RadiomicsPipeline
using standard_fbn_32 and standard_fbs_16 after sitk_to_pictologics (Spacing/Origin axes flip).
Single-timepoint columns follow {sequence}_{config}_{feature} then h{H}_ flatten; delta columns
follow h{idx}_{config}_{feature} then delta_abs_/delta_pct_ flatten. Software version and config
names are recorded."*
