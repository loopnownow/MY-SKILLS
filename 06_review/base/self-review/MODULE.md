---
name: "self-review"
domain: "06_review"
trigger: ["自审", "投稿前预审", "找洞", "论文数字核对", "check paper claims"]
outputs: ["blocking_major_minor", "paper_claim_audit"]
owner: "06_review/base/self-review/MODULE.md"
---

trigger is documentation only; not independently discoverable.

# Self-audit / pre-submission

Find holes in **the user's own** manuscript before submission. Other-paper review is
`peer-review`. Point-by-point **response** is `revise` — this pack does not
own 回复审稿人 (response to reviewers).

Contract only: this pack states scope, bans, and pointers. The generic review envelope is `06_review/base/peer-review/references/review-envelope.md`; review voice, opener templates and the statement-then-data protocol are `06_review/advanced/review.md`; gate scores are `06_review/qc/`.

## When to open

| File | Open when |
|---|---|
| [pre-submission.md](references/pre-submission.md) | Simulated reviewer critique of own draft |
| [pre-submission-hard-gates.md](references/pre-submission-hard-gates.md) | Final hard-gate audit |
| [review_checklist_export.md](references/review_checklist_export.md) | Exportable checklist |
| [paper-claim-audit.md](references/paper-claim-audit.md) | Zero-context number/claim vs primary tables (Word+evidence); before submit or after major number changes |
| [reviewer-nits.md](references/reviewer-nits.md) | Pre-submission pass with the comment classes real reviewers write: design naming, executable inclusion, stats reporting, reproducibility, format nits |

## Workflow

1. Confirm venue/study type. Do not fill title-page ethics/author fields here.
2. Scan leakage, split, validation, overclaim, reporting gaps. Then run
   [reviewer-nits.md](references/reviewer-nits.md) for the reviewer-language classes (design
   naming, executable inclusion, statistics as reported, reproducibility, format nits).
3. Output Blocking / Major / Minor with a concrete fix each.
4. Do not invent rescue experiments. Prose rewrite → `write-paper`.
5. For number fidelity vs primary tables → [paper-claim-audit.md](references/paper-claim-audit.md).
