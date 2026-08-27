# 数据

Use this file for imaging data formats, labels, masks, privacy, repositories, and
availability statements.

## Data inventory

Track:

- DICOM, NIfTI, PNG/JPEG, DICOM-SEG, RTSTRUCT, masks, feature CSV, clinical table
- patient ID, study ID, series ID, lesion ID, timepoint
- modality and scanner/protocol metadata
- label source and label date
- segmentation source, reader role, consensus, quality control
- train/validation/test assignment
- derived features and model outputs

## Sharing and privacy

- Do not promise public sharing of identifiable or re-identifiable clinical imaging data.
- Prefer de-identified data, metadata, code, feature tables, trained weights, or controlled
  access routes when raw images cannot be public.
- State restrictions: consent, ethics, law, third-party ownership, hospital policy, or
  data-use agreement.
- Keep data, code, model weights, and protocols separate unless the journal asks for a
  combined statement.

## Availability pattern

```text
The de-identified [data type] supporting this study are [available/restricted] because
[reason]. [Public metadata/feature tables/source data/code/model weights] are available
at [repository/identifier] where applicable. Access to restricted clinical imaging data
requires [committee/institution/procedure] and [approval/agreement].
```

Do not invent repository identifiers or ethics approvals.
