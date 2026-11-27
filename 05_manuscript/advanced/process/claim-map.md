# Claim Map (pre-draft claim-evidence plan)

**Owner:** `05_manuscript` advanced. This is a writing-prep plan, **not a QC gate**.
**Not:** a new fine id, a second audit, or a replacement for `evidence.md`, `result-to-claim.md`, `paper-claim-audit-gate.md`, or `claim-number-align.md`.

## Purpose

Before drafting (or when revising a load-bearing sentence), make each main claim explicit and tie it to:

Claim → evidence source → statistical support (when the claim is from this study) → wording level → manuscript location.

The map is a planning aid for `write-paper`. Whether the finished prose is actually supported, and whether numbers match the sources, remains the job of the existing claim QC files.

## When to load

写全文 · 写结果 / 讨论 · 起草或改写主张 · 收紧结论措辞. Load before `write-paper` modes `draft-section` or `full-imrad`, and again if a load-bearing claim changes.

Do not wait until pre-submit QC to discover that a conclusion has no source.

## Inputs

- User-locked study aim, design, endpoints, and statistical plan (do not revise these to make a sentence writable)
- Supplied results: tables, figures, `*-results.html`, or a named 02 handoff
- Verified literature rows, when a background or framing claim needs a citation (`evidence.md`)
- The current draft, when this is a revision rather than a first draft

Missing inputs stay missing: comment (author **A**) and leave the claim open, weaken it, or drop it. Never invent a number, a citation, or an unrun analysis.

## Outputs

A short map (Word comment, handoff note, or project `ref/` scratch). Working labels such as C1, C2 are local to this manuscript. They are not registry / fine ids and do not start a new ID scheme.

The map may later be offered as the intended-claims list to `result-to-claim.md`. This file must **not** emit `RESULT_TO_CLAIM.json` or `PAPER_CLAIM_AUDIT.json`, and it must not assign PASS / FAIL.

Compact row (omit a cell when it does not apply):

```text
Claim ID | Claim | Type | Evidence source | Statistical support | Strength | Wording | Location | Limitation | Status
```

## Fields (keep light)

| Field | What to record |
|---|---|
| Claim ID | Stable in-manuscript label (C1, C2, …) |
| Claim | One core meaning per row; split compound sentences |
| Claim type | background, study aim, primary finding, secondary finding, mechanism interpretation, clinical implication, or limitation |
| Evidence source | The table, figure, stats output, or verified reference that actually supports the row |
| Statistical support | Effect, 95% CI, *P*, model metric, or adjusted result, only when the claim is from this study's data; otherwise leave the cell blank |
| Evidence strength | direct / indirect / insufficient / conflicting |
| Wording level | keep / hedge / hypothesis / drop (observational findings stay *associated with* unless the design supports more) |
| Manuscript location | Abstract, Introduction, Results, Discussion, Conclusions, or a named table/figure callout |
| Limitation | Scope, confounding, or why a stronger verb is not allowed |
| Status | open / keep / weaken / delete |

Do not force every cell on every row. Introduction background usually needs a verified literature source, not a study statistic. Primary Results rows need this study's numbers.

## Hard constraints

1. Do not search for evidence in order to justify a pre-chosen strong conclusion. Fix wording to the evidence you already have.
2. If evidence is insufficient or conflicting: **weaken**, **qualify**, or **delete** the claim. Do not hide the gap with rhetoric.
3. Mechanism interpretation and clinical implication must not be written as results this study has directly verified, unless the locked design and the supplied data actually tested them.
4. Do not change a user-locked study design or statistical plan so that a stronger claim becomes writable.
5. Do not invent statistical results, sample sizes, procedures, ethics IDs, or citations.

## Procedure

1. Pull candidate claims from the locked aim, the named endpoints, and the supplied results (plus verified literature for background or framing).
2. Split compound claims so each row has one core meaning.
3. Point each row at a direct source. Literature gaps are raised through `evidence.md` (Part A): 03 searches, A 05 Accept / Weaken / Delete. 05 does not run a literature-research route of its own.
4. Judge strength, then set wording to match. Place the claim in the fitting IMRAD slot.
5. Apply weaken / qualify / delete now for weak or conflicting rows.
6. After the prose exists, the existing gates still run unchanged (see Call graph). This plan is an input, not their verdict.

## Call graph

| Direction | File | Role |
|---|---|---|
| Entry | `05_manuscript/base/write-paper/MODULE.md` (and the thin `SKILL.md`) | Load this plan before `draft-section` / `full-imrad` |
| Literature gaps | `05_manuscript/advanced/process/evidence.md` | Request, consume, and judge citations; do not copy that protocol here |
| After drafting | `05_manuscript/qc/result-to-claim.md` | Layer 2: does the reported result support the scientific claim |
| After drafting | `05_manuscript/qc/paper-claim-audit-gate.md` | Layer 3: does the manuscript report numbers truthfully |
| After drafting | `05_manuscript/qc/claim-number-align.md` | Prose / table / figure number alignment |
| Downstream | `05_manuscript/advanced/process/figure-table-plan.md` | Which claims need a main-text display; do not copy that plan here |

## Out of scope

- Study-type routing, quantitative style metrics, method-experiment alignment, or an intake brief
- New fine ids, new gates, or changes to 00 gate composition or 02 figure production
- Restating the QC checklists in this file

*Method reference (abstract rewrite; no source-skill text, paper excerpts, or templates copied): [gulucaptain/Best-Paper-Writing-Skill](https://github.com/gulucaptain/Best-Paper-Writing-Skill), absorbed 2026-11-27. See `NOTICE`.*
