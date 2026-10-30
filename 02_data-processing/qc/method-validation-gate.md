# Analytical method-validation gate (02 qc — domain-gated)

**Owner:** `00_orchestrator` at Gate → 02 **only when** the packet validates / verifies / transfers an analytical procedure (HPLC, LC-MS, qPCR, ligand-binding, etc.).
**Default for this lab:** **NOT_APPLICABLE** for radiology nomogram / radiomics / imaging-ML manuscripts that do not claim assay validation.
**Distill of:** K-Dense `analytical-method-validation` framework-selection + anti-pattern headings (MIT). **No** ICH/USP/CLSI clause text paste; **no** invented acceptance numbers; **no** validation scripts absorb.

## Hard rules (from upstream, kept)

1. Name the **governing framework** before designing checks (ICH Q2(R2) vs M10 vs USP/CLSI/ISO) — do not blend.
2. Acceptance criteria are stated **before** seeing validation data (post-hoc criteria → FAIL comment).
3. Paywalled chapter text (USP/CLSI/ISO) is never reconstructed from memory — cite designation + authorised copy only.

## Must-check when in scope (AMV)

| Id | Check | Fail → |
|---|---|---|
| AMV-1 | Framework named; characteristics match attribute (assay / impurity / identity / bioanalytical) | 02 |
| AMV-2 | Acceptance criteria pre-specified in protocol / methods | 02 |
| AMV-3 | Linearity not argued from r² alone when lack-of-fit / back-calc errors exist | 02 |
| AMV-4 | Intermediate precision (between-day/analyst) not silently replaced by within-run repeatability | 02 |
| AMV-5 | DL/QL: approach named + confirmation near limit when claimed | 02 |
| AMV-6 | Method comparison: equivalence margin pre-stated; “p > 0.05” alone is **not** equivalence | 02 |

## Clinical-reports boundary (related)

If the request is a **clinical case / CSR / safety** scaffold: use de-identified / aggregate inputs only; mark DRAFT; never diagnose or invent results. Prefer ethics / qualified-review path over this AMV gate. Source headings: K-Dense `clinical-reports` (MIT) — no runtime.

**PASS:** AMV-1-6 clean or commented when domain-gated in.
**FAIL / NOT_APPLICABLE:** wrong domain → emit `NOT_APPLICABLE` with one-line reason (do not silent-skip at submission if AMV was claimed).

*Attribution: K-Dense analytical-method-validation + clinical-reports boundaries (MIT). No CDS; no invented RI / acceptance thresholds.*
