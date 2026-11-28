---
name: "preprocess-imaging"
domain: "02_data-processing"
trigger: ["DICOM", "NIfTI", "nii", "读图", "格式转换", "ROI QC", "mask QC", "读片协议", "reader protocol", "ICC", "Dice", "mask geometry", "habitat", "生境", "配准", "delta-habitat"]
inputs: ["images", "masks", "reader_logs"]
outputs: ["volume_or_series", "qc_report"]
tools: ["pydicom", "SimpleITK", "nibabel"]
quality_control: "geometry match before features; ICC/Dice on training subset only"
owner: "02_data-processing/base/preprocess-imaging/MODULE.md"
---

trigger is documentation only; not independently discoverable.

# Imaging I/O and ROI/reader QC

Contract only for preprocess-imaging: scope, bans, phase names, and pointers. The house working method and the revision authority live in `02_data-processing/advanced/analysis/pipeline.md`; pack data (`references/`, `scripts/`) stays beside it as data.

Covers volumetric **I/O** (DICOM/NIfTI read, convert, organise, geometry preserve) and **ROI / reader / mask QC** before radiomics or modelling. Absorbed former fine id `imaging-io` (retired name, not a runtime id). This pack does **not** translate papers and does **not** launch a bilingual reader. Full-text retrieve is `lit-search`.

## When to use

- Read, convert, or organise DICOM series / NIfTI volumes
- Who segmented, with what experience, blinded to what?
- Do image and mask share spacing / origin / direction / dimensions?
- Inter- and intra-observer ICC, Dice, Hausdorff on a pre-specified subset?
- Which lesion, 2D vs 3D, peritumoral ring, habitat sub-region?
- Longitudinal pair: register follow-up to baseline, define habitats at baseline, propagate, then Δ?

## When to open extra files

| File | Open when |
|---|---|
| [references/acquisition-and-parametric-maps.md](references/acquisition-and-parametric-maps.md) | PACS export → patient folder, DICOM series grouping/splitting, DKI/IVIM maps, radiomics extractor settings, DPABI batch |
| [references/data.md](references/data.md) | Imaging formats, labels, masks, privacy, repositories, availability wording |
| [references/reader-protocol.md](references/reader-protocol.md) | Number of readers, blinding, independent vs consensus, adjudication |
| [references/mask-geometry.md](references/mask-geometry.md) | Spacing/origin/direction mismatch; DICOM to NIfTI flips; mask resample |
| [references/reproducibility-qc.md](references/reproducibility-qc.md) | ICC / Dice / HD95; feature-stability filter before selection |
| [references/lesion-selection.md](references/lesion-selection.md) | 2D vs 3D, index lesion, multi-lesion rule, peritumoral ring |
| [references/delta-habitat-radiomics.md](references/delta-habitat-radiomics.md) | Longitudinal pair: registration gates, baseline-defined habitats, mask/label propagation, Δ features |

## Workflow

### Phase A - I/O (former imaging-io)

1. **Identify** the input: DICOM series, NIfTI/NII, or mixed.
2. **Read** with a named library (pydicom, SimpleITK, nibabel). Record software + version.
3. **Preserve geometry** - spacing, origin, direction, slice order. Do not silently flip axes.
4. **Convert** only when asked. After DICOM to NIfTI, overlay or print geometry vs the source.
5. **Organise** one volume per series (or BIDS-like layout if the user wants it). Log unmatched files.

### Phase B - ROI / reader / mask QC

6. **Inventory** modality, software, mask format (NIfTI / DICOM-SEG / RTSTRUCT), intended ROI.
7. **Geometry QC** (`mask-geometry.md`) - assert image/mask invariants; overlay a sample; nearest-neighbour mask resample only.
8. **Reader protocol** (`reader-protocol.md`) - blinded readers on a reproducibility subset; define the analysis mask provenance.
9. **Reproducibility** (`reproducibility-qc.md`) - ICC/Dice/HD on that subset, **training only**; drop unstable features before selection.
10. **Lesion rule** (`lesion-selection.md`) - pre-specify index lesion / aggregation; do not change it after seeing AUC.
11. **Hand off** feature extraction / habitat clustering - `stats-analysis`. Do not fit models here.

