# Review isolation (06_review)

Capability engines live here. Orchestration / post-QC re-review authority lives in `06_review`.

## First-pass pattern

1. `simulate-reviewers/` -- keep personas isolated
2. In parallel: `self-review/` || `peer-review/`
3. Hand isolated finding artifacts to **00 QC**, then 06 re-review

Do not merge finding sets inside base before 06. See `06_review/personal/review-isolation.md`.
