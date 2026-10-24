# Forbidden / replace table (lab SCI)

**Owner:** manuscript-core. Apply on every polish/draft/de-ai pass.
**Authority (skill SSOT after 2026-10-18):** standing body/comment bans live in `05_manuscript/qc/manuscript-local-qc.md`. This file is the phrase/table detail (`ban-terms.yaml` = machine source). Do not fork standing bans here.

## Exception checks (before applying a ban)

1. **Quoted from a source** — Hard-ban terms are allowed only when literally quoted from a cited source.
2. **Technical stem collision** — Keep discipline nouns that share a banned stem (e.g. imaging *attenuation*; metric names like *relative CBF* / *relCBF*). Rewrite only when the surrounding prose uses the banned word as comparison/hype.
3. **Keep list** — Sequence/gene/anatomy terms, reporting-guideline language (STROBE/TRIPOD/CLAIM), and calibrated Discussion hedges (*may* / *might* / *could* / *suggest*) stay; see **Keep (discipline-specific)** below.


**Machine source = `ban-terms.yaml`; edit the yaml first, then regenerate/sync tables and linters.** This file is for humans. Machine enforcement of hard-ban terms follows `05_manuscript/base/vocab/L1/ban-terms.yaml` (personal/vocab is pointer-only) as authority（`00_orchestrator/scripts/style_lint.py` 运行时读取）。

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
| attenuated | reduced / lower / decreased |
| disentangled / disentangle* | separated / distinguished / isolated / teased apart (plain wording) |

| novel | (drop, or name what changed) |
| notably | delete; state the fact |
| interestingly | delete; state the fact |
| importantly | delete, or restructure so the load-bearing sentence carries its own weight |

**Policy reversal, 2026-08-29:** *novel*, *notably*, *interestingly*, *importantly* are **banned**. Corpus counts do not lift the ban.

**Disentangled (2026-10-14):** AI-ism. Ban *disentangle / disentangled / disentangling*. Prefer *separated*, *distinguished*, *isolated*, or plain *teased apart*.

**Attenuated (2026-10-03):** AI-ism. Replace with *reduced*, *lower*, or *decreased*. The imaging noun *attenuation* (attenuation correction, beam attenuation) is not this ban.

## Comparison wording (2026-10-03)

Prefer *Compared* when *Relative* is a comparison word in prose.

| Avoid | Prefer |
|-------|--------|
| Relative to the clinical model, … | Compared with the clinical model, … |
| relative to controls | compared with controls |

Do **not** rewrite technical metric names (*relative CBF*, *relCBF*, and other "relative …" measures). Rewrite those only when the surrounding prose uses *relative* as a comparison word.

## Process and placeholder language (final body and legends)

Banned in the manuscript the authors call final, including figure legends. Missing facts become a Word comment (author **A**). Check ids: `05_manuscript/qc/manuscript-local-qc.md`.

| Avoid | What to do |
|-------|------------|
| `TRAIN_RATIO`, `VAL_MODE`, `settings.ini` keys, other pipeline tokens | Write the procedure in words, or comment if the value is unknown |
| as stated by the source / according to the HTML / the source says | State the fact. The lab file stays off the page |
| 待补 / 待补充 / TBD / XX / `[parameter]` / empty query strings | Comment. Do not leave the placeholder in prose |
| 标签未与方案核对 and other internal QC labels | Comment only. Never in the body |
| The same disclaimer pasted again | Keep one locus |

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

Reduce adverb use. Short rule, not a lexicon: cut decorative *-ly* softeners and intensifiers. Do **not** ban statistical *significantly* when it is p-value language (already governed in `04_analysis/qc/report-checks.md` / Results reporting).

## Lab-unused stock (0 hits in 389 unique drafts, 2026-08-28)

These used to appear as recommended conclusion templates. Harvest of 389 unique drafts found **0** uses. Do not recommend; do not insert.

| Avoid | Prefer |
|-------|--------|
| suggesting its potential | name the task (`could assist [task]`) or drop the clause |
| demonstrated good performance | report `AUC of X (95% CI: X–X)` in training **and** test |

See `vocab/L2/preferred.md` §1c (the former `sentence-templates.md` / `corpus-phrase-bank.md` were merged into it on 2026-10-16).

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

See also: `archive/blog/` (archived blog references), parent hard rules.


## Meta-narration / pipeline self-talk / QC-in-body (2026-10-24)

Banned in manuscript **body** and figure legends (put in Word comment author **A** if needed). From Grok-session triage; not already covered by the pipeline-token row above.

| Avoid | What to do |
|-------|------------|
| Meta draft banners (“Working manuscript draft covering…”, “Do not submit until…”) | Delete; never ship tool status as prose |
| Pipeline self-narration (“The present clinical matrix stored a binary Group column…”, console/HTML process paragraphs) | Rewrite as Methods facts, or comment |
| QC intermediate dumps in body (e.g. `QC_MI_Warn 0.0674`, mutual-information registration warning counts) | Comment / QC report only |
| “A formal a priori sample-size calculation was not performed.” when an estimate exists | Use the post hoc / performed estimate wording |
| “the band limits are not stated in the current draft” style gap-exposure | Move to a Word comment with suggested fix |

Polish-language: no separate personal digest — these bans live here.
