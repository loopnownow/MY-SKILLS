# Style QC (QCV, soft): voice, structure, de-AI

**Class:** QCV (style/voice). **Not** a science score and never merged into one. Gate/routing owner: `00_orchestrator`; checklist body: `05_manuscript`. This report is **report-only**: hits become Word comments (author **A**), never silent body rewrites, and a FAIL-SOFT never blocks a science gate (G-05 / G-FACT).

Style QC answers one question: does this draft read in the house voice and follow the house shape? It does not re-score evidence, numbers, or claims; those stay with QCS (`manuscript-local-qc.md`, `02_data-processing/qc/report-checks.md`) under G-FACT / G-STATS.

## 1 When it runs

- **S4 only**, after the advanced revision (S3) and after science QC (S2), when the run actually applied advanced/personal style revision.
- On an explicit request: 去AI / de-AI, 润色, "check my voice", house.docx pass.
- **Never** in S1 (base first pass, no advanced loaded) and never in S2 (science QC). A base-only run skips this report.
- No new gate id: this is the S4 incremental checkpoint plus the existing G-05 `style-lint` sub-check. `00_orchestrator/gates.md` still owns WHEN / PASS-FAIL.

## 2 Verdicts and evidence

| Verdict | Meaning | Effect |
|---|---|---|
| PASS | check ran, no finding | none |
| WARN | house-style drift, acceptable if intentional | comment, no block |
| FAIL-SOFT | clear house-voice/format breach | comment, returns to 05 advanced revision |
| UNVERIFIABLE | the check could not run (e.g. `style_lint.py` not run) | must be named as such; never reported as PASS |

Every check names its evidence: `style_lint.py --json` output, a paragraph map, a filled scorecard sheet, or the manuscript text. No evidence, no PASS.

## 3 Checks (QCV)

