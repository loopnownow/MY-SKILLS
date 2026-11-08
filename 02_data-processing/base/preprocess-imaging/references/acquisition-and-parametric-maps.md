# Acquisition, series organisation, and parametric maps

Read this when the work starts **before** the ROI: PACS exports, DICOM series assembly, DWI model
fitting (DKI / IVIM), radiomics feature extraction settings, or a DPABI/DPARSF batch.

## PACS export → patient folder

- Vendor exports usually arrive as `…/<study>/DICOMDIR` + `DICOMOBJ/` (+ optional `LABEL.TXT`).
- `DICOMDIR` carries a `DirectoryRecordSequence`; the fields worth reading are
  `PATIENT` (PatientName, PatientID) and `STUDY` (StudyID, AccessionNumber).
- Two naming conventions exist in practice — **pick one and keep it for the whole project**:
  `name + PatientID + AccessionNumber + StudyID` (PACS side) or
  `name + given_name + sex + birth_date` (workstation side, which reuses `given_name` as the ID).
  Mixing them produces two folders for the same patient.
- Record the export date and converter version with the converted data.

## DICOM series: group, then split

- Group key = `SeriesInstanceUID`; ordering key = `SeriesNumber`; folder label = `SeriesDescription`.
- Read headers only (`stop_before_pixels=True`, `force=True`) — pixel loading makes large exports crawl.
- Split folder name: zero-padded series number + sanitised description (`[<>:"/\|?*]` → `_`).
- Log files that fail header parsing; do not silently drop them.

## DWI parametric maps

| Model | Computable from trace-weighted data | Needs multi-direction tensor |
|---|---|---|
| **DKI** | S0, MD, MK, ADC(b1000/b2000), non-Gaussianity, fit R² | FA, AD, RD, AK, RK, MK-tensor |
| **IVIM** | S0, D, f, D* | — |

- **DKI fit:** `ln S(b̃) = c0 − c1·b̃ + c2·b̃²` with `b̃ = b/1000` (normalise before squaring);
  `D = c1/1000` (mm²/s), `K = 6·c2/c1²`. Require `c1 > 1e-4` before reporting MK.
  Clip MK **before** deriving non-Gaussianity, otherwise near-zero `c1` voxels blow up.
- **IVIM (segmented, two steps):** high-b (`≥200 s/mm²`) log-linear OLS → `D`, `f`;
  then residual fast component on low-b only (`S/S0 − (1−f)·e^(−b·D)`, and only where `f > 0.01`) → `D*`.
- Report plausible-range clipping explicitly: MD/ADC `0–5e-3`, MK `0–3`, D `0–3e-3`, f `0–1`,
  D* `5e-3–0.3`. A clipped map is not a measured value — say so.
- Brain mask: `median_otsu` on the b0 volume (`median_radius=3`, `numpass=2`); zero outside the mask.

## Radiomics extractor settings (record verbatim in Methods)

- Feature classes: first-order, GLCM, GLRLM, GLSZM, GLDM, NGTDM.
- `binWidth = 1`, `interpolator = sitkBSpline`, `resampledPixelSpacing = [0,0,0]` (no resampling),
  `additionalInfo = false`.
- Any change to bin width, resampling, or discretisation changes every feature value — version it.

## MRI voxel-level work (habitat / delta)

- Fixed grid before everything: resample to `1×1×1 mm³` with B-spline.
- MRI: N4 bias-field correction then intensity normalisation (Z-score) — signal has no absolute scale,
  so two scans of the same patient are not comparable without it. CT has HU and skips N4.
- Voxel-level features span wildly different ranges — Z-score each channel before clustering.
- Choose the cluster number by a stated criterion (e.g. silhouette) on the **baseline** scan, then
  propagate the baseline habitat masks to follow-up; do not re-cluster each time point.
- Derived (delta) features: standardise with training-set statistics only.

## DPABI / DPARSF batch

- `DPARSF_myrun` adapts the basic struct to the advanced one and calls `DPARSFA_run`; it needs the
  version-matched `Jobmats/Template_CalculateInMNISpace_TraditionalOrder.mat` — do not reuse a `.mat`
  written by another DPABI release.
- Normalisation switch maps to preprocessing chain: `1` = no coreg/segment/DARTEL, `2` = coreg + segment,
  `3` = coreg + segment + DARTEL. Normalisation off also forces reorient/BET/auto-mask off.
- Head-motion regressors are scaled by 4 in the advanced struct; filtering runs after normalisation.
- `DPARSFA_head.mat` is editable programmatically (`loadmat(struct_as_record=False, squeeze_me=True)`;
  write back with `do_compression=False, oned_as='row'`), always `.bak` first and re-read to confirm `Cfg`.

## Cautions

- **PHI wall.** Hospital information-system scraping (intranet URLs, login flows, patient views) never
  enters shared storage, git, or these references. Keep the *procedure and field mapping* only.
- **Irreversible clean-up.** Scripts that delete "non-brain" series or move empty folders must run
  preview-first, with the file list written down before deletion.
- **Trace-weighted data cannot yield tensor metrics.** Do not report FA/AK/RK from single-direction DWI.
