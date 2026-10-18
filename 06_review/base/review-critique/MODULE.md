---
name: "review-critique"
domain: "06_review"
trigger: ["自审", "投稿前预审", "找洞", "论文数字核对", "check paper claims"]
outputs: ["blocking_major_minor", "paper_claim_audit"]
owner: "06-review/review-critique/MODULE.md"
---

# trigger is documentation only; not independently discoverable.

# Self-audit / pre-submission

Find holes in **the user's own** manuscript before submission. Other-paper review is
`06-review-peer`. Point-by-point **response** is `07-review-response` — this pack does not
own 回复审稿人.

Personal review voice stays in A.

## When to open

| File | Open when |
|---|---|
| [pre-submission.md](references/pre-submission.md) | Simulated reviewer critique of own draft |
| [pre-submission-hard-gates.md](references/pre-submission-hard-gates.md) | Final hard-gate audit |
| [review_checklist_export.md](references/review_checklist_export.md) | Exportable checklist |
| [paper-claim-audit.md](references/paper-claim-audit.md) | Zero-context number/claim vs primary tables (Word+evidence); before submit or after major number changes |

## Workflow

1. Confirm venue/study type. Do not fill title-page ethics/author fields here.
2. Scan leakage, split, validation, overclaim, reporting gaps.
3. Output Blocking / Major / Minor with a concrete fix each.
4. Do not invent rescue experiments. Prose rewrite → `05-write-manuscript`.
5. For number fidelity vs primary tables → [paper-claim-audit.md](references/paper-claim-audit.md).