### Phase C - Longitudinal (delta-habitat)

12. **Register** follow-up onto baseline on the original grayscale images (affine 12 DOF, then
    deformable) and pass the four gates — DSC, Hausdorff, Jacobian, visual — before any feature.
13. **Define habitats at baseline**, pick K by ≥3 agreeing methods, then **propagate** labels
    nearest-neighbour; verify per-habitat volume change <30% and inter-habitat DSC <0.1.
14. **Δ features** per matched habitat from identically extracted ROI features; hand the Δ table to
    `stats-analysis`. Recipe: [`references/delta-habitat-radiomics.md`](references/delta-habitat-radiomics.md).

## Output contract

- Volume or series path(s) with software/version and geometry note when I/O ran.
- Geometry pass/fail per case (or sampled subset) with the mismatch named.
- Reader protocol sentence (n readers, seniority, blinding, consensus rule, software).
- Reproducibility metrics and the pre-specified ICC threshold, with how many features survived.
- No invented n, ICC, or Dice. Paper translation is out of scope.

## House layout and conversion (disk contract)

Leaf layout and DICOM→NIfTI rules for this lab. Do not vendor scripts here; implementations live in `{code_root}` when reusable.

- A raw leaf has only two trees: `img\<sample>\` and `roi\<sample>\` (multiple segs for one case stay in the same `roi` folder). Do not colocate `img` and `roi` files in one folder.
- Forms: raw DICOM, or NIfTI converted from DICOM (counts as raw). After conversion, nii lands in `img\<sample>\`, the source DICOM moves to `{DEL}` in the same batch with a ledger, and the raw volume does not keep both.
- If the same sample has thin and thick series, **keep only the thin series** (smallest slice thickness that still matches `roi\`); move thick series to `{DEL}`.
- Do not keep localizers or secondary reconstructions (scout / topogram / localizer / MIP / MPR, and similar). Recover them from `{DEL}` or the processed volume only when needed.
- `DICOMDIR` and disc sidecar files stay with the DICOM tree; move loose text, inventories, and scripts out of the leaf.
- One leaf may be shared by several projects; express the share at the leaf, do not copy a second tree.
- Unmatched files go to the family `_unmatched\img\` and `_unmatched\roi\`, with `needs_owner=1` on the ledger.

### Dedup pointers when the filesystem cannot hard-link

- The dedup unit is `(leaf, sample, modality)`; `img` and `roi` are judged as a pair. Identical sha256 keeps one canonical leaf.
- If the filesystem cannot create hard links, symbolic links, or junctions, use a `_links.tsv` pointer table; do not pretend a filesystem link exists.
- Dedup keys must be **file-level** paths, never the sample key alone (that would collapse multiple files in one folder).
- Generate cheaply: group by byte size first, hash only same-size candidates, reuse a hash cache.
- Tools must resolve the pointer table before reading images; a missing table or a missing canonical target fails loud, with no silent fallback. Live pointers still must not point into `{DEL}`.

### Multicentre series queues

For one disease, several centres, and several modalities in a retrospective queue:

1. Split by `center` × `modality`. Each cell is its own subgroup; do not pool across subgroups for stats or models unless the comparison is declared.
2. Sample key: `<prefix>_<MOD>_<CENTER>_NNNN`. The key is the path and table primary key; it carries no name, record number, or non-ASCII.
3. Keep every study as its own row (salted hash to link the same person). Do not drop follow-up exams at ingest; pick baseline or index lesion only in the analysis plan.
4. CT and MRI of the same person are two studies, two rows, same hash; do not merge images or label sources.
5. Internal training and external validation are separate leaves and separate books; an external-validation leaf must not be merged back into the training leaf.
6. Each project has its own `combined.csv`; multicentre projects do not share one book; CT and MRI are curated separately.
7. Pairing gate: clinical-table study UIDs must match image folder names 1:1. A row only in the table, or a folder only on disk, stops the run. Do not guess or fuzzy-match; pairing must be 100%.
8. Multi-subtype queues use integer codes plus a standalone dictionary; freeze codes after the pathology side confirms them. Derived labels must record `label_source`.
9. PHI stays in the on-machine family library. Project tables, paths, and ledgers use the sample key or hash only.

### DICOM → nii ledger

- Folder shape: `img\<sample>\<MOD>_s<NN>_image.nii.gz`. `<MOD>` is the DICOM Modality value (`CT` / `MR`); `<NN>` is `SeriesNumber` zero-padded to two digits. No non-ASCII and no spaces in paths.
- Batches with masks use `<SEQ>_image` + `<SEQ>_label`; `<SEQ>` is an ASCII readable name (for example `CT_plain` / `CT_arterial`), never the series number as the human-readable name.
- Each case folder carries `_series.tsv` (one row per series: UID, description, geometry, nii bytes and sha256, source directory, status). That file is the only authority for that case's DICOM information.
- Use SimpleITK `ImageSeriesReader` in **multiple processes**. Do not share GDCM across threads (that combination has been observed to hang). Resume by skipping existing targets and filling gaps only.
- Failures do not write a fake file: record `status=fail` and the reason; do not skip silently.
- If `SeriesNumber` repeats inside a study, disambiguate the series name; never overwrite an existing file.

**MRI filter (this is the rule):** classify first by `SeriesDescription`. Keep a whitelist such as
`t1` / `t2` / `dwi` / `adc` / `dixon` / `dynamic_ce` / `other`. The blacklist is not converted to
nii and is recorded only in the census: localizers / SURVEY / scout, registration-derived series,
MRCP and overly thick single slices, empty descriptions, and secondary reconstructions (description
contains `Range` / `MPR` / `MIP` and is not an original series). Convert the whole whitelist,
including multiple b-values in one case. Changing either list requires a rerun of the census and a
rule sync. Do not write a "convert every series" policy.

**CT has no description filter:** convert every phase. Still do not convert reconstructed series.

### Parameters, compression, and pairing traps

- Protocol fingerprint = device + series name + stable protocol fields (slice thickness × kernel × reconstruction matrix × pitch). Using every header field fragments the fingerprint.
- Coverage tiers: T1 complete parameters / T2 geometry only / T3 header emptied. T3 must not support field-strength, model, or kVp conclusions.
- CT cases often have several reconstructed thicknesses; fix one before analysis, or the same case is counted twice.
- Coexisting 1.5 T and 3.0 T MR must be stratified. XR kVp is a continuous exposure; record a range, do not use it as a primary key.
- nii→gz is accepted only as "gzip level 6 + decompressed sha256 matches the source"; on mismatch delete the gz and record an error. Never delete the source before the compressed copy verifies.
- Single-frame or geometry-less DICOM uses a dedicated fallback; do not patch headers by hand.
- 8-bit lossy images are for viewing or model input only; quantitative work still uses the original DICOM / nii.
- Same name and same fingerprint do not mean the same person: ingest on PatientID + StudyInstanceUID, and re-check UIDs rather than assuming an ID is unique.
- `ROI` / `label` are located by their folder: splitting them from the series folder breaks pairing. A real split needs a same-relative-directory pairing key in the tool first.
- Mixed vendors in one leaf must be stratified before any cross-scanner merge.
- A nii / nrrd leaf with no DICOM cannot yield scan parameters; parameters come from DICOM only.
- Broken objects (DICM magic but no pixels) cannot be converted; isolate them and record FAIL.
- `INCOMING` is an external delivery tree, read-only, and does not enter triage.

## Data availability

Imaging formats, labels, masks, privacy, repositories, and availability wording:
[data.md](references/data.md). That file is **not** the `clean-data` clinical-Excel front.

Clinical Excel/CSV (headers, missingness, ID, cohort) - `clean-data`.

Backup sources (not vendored): Scientific `pydicom` / `bids` / `imaging-data-commons`.

## Handoffs

- Clinical Excel/CSV - `clean-data`
- Radiomics / habitat / leakage - `stats-analysis`
- Modelling / calibration - `model-evaluation`
