# Introduction (generic contract)

The `05_manuscript/advanced/` layer (house format, quotas, forbidden lists) overrides this file. This file states what a defensible Introduction contains, whichever house style applies.

Aligned with `05_manuscript` Introduction v4 (owner 2026-10-30 t1401u/t1402u: five paragraphs, eight beats). Frontiers/graylist are 选刊-side only.

## Paragraph map (funnel)

| Para | Beats |
|------|-------|
| 1 | Disease / burden → clinical significance |
| 2 | Guideline definition (diagnostic or examination criteria) → current standards / methods |
| 3 | Latest research methods used in this study → related studies |
| 4 | Gap and method link |
| 5 | Aim and hypothesis (**no citations**) |

## Elements (eight beats)

1. **Disease / burden** (para 1). Opening cites the verified source when one exists.
2. **Clinical significance** (para 1). Why the disease or decision matters for patients or practice.
3. **Guideline definition** (para 2). Latest edition that defines the endpoint or the clinical decision (diagnostic criteria or examination criteria): paraphrase; state the decision that rests on it.
4. **Current standards / methods** (para 2). Routine standards or tests the guideline relies on, and what they leave open or cannot resolve.
5. **Latest research methods (this study)** (para 3). Name the method family this study uses (e.g. radiomics, nomogram), hedged as current research practice, not as a solved problem.
6. **Related studies** (para 3). Main results of the two or three most relevant (n, design, effect), then a group appraisal: the strength this study keeps and the weakness it targets. No study-by-study list.
7. **Gap and method link** (para 4). One open question as an unknown, then one hedged sentence on why this study's method may address it (*may* / *could*; never *solves* / *overcomes* / *resolves*).
8. **Aim and hypothesis** (para 5). No citations. One endpoint name; the set and the comparator named.

## Writing rules

- Sentences of 10-30 words, one main proposition each.
- Synthesize; do not list. No run of sentences that each report one study. At most one triplet per paragraph. No repeated sentence openers.
- Scarcity is worded as what a logged search found ("in the studies we identified"), not as what exists.
- Inference about why a method may help is allowed. Hedge it, and keep the gap - method - expected benefit - measured output map in a comment.
- Reporting guidelines (TRIPOD, CLAIM, CLEAR) belong to the checklist and the submission form, not to the Introduction. Route to `check-reporting`.
- Numbers only from sources read at abstract level or above; guideline definitions and appraisals from the full text.
- Missing evidence - an Evidence Request card (`missing_prior_result`, `guideline_definition`, `related_work_appraisal`, `scarcity_check`), never a guessed citation.
- **Citation number order:** claim-source fit outranks ascending numbers; never move a sentence only to keep numbers ascending. After drafting (or on revise), renumber in-text Vancouver citations to appearance order against the reference list by script; authenticity stays with `verify-refs`.

## Handoff

Evidence: `meta-analysis` (`02_data-processing/base/meta-analysis/`) and `lit-search` (Introduction evidence pack). Language: `humanize`. Reporting: `check-reporting`. Citation authenticity: `verify-refs`. Self-audit: `self-review`. Advanced scoring / house quotas: `05_manuscript/advanced/` (not duplicated here).
