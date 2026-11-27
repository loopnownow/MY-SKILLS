# Study-type route (writing constraints)

**Owner:** `05_manuscript` advanced, on the existing writing route (`05_manuscript/advanced/route.md`).
**Not a second router.** Also not a new fine id, a top-level module, or a QC gate.

## Purpose

Before drafting, name a **coarse** study type from the *user-locked* design and attach the wording and distinction constraints that type requires. This route does not choose a conclusion, does not grade completeness, and does not replace Claim Map or reporting-guideline QC.

## When to load

Load this file with `write-paper` modes `draft-section` or `full-imrad`, **before** building or refreshing the Claim Map (`05_manuscript/advanced/process/claim-map.md`). Re-load only if the locked design itself changes (the user says so).

## How to choose (four coarse classes only)

Do not grow a finer live catalogue this round. Pick one primary class, or record a mixed pair when both are truly in play:

| Class | Use when the locked design is mainly |
|---|---|
| observational | A non-interventional clinical study whose main argument is description or association (cohort, case-control, cross-sectional, or a similar design) |
| diagnostic or prognostic model | Development and/or validation of a prediction model, whether the target is diagnosis or prognosis |
| radiomics | Hand-crafted radiomics or an imaging-derived marker/model as the main argument |
| mechanism | Experimental or translational work whose main argument is a biological or pathophysiological mechanism |

A mixed paper (for example a retrospective cohort that also develops a radiomics model) keeps both labels and applies the stricter wording and distinction rules. Do not invent a fifth live class to name the mix.

If the locked design is clearly outside these four (for example a randomized trial or a systematic review), do not force a fit. List the mismatch, ask the user to confirm, and point to `05_manuscript/qc/reporting-guideline-route.md` for the matching guideline family. That is a confirmation request, not a new class.

If the type is unclear, list the uncertain points and ask. Do not guess the design from the title, the journal, or a convenient template.

## Hard constraints

1. Do not change the study design, endpoints, eligibility, covariates, missing-data handling, or statistical plan in order to fit a manuscript template.
2. This route does not override a user-locked design or statistical plan. Writing follows the lock; the lock is not rewritten to match the route.
3. If the type is unclear, list the uncertain points and request confirmation. Do not guess from the title.
4. Observational work defaults to association wording (*associated with*). Causal verbs are allowed only when the locked design and the supplied evidence actually support them.
5. For a prediction model, keep development, internal validation, external validation, and clinical utility distinct. Do not treat one as if it were another.
6. For an imaging model, an improvement in AUC (or a similar discrimination metric) is not by itself a clinical benefit. Distinguish feature-level findings, model performance, and clinical utility.
7. Do not invent results, sample sizes, procedures, ethics IDs, or citations.

## Writing emphasis and guidelines

Guidelines are a completeness check, not a certificate that the methods were adequate. Choose only the family that actually applies; do not stack every named standard onto one paper. The gate-level router remains `05_manuscript/qc/reporting-guideline-route.md`. Imaging-specific writing stacks remain `05_manuscript/qc/check-reporting/radiology-reporting/guideline-router.md`. This file does not emit those verdicts and does not copy their checklists.

### observational

Emphasize setting, eligibility, time direction, and how the exposure and outcome were defined. Keep conclusions inside association, residual confounding, and the sampled population. Usual completeness family: STROBE.

### diagnostic or prognostic model

Name the target population, the predictors or index test, and the outcome or reference standard (and time zero, for prognosis). Keep development, internal validation, external validation, and clinical utility (for example calibration or decision-analytic metrics *when the user supplied them*) in separate claims. Do not claim generalizability from internal validation alone. Usual completeness family: TRIPOD, or TRIPOD+AI when the locked methods are ML/AI; use STARD when the main task is diagnostic accuracy rather than a multivariable model.

### radiomics

Be explicit about acquisition, segmentation, feature stability, leakage risk, and validation. Distinguish a feature-level finding, a model's discrimination or calibration, and any clinical-utility claim. An AUC gain is not a clinical-benefit sentence. Use CLAIM and/or CLEAR only when that stack applies; if the same paper also develops a prediction model, add TRIPOD as above, still without loading every imaging checklist at once.

### mechanism

Distinguish what was observed, what was experimentally manipulated, and what is inferred as mechanism. A mechanistic reading belongs in the Discussion and stays hedged unless the locked design and the supplied data actually tested it. Do not default-stack STROBE or TRIPOD onto a mechanism paper; follow the design the user locked.

## Output (keep light)

Record in a Word comment (author **A**) or the handoff note:

```text
Study-type route
----------------
Class: observational | diagnostic or prognostic model | radiomics | mechanism | mixed (name the pair) | unclear
Locked design (user's words): ...
Guideline family (only if it applies): ...
Constraints in force: ...
Uncertainties / confirmation asked: ...
```

## Relation to Claim Map

This route supplies design-level constraints (what wording and distinctions the locked design allows). The writing-entry summary is in `05_manuscript/advanced/process/intake-brief.md`. `05_manuscript/advanced/process/claim-map.md` then traces each load-bearing claim to its evidence, statistical support, wording, and location. The two-way method-experiment trace is in `05_manuscript/advanced/process/method-experiment-align.md`. Do not copy those rule bodies here. After drafting, existing claim QC and reporting-guideline gates still run unchanged.

## Out of scope

- Style metrics or figure/table planning
- New fine ids, new gates, or a parallel 05 router
- Changing 00 gate composition or 02 figure production
- Pasting EQUATOR / TRIPOD / CLAIM item bodies into the manuscript or this file

*Lab rewrite, 2026-11-27. The idea of routing writing constraints by research type is noted as a method reference to [gulucaptain/Best-Paper-Writing-Skill](https://github.com/gulucaptain/Best-Paper-Writing-Skill); the classes, constraints, and wording here were written in this seat. See `NOTICE`.*
