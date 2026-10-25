# Review isolation workflow (06 personal)

Contract 2026-10-17. Bodies of engines stay in `06_review/base/`. This file is the orchestration pointer.

## Pattern

```text
B: simulate-reviewers (isolation)
 -> B: self-review || B: peer-review (parallel; finding sets MUST stay isolated)
 -> 00 QC gate (gates.md check (a): isolated dual-review artifacts)
 -> 06: post-QC re-review only (merge / grade / English envelope)
 -> (optional) 07 response
```

## Isolation rules

1. Do **not** let reviewer personas or engine outputs cross-contaminate before 00 QC.
2. Each finding set keeps its source prefix (`[self-review]`, `[peer-review]`, `[simulate-reviewers]`,...).
3. 06 merges only **after** 00 confirms isolated artifacts exist.
4. 06 does **not** re-run first-pass base engines; it re-reviews and adjudicates.

## Pointers

- A route: `route.md` (re-review only)
- A envelope: `review.md`
- 00 checks: `00_orchestrator/gates.md` section top-layer QC checks
- Body engines: `06_review/base/simulate-reviewers/`, `self-review/` (self-review), `peer-review/` (peer-review)
- Optional base README: `06_review/base/REVIEW-ISOLATION.md`

## R&R re-review

Post-QC 06 re-review is **verification only**. Use `00_orchestrator/templates/rr-traceability.md`. See `runtime-flow.mmd` `P06r` / `handoff.md`.
