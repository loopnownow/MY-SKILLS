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
| elucidat* (elucidate / elucidating / elucidated) | purpose/aim: exploring; mechanism-unknown: remain unclear (not explain / clarify) |

| novel | (drop, or name what changed) |
| notably | delete; state the fact |
| interestingly | delete; state the fact |
| importantly | delete, or restructure so the load-bearing sentence carries its own weight |

**Policy reversal, 2026-08-29 (user editorial decision, not a corpus
contradiction):** *novel*, *notably*, *interestingly*, *importantly* are now
**banned**. This overrides the prior "not banned — corpus-verified" entry
below, which is kept for historical record, not as current guidance. The
corpus evidence itself hasn't changed — these words are still genuinely
attested, used sparingly and purposefully, in the source manuscripts (see
counts and in-context examples preserved in `corpus-phrase-bank.md`
§8). The user has simply chosen, as an editorial stance independent of
frequency data, to cut them regardless. Do not re-litigate this by
re-citing the corpus counts as a reason to un-ban; the counts were never in
dispute, the policy is a separate choice on top of them.

<details>
<summary>Superseded reasoning (pre-2026-08-29, kept for history — do not act on this)</summary>

Not banned — corpus-verified: *novel* (59 occurrences in the deduplicated
corpus), *notably* (21), *interestingly* (13), *importantly* (9). These are
used sparingly and purposefully in the edited, submission-ready manuscripts
— e.g. flagging one genuinely unexpected result, or the single clinically
load-bearing sentence in a paragraph — not as filler. Cut them when they're
decorative throat-clearing; keep them when they're doing that flagging work.
See `corpus-phrase-bank.md` §8 for verified examples.
</details>

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
