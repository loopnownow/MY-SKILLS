# Forbidden / replace table (lab SCI)

**Owner:** manuscript-core. Apply on every polish/draft/de-ai pass.

## Hard ban (unless literally quoted from a source)

| Avoid | Prefer |
|-------|--------|
| delve / dive deep | examine / assess |
| landscape | field / setting |
| pivotal / crucial / critical (hype) | important / key (sparingly) or name the finding |
| robust (vague) | name the metric (higher AUC, narrower CI) |
| comprehensive | complete / included X–Y |
| leverage | use |
| framework (vague AI prose) | approach |
| labeled / labelled (vague AI prose) | classified as / assigned to / named; abstract parts: headed Objective/Methods/… |
| locked (vague AI prose) | fixed / decided / settled / finalized |
| seamless | without additional steps / integrated |
| groundbreaking / state-of-the-art | drop or prove novelty with citation |
| surprisingly / remarkably | delete |
| proved | demonstrated |
| superior | outperformed / higher AUC than |
| will (prediction of clinical impact) | may / could |
| It is worth noting that | delete; state the fact |
| furthermore / moreover (stacked) | vary or cut |
| elucidat* (elucidate / elucidating / elucidated) | purpose/aim: exploring; mechanism-unknown: remain unclear (not explain / clarify) |

| novel | (drop, or name what changed) |
| notably | delete; state the fact |
| interestingly | delete; state the fact |
| importantly | delete, or restructure so the load-bearing sentence carries its own weight |

**Policy reversal, 2026-08-29:** *novel*, *notably*, *interestingly*, *importantly* are **banned**. Corpus counts do not lift the ban.

## Commentary voice (body ban)

Do not tell the reader how **not** to read the paper. Ban in the body:

- they should not be summarized as
- is not reported as
- should not be read as
- given this extent
- should not be described as
- rhetorical *rather than* / *but not by* that steer interpretation

Observational contrast may still use *associated with*. Do **not** blanket-ban factual *rather than* / *but not by* (e.g. *but not by sex*).

## Adverbs (new writing and polish)

Reduce adverb use. Short rule, not a lexicon: cut decorative *-ly* softeners and intensifiers. Do **not** ban statistical *significantly* when it is p-value language (already governed in `04_analysis/personal/stats-checklist.md` / Results reporting).

## Lab-unused stock (0 hits in 389 unique drafts, 2026-08-28)

These used to appear as recommended conclusion templates. Harvest of 389 unique drafts found **0** uses. Do not recommend; do not insert.

| Avoid | Prefer |
|-------|--------|
| suggesting its potential | name the task (`could assist [task]`) or drop the clause |
| demonstrated good performance | report `AUC of X (95% CI: X–X)` in training **and** test |

See `sentence-templates.md` and `corpus-phrase-bank.md` §1c.

## Also cut (stop-slop / detector overlap)

- Throat-clearing: "Here is…", "In this section we…"
- Binary contrast templates: "Not X, but Y" when Y alone suffices
- Em-dash stacks (Claude tell); prediction full papers: no em-dash
- Symmetrical three-item lists used as style filler
- Pull-quote one-liners ending every paragraph

## Keep (discipline-specific)

- Sequence names, gene symbols, anatomical terms
- Reporting-guideline language (STROBE/TRIPOD/CLAIM)
- Calibrated hedges in Discussion only: may, might, could, suggest

See also: `phrases.md`, `structures.md`, parent hard rules.
