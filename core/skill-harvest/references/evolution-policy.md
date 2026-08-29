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

Formal Evolution Proposals start at **E4** (repeated same-class user corrections). Prefer **E5** when a golden set or deterministic test exists. E0–E3 stay in the evidence log. See `SKILL.md` Human-approved evolution protocol.

## Evolution budget

Per proposal: ≤1 core behavioral change, ≤3 new rules, prefer no net length increase, no duplicate rules, no boundary expansion. `CHANGE_TOO_LARGE` exits this loop into a human design task.

## Approval

User silence, "不错", or "可以考虑" is not approval. Explicit `approve` / `批准` / `把这个修改加入 Skill` / `批准这个 Proposal` only.

Do not auto-modify, auto-promote, auto-merge, or auto-delete an active Skill.

