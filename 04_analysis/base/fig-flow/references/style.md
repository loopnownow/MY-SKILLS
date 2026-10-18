# Type A STROBE — visual spec

How the boxes look. Rules and spec: `patient-flow.md`. Gold standard: 2023 BJR POLE Fig.1.

## Layout (top → bottom)

1. Screened / identified cohort `(n=N)`.
2. Right-hand **Inclusion criteria**; horizontal arrow **IN** to the spine (arrowhead on the spine).
3. Right-hand **Exclusion criteria**; horizontal arrow **OUT**; each reason `(n=k)`.
4. Enrolled / analyzed n plus class counts.
5. Training Cohort | Validation Cohort (written sizes). Never "Development set".
6. Stop. No pipeline / analysis row.

## Geometry

- Vertical spine left-of-center so the right column has room.
- All boxes: 1 pt black rule, square corners, white fill, regular (not bold) type. Width and height follow the text.
- Inclusion sits above exclusion on the right of the stem between screened and enrolled.
- Split boxes on one line when possible; equal height.
- Arial (or Calibri / Helvetica / DejaVu Sans). No grey, no rounded corners.

## Text

- English for English SCI papers.
- Inclusion and exclusion copied from Methods; trim length, not meaning.
- Split labels include `n =`. Default labels: Training Cohort / Validation Cohort.
- No *P*, AUC, or ethics identifiers inside boxes.

## Export

- PNG, 300 dpi; optional PDF/SVG if the caller asks.
- Width on the page: 16 cm.
- Legend: `Figure 1. Flowchart of patient selection and study design.`
- Do not center the Word legend.
