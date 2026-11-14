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

Pass bands for the two 70-point scorecards: FAIL-SOFT < 45, WARN 45-59, PASS >= 60. A FAIL-SOFT means "revise with advanced", not "reject the science".

## 4 Report shape

Write one block per check, on the same page as (but separate from) the QCS report:

```yaml
QCV-VOC-1: PASS        # evidence: style_lint.json run 14:02, 4/4 groups
QCV-STR-1: WARN        # evidence: paragraph map, para 3 merges methods+related studies
QCV-SCORE-1: 54 WARN   # evidence: scorecards.md sheet, LOG-2 x2
```

Then one summary line: `QCV: n PASS / n WARN / n FAIL-SOFT` — **never** merged with `QCS`. Word comments carry the tag `style-lint` (or the QCV ID) and author **A**; suggestions give the preferred wording, they do not overwrite the body.

## 5 Load order (with the three layers)

S1 base first pass (no advanced) → S2 science QC (`manuscript-local-qc.md`, `report-checks.md`) → S3 advanced revision (only if needed) → **S4 this report + incremental QCS on the changed sentences** → S5 re-gate. The normative run order is SSOT in `00_orchestrator/references/base-vs-advanced-top-loops.md` §2.

## 6 Boundaries

- Personal bans and house shape are **not** scientific errors. Never subtract a QCV finding from a QCS score, and never fail G-05 for a FAIL-SOFT alone.
- Style QC does not check numbers, citations, leakage, or statistics; if it spots one, hand it to QCS / G-FACT, do not score it here.
- `style_lint.py` stays report-only; the machine list stays in `05_manuscript/base/vocab/L1/ban-terms.yaml`.
