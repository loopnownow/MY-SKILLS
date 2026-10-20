---
name: "imaging-io"
domain: "02_data-processing"
trigger: ["DICOM", "NIfTI", "nii", "读图", "格式转换"]
outputs: ["volume_or_series"]
owner: "02_data-processing/base/imaging-io/MODULE.md"
---

# CT/MRI I/O (DICOM / NIfTI)

Read, convert, and organise volumetric series. QC / ROI / reader protocol lives in
`preprocess-imaging` (`02_data-processing/base/preprocess-imaging/`). Personal MATLAB preprocess stays in A.

## Workflow

1. **Identify** the input: DICOM series, NIfTI/NII, or mixed.
2. **Read** with a named library (pydicom, SimpleITK, nibabel). Record software + version.
3. **Preserve geometry** — spacing, origin, direction, slice order. Do not silently flip axes.
4. **Convert** only when asked. After DICOM→NIfTI, overlay or print geometry vs the source.
5. **Organise** one volume per series (or BIDS-like layout if the user wants it). Log unmatched files.
6. **Hand off** masks/readers to `preprocess-imaging` (`02_data-processing/base/preprocess-imaging/`). Do not extract radiomics here.

Backup sources (not vendored): Scientific `pydicom` / `bids` / `imaging-data-commons`; MedSci `preprocess-imaging`.

## Data availability

Imaging formats, labels, masks, privacy, repositories, and availability wording:
[data.md](references/data.md). That file is **not** the `clean-data` clinical-Excel front.

Clinical Excel/CSV (headers, missingness, ID, cohort) → `clean-data`.
