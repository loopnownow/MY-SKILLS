# Forensic consistency gates (06 qc · standards only)

**Owner:** `00_orchestrator` at Gate · 06 / Integrity · pre-06 (compose with **G-FACT** when numbers cited).
**Distill of:** Yuan1z `nature-reviewer` → `forensic-consistency-audit` layers (Apache-2.0). Pass/fail gates only; not a fourth reviewer essay.

## When

After quantitative claims are frozen for the review packet (or at Integrity · pre-06). Keep audit findings labeled as **audit**, not fake reviewer consensus.

## Evidence status (required label per check)

`passed` | `confirmed_internal_error` | `aggregation_ambiguity` | `provenance_gap` | `suspected_duplication` | `unresolved_input_needed` | `not_assessable`

Never upgrade suspicion to confirmed without proof from supplied material.

## Layers (pass/fail)

| # | Layer | PASS | FAIL → |
|---|---|---|---|
| 1 | **Arithmetic** | Subgroup sums, %, deltas, paired diffs, ranges, integer counts reconcile | G-FACT + 04/05 |
| 2 | **Metric bounds** | Metric definition + aggregation known; values inside possible bounds | 04 / 05 (or ambiguity → comment) |
| 3 | **Prose ↔ table ↔ figure** | Headline ranks/“always/only/best” match displays; same quantity consistent precision | G-FACT + 05 |
| 4 | **Aggregation / unit** | Inferential unit stated at each level (patient vs image vs tile; macro/micro) | 04 / 05 |
| 5 | **Provenance / leakage** | Train/val/test (or analysis sets) reconstructible; no silent target leakage | 04 / ethics |
| 6 | **Dispersion** | Extreme/near-zero variance or identical rows flagged; not called fraud without proof | annotate 06; escalate if confirmed |

## Release rule

- Confirmed central arithmetic/bounds/prose contradiction → **HARD** with G-FACT; do not release review as clean.
- Ambiguity / not_assessable → Word comment; do not invent numbers.

**PASS:** layers 1–3 clean on cited numbers; 4–6 clean or commented.
**FAIL:** `confirmed_internal_error` on a central claim → block next node until 04/05 clears.

*Attribution: distilled from Yuan1z0825/nature-skills `nature-reviewer` (Apache-2.0).*
