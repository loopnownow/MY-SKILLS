# Type B — study-workflow figure (rules only)

Chinese-journal "研究流程图" that mixes **enrolment with analysis steps** (GGN-style: screened n → train/test split → Radscore / clinical model → nomogram).

This is **not** the default Figure 1. Type A (published STROBE) is the default; see `patient-flow.md`.

## When type B applies

- The target venue expects a single "study flowchart" that already shows modelling steps.
- Typical published pattern: cohort n → 7:3 (or similar) split → radiomics signature and clinical model in parallel → combined nomogram / decision.

Do **not** force this into `draw_strobe_flow.py`. That script is type A only (inclusion IN, exclusion OUT, Training/Validation, no pipeline row).

## Rules (first version: no drawing code)

1. Keep patient n honest and unique to this endpoint. Do not invent n.
2. Enrolment still follows STROBE sense: screened → reasons out → analyzed. If inclusion/exclusion exist, show them; do not drop inclusion to save space.
3. Split labels on the page: Training Cohort / Validation Cohort (or the venue's wording). Never "Development set".
4. Analysis steps (feature selection, Radscore, clinical model, nomogram) sit **after** the enrolled n, as a separate block — they are not a substitute for the patient-selection spine.
5. Do not paste specimen photos, CT slices, heatmaps, or LASSO path plots into the workflow.
6. Caption names it a study workflow, not a CONSORT diagram. CONSORT randomisation arms are not the default in this lab.

Drawing code for type B is out of scope for this revision. Until a dedicated drawer exists, sketch type B by hand or in PowerPoint from these rules; do not extend `draw_strobe_flow` with a pipeline row to fake it.
