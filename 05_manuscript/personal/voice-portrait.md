# Writing voice portrait (Aitor / Jinshan)

Personal upper layer for **writing**. Corpus: multi-paper Track Changes + comments (SCI medical).  
Executable format remains `Aitor-format.md`. This file keeps the **overall portrait** and habits that must not be watered down.

**Locks (2026-09-24 / 2026-10-01):** keep **set** (`training` / `test` / `validation set`); **short sentences** (one fact per sentence) **inside continuous paragraphs**; figure legends **below** figures; Discussion **not** compressed by page quota.

**Paragraph lock (2026-10-01):** Write body as paragraphs; do not one-sentence-per-line / one-sentence-per-paragraph. Short sentences OK, but keep related sentences in the same paragraph. Abstract four-section labels, Methods/Results subheads, Highlights bullets, table/figure notes still follow `Aitor-format.md`.

**Pre-submit (2026-10-02):** run `05_manuscript/qc/manuscript-local-qc.md` before a house draft is called final. Introduction opening paragraph cites when a verified source exists. Element 6 stays uncited. Final body and legends carry no pipeline tokens, source-attribution hedges, or placeholders.

---

**Corpus harvest (2026-10-23):** additive notes in `personal/references/corpus-voice.md` (quote habits). Do not wipe this portrait; process 否定句 stay in Word 批注 only.

## 1. Overall portrait

Priority order: **data accuracy and term consistency first**, then **restrained clinical wording**.

- Write like a structuralist: fixed Abstract four-block, Discussion six-step order, Limitations as its own paragraph with First… Second…, and a Future-research closer.
- Once a term is locked (especially split names), enforce it end-to-end. “Close enough” is not enough.
- When uncertain: **mark it** (Word comment, author **A**). Do not invent ethics IDs, *n*, AUC, DOI, or unrun analyses.
- Do not oversell clinical impact. Net benefit / “superior” claims need the supporting statistic in the same breath, or hedge / weaken.
- Batch related papers from one cohort is fine; decisions prefer finite choices. Real doubts still get an explicit human confirm.

This portrait does **not** replace `Aitor-format.md`. On conflict, locks above + `Aitor-format.md` win.

---

## 2. House structure (writing)

| Piece | Rule |
|---|---|
| Abstract | Objective / Methods / Results / Conclusion |
| Discussion order | Main findings → prior literature → mechanism (hedged) → clinical meaning → Limitations → Conclusion |
| Limitations | Own paragraph; First… Second…; last item often needs prospective / multicenter validation wording when true |
| Closer | Prefer `Future research/studies should…`; avoid `…are warranted…` as default |
| Refs placement | After Conclusion, before Tables (full paper) |
| Aim openers | `This study aimed to…` / `The aim of this study was to…` |
| Voice | Methods: prefer passive where lab default applies; Discussion: calibrated hedges; Results: no hedges |
| Banned hype | `novel`, `notably`, `interestingly`, `importantly` + `vocab/L1/ban-phrases.md` |

Do **not** add a Discussion page-length quota (no “cut to 1.5 pages”). Length follows `Aitor-format.md` word bands and content need.

---

## 3. Terms, numbers, short prose

- Split names: **training set** / **test set** / **validation set** only (never `development set`; never rewrite set→group).
- One fact per sentence, inside a continuous paragraph. Do not merge adjacent Results sentences into long stacks. Do not lay the body out as one sentence per line.
- Introduction opening paragraph cites the verified source when one exists. An opening with zero citations is unfinished when the evidence pack has a source.
- *P* italic; space before comparator (`P < 0.05`); report exact *P* when above the extreme threshold the lab uses (see stats rules in 02 / Aitor-format).
- Number–unit spacing consistent; English punctuation only; abbreviations: expand at first use, then one form only.
- Spelling system (US/UK) follows the target journal; **one system per manuscript**.
- `multivariable` (multiple predictors), not `multivariate`, unless multiple outcomes are truly meant.

---

## 4. Figures and tables

- Figure legend sits **below** the figure.
- Do not restate table cells in prose when the table already carries the same numbers.
- Radiomics full papers usually need the familiar product set when the HTML has them: feature selection → signature → nomogram → ROC/AUC → calibration → DCA (± NRI/IDI). Do not invent missing products.

---

## 5. Precision habits (from revision corpus; reinforce Methods/Results)

Use these when the HTML / source tables support them; never invent.

1. **Causal language → association.** If mediation / pathway language appears, put the estimate + 95% CI and state explicitly when the interval crosses zero / is not causal evidence.
2. **Performance with CI, both sides.** AUC (and similar) as value + 95% CI in the training set **and** the test set as a pair when both exist.
3. **Sample flow is checkable.** Counts before/after downsample, events-per-coefficient, α/β once in Study design — do not restack across Abstract/Results/Discussion.
4. **Concept boundaries.** If two endpoints can be confused (e.g. continuous change vs categorical response), one clarifying sentence beats a later reviewer fight.
5. **Weak metrics stay honest.** Modest sensitivity / null pathways stay in the text; do not delete because the number is inconvenient.
6. **RadScore / formulas.** Human-readable feature names + internal codes; coefficients on the original scale when that is how the model was fit.
7. **Scanner matrix.** List vendor/model and key acquisition parameters per scanner; no “standard protocol” hand-wave.
8. **Agreement stats.** Prefer mean, median, and range together (e.g. Dice / Hausdorff), not mean alone.
9. **Missingness / remapping.** State median imputation (or the real rule) and any remapping to original scale before standardization.
10. **Refs serve the narrative.** Order and adds follow the argument (background for key covariates), not a frozen citation bingo.

Detail templates stay in `polisher-sections.md` / `Aitor-format.md`. This section is the habit checklist.

---

## 6. Delivery (writing side)

- Revise the original `.docx` in place with Track Changes; comments author **A**. Ownership: see `00_orchestrator/references/ownership-contract.md`.
- Missing facts → comment / ask; never yellow fill; never silent overwrite of existing corresponding-author / funding / ethics text.
- Full delivery rules: `06_review/personal/word-edit.md`.
- Before calling the draft final, run `05_manuscript/qc/manuscript-local-qc.md`. Number conflicts stay comments. Do not leave `TRAIN_RATIO`, "as stated by the source", 待补, or internal QC labels in the body or legends.

---

## L2 format / paragraph slice (merged 2026-10-16)

# L2 format / paragraph habits (writing layer)

**Authority:** full locks and portrait stay in `voice-portrait.md` and IMRAD/DOCX in `Aitor-format.md`.
This file is the **L2 writing slice** only (how paragraphs and set wording are preferred).

## Preferred paragraph habit
- One fact per sentence, inside **continuous paragraphs** (not one sentence per line/paragraph in IMRAD body).
- Abstract headed labels, Methods/Results subheadings, Highlights, table/figure notes follow `Aitor-format.md`.

## Preferred set wording
- Body: **training / test**; Figure 1: Training Cohort / Test Cohort; external other-hospital only = **validation set**.
- Never Development set; never call same-hospital random split external validation.

## Figure legends
- Legends **below** figures (`voice-portrait.md`).

## Em-dash / typography that affect wording
- Prediction-model full papers: no em-dash (see `Aitor-format.md`).

