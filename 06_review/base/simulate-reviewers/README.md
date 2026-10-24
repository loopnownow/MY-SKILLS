# `nature-reviewer` skill

`nature-reviewer` simulates Nature-style pre-submission review from a reviewer viewpoint, helping authors find risks in novelty, significance, technical soundness, and reader value before submission.

## What it is for

- Stress-test a manuscript, abstract, figures, or results storyline before submission.
- Score originality, scientific importance, interdisciplinary readership, technical soundness, and readability on Nature official review axes.
- Produce three reviewer reports in mutually invisible independent contexts, then a separate cross-review synthesis after all three are frozen.
- Flag unsupported claims, technical defects, evidence-chain breaks, and barriers for non-specialist readers.
- Split opinions into `Major Concerns` and `Minor Comments`; mark Majors that block the core argument with `Blocking Yes`.
- Keep sharp opinions direct, professional, and evidence-backed; keep minor issues concrete and actionable; do not invent issues to pad the count.
- Prefer short clauses, commas, semicolons, parentheses, or short labels on their own line over dashes or colons as sentence glue; stable numbering, required hyphens, and immutable source formatting stay untouched.
- Cover an internal 12-axis technical checklist and bind every substantive comment to a claim pointer and a verifiable evidence locus.
- Cross-check terminology, units, numeric precision, Methods counts, and table support inside the manuscript; separate language issues from contradictions that weaken credibility.
- After all three reviewer reports are frozen, run an independent forensic consistency audit (arithmetic identities, metric bounds, aggregation level, body-vs-table contradictions, duplicate rows, dispersion anomalies, data provenance, reproducibility bar). Audit results do not feed back to reviewers and do not rewrite frozen reports.
- Do not coordinate or rewrite opinions early just to cut duplication; list a consensus only when at least two reviewers independently raised the same issue.
- Judge which readers will care about this work, and why.

## Typical requests

- “Review this introduction and Figure 1 like a Nature reviewer.”
- “Before submission, find the technical issues reviewers are most likely to attack.”
- “Give me three reviewer reports and a synthesis judgment — no rebuttal.”

## What you need to provide

- Full manuscript, abstract, key sections, figures, legends, or author notes.
- Target journal, field, and the review risks you worry about most.
- Limits on already-available or unavailable new experiments.

## Outputs

- Three peer-review style reports.

- Three peer-review style reports.
- One cross-review synthesis (written only after the three reports are frozen).
- Blocking Yes / No on Majors that threaten the core argument.
- Optional forensic consistency audit appendix (does not rewrite frozen reports).

## What it is not

- Not a rebuttal / response-letter writer (that is `07_response`).
- Not a substitute for journal selection (`03_research`).
- Not a place to invent experiments or AUCs the manuscript does not contain.
