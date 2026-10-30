---
name: "peer-review"
domain: "06_review"
trigger: ["评阅", "审稿", "peer review", "审他人稿"]
inputs: ["manuscript_docx"]
outputs: ["peer_review_letter"]
tools: ["dealbreakers"]
quality_control: "flag leakage first; do not invent rescue experiments"
owner: "06_review/base/peer-review/MODULE.md"
---

Checklist (AI + public-data/imaging): [references/ai-public-data-imaging-checklist.md](references/ai-public-data-imaging-checklist.md).

trigger is documentation only; not independently discoverable.

# Other-paper peer review

Write an English review of **someone else's** manuscript. This pack is **other-paper only**.

Retired id `peer-review-pdf-scan` (PDF inject/attack scan, Phase 1.5) resolves here.

- Self-audit / pre-submission of the user's own draft → `self-review`
- Point-by-point response letter → `revise` (this MODULE does **not** own mode-3)
- Sentence rewrite → `write-paper` / `humanize`
- Advanced review voice stays in `06_review/advanced/`

## When to use

The user is a reviewer of **another** group's paper and needs a submittable English review.

## Workflow

1. Identify study type (DTA / prediction / radiomics / other).
2. Scan [dealbreakers.md](references/dealbreakers.md) before cosmetic comments.
3. Structure the letter with [review-report-format.md](references/review-report-format.md) and
   [mode-2-prereview.md](references/mode-2-prereview.md) (other-paper path only).
4. Each comment: fact → why it is a problem → what the authors should do.
5. Do not invent experiments, AUC, or ethics numbers. Do not rewrite the paper.

## Letter shape

```text
[Opening 2-4 sentences: design + clinical question + value + methodological catch]

Major Comments
Abstract / Introduction / Methods / Results / Discussion / Limitations
…

Other / Minor
…
```

Recommendation (Accept / Minor / Major / Reject) stays in an **internal note**, not in the
submitted letter unless the journal form requires it.

## Frequent methodological catches

Leakage, non-patient-level split, ROI/reader opacity, no external validation while claiming
generalisability, overclaim, missing calibration/DCA when clinical utility is claimed.

## Envelope

```text
Skill: peer-review
Path: peer-review-others

[Letter]

Internal note: dealbreakers — [list or none]
```

Principles extracted from cross-package research (not a fine id; rule reference only): [external-principles.md](references/external-principles.md)

## On-demand references

| File | Open when |
|---|---|
| `references/manuscript-quality.md` | What "quality" means in an other-paper review report |
