# Assurance audit chain (5 layers · one-page map)

**Owner:** `00_orchestrator` loads at Integrity · pre-06 / G-05 / G-06 / submit.
**Contract:** `06_review/qc/assurance-verdicts.md` (effort vs assurance; 6-state; who may ACCEPT).
**Source map:** ARIS AGENT_GUIDE “Assurance & Audit Chain” — lab paths + seats below.
**Silent skip forbidden** at `assurance: submission` / `conference-ready`.

## Layer → path → seat

| # | Question | Lab standard | Verdict file | Runs / repairs |
|---|---|---|---|---|
| 1 | Eval honest? (no fake GT / phantom / self-norm) | `06_review/qc/experiment-integrity-audit.md` | `EXPERIMENT_AUDIT.json` | Lee collects paths; **independent** judges; Loopnow repairs code |
| 2 | Claim follows from result scientifically? | `05_manuscript/qc/result-to-claim.md` | `RESULT_TO_CLAIM.json` | Independent judges; Aitee revises claim; Loopnow if more data |
| 3 | Paper reports numbers truthfully? | `05_manuscript/qc/paper-claim-audit-gate.md` (+ base `paper-claim-audit.md`) | `PAPER_CLAIM_AUDIT.json` | Cold-read independent; Aitee/Loopnow fix |
| 4 | Cite exists + metadata + context OK? | `05_manuscript/qc/citation-audit-gate.md` (+ `refs-verified.md`, G-CIT) | `CITATION_AUDIT.json` | Victor verify; Aitee wording |
| 5 | Strongest rejection memo survive? | `06_review/qc/kill-argument-preflight.md` | `KILL_ARGUMENT.json` | Lee preflight; Aitee TC after user |

## Gate composition (existing ids — no new G-*)

| Moment | Layers |
|---|---|
| **G-FACT** / numbers cited | 1-3 (compose forensic-consistency / claim-number-align — link, don’t redo) |
| **G-LIT** / **G-CIT-1/2** | 4 |
| **Integrity · pre-06** | 1-4 as applicable + existing 05/06 qc subset in `gates.md` |
| **G-06** / pre-submit | +5 when assurance ≥ conference-ready |
| **Integrity · post-re-review lite** | Spot re-check 2-3 if numbers/claims changed |

## Link instead of duplicate

- Forensic arithmetic / prose↔table → `forensic-consistency.md`
- Stats P0 taxonomy → `stats-failure-modes.md`
- Claim↔number CN-* → `claim-number-align.md`
- DOI field audit RV-* → `refs-verified.md`
- Release isolation → `review-release-gates.md`

## Seats (ownership-contract)

| Seat | Role in chain |
|---|---|
| Aitor (00) | Loads standards; HARD recoveries; does not invent numbers |
| Loopnow (02) | Eval/results repairs (L1); evidence gaps (L2/L3) |
| Victor (03) | Citation verify L4; G-CIT |
| Aitee (05) | Claim/prose TC; never self-certify lit or integrity |
| Lee (06) | Path collection / cold-read / kill-argument; marks, does not self-revise ms by default |
| Bai | Portal submit only after submission-level assurance green or user override recorded |

## ARIS P1 process standards (absorbed 2026-10-19)

- Stage map W1→W3 + artifact contracts → seats: `03_research/qc/research-stage-artifacts.md`
- Review→fix→re-review + resumable `REVIEW_STATE`: `06_review/qc/review-loop-state.md` (Lee)
- Resubmit edit-whitelist + failure ledger: `07_response/qc/resubmit-edit-whitelist.md`
- Still **out of scope**: installing ARIS runtime / host MCP / `verify_paper_audits.sh` as-is

*Attribution: ARIS (wanshuiyin/Auto-claude-code-research-in-sleep) assurance chain; lab layout + seats.*
