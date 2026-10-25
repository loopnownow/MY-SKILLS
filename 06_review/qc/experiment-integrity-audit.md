# Experiment integrity audit (06 qc · Layer 1)

**Owner:** `00_orchestrator` at Integrity · pre-06 / G-FACT compose.
**Seat:** Lee (06) collects paths; **independent reviewer** judges. Loopnow (02) repairs eval/stats code. Executor must **not** self-acquit.
**Distill of:** ARIS `experiment-audit` + `experiment-integrity.md`. Clinical/imaging analogue for radiomics/prediction studies.
**Do not duplicate:** numeric arithmetic layers → `forensic-consistency.md`; stats P0 taxonomy → `stats-failure-modes.md`.

## Purpose

Is the evaluation honest? No fake GT, no phantom metrics, no self-normalized scores, no scope language beyond actual N.

## When

- After primary analysis / `*-results.html` exists, **before** load-bearing claims in 05.
- Mandatory emit at `assurance: submission` / `conference-ready` (see `06_review/qc/assurance-verdicts.md`).

## Inputs (paths only)

- Eval / metric scripts; primary result files (`*-results.html`, Table CSV/xlsx, R/Python outputs)
- Config / split definitions; experiment log if present
- **Exclude** executor summaries and chat as evidence

## Checklist (clinical / imaging analogue)

| id | Check | FAIL if |
|---|---|---|
| EI-A | **GT provenance** — labels from dataset / reference standard, not from model outputs | Proxy GT without `synthetic_proxy` label |
| EI-B | **Score normalization** — no divide-by-own-max; raw + normalized if any rescale | Self-normalized “0.99+” |
| EI-C | **Result existence** — each claimed metric traces to a real file/key | Phantom / mismatched number |
| EI-D | **Dead metrics** — defined but never computed | WARN (or FAIL if paper cites them) |
| EI-E | **Scope honesty** — N / centers / seeds match “comprehensive / robust” language | Overclaim |
| EI-F | **Eval type declared** | `real_gt` / `synthetic_proxy` / `simulation_only` / `human_eval` missing when non-obvious |
| EI-G | **Leakage** — train/val/test (or analysis sets) reconstructible; no silent target leak | Compose with forensic L5 |

## Pass / fail

- **PASS:** EI-A–C green; E–G clean or disclosed; D dead-code absent or WARN only.
- **WARN:** Scope language soft; dead code; proxy labeled but claim ceiling unclear.
- **FAIL:** Fake GT, self-norm fraud, phantom results, or undeclared proxy sold as real performance.
- **BLOCKED:** Claims present; no primary result artifacts to audit.
- **NOT_APPLICABLE:** No quantitative evaluation in this packet (artifact still written).
- **ERROR:** Reviewer/tool failure.

## Fail → rollback

| Verdict | Rollback |
|---|---|
| FAIL / BLOCKED | 02 Loopnow (eval/results) and/or 05 Aitee (claim language); HARD with G-FACT before 06 |
| WARN | Comment + integrity tag on affected claims; continue only if assurance ≤ polished |
| ERROR | Re-run once; else escalate user |

## Verdict artifact

- `EXPERIMENT_AUDIT.json` (+ optional `.md`)
- Fields per `06_review/qc/assurance-verdicts.md`
- `reason_code` examples: `real_gt_ok` | `proxy_undeclared` | `phantom_metric` | `no_raw_evidence` | `no_eval`

*Attribution: ARIS experiment-audit / experiment-integrity (wanshuiyin/Auto-claude-code-research-in-sleep). Host-agnostic checklist.*
