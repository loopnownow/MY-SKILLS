# Skill Evolution Policy

## Versioning

Use semantic intent rather than file-count growth:

- PATCH: wording, typo, routing clarification, non-behavioral reference correction.
- MINOR: new mode, decision rule, tool, workflow, or measurable capability within the existing boundary.
- MAJOR: ownership boundary, input/output contract, or routing behavior changes.

## Change classes

| Class | Example | Approval |
|---|---|---|
| Fix | Correct a wrong rule | User approval unless explicitly autonomous |
| Optimize | Reduce context or redundant steps | User approval |
| Extend | Add a reusable mode | User approval |
| Toolize | Move deterministic work into a script | User approval |
| Workflow | Combine existing Skills | User approval |
| Rollback | Undo harmful iteration | User approval unless safety-critical |

## Evolution record

Maintain a dated record for meaningful changes. Minimum fields:

```text
change_id
date
skill
from_version
to_version
problem
change
expected_benefit
evidence
metrics
decision
```

## Keep / revise / rollback

Keep when the change demonstrates benefit and preserves boundaries.

Revise when the problem is real but the implementation has weak evidence, excess complexity, or boundary ambiguity.

Rollback when the change causes measurable regression, contradictory behavior, routing degradation, or unacceptable context cost.

Archive when the capability is no longer used but may be useful for recovery or historical analysis.

## Anti-bloat rule

Every addition should answer:

> What recurring problem does this prevent, and how will we know it helped?

If neither answer is available, do not add it yet.

## Evidence threshold (E0–E5)

Formal Evolution Proposals start at **E4** (repeated same-class user corrections). Prefer **E5** when a golden set or deterministic test exists. E0–E3 stay in the evidence log. See Human-approved evolution protocol below.

## Evolution budget

Per proposal: ≤1 core behavioral change, ≤3 new rules, prefer no net length increase, no duplicate rules, no boundary expansion. `CHANGE_TOO_LARGE` exits this loop into a human design task.

## Approval

User silence, "不错", or "可以考虑" is not approval. Explicit `approve` / `批准` / `把这个修改加入 Skill` / `批准这个 Proposal` only.

Do not auto-modify, auto-promote, auto-merge, or auto-delete an active Skill.


## Human-approved evolution protocol (detail)

`skill-harvest` is an **Evolution Advisor**, not a self-modifying Skill. The user owns Skills; Git is the version/audit layer.

### User Correction First

Evidence priority (highest first):

`用户实际编辑后的输出 > 用户明确纠正 > 用户明确评价 > 单次任务观察 > AI 自我反思`

A user edit is Evidence. It does **not** change an active Skill by itself.

### Evidence E0–E5 (proposal gate)

| Level | Evidence | Default action | Enough to evolve? |
|---|---|---|---|
| E0 | AI self-reflection | may record | no |
| E1 | Single-task issue | record | no |
| E2 | User names a problem | record and watch | usually no |
| E3 | User actually edits the output | high-value signal, still watch | usually no |
| E4 | Same class of user edit across similar tasks | Candidate / Proposal | yes (default threshold) |
| E5 | Repeated pattern + eval/golden-set improvement | strong promotion evidence | best |

Default: **E4** before a formal Evolution Proposal. Prefer **E5** when a golden set or deterministic test exists. One event never evolves a Skill.

### Feedback taxonomy

| Type | Meaning | Handling |
|---|---|---|
| `ERROR` | wrong output | record; decide if it is a Skill defect |
| `OMISSION` | missing required step/info | add a principle only if it repeats |
| `PREFERENCE` | taste | Memory / Feedback, not Skill |
| `OPTIMIZATION` | correct but could be cheaper | needs demonstrated benefit |
| `NEW_PATTERN` | reusable method | Candidate after it repeats and generalizes |
| `REGRESSION` | new version hurts old capability | protect old capability; propose rollback |

### Pipeline

```text
OBSERVE → HARVEST → CLASSIFY → STORE EVIDENCE
  → repeated and generalizable?
       no  → keep observing / Memory
       yes → EVALUATE → REGRESSION CHECK → EVOLUTION BUDGET
             → EVOLUTION PROPOSAL → PENDING USER APPROVAL
                  APPROVE → apply the exact approved change (Git PR)
                  REJECT  → Skill unchanged
                  MODIFY  → revise proposal
```

Controller **may**: observe, record corrections, classify, detect repeated patterns, evaluate, write a Proposal.

Controller **must not**: modify, overwrite, promote, merge, or delete an active Skill; auto-merge a PR; treat silence as yes.

### Skill vs Memory

Stable, cross-task, procedural method with repeated user evidence → Skill.

Project facts, one-off preference, temporary constraints, unconfirmed observation → Memory / Feedback, not Skill.

### Rollback proposal

If a promoted version regresses, **propose** restore to the Git commit recorded as the rollback point. Do not auto-patch a second evolution on top. Decision matrix: `keep-merge-delete.md`.
