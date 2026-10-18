# Pipeline stages (prediction papers, P0–P6)

Generic dual-set IMRAD constraints for prediction / radiomics papers. Personal house format
(word-count quotas, DOCX typography, title-page defaults) is **not** in this pack.

## P0 — Plan only

1. One-sentence argument
2. Intro paragraph map (stakes → prior tools → gap → purpose)
3. Methods order confirmation
4. Table/Figure list (Training / Test; Validation set only if an external cohort exists)
5. Open items (IRB, head-to-head, journal) — ask, do not invent

Do **not** draft long prose until the plan is accepted (unless the user says skip plan).

## P1 — Introduction

Stakes → prior tools → gap → purpose. No AUC dump of the current study. Do not delete genuine
references to hit a quota.

## P2 — Methods

Use `methods_template_export.md` order. Prediction papers must also include:

- Patient-level split language
- Any clustering / feature-selection steps **on the training set only**
- Primary model named (e.g. combined / nomogram)
- LASSO → RadScore definition when that is the analysis

## P3 — Results

Mirror Methods order. Dual-set for every performance claim.

Typical tables:

| Table | Content |
|-------|---------|
| 1 | Primary-cohort baseline. Train/test balance → supplement |
| 2 | Combined / RadScore / Clinical discrimination on training and test |

Required narrative for the **primary** model when numbers were supplied:

- AUC (95% CI) training and test
- Operating-point metrics at the rule actually used
- Calibration + DCA both sets if exported
- Full RadScore formula if LASSO was run

Missing exports → comments, not invented body text.

## P4 — Discussion

What the result means, 2–3 comparators with numbers when available, bounded clinical
implication, explicit limitations. No disclaimer stack.

## P5 — References + QC

- Prefer DOI-verified citations
- QC from pipeline summary if supplied: pass rate, K, fallback

## P6 — Export

Typography and house DOCX live in A personal / `05-write-venue`. Figures: STROBE flow →
`04-fig-flow`; plots → `04-fig-plot`. A validation set appears only when an external cohort exists.
