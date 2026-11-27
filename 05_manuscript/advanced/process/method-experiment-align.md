# Method-experiment alignment (trace check, not a gate)

**Owner:** `05_manuscript` advanced, on the existing writing route (`05_manuscript/advanced/route.md`).
**Not a QC gate**, and not a new skill, experiment matrix, fine id, or second router.

## Purpose

Run a short two-way check along this chain: study aim or hypothesis → design and methods → statistical analysis → results → interpretation bounds. The point is to find a break in that chain before the prose hardens. This is a writing-prep trace for `write-paper`. It does not open a new Gate, and it does not replace G-FACT, G-STATS, or reporting-guideline completeness.

## When to load

Load after `05_manuscript/advanced/process/study-type.md` and `05_manuscript/advanced/process/claim-map.md`, when drafting or revising Methods, Results, or Discussion. Revisit a row only if a locked aim, a described method, or a supplied result file changes.

## Two-way check (keep light)

One short row per main analysis or main aim. Leave a cell blank when it does not apply. Do not turn this into a heavy experiment matrix.

1. Does each main analysis have a clear study aim or a pre-stated reason?
2. Does each main study aim have a corresponding method in Methods?
3. Can each main result be traced to an analysis described in Methods?
4. Can each Discussion claim be traced to Results or to verified literature?
5. Is there an analysis that appears in Results but was not described in Methods?
6. Is an exploratory analysis written as if it were a pre-specified confirmatory analysis?

```text
Aim / analysis | Methods locus | Results locus | Discussion locus | Prespecified or exploratory | Status
```

Status is `aligned`, `mismatch`, or `awaiting data`. `awaiting data` means the real output is not in hand; it is a comment (author **A**), not a licence to invent numbers or analyses.

If the row is a mismatch: comment (author **A**), weaken the claim, or drop it. Never invent the missing method, step, or result to close the row.

## Prediction, radiomics, and machine learning

When the study type is a diagnostic or prognostic model, radiomics, or another trained model, also locate and check:

- whether the data split was handled correctly before feature selection and training
- whether preprocessing was fitted on training data only and then applied to validation data
- whether data leakage is present, including patient-level leakage across splits
- whether model comparisons used the same dataset and the same evaluation metrics
- whether internal validation and external validation are kept distinct

Do not copy the production or gate checklists here. Split, leakage, and train-only fitting remain with `02_data-processing/qc/ml-experiment-checklist.md` and `02_data-processing/qc/report-checks.md` (G-STATS / G-FACT as already routed). Reporting-guideline completeness stays in `05_manuscript/qc/reporting-guideline-route.md`. Claim support after drafting stays in `05_manuscript/qc/result-to-claim.md`. Study-type wording stays in `05_manuscript/advanced/process/study-type.md`. Methods and Results recipes stay in `05_manuscript/base/write-paper/radiology-writing/methods.md` and `results.md`.

## Hard constraints

1. Do not change a user-locked design or statistical plan so that the manuscript looks aligned.
2. Do not invent an analysis or a result that was not performed.
3. Do not write an unperformed step into Methods or Results for writing convenience. Missing steps stay comments (author **A**), or the claim is weakened or dropped.
4. Do not recast an exploratory analysis as confirmatory.

## Call graph

| Direction | File | Role |
|---|---|---|
| Upstream | `05_manuscript/advanced/process/study-type.md` | Coarse design class; do not copy those wording rules here |
| Upstream | `05_manuscript/advanced/process/claim-map.md` | Which claims must be traceable; do not copy that map here |
| Entry | `05_manuscript/base/write-paper/MODULE.md` | Load this trace when drafting Methods, Results, or Discussion |
| Writing hosts | `05_manuscript/base/write-paper/radiology-writing/methods.md` and `results.md` | Section recipes; this file is the cross-section trace |
| Later science QC | `05_manuscript/qc/result-to-claim.md` (G-FACT) | Whether a reported result supports the claim; not this trace |
| Later science QC | `05_manuscript/qc/reporting-guideline-route.md` | Guideline completeness; do not paste checklists here |
| Later stats / ML QC | `02_data-processing/qc/report-checks.md`, `ml-experiment-checklist.md` | How leakage and split are judged at G-STATS / G-FACT |

## Out of scope

- An intake brief
- New fine ids, new gates, or a parallel QC or skill
- Copying study-type, Claim Map, result-to-claim, or 02 checklist bodies
- Changing 00 gate composition or editing 02 production rules

*Thin lab rewrite, 2026-11-27, on a two-way method-experiment trace (aim to methods to results to interpretation bounds, not a new gate). Method reference: [gulucaptain/Best-Paper-Writing-Skill](https://github.com/gulucaptain/Best-Paper-Writing-Skill). See `NOTICE`.*
