# Appraisal tool route (06 qc · standards only)

**Owner:** `00_orchestrator` at Gate · 06 when formal RoB / certainty appraisal applies.
**Distill of:** K-Dense `scientific-critical-thinking` framework **routing** (MIT). Router only — **no** full Cochrane/GRADE essay text.

## When appraisal applies

Use this file when the task is evidence appraisal, systematic-review support, or a review comment that requires a named RoB/certainty tool. Ordinary radiology prediction pre-review still uses TRIPOD+AI / PROBAST+AI via `05_manuscript/qc/reporting-guideline-route.md`.

## Route (study type → tool family)

| Study / estimate type | Route to (official tool; verify current version URL) | Do not |
|---|---|---|
| Diagnostic accuracy | QUADAS family (current major version per official site) | Score a whole paper as one number |
| Prediction model (dev/val) | PROBAST+AI / TRIPOD+AI reporting route (lab already has) | Paste EQUATOR item bodies here |
| RCT (effect of assignment) | RoB 2 (result-level: outcome, time, comparison) | One blanket score for all outcomes |
| Non-randomized intervention | ROBINS-I (state 2016 vs later draft; do not mix domains) | Mix domain sets across versions |
| Body of evidence certainty | GRADE per outcome/comparison when synthesizing | Grade a paper by design label alone |
| Imaging AI / radiomics MS | Prefer lab reporting + PROBAST+AI; RoB tools only if SR/appraisal asked | Force Cochrane RoB on every MS |

## Pass/fail (coverage, not checklist paste)

| id | Check | Fail → |
|---|---|---|
| AT-1 | Tool chosen matches study/estimate type; version/URL noted | 06 Lee |
| AT-2 | Appraisal unit recorded (result / outcome / model) — not whole-paper score | 06 |
| AT-3 | No EQUATOR/Cochrane **item bodies** pasted into lab qc; link official source | 06 |

**PASS:** AT-1–3 when appraisal is in scope; else N/A.
**FAIL:** wrong tool or checklist-item dump → rollback **06** (re-route).

*Attribution: routing distilled from K-Dense-AI/scientific-agent-skills `scientific-critical-thinking` (MIT).*
