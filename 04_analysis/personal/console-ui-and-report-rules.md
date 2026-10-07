# Console UI and results-report rules (lab)

**Owner:** `04_analysis`. Source: session harvest 2026-10-07 (P-04–P-08).  
Implementation: `D:\0Grok\0script\stats-analysis\modules\console\` and results HTML writers.  
Word / 0doc 政策不在本文件；见 `C:\Users\loopn\Documents\Cline\Rules\`.

## 1 Interactive HTML acceptance (P-04)

- Choice controls (checkboxes, selects) **must persist** the user’s selection (save/load; refresh does not wipe unchecked intent).
- Every interactive proposal / upgrade HTML ends with **one blank input row** the user can type into.
- If persistence is missing, treat as FAIL and fix before delivery.

## 2 Layout density (P-05)

- Prefer **few rows, many columns** on one row.
- Columns in a row share width evenly unless a control needs a fixed width.
- Place checkboxes **above** their related dropdowns when both control the same block.

Acceptance (inspectable): first viewport of console / proposal HTML does not stack one control per full-width row when peers can share a row.

## 3 Language in results HTML and figures (P-06)

- Results `Results*.html` body text and figure glyphs: **no Chinese**.
- Use English labels; put Chinese (if needed) only in hover / title tooltips.
- Figure fonts: Arial for plots; flowcharts stay PDF + Times New Roman 12 (already owned elsewhere).

## 4 External validation display (P-07)

- External-validation tables, previews, and subgroup-style blocks use the **same layout and logic** as internal / subgroup pages.
- Do not invent a second HTML schema for external-only views.

## 5 Figure and report switches (P-08)

- DCA / SHAP / NRI / IDI / tiff / pdf / survival curves (and any similar optional figure) appear **only when the corresponding switch is on**.
- Switch off → that artifact must not be written to disk and must not appear in the results HTML.
- Acceptance: with all optional switches off, only always-on core outputs remain; turning one switch on adds exactly that family of outputs.
