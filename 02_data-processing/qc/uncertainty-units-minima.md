# Uncertainty and units minima (02/05 qc — standards only)

**Owner:** `00_orchestrator` at Gate → 02 / 05 when quantitative measurements carry units or ± uncertainty.
**Compose:** `02_data-processing/qc/report-checks.md` (radiology reporting style) + `05_manuscript/qc/claim-number-align.md`.
**Distill of:** K-Dense `uncertainty-and-units` reporting / failure headings (MIT). **No** pint / uncertainties CLI / Monte Carlo runtime absorb — checklist only.

## Domain gate

Run when manuscript or HTML reports physical/lab units, ± intervals, or converted quantities. **NOT_APPLICABLE** for pure count / AUC-only packages with no united measurands.

## Must-check (UU)

| Id | Check | Fail → |
|---|---|---|
| UU-1 | Unit stated at first report of each measurand; same quantity keeps the same unit across prose/table/figure | 02 / 05 |
| UU-2 | `±` / interval meaning stated (SD vs SEM vs 95% CI vs expanded U) — no bare ± ambiguity on central claims | 02 / 05 |
| UU-3 | No silent unit strip / rescale between table and prose (compose G-FACT) | G-FACT |
| UU-4 | Order-of-magnitude / physio plausibility soft-flag when value is impossible for the named unit (compose lab-ref Hook C when lab analyte) | 02 / 06 comment |
| UU-5 | Do not invent coverage factor `k`, GUM budgets, or CODATA constants from memory | 02 |

**PASS:** UU-1-5 clean or commented.
**FAIL:** unit mismatch on a central number → HARD with **G-FACT**.

*Attribution: K-Dense-AI scientific-agent-skills `uncertainty-and-units` (MIT); distill headings only.*
