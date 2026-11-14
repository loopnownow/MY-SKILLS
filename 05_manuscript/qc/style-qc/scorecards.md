# Style scorecards (QCV, soft): Introduction and Discussion

**Class:** QCV (style/voice). Not a science score. Load only at S4 (after the advanced revision) or on an explicit de-AI / polish request. Verdicts are PASS / WARN / FAIL-SOFT; a FAIL-SOFT never blocks a science gate (G-05 / G-FACT) and never merges into a QCS total. Report shape and the mapped checks: `style-qc.md` in this folder.

Purpose: score the house voice and structure of a draft that has already passed science QC. Personal style is not a scientific error.


## Introduction scorecard

> **QC routing:** Formal Gate/scoring ownership: `00_orchestrator`. This file is the 05 local checklist.


**Owner (checklist body):** `05_manuscript`. Use as a self-check after drafting and as an independent score before submission. A drafter's own score is provisional; **final Gate / scoring authority = `00_orchestrator`** (seats do not self-certify).

**Funnel contract (owner 2026-10-30 t1402u/t1404u):** five paragraphs / eight beats, authority `05_manuscript/advanced/Aitor-format.md` § Introduction. Para 1 = burden + clinical significance; para 2 = guideline (diagnostic or examination criteria) + current standards/methods; para 3 = this-study methods + related studies; para 4 = gap and method link; para 5 = aim/hypothesis (**no citations**). Score Logic against that map; do not invent a sixth body paragraph for the aim. The beats themselves are not restated here.

Seven dimensions, 0-10 each, total 70. Start every dimension at 10, apply the deductions below, floor at 0, then apply the caps. Write the deduction codes next to each score.

| # | Dimension | Question |
|---|---|---|
| 1 | Logic | Does each paragraph follow from the last, under one endpoint frame? |
| 2 | Fluency | Does it read as one argument, without listing or repeated frames? |
| 3 | Citation use | Does each literature claim have the right source, verified to the right level? |
| 4 | Prior results | Are the main results of the most relevant studies stated and appraised? |
| 5 | Gap | Is the gap a specific unknown, traceable to the guideline, with what the evidence already shows? |
| 6 | Method link | Could this study's method plausibly address the gap, and does the text say why? |
| 7 | Aim and hypothesis | Are aim, endpoint, set, and comparator explicit and testable? |

### Deduction codes

