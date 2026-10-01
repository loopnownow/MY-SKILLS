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

Required before a 05 deliverable is done (Gate · 05) and inside every 06 review. 05 and 06 **call/require 03 citation-verify — do not self-certify lit**. A prior 05 pass does not waive the 06 pass. Mid-entry into 05 or 06 does not waive it.

Mounted `verify-refs` may check metadata. Victor owns this pass. Aitee keeps Accept / Weaken / Delete on the sentence after the table comes back. Lee keeps statement consistency, then data consistency. Literature accuracy is joint with Victor.

## Output

No manuscript prose. Return a claim→ref table and a spot-check note.

| claim_id | locus | claim | ref | doi or pmid | level | match |
|---|---|---|---|---|---|---|

`level` is L1 metadata, L2 abstract or full text for numbers, L3 full text for guideline definitions and appraisals. `match` is yes, weaken, or fail.

## Steps

1. **Claim→ref table.** One row for every literature claim in the Introduction and Discussion. Methods stay uncited. Element 6 of the Introduction and the Discussion's first paragraph stay uncited (`Aitor-format.md`).
2. **Spot-check strong claims against the source.** Population, modality, direction of effect, author list, year, volume, DOI. A string copied from a sister manuscript is not a check. A year or volume "correction" counts only after the source confirms it.
3. **Fail the row** when the sentence asserts something the cited work does not claim, when consecutive sentences cite the same paper without a new claim, or when the DOI or author list was not read against the work. Do not invent a PMID or DOI.
4. **Hand back.** Fails return to 05 for wording (Accept / Weaken / Delete) or stay as 06 comments with the G-LIT dual plan. 00 may still decide whether a further substitute-ref search runs. 00 does not waive this verify pass.

## Not this file

- New Introduction search → `literature/intro-evidence-pack.md`
- Number conflicts inside the cohort → `04_analysis/personal/stats-consistency.md` and `05_manuscript/personal/pre-submit-consistency.md` (annotate only; do not invent the number)
