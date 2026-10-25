---
name: "polish-language"
domain: "05_manuscript"
trigger: ["润色", "polish", "学术英语", "Introduction lint"]
outputs: ["polished_prose", "lint_report"]
owner: "05_manuscript/base/polish-language/MODULE.md"
---

# Generic language polish

Academic English / house polish. Does **not** replace A personal de-AI. Generic de-AI is
`humanize` (`05_manuscript/base/humanize/`); personal list still wins.

## Introduction / Discussion lint (report only; never change numbers or citations)

Run before polishing and again after. Output one table: check, result, sentences affected.

| Check | Rule |
|---|---|
| Sentence length | Target 10–30 words; list sentences outside it. Measurable bands are short ≤ 12 words / long ≥ 25 words / ceiling 70, identical to `check_sentence_variety.py` (`05_manuscript/base/humanize/scripts/`), so the lint table and the gate cannot disagree |
| Repeated openers | Same first two words in three or more sentences of a paragraph |
| Triplets | More than one "X, Y, and Z" series in a paragraph |
| Number-and-cite chain | Three consecutive sentences that each carry a number and a citation |
| Connector chain | Consecutive sentences opened by However, Moreover, Therefore, In addition |
| Uniform length | Three consecutive sentences within ±3 words of each other. The formal verdict is `SENTENCE_UNIFORM` from the script named above; it is silent below 15 sentences |
| Reporting standards | TRIPOD, CLAIM, or CLEAR named in the Introduction |
| Abbreviations | Defined at first use in the body |
| Claim coverage | Literature claims with no citation in their sentence or same-source group (listed, not gated) |

Fixes are proposals for A 05 at sentence unit: merge, split, or restructure. Never rewrite a whole
paragraph.

## Division with humanize

- This pack **reports** rhythm items. `humanize` **measures and rewrites** them (Fix rule 7,
  Patterns 25-27). Do not score the same sentence twice in one round: the lint table feeds the
  report, the script plus the humanize pass drives the fix.
- Order stays `polish-language` → `humanize` (`05_manuscript/personal/route.md`).
- de-AI ban lists are not here: `05_manuscript/base/vocab/L1/ban-phrases.md` wins.

## On-demand references

| File | Open when |
|---|---|
| `radiology-polishing/style-guardrails.md` | Overclaiming / causation / hedging sweep while polishing prose |
| `radiology-polishing/stat-reporting.md` | Radiology/AMA number formatting. House-style authority is `05_manuscript/base/write-paper/radiology-polishing/radiology-house-style.md`; on conflict that file wins |
