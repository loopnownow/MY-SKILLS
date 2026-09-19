# Introduction scorecard

**Owner:** `05_manuscript` personal. Use it as a self-check after drafting and as an independent score before submission. A drafter's own score is provisional; it is never the final score.

Seven dimensions, 0–10 each, total 70. Start every dimension at 10, apply the deductions below, floor at 0, then apply the caps. Write the deduction codes next to each score.

| # | Dimension | Question |
|---|---|---|
| 1 | Logic | Does each paragraph follow from the last, under one endpoint frame? |
| 2 | Fluency | Does it read as one argument, without listing or repeated frames? |
| 3 | Citation use | Does each literature claim have the right source, verified to the right level? |
| 4 | Prior results | Are the main results of the most relevant studies stated and appraised? |
| 5 | Gap | Is the gap a specific unknown, traceable to the guideline, with what the evidence already shows? |
| 6 | Method link | Could this study's method plausibly address the gap, and does the text say why? |
| 7 | Aim and hypothesis | Are aim, endpoint, set, and comparator explicit and testable? |

## Deduction codes

| Code | Dim | Trigger | Deduct | Fix at writing time |
|---|---|---|---|---|
| LOG-1 | 1 | The Introduction frames a guideline construct, but the aim or Methods name a different endpoint and no clause says how they relate | 1.5 | Fix the frame first: element 2 states the construct, element 6 names the endpoint, one clause states the relation; algorithm details stay in Methods |
| LOG-2 | 1 | A sentence sits where it does for citation numbering or for a writing standard (TRIPOD) rather than for the argument | 1 | Claim–source fit outranks numbering; renumber by script; no reporting standards in the Introduction |
| LOG-3 | 1 | A paragraph reports studies one after another with no group appraisal | 1.5 | One or two sentences: the strength this study keeps, the weakness it targets |
| FLU-1 | 2 | Three or more sentences in a paragraph open with the same words or the same frame | 2 | Change the subject and the structure; put the number inside a comparison |
| FLU-2 | 2 | A run of three sentences that each carry a number and a citation | 1 | Merge into one comparative sentence, or drop the weakest |
| FLU-3 | 2 | More than 10% of sentences outside 10–30 words | 1 per 10%, max 3 | Split or merge |
| CIT-1 | 3 | A literature claim with no citation in its sentence or its same-source group | 1 per 2 claims | Cite, weaken, or delete (`evidence-request.md`) |
| CIT-2 | 3 | More than 15 references without a recorded ranking, or an incomplete entry (volume, pages, DOI) | 1 | Budget before drafting; complete the entry |
| CIT-3 | 3 | Numbers verified below L2, or a guideline definition or appraisal verified below L3 | 1 | Read the full text, or weaken to "reported" |
| CIT-4 | 3 | No retraction and correction check on the reference list | 1 | Run it |
| RES-1 | 4 | Only favourable results are reported | 1.5 | Include one weaker or limited result if one exists |
| RES-2 | 4 | Fewer than two of the three result classes covered, or the search log lacks a second source | 1.5 | Raise `missing_prior_result`; log the search |
| GLD-1 | 5 | Element 2 is missing, cites a superseded edition, or the gap is not traceable to the guideline | 2 | Raise `guideline_definition`; mine the open issue |
| GAP-1 | 5 | A scarcity claim with no logged search | 1 | Raise `scarcity_check` |
| GAP-2 | 5 | A field-wide statement drawn from one study | 1 | Write "in the studies we identified", or find a second |
| GAP-3 | 5 | The gap does not say what existing evidence already shows | 1 | State the settled part, then the unknown |
| MET-1 | 6 | No map from gap to method to expected benefit to measured output | 2 | Keep the map in the comment; one hedged sentence in the text |
| MET-2 | 6 | The method is said to solve the gap (*solves*, *overcomes*, *resolves*) | 2 | *may address part of* |
| MET-3 | 6 | The link rests on an assertion with no support and no hedge | 2 | Add a supporting source, or word it as inference |
| AIM-1 | 7 | The endpoint origin is not stated in one clause when it differs from the guideline construct | 2 | See LOG-1 |
| AIM-2 | 7 | The hypothesis has no set or no comparator | 2 | Name the test set and the comparator |
| AIM-3 | 7 | The endpoint name differs between Abstract, Methods, and Introduction | 1 | One name |

## Caps

- No quantified prior result: dimension 4 ≤ 3
- No explicit gap sentence: dimension 5 ≤ 4
- No hypothesis: dimension 7 ≤ 3
- A number in the Introduction that does not match its source: dimension 3 ≤ 4, and stop for correction

## Procedure

1. Run the Introduction lint (`05-write-polish`) and keep its table as evidence for FLU and CIT-1.
2. Score each dimension and write the codes.
3. The scorer is not the drafter: a different mount (`nature-reviewer`, isolated) or the user. A drafter's score is labelled *provisional*.
4. Record the date, manuscript, scorer, and the scores with codes.

## Record: Risk manuscript, first rewrite (2026-09-19, provisional, self-check)

Logic 6 (LOG-1, LOG-2, LOG-3) · Fluency 7 (FLU-1, FLU-2) · Citation use 7 (CIT-2, CIT-3, CIT-4) · Prior results 7 (RES-1, RES-2) · Gap 7 (GAP-1, GAP-2, GAP-3) · Method link 6 (MET-1, MET-3) · Aim 8 (AIM-1) · total 48/70.

The 25% sentence-level uncited gate used at that time is replaced by claim coverage (`intro-discussion-evidence.md`). Re-scored with GLD-1 (the rewrite cited the 2016 consensus, not the latest guideline): Gap 5, total 46/70.