| QC_ID | Target | Condition | Evidence | Severity | Repair anchor |
|---|---|---|---|---|---|
| QCV-VOC-1 | vocabulary / constructions / dash cadence / rule-of-three | any of the four `style_lint.py` groups fails | lint JSON | FAIL-SOFT | `05_manuscript/base/vocab/L1/ban-terms.yaml` (+ `ban-phrases.md` for why) |
| QCV-VOC-2 | AI-pattern reading beyond the machine list | pattern from `05_manuscript/base/vocab/L1/patterns.md` Tier 1-3 still present after revision | annotated excerpt | WARN only (judgement call) | `patterns.md`; de-AI pass below |
| QCV-STR-1 | Introduction map | not five body paragraphs / eight beats, or a beat is moved/missing | paragraph map (one line per paragraph) | FAIL-SOFT | `05_manuscript/advanced/Aitor-format.md` § Introduction |
| QCV-STR-2 | Discussion shape | not the inverted funnel (findings without cites/numbers → contrast → hedged mechanism → clinical use → Limitations paragraph → Conclusion), or aims unanswered | paragraph map + aim table | FAIL-SOFT | `Aitor-format.md` § Discussion |
| QCV-STR-3 | paragraph lock | one sentence per line / per paragraph in IMRAD body | layout excerpt | FAIL-SOFT | `05_manuscript/advanced/voice-portrait.md` § Paragraph lock |
| QCV-LEN-1 | sentence band | more than 10% of sentences outside 10-30 words | sentence-length histogram | WARN | `voice-portrait.md` § Sentence habits |
| QCV-FMT-1 | house format numbers | word bands, 10-15 refs, Table 1 shape, typography diverge from house defaults | side-by-side table | FAIL-SOFT | `Aitor-format.md` § Format / § Tables / § Figures |
| QCV-HED-1 | calibrated hedging | unhedged mechanism claim in Discussion, or stacked empty hedges | sentence list | WARN | `voice-portrait.md` § Hedging; science side = QCS `no_causal_overclaim_observational` |
| QCV-DEAI-1 | de-AI pass | de-AI procedure not run, or banned strings remain in body/legends | before/after table + lint | FAIL-SOFT | `05_manuscript/advanced/process/polisher-sections.md` § De-AI pass |
| QCV-SCORE-1 | Introduction scorecard | score below PASS band | filled sheet (`scorecards.md` § Introduction) | FAIL-SOFT if < 45; WARN if 45-59 | `scorecards.md` |
| QCV-SCORE-2 | Discussion scorecard | score below PASS band | filled sheet (`scorecards.md` § Discussion) | FAIL-SOFT if < 45; WARN if 45-59 | `scorecards.md` |
| QCV-LEN-2 | sentence-pattern repetition | a run of sentences in one paragraph opens with the same words or the same frame | located excerpt + paragraph map | WARN | Introduction hits may already be coded as FLU-1 on the existing scorecard; do not add a second total |
| QCV-CONN-1 | high-frequency conjunctions and template phrases | a dense run of stock transitions or template stems in one span | located excerpt | WARN | `05_manuscript/base/vocab/L1/ban-phrases.md` / `05_manuscript/base/vocab/L1/patterns.md`; do not ban a conjunction as such |
| QCV-ABBR-1 | abbreviation definition and consistency | first use lacks a definition, or later use expands differently | located first-use and later-use excerpts | WARN | house or venue abbreviation practice; do not invent a new exemption list |
| QCV-NUM-1 | number, percentage, or *P* / AUC format | a numeral, percent, or *P* / AUC string diverges from the confirmed venue plus house decimals | located excerpt | WARN | `05_manuscript/advanced/Aitor-format.md` § Results (decimals); venue house style, with `05_manuscript/advanced/references/stat-reporting.md` as the Radiology/AMA quick reference. Do not invent a third precision rule. |
| QCV-REP-1 | vocabulary over-repetition | the same non-structural word is repeated densely in a short span | located excerpt + counts | WARN | do not flag required technical repeats (endpoint names, group labels, AUC) |
| QCV-SEC-1 | Results scope | Results states a mechanism interpretation that the supplied data do not support, or states it as if it were a result | located excerpt | WARN | `05_manuscript/advanced/Aitor-format.md` § Results; if the sentence claims an untested result, hand to QCS, do not score the science here |
| QCV-SEC-2 | Discussion distinctions | this study's observations, prior evidence, and mechanism inference are not kept distinct, or negative findings / limitations are dropped without a recorded reason | paragraph map + excerpts | WARN | `05_manuscript/advanced/Aitor-format.md` § Discussion; `scorecards.md` D-MECH / D-LIM. Keep negatives and the Limitations paragraph. |
| QCV-SEC-3 | Conclusion scope | Conclusion does not answer the study aim, introduces a result that is not in Results, or writes a potential use as proven clinical benefit | located excerpt | WARN | `05_manuscript/advanced/Aitor-format.md` § Discussion (Conclusion); D-CRAFT-1. Overclaim of benefit also goes to QCS. |

Pass bands for the two 70-point scorecards: FAIL-SOFT < 45, WARN 45-59, PASS >= 60. A FAIL-SOFT means "revise with advanced", not "reject the science".

## 4 Report shape

Write one block per check, on the same page as (but separate from) the QCS report:

```yaml
QCV-VOC-1: PASS        # evidence: style_lint.json run 14:02, 4/4 groups
QCV-STR-1: WARN        # evidence: paragraph map, para 3 merges methods+related studies
QCV-SCORE-1: 54 WARN   # evidence: scorecards.md sheet, LOG-2 x2
```

Then one summary line: `QCV: n PASS / n WARN / n FAIL-SOFT` — **never** merged with `QCS`. Word comments carry the tag `style-lint` (or the QCV ID) and author **A**; suggestions give the preferred wording, they do not overwrite the body.

Every locatable or section finding is recorded as its own row, not only as a scorecard total:

```text
ID | Location | Type | Excerpt | Reason | Direction | Verdict
```

Location is a heading plus a short quote from the manuscript. Direction is a suggested revision path; it must not change the scientific meaning to raise a score.

## 5 Load order (with the three layers)