| Code | Dim | Trigger | Deduct | Fix anchor (advanced) |
|---|---|---|---|---|
| LOG-1 | 1 | The Introduction frames a guideline construct, but the aim or Methods name a different endpoint and no clause says how they relate | 1.5 | `05_manuscript/advanced/Aitor-format.md` § Introduction (beats 3 and 8) |
| LOG-2 | 1 | A sentence sits where it does for citation numbering or for a writing standard (TRIPOD) rather than for the argument | 1 | `05_manuscript/advanced/Aitor-format.md` § Citation (claim-source fit, renumber by script) |
| LOG-3 | 1 | A paragraph reports studies one after another with no group appraisal | 1.5 | `05_manuscript/advanced/Aitor-format.md` § Introduction (beat 6) |
| LOG-4 | 1 | Paragraph order or beat placement breaks the five-paragraph funnel (e.g. aim before gap; related studies before guideline; this-study method missing from para 3) | 2 | `05_manuscript/advanced/Aitor-format.md` § Introduction (paragraph map) |
| LOG-5 | 1 | An Introduction aim or hypothesis is never answered in Discussion (no matching finding, limitation, or explicit deferral) | 2 | `05_manuscript/advanced/Aitor-format.md` § Discussion (aim answered) |
| LOG-6 | 1 | Clinical significance (beat 2) is missing from para 1, or current standards/methods (beat 4) are missing from para 2 | 1 | `05_manuscript/advanced/Aitor-format.md` § Introduction (beats 2 and 4) |
| FLU-1 | 2 | Three or more sentences in a paragraph open with the same words or the same frame | 2 | `05_manuscript/advanced/Aitor-format.md` § Introduction (structure bans) |
| FLU-2 | 2 | A run of three sentences that each carry a number and a citation | 1 | `05_manuscript/advanced/Aitor-format.md` § Introduction (structure bans) |
| FLU-3 | 2 | More than 10% of sentences outside 10-30 words | 1 per 10%, max 3 | `05_manuscript/advanced/Aitor-format.md` § Introduction (sentence length) |
| FLU-4 | 2 | IMRAD body laid out as one sentence per line or one sentence per paragraph | 2 | `05_manuscript/advanced/voice-portrait.md` § 3 (paragraph lock) |
| CIT-1 | 3 | A literature claim with no citation in its sentence or its same-source group | 1 per 2 claims | `05_manuscript/advanced/process/evidence.md` § Claim coverage |
| CIT-2 | 3 | More than 15 references without a recorded ranking, or an incomplete entry (volume, pages, DOI) | 1 | `05_manuscript/advanced/Aitor-format.md` § Citation (quota) |
| CIT-3 | 3 | Numbers verified below L2, or a guideline definition or appraisal verified below L3 | 1 | `05_manuscript/advanced/process/evidence.md` § Verification levels |
| CIT-4 | 3 | No retraction and correction check on the reference list | 1 | `05_manuscript/advanced/process/citation-and-language.md` § Citation hygiene |
| CIT-5 | 3 | Introduction opening paragraph has no citation although a verified source for that claim exists | 2 | `05_manuscript/advanced/Aitor-format.md` § Introduction (beat 1) |
| CIT-6 | 3 | Consecutive sentences cite the same paper without a new claim that paper supports | 1 | `05_manuscript/advanced/Aitor-format.md` § Introduction (structure bans) |
| CIT-7 | 3 | DOI, author list, year, or volume copied from another manuscript, or a year/volume change without a source check | 2 | `05_manuscript/advanced/process/citation-and-language.md` § Citation hygiene |
| RES-1 | 4 | Only favourable results are reported | 1.5 | `05_manuscript/advanced/Aitor-format.md` § Introduction (beat 6) |
| RES-2 | 4 | Fewer than two of the three result classes covered, or the search log lacks a second source | 1.5 | `05_manuscript/advanced/process/evidence.md` § When to raise a card |
| GLD-1 | 5 | Beat 3 (guideline definition, para 2) is missing, cites a superseded edition, or the gap is not traceable to the guideline | 2 | `05_manuscript/advanced/process/evidence.md` § Guideline rule with `05_manuscript/advanced/Aitor-format.md` § Introduction (beat 3) |
| GAP-1 | 5 | A scarcity claim with no logged search | 1 | `05_manuscript/advanced/process/evidence.md` § Claim coverage (scarcity check) |
| GAP-2 | 5 | A field-wide statement drawn from one study | 1 | `05_manuscript/advanced/Aitor-format.md` § Introduction (beat 7) |
| GAP-3 | 5 | The gap does not say what existing evidence already shows | 1 | `05_manuscript/advanced/Aitor-format.md` § Introduction (beat 7) |
| MET-1 | 6 | No map from gap to method to expected benefit to measured output | 2 | `05_manuscript/advanced/Aitor-format.md` § Introduction (beat 7) |
| MET-2 | 6 | The method is said to solve the gap (*solves*, *overcomes*, *resolves*) | 2 | `05_manuscript/advanced/Aitor-format.md` § Introduction (beat 7) |
| MET-3 | 6 | The link rests on an assertion with no support and no hedge | 2 | `05_manuscript/advanced/process/evidence.md` § When to raise a card |
| AIM-1 | 7 | The endpoint origin is not stated in one clause when it differs from the guideline construct | 2 | `05_manuscript/advanced/Aitor-format.md` § Introduction (beat 8) |
| AIM-2 | 7 | The hypothesis has no set or no comparator | 2 | `05_manuscript/advanced/Aitor-format.md` § Introduction (beat 8) |
| AIM-3 | 7 | The endpoint name differs between Abstract, Methods, and Introduction | 1 | `05_manuscript/advanced/Aitor-format.md` § Abstract and § Introduction (beat 8) |

Fix cells are anchors only. The recipe (what to write, how many sentences, which band) lives at the anchor; if an anchor is missing, the fix is to add it there, never to write it into this file.

### Caps

- No quantified prior result: dimension 4 ≤ 3
- No explicit gap sentence: dimension 5 ≤ 4
- No hypothesis: dimension 7 ≤ 3
- A number in the Introduction that does not match its source: dimension 3 ≤ 4, and stop for correction
- Opening paragraph uncited when a verified source exists: dimension 3 ≤ 5

### Procedure

1. Run the Introduction lint (advanced De-AI: `05_manuscript/advanced/process/polisher-sections.md` section De-AI pass) and keep its table as evidence for FLU and CIT-1.
2. Score each dimension and write the codes.
3. The scorer is not the drafter: a different fine id (`simulate-reviewers`, isolated) or the user. A drafter's score is labelled *provisional*.
4. Record the date, manuscript, scorer, and the scores with codes.

### Record: Risk manuscript, first rewrite (2026-09-19, provisional, self-check)

