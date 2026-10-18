---
name: "write-polish"
domain: "05_manuscript"
trigger: ["润色", "polish", "学术英语", "Introduction lint"]
outputs: ["polished_prose", "lint_report"]
owner: "05-manuscript/write-polish/MODULE.md"
---

# Generic language polish

Academic English / house polish. Does **not** replace A personal de-AI. Generic de-AI is B `humanize` (`05-manuscript/humanize/`); personal list still wins.

Backup: MedSci `skills/polish-language/`.

## Introduction / Discussion lint (report only; never change numbers or citations)

Run before polishing and again after. Output one table: check, result, sentences affected.

| Check | Rule |
|---|---|
| Sentence length | 10–30 words; list sentences outside the range |
| Repeated openers | Same first two words in three or more sentences of a paragraph |
| Triplets | More than one "X, Y, and Z" series in a paragraph |
| Number-and-cite chain | Three consecutive sentences that each carry a number and a citation |
| Connector chain | Consecutive sentences opened by However, Moreover, Therefore, In addition |
| Uniform length | Three consecutive sentences within ±3 words of each other |
| Reporting standards | TRIPOD, CLAIM, or CLEAR named in the Introduction |
| Abbreviations | Defined at first use in the body |
| Claim coverage | Literature claims with no citation in their sentence or same-source group (listed, not gated) |

Fixes are proposals for A 05 at sentence unit: merge, split, or restructure. Never rewrite a whole paragraph.