S1 base first pass (no advanced) → S2 science QC (`manuscript-local-qc.md`, `report-checks.md`) → S3 advanced revision (only if needed) → **S4 this report + incremental QCS on the changed sentences** → S5 re-gate. The normative run order is SSOT in `00_orchestrator/references/base-vs-advanced-top-loops.md` §2.

## 6 Boundaries

- Personal bans and house shape are **not** scientific errors. Never subtract a QCV finding from a QCS score, and never fail G-05 for a FAIL-SOFT alone.
- Style QC does not check numbers, citations, leakage, or statistics; if it spots one, hand it to QCS / G-FACT, do not score it here.
- `style_lint.py` stays report-only; the machine list stays in `05_manuscript/base/vocab/L1/ban-terms.yaml`.
- Locatable metrics and IMRAD section differences in this file are part of the same QCV report. They are not a second scoring system and do not block a science gate.

## 7 Locatable metrics (same report, not a second scoring system)

The checks above in QCV-LEN-2, QCV-CONN-1, QCV-ABBR-1, QCV-NUM-1, and QCV-REP-1 are quantitative supplements to this same Style QC report. They are **not a second scoring system**: they do not add a third scorecard, a new pass band, or a second total. House sentence length stays with the existing QCV-LEN-1 / FLU-3 band. Do not import an external word, sentence, or paragraph cutoff, and do not mechanically ban a punctuation mark or a sentence type.

Each auto-detectable hit must be locatable in the manuscript (heading plus excerpt). Do not report only QCV-SCORE-1 / QCV-SCORE-2 totals.

Do not rewrite scientific meaning to raise a score. Do not shorten a precise medical sentence, or switch it to passive, only to enter the house word band.

Number and *P* / AUC format follow the confirmed target venue plus `05_manuscript/advanced/Aitor-format.md` § Results (decimals). `05_manuscript/advanced/references/stat-reporting.md` is the Radiology/AMA quick reference; it does not override a confirmed venue or the house decimal rule. If those sources already disagree, comment the conflict; do not invent a third rule. AI-prose bans such as *labeled* / *labelled* and *locked* stay in `05_manuscript/base/vocab/L1/ban-phrases.md` (and `ban-terms.yaml`); cite them, do not restack a conflicting list here.

## 8 Section differences

These are writing-scope checks on the existing IMRAD house shape (`05_manuscript/advanced/Aitor-format.md`), not a new section template.

- **Results (QCV-SEC-1).** Report what the supplied data show. Do not front-load a mechanism interpretation that the data do not support, and do not write that interpretation as if it were a result.
- **Discussion (QCV-SEC-2).** Keep this study's observations, prior evidence, and mechanism inference distinct. Retain negative findings and the Limitations paragraph. Hedging of mechanism stays aligned with QCV-HED-1 and D-MECH-1.
- **Conclusion (QCV-SEC-3).** Answer the study aim directly. Do not introduce a result that is not in Results. A potential clinical use is not proven clinical benefit.

Do not impose a blanket ban on limitations in the Abstract or Introduction.

Claim Map, study-type, and figure-table-plan stay in `05_manuscript/advanced/process/`. This report does not copy those rule bodies. Science support of claims stays with QCS.

## 9 Human judgement (do not auto-verdict)

The following questions require a human reading. A detector may surface a candidate excerpt, but do not auto-assign PASS, WARN, or FAIL-SOFT on the question itself:

- whether the argument actually holds
- whether a proposed mechanism is scientifically reasonable
- whether the tone is too strong (beyond locating an unhedged verb already in QCV-HED-1)
- whether a sentence is factually accurate
- whether the wording fits the target journal's discipline

Tag such candidates for review. Do not pretend they were machine-decided.

*Thin lab rewrite, 2026-11-27, on locatable style metrics and IMRAD section differences inside the existing Style QC (not a second scoring system). Method reference: [gulucaptain/Best-Paper-Writing-Skill](https://github.com/gulucaptain/Best-Paper-Writing-Skill). See `NOTICE`.*
