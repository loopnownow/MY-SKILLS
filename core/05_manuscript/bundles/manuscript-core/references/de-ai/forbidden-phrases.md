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
| seamless | without additional steps / integrated |
| groundbreaking / state-of-the-art | drop or prove novelty with citation |
| surprisingly / remarkably | delete |
| proved | demonstrated |
| superior | outperformed / higher AUC than |
| will (prediction of clinical impact) | may / could |
| It is worth noting that | delete; state the fact |
| furthermore / moreover (stacked) | vary or cut |

**Not banned — corpus-verified (do not re-add to this table):** *novel*
(59 occurrences in the deduplicated corpus), *notably* (21), *interestingly*
(13), *importantly* (9). These are used sparingly and purposefully in the
edited, submission-ready manuscripts — e.g. flagging one genuinely
unexpected result, or the single clinically load-bearing sentence in a
paragraph — not as filler. Cut them when they're decorative throat-clearing;
keep them when they're doing that flagging work. See
`../corpus/corpus-phrase-bank.md` §8 for verified examples.

## Lab-unused stock (0 hits in 389 unique drafts, 2026-08-28)

These used to appear as recommended conclusion templates. Harvest of 389 unique drafts found **0** uses. Do not recommend; do not insert.

| Avoid | Prefer |
|-------|--------|
| suggesting its potential | name the task (`could assist [task]`) or drop the clause |
| demonstrated good performance | report `AUC of X (95% CI: X–X)` in training **and** test |

See `../sentence-templates.md` and `../corpus/corpus-phrase-bank.md` §1c.

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
