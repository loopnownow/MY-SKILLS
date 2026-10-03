---
name: citation-verify
owner: 03_research
audience: Victor
required_before:
  - gate_05_done
  - gate_06
self_certify: forbidden
outputs:
  - claim_ref_table
  - strong_claim_spot_check
---

# Citation verify (Victor)

Required before a 05 deliverable is done (Gate · 05; semantic label **G-CIT-1**, draft evidence verification) and inside every 06 review (semantic label **G-CIT-2**, post-revision / inside 06). G-CIT-1 does not waive G-CIT-2. These names are labels, not new gate ids. 05 and 06 **call/require 03 citation-verify — do not self-certify lit**. A prior 05 pass does not waive the 06 pass. Mid-entry into 05 or 06 does not waive it.

Mounted `verify-refs` may check metadata. Victor owns this pass. Victor owns citation-verify (Lit05/Lit06) and supplies suggested literature for comments when needed. He does not apply manuscript Track Changes. Aitee keeps Accept / Weaken / Delete on the sentence after the table comes back and applies Track Changes. Lee keeps statement consistency, then data consistency. Literature accuracy is joint with Victor.

All manuscript Track Changes are owned by Aitee (05). Lee must not self-revise as default. Lee marks/comments; Aitee applies Track Changes. Decidable issues: Lee annotates for Aitee to TC-fix and does not apply the body revisions as default. Undecidable issues: Chinese 批注 body plus attached English suggested wording and/or suggested literature.

## Output

No manuscript prose. Return a claim→ref table and a spot-check note.

| claim_id | locus | claim | ref | doi or pmid | level | match |
|---|---|---|---|---|---|---|

`level` is L1 metadata, L2 abstract or full text for numbers, L3 full text for guideline definitions and appraisals. `match` is yes, weaken, or fail.

## Steps

1. **Claim→ref table.** One row for every literature claim in the Introduction and Discussion. Methods stay uncited. Element 6 of the Introduction and the Discussion's first paragraph stay uncited (`Aitor-format.md`).
2. **Spot-check strong claims against the source.** Population, modality, direction of effect, author list, year, volume, DOI. A string copied from a sister manuscript is not a check. A year or volume "correction" counts only after the source confirms it.
3. **Fail the row** when the sentence asserts something the cited work does not claim, when consecutive sentences cite the same paper without a new claim, or when the DOI or author list was not read against the work. Do not invent a PMID or DOI.
4. **Hand back.** Fails return to 05 for wording (Accept / Weaken / Delete) or stay as 06 comments with the G-LIT dual plan. When a comment needs a substitute or supporting ref, Victor supplies suggested literature. Lee marks/comments; Aitee applies Track Changes. 00 may still decide whether a further substitute-ref search runs. 00 does not waive this verify pass.

## Not this file

- New Introduction search → `literature/intro-evidence-pack.md`
- Number conflicts inside the cohort → `04_analysis/personal/stats-consistency.md` and `05_manuscript/personal/pre-submit-consistency.md` (annotate only; do not invent the number)
