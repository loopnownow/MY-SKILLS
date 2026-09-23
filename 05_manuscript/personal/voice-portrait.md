# Writing voice portrait (Ying Li / Jinshan)

Personal upper layer for **写作**. Corpus: multi-paper Track Changes + comments (SCI medical).  
Executable format remains `Aitor-format.md`. This file keeps the **overall portrait** and habits that must not be watered down.

**Locks (2026-09-24):** keep **set** (`training` / `test` / `validation set`); **short sentences** (one fact per sentence); figure legends **below** figures; Discussion **not** compressed by page quota.

---

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
| Banned hype | `novel`, `notably`, `interestingly`, `importantly` + `forbidden-phrases.md` |

Do **not** add a Discussion page-length quota (no “cut to 1.5 pages”). Length follows `Aitor-format.md` word bands and content need.

---

## 3. Terms, numbers, short prose

- Split names: **training set** / **test set** / **validation set** only (never `development set`; never rewrite set→group).
- One fact per sentence. Do not merge adjacent Results sentences into long stacks.
- *P* italic; space before comparator (`P < 0.05`); report exact *P* when above the extreme threshold the lab uses (see stats rules in 04 / Aitor-format).
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

- Revise the original `.docx` in place with Track Changes; comments author **A**.
- Missing facts → comment / ask; never yellow fill; never silent overwrite of existing corresponding-author / funding / ethics text.
- Full delivery rules: `06_review/personal/word-edit-rules.md`.
