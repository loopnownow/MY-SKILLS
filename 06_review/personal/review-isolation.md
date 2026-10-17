# Review isolation workflow (A06 personal)

Contract 2026-10-17. Bodies of engines stay in **B**. This file is the A-side orchestration pointer.

## Pattern

```text
B: simulate-reviewers (isolation)
  -> B: self-review  ||  B: peer-review   (parallel; finding sets MUST stay isolated)
  -> 00 QC gate (gates.md check (a): isolated dual-review artifacts)
  -> A06: post-QC re-review only (merge / grade / English envelope)
  -> (optional) A07 response
```

## Isolation rules

1. Do **not** let reviewer personas or engine outputs cross-contaminate before 00 QC.
2. Each finding set keeps its source prefix (`[B:self-review]`, `[B:peer-review]`, `[B:simulate-reviewers]`, ...).
3. A06 merges only **after** 00 confirms isolated artifacts exist.
4. A06 does **not** re-run first-pass B engines; it re-reviews and adjudicates.

## Pointers

- A route: `route.md` (re-review only)
- A envelope: `review.md`
- 00 checks: `00_orchestrator/gates.md` section A/B top-layer QC checks
- B engines: MY-SKILLS-capabilities `06-review/simulate-reviewers/`, `review-critique/` (self-review), `review-peer/` (peer-review)
- Optional B README: `06-review/REVIEW-ISOLATION.md`
