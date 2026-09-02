# Pipeline stages (P0–P6)

Full-paper **layout, Methods order, word counts, and DOCX** live in [`Aitor-format.md`](Aitor-format.md). This file only adds **prediction-model** constraints (dual-set metrics, LASSO/RadScore, habitat lock).

## P0 — Plan only

Deliver:

1. One-sentence argument  
2. Intro paragraph map (4 jobs)  
3. Methods opening order confirmation  
4. Table/Figure list (Training / Test; Validation set only if an external cohort exists)  
5. Open items (IRB, head-to-head, journal)  

Do **not** draft long prose until plan accepted (unless user says skip plan).

## P1 — Introduction

Follow `Aitor-format.md` (800–1000 words, 10–15 refs when **writing new**, one cite/sentence). Checking an already-written Intro: do not delete genuine refs to hit quota. Habitat papers still use stakes → prior tools → habitat gap → purpose. No AUC dump of the current study.

## P2 — Methods

Fixed order: **`Aitor-format.md`**. Prediction papers must also include:

- Patient-level split language  
- Habitat centroids on the training set only  
- K selection protocol (WCSS / silhouette / consensus ARI ≥ 0.70)  
- Nodule-level fallback definition  
- Primary model = combined (nomogram)  
- LASSO → RadScore definition  

## P3 — Results

Mirror the `Aitor-format.md` Methods order. Dual-set for every performance claim.

Required tables (minimum) — **`Aitor-format.md` wins**:

| Table | Content |
|-------|---------|
| 1 | Primary-cohort baseline (positive vs negative). Train/test balance → S1 |
| 2 | Combined / RadScore / Clinical discrimination on training and test |

No LASSO, logistic-coefficient, SHAP, correlation, or mediation table.

Required narrative for **combined (primary)**:

- AUC (95% CI) training and test  
- ACC/SEN/SPE at the Youden rule actually used (split-specific unless locked)  
- NRI / IDI only if exported (else Word comment: not generated; not in body)  
- Calibration + DCA both sets if exported  

Incremental wording (including the DeLong caveat): **`Aitor-format.md`**.

Full **RadScore formula** in Results (or Methods + Results pointer).

## P4 — Discussion

Follow `Aitor-format.md` (800–1000 words, 10–15 **new** refs when **writing new**, no Intro overlap). Checking an already-written Discussion: do not delete genuine refs to hit quota. Prediction papers still expand:

- Add mechanism sentences for selected feature *families* (not every coefficient)  
- Add 2–3 comparator studies with numbers when available  
- Clinical application: one sentence (`Aitor-format.md`; no disclaimer stack)  
- Expand limitations First…Seventh  

## P5 — References + QC

- `references_vancouver.csv`: id, section, citation_text, doi, verified  
- 100% DOI or drop/replace paper  
- Intro pool vs Discussion pool minimize overlap  
- QC from pipeline summary (`u_QC` or equivalent): pass rate, K, fallback, habitat fractions  

## P6 — DOCX export

Typography, table titles **above**, figure legends **below**, no Heading styles: `Aitor-format.md`.  
Also: Supplementary (QC, K protocol, TRIPOD map) stay in the project folder — **do not** print those paths in the manuscript. Figures labeled training / test. A validation set appears only when an external cohort exists. Note if PNG not yet re-run after split change.  