Logic 6 (LOG-1, LOG-2, LOG-3) · Fluency 7 (FLU-1, FLU-2) · Citation use 7 (CIT-2, CIT-3, CIT-4) · Prior results 7 (RES-1, RES-2) · Gap 7 (GAP-1, GAP-2, GAP-3) · Method link 6 (MET-1, MET-3) · Aim 8 (AIM-1) · total 48/70.

The 25% sentence-level uncited gate used at that time is replaced by claim coverage (`05_manuscript/advanced/process/evidence.md`). Re-scored with GLD-1 (the rewrite cited the 2016 consensus, not the latest guideline): Gap 5, total 46/70.



---

## Discussion scorecard (inverted funnel)

**Owner (checklist body):** `05_manuscript`. House shape: `Aitor-format.md` Discussion. Run after Introduction scorecard on the same draft.

Five content beats + loop + craft, 0-10 each, total 70. Start at 10, deduct, floor at 0.

| # | Dimension | Question |
|---|---|---|
| 1 | Key findings | First paragraph states main findings without citations and without result numbers (AUC/CI/*n*/*P*)? |
| 2 | Literature contrast | Each load-bearing finding is compared to representative prior work, with agreement or disagreement explained? |
| 3 | Mechanism | Any mechanism claim is hedged and not presented as proven causality from an observational design? |
| 4 | Clinical application | One short use-case sentence; no disclaimer / CYA stack in body? |
| 5 | Limitations | Own paragraph; facts only; label circularity First when a predictor is part of the endpoint? Prefer no literature citations in Limitations? Ordinals (`First` / `Second` / `Third` …) sequential, complete, and in the actual sentence order, with the count matching the limitation sentences? |
| 6 | Intro loop | Every Intro aim/hypothesis has a matching Discussion response (finding, limitation, or explicit deferral)? |
| 7 | Craft | No listing cadence; sentences mostly 10-30 words; Conclusion echoes objective without AUC/CI/*n*? |

### Discussion deduction codes

| Code | Dim | Trigger | Deduct | Fix anchor (advanced) |
|---|---|---|---|---|
| D-KEY-1 | 1 | First Discussion paragraph has citations or result numbers | 2 | `05_manuscript/advanced/Aitor-format.md` § Discussion (item 1) |
| D-KEY-2 | 1 | Key findings omit a load-bearing Intro aim with no deferral | 2 | `05_manuscript/advanced/Aitor-format.md` § Discussion (item 1, aim answered) |
| D-LIT-1 | 2 | No comparison to prior work for a load-bearing finding | 1.5 | `05_manuscript/advanced/Aitor-format.md` § Discussion (item 2) |
| D-LIT-2 | 2 | Discussion reuses Introduction references as the only "new" lit without appraisal | 1 | `05_manuscript/advanced/Aitor-format.md` § Citation (10-15 new refs) |
| D-MECH-1 | 3 | Observational association worded as *causes* / *proves* / *demonstrates that X leads to* | 2 | `05_manuscript/advanced/voice-portrait.md` § 2 (voice) and `05_manuscript/advanced/process/citation-and-language.md` § Language |
| D-CLIN-1 | 4 | Missing clinical use-case, or disclaimer stack in body | 1.5 | `05_manuscript/advanced/Aitor-format.md` § Discussion (item 3); AL-5 comment rule |
| D-LIM-1 | 5 | Limitations not its own paragraph, or ends with tool-readiness CYA | 1.5 | `05_manuscript/advanced/Aitor-format.md` § Discussion (item 4) |
| D-LIM-2 | 5 | Limitations cites literature (prefer none; move the cite to the lit-contrast block if it carries a point) | 1 | `05_manuscript/advanced/Aitor-format.md` § Discussion (Limitations) |
| D-LIM-3 | 5 | Limitations ordinal labels missing, out of order, duplicated, or not matching sentence count/order | 1 | `05_manuscript/advanced/Aitor-format.md` § Discussion (Limitations) |
| D-LOOP-1 | 6 | Intro hypothesis unanswered in Discussion | 2 | `05_manuscript/advanced/Aitor-format.md` § Discussion (aim answered) |
| D-CRAFT-1 | 7 | Conclusion carries AUC / CI / *n*, or does not echo the objective | 1 | `05_manuscript/advanced/Aitor-format.md` § Discussion (item 5) |

### Discussion procedure

1. List Intro aims/hypotheses (para 5); tick each against Discussion.
2. Score dimensions; record codes.
3. Scorer is not the drafter (`simulate-reviewers` isolated, or the user).
4. Pair with `claim-number-align.md` (CN-4) and `result-to-claim.md` before freezing Conclusions.


---
