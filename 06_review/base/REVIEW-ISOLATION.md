# Review isolation (B 06-review)

Capability engines live here. Orchestration / post-QC re-review authority lives in A `06_review`.

## First-pass pattern

1. `simulate-reviewers/` -- keep personas isolated
2. In parallel: `review-critique/` (self-review) || `review-peer/` (peer-review)
3. Hand isolated finding artifacts to **00 QC**, then A06 re-review

Do not merge finding sets inside B before A06. See A `06_review/personal/review-isolation.md`.
