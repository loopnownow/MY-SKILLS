---
name: "fig-flow"
domain: "04_analysis"
trigger: ["STROBE", "流程图", "patient flow", "入组图"]
outputs: ["flow_figure"]
owner: "04-analysis/fig-flow/MODULE.md"
---

# trigger is documentation only; not independently discoverable.

# Study / patient flow figures

STROBE-style enrolment flow, study-workflow diagrams, and methods-pipeline cartoons.
Statistical plots live in `04-fig-plot`.

`scripts/draw_strobe_flow.py` draws **type A only**. Do not invent n.

## Figure 1 types (do not mix)

| Type | When | Draw with |
|---|---|---|
| **A — published STROBE** (default) | Retrospective cohort / prediction patient selection | `scripts/draw_strobe_flow.py`. Inclusion arrow IN, exclusion arrow OUT with `(n=k)`, Training Cohort / Validation Cohort, no pipeline row. See [references/patient-flow.md](references/patient-flow.md) and [references/style.md](references/style.md). |
| **B — study workflow** | Enrolment mixed with analysis steps | Rules only: [references/study-workflow.md](references/study-workflow.md). Do not extend `draw_strobe_flow`. |
| **C — methods pipeline** | Radiomics-step / specimen-to-model cartoon | **Must not** call `draw_strobe_flow`. See [references/methods-pipeline.md](references/methods-pipeline.md). |

CONSORT randomisation arms are **not** the default. Draw CONSORT only for an actual RCT.

`draw_strobe_flow` exits nonzero if `screened − Σ exclusion n ≠ analyzed` or `Σ split n ≠ analyzed`.
Historical printed figures that fail arithmetic may use `--no-audit` only when that mismatch is documented.

Caption: `Figure 1. Flowchart of patient selection and study design.`

## When to open extra files

| File | Open when |
|---|---|
| [references/patient-flow.md](references/patient-flow.md) | Type A published STROBE Figure 1 (default), n-audit |
| [references/style.md](references/style.md) | Type A box geometry (white, black squares, Arial, arrows IN/OUT) |
| [references/study-workflow.md](references/study-workflow.md) | Type B study-workflow rules only |
| [references/methods-pipeline.md](references/methods-pipeline.md) | Type C methods pipeline cartoon |
| [scripts/draw_strobe_flow.py](scripts/draw_strobe_flow.py) | Draw type A (`--json` `--out`; `--no-audit` only for documented historical n mismatches) |

Plots (ROC, calibration, imaging panels) → `../fig-plot/`.
