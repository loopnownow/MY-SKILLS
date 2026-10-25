# Review release gates (06 qc · standards only)

**Owner:** `00_orchestrator` at Gate · 06 / before releasing a review packet.
**Distill of:** Yuan1z `nature-reviewer` → `qa-checklist` isolation / grounding / severity / final release rule (Apache-2.0). Short gates only.

## Isolation

| id | PASS | FAIL → |
|---|---|---|
| RL-I1 | Dual/multi engines isolated; findings labeled by source prefix before merge | 06 / base engines |
| RL-I2 | No report cites or anticipates another reviewer | 06 |
| RL-I3 | If isolation unavailable, packet must not claim mutual blindness | 06 |

## Grounding

| id | PASS | FAIL → |
|---|---|---|
| RL-G1 | Substantive concerns have claim_pointer + evidence_pointer (or “location not provided”) | 06 |
| RL-G2 | No invented experiments, line numbers, or PMID/DOI | 06 / G-LIT |
| RL-G3 | Partial evidence → `AUTHOR_INPUT_NEEDED` / not assessable — not silent fill | 06 |

## Severity

| id | PASS | FAIL → |
|---|---|---|
| RL-S1 | Major/Minor from impact on central case, not tone or quota | 06 |
| RL-S2 | Blocking only on Major that prevents establishing the central case | 06 |
| RL-S3 | Empty Major/Minor tier allowed (`None identified…`) | 06 |

## Final release rule

Do **not** release when:

1. Severity/Blocking flags conflict with rationale or resolution test.
2. Confirmed central forensic contradiction (`forensic-consistency.md`) is omitted from risk.
3. Grounding invents facts to look complete.
4. Isolation was not achieved but the packet claims three-blind consensus.

**PASS:** RL-* clean + forensic central errors disclosed if any.
**FAIL:** any release-rule hit → hold packet; local rework at 06 (or 02/05 if fact-lineage).

*Attribution: distilled from Yuan1z0825/nature-skills `nature-reviewer` (Apache-2.0).*
