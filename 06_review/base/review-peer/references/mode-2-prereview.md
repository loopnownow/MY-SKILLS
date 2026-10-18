# Other-paper English peer review

This file is the **other-paper** path only. Pre-submission of the user's own draft lives in
`06-review-critique`. Response letters live in `06-review-response` (mode-3).

Personal review-style corpora stay in A.

## When to use

The user is reviewing **another** group's manuscript and needs a letter the journal system
will accept.

## Workflow

1. Identify study type (DTA / prediction / radiomics / other).
2. Open:
   - [dealbreakers.md](dealbreakers.md)
   - [review-report-format.md](review-report-format.md)
   - Reporting checklists → `05-write-reporting` (not a retired writing-generic mount)
3. Each comment: fact → why it is a problem → what the authors should do (point to Abstract /
   Methods / Table X). Do not invent unrun experiments or AUC.
4. Deliver the letter below. Keep Accept/Minor/Major/Reject in an **internal note**.

## Letter

```text
[Opening 2–4 sentences: design + clinical question + overall value + the methodological catch]

Major Comments

Abstract / Title
…

Introduction
…

Methods
…

Results
…

Discussion / Limitations
…

Other / Minor
… language, abbreviations, figure legends, ethics placeholders
```

Numbered `#n` comments are optional, not the default.

## Frequent catches (write if present, skip if absent)

1. Discussion / limitations incomplete
2. ROI / segmentation reproducibility (who, tumour vs node, inter-/intra-observer, blinding)
3. Sample-size / missing-record bias
4. Ethics placeholder / missing approval
5. No comparison with conventional imaging or clinical factors (DeLong, NRI/IDI, calibration, DCA)
6. Language / abbreviations
7. Near-perfect training AUC with a large test drop → overfitting
8. Feature selection on the full dataset (leakage)
9. Scanner parameters / multi-vendor consistency
10. "External validation" that is same-hospital temporal split

## Forbidden

Empty praise ("interesting"); scores without a fix; importing a Chinese A–F score sheet into
the English letter; owning mode-3 response.

## Internal note (not submitted)

```text
Skill: 06-review-peer
Recommendation: Accept | Minor revision | Major revision | Reject
Dealbreakers: [list, or none]
```
