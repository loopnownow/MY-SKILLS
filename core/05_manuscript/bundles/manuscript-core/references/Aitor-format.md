# Aitor-format (Ying Li / Jinshan)

Formerly `house-format.md`.

**Owner:** `manuscript-core`. Single source for **every English SCI full paper** in this lab.

**Gold manuscript (typography and page geometry):**  
`D:\0Grok\0RAD\0del\lxf_LG\Response\Manuscript_Response_house.docx`

**Voice and revision marks (same Aitor-format, do not fork):**  
`0del/lxf_LG/Response/Manuscript_Response_house.docx` (prose skeleton) ·  
`xlm_LG/Growth/Manuscript_Growth_polished.docx` (Ying Li hand; incremental + DeLong) ·  
`lxf_LG/Response/Manuscript_Response_polished.docx` (CI en-dash; table `NC`) ·  
`0del/xlm_LG/Growth/Manuscript_Growth_house.docx` (training / test) ·  
`0del/lya_WML/MCI/Manuscript_MCI_house.docx` (circular labels; delete extra tables) ·  
`0del/lya_CTA/Stroke/Manuscript_Stroke_house.docx` (missing products; circular symptom field).

Later-polish live files are `Manuscript_<结局>_polished.docx` in the outcome folder (house drafts in `0del/<project>/<outcome>/`). Use them for de-pipeline + number realignment only; **do not copy** sentence fusion, em-dash, internal `development`/`validation`, or disclaimer stacks.

If a rule is unclear, **ask the user**. Do not invent a second Aitor-format.  
Letters / short communications: apply only if the user asks.

Voice and de-AI lists stay in `MODULE.md` / `de-ai/` / `stats-checklist.md`.

---

## How to use

- Write or revise an SCI paper → follow this file.
- Numbers only from the latest `*-results.html` / locked tables. **Never invent** *n*, AUC, CI, *P*, ethics Date/NO, DOI, or unmade experiments. Never change an AUC/CI/*P* without re-reading that file. For ROC rows, take the **nomogram** (Combined) line, not a leftover pipeline `Combined` figure label that disagrees with Results.
- Canonical file: `Manuscript_<结局>_house.docx` (unpolished) or `Manuscript_<结局>_polished.docx` after archive. **Overwrite in place.**
- Embed current figures from the subproject `PNG/` (the paper must contain images).
- **Any blank is yellow highlight** (ethics Date/NO, author `[]`, missing *n*/AUC/DOI, unfinished phrases, placeholder cells). Never leave a gap that looks like finished text.

---

## Page

- A4 (21.0 × 29.7 cm). Margins 2.54 cm all sides.
- Entire document uses Word **Normal** style. **Never** Heading 1/2/3.

---

## DOCX typography (match the gold file)

**Times New Roman throughout. Black.**

| Surface | Size | Line spacing | Bold | Align / indent |
|---------|------|--------------|------|----------------|
| Paper title | **12 pt** | 1.5 | **yes**, whole title | Center, no indent |
| Authors (`Ying Li¹`) | 12 pt | 1.5 | no | Center, no indent |
| Affiliation | 12 pt | 1.5 | **no** | **Left**, no indent |
| Title-page / abstract **labels** (`Corresponding author:` `Objective:` …) | 12 pt | 1.5 | **label + colon only** | Left, no indent; rest of the same paragraph not bold |
| `Highlights` `Abbreviations` `Abstract` and IMRAD section titles | 12 pt | 1.5 | **yes** | Left, no indent |
| Methods / Results **subtitles** | 12 pt | 1.5 | **yes** | Left, no indent |
| Highlights body, abbreviations body, references, table notes | 12 pt | 1.5 | no | **Flush left, no indent** |
| Body after abstract | 12 pt | 1.5 | no | Justified, first-line indent **0.74 cm** |
| `Table N.` / `Figure N.` / `Supplementary …` **prefix** | 12 pt | 1.5 | **prefix only** | Left, no indent |
| Table **cells** | **11 pt** | **1.0** | header row yes | No indent |

There is **no 16 pt title** and **no 14 pt section title**. Everything that is not a table cell is 12 pt.

- *P* italic. `n = N`. `95% CI: X–X` (en-dash, no spaces). Not `X to X`. No em-dash as punctuation.
- **English punctuation only.**
- English sentence ≤55 words. **One fact per sentence.** Do not merge adjacent sentences with semicolons or stacked *and*.
- Software: `Analyses were performed in Python 3.13.` (version after Python; no parentheses unless the user adds a build, e.g. 3.13.9).
- Split names (full paper), three words only:  
  - **training set** — internal fitting (never `development set` / `Dev`)  
  - **test set** — internal evaluation (never `hold-out`, `holdout`, or `hold out`)  
  - **validation set** — the external confirmation cohort (never `external test set`)  
  Compound forms: `training-set`, `training-fitted`, `test-set`, `test AUC`, `validation-set`. Sentence start: `Training-set` / `Test-set` / `Validation-set`. Keep `10-fold cross-validation` (algorithm, not a cohort). If no external cohort exists, write `No validation set was available` or `A validation set is required` — still never `hold-out` or `external test set`.

---

## Title page order

Title → Authors → Affiliation →  
`Corresponding author:` `Funding:` `Ethics:` `Acknowledgments:` `Author contributions:` `Data availability:` →  
`Highlights` (3 bullets) → `Abbreviations` (alphabetized, terms used ≥2 times; expand at first use in the body).

| Field | Default text |
|-------|----------------|
| Affiliation | `1 Department of Radiology, Jinshan Hospital of Fudan University, 1508 Longhang Road, Shanghai 201508, China` |
| Corresponding author | `Ying Li, E-mail: dr.yingli@foxmail.com` |
| Funding | `This work was funded by Jinshan Hospital (KYQDJJ202501) to Hai-Feng Shi.` |
| Ethics | IRB of Jinshan Hospital of Fudan University (Date:  , NO:  ). Retrospective waiver. Helsinki allowed. |
| Acknowledgments | `None` |
| Author contributions | `[]`: writing original draft, data collection, and statistical analysis. `[]`: data collection and manuscript revision. `Ying Li`: conceptualization, writing-review and editing, and correspondence. |
| Data availability | `The raw data of this manuscript are available from the corresponding author on reasonable request.` |

Delete pipeline banners. Hai-Feng Shi in **Funding only**.

**Highlights (3 bullets).** Report findings, not missing data. Do **not** write “No validation set was available” as a highlight. A missing **product** may be a highlight when it is the scientific fact (e.g. no radiomics matrix, so no RadScore / nomogram). Typical order: main test-set metric → incremental value or its absence → incomplete later endpoint or planned validation set.

`Highlights` and `Abbreviations` may take a colon; bold through the colon.

---

## Abstract

Same-paragraph labels, **bold through the colon only**:  
`Objective:` `Methods:` `Results:` `Conclusion:` `Keywords:`  
Flush left, no indent. Objective → Methods (*n*) → Results (AUC, CI) → hedged Conclusion.

Lead Results with **test-set** AUC (training in parentheses if needed). If a nomogram, calibration, NRI, or RadScore was not exported, say so in Methods or Results. Do not invent those numbers.

---

## Document order

Title page → Abstract → Keywords → Introduction → Materials and Methods → Results → Discussion → Conclusion → References → Tables → Figures → Supplementary files (if any).

Methods still opens with Ethics even if ethics is on the title page.

---

## Citation

- Vancouver / NLM + DOI on every entry. Number by first appearance.
- Do not cite every sentence. Shared source on neighbouring sentences: cite once.
- Do not reuse an earlier number after a later number has entered.
- No `[1–3]` clusters.
- Introduction 800–1000 words, 10–15 refs. **Last paragraph (aim / hypothesis): no citations.**
- Discussion 800–1000 words, 10–15 **new** refs (no overlap with Introduction). **First paragraph: no citations.**
- **Methods: no citations.**
- References: flush left, **no hanging indent**.

---

## Introduction (800–1000 words)

1. Disease / burden  
2. Clinical pathway  
3. Limits of current tests  
4. Imaging / radiomics / habitat gap  
5. Missing piece  
6. **Aim and hypothesis — no citations.**

No current-study AUC dump. Expand abbreviations at first use.

---

## Methods — fixed order

1. **Ethics** — subtitle is `Ethics` (never `Ethics: Ethics`).  
2. **Study design and sample size** — honest split. Estimation **was performed** (post hoc allowed). State **α = 0.05**, **β = 0.20** (power 80%), observed event proportion *p*, required events ≥ 10 per fitted nomogram coefficient, and whether this sample met that threshold. Never write that a calculation “was not performed.” **Never mention a random seed.**  
3. **Patients** — Jinshan default **1 August 2024 to 1 August 2026** (not ADNI). Analyzed *n*. Group counts: `(Stroke, n = 89; non-stroke, n = 187)`, not `(Stroke 89, non_Stroke 187)`. Prefer *patients were analyzed and divided* over *cases were split*. No subject IDs. No “pipeline treated rows as observations.” Secondary ADNI / non-Jinshan extracts: say so here or in Limitations, not as a worksheet dump.  
4. **Inclusion and exclusion** — one paragraph each; inline `follows: (1) x; (2) y; and (3) z`, not a vertical list.  
5. **Diagnostic and treatment criteria**  
6. **Outcomes** — pathology **positive versus absent** (e.g. LVSI) or a **follow-up / RECIST** event (e.g. ORR = CR/PR versus SD/PD). Use the clinical name (stroke, recurrence, dedifferentiated). **Do not write *coded* or *displayed*** as an endpoint prefix. If labels were not locally re-adjudicated, say so **once** in Outcomes or Limitations (*labels followed the source field; they were not re-read against a local protocol*). Do not claim local re-adjudication.  
7. **Laboratory tests** — pathologic endpoint: labs within **30 days** of pathology. Do not apply that sentence to pure survival / response-horizon papers.  
8. **Imaging examinations** — MRI: primarily 3.0 T Magnetom Verio (Siemens Healthineers, Erlangen, Germany). CT: primarily Canon Aquilion (Canon Medical Systems, Otawara, Japan). Minority-of-scanners sentence allowed.  
9. **Image processing** — method only. No QC field dumps. Lead-in fragments allowed (`Tumor segmentation.` `Preprocessing.`). Write what was **not** done (no ICC filter, no IBSI phantom, empty radiomics sheet). Habitats are imaging constructs, not histologic maps. Spatial ratios / subfield percentages are not a texture-radiomics panel unless that matrix exists.  
10. **Model building** — patient-level split; **training-set** selection only; **test set** for evaluation only. Primary model = **nomogram** (the Combined / combined logistic model; do not use those pipeline names). Youden is **split-specific** unless a training threshold was actually locked. A predictor that is part of the label (MMSE in MCI, a symptom field that already contains infarction) is **not** an independent imaging biomarker — say so here.  
11. **Statistical analysis** — start with `Analyses were performed in Python 3.13.` (no package list). Write **median and interquartile range**. If calibration, DCA, NRI, IDI, or mediation were not exported, write **not generated / not exported**. Do not invent them.

---

## Results

Subtitles: **12 pt bold, left, no indent.**

**First body paragraph under Patient characteristics must include:**

- `The study flowchart is shown in Figure 1.`  
- `Binary percentages in Table 1 follow the results and do not name the displayed level in every row.`  
Two separate sentences. Never glue them as `Figure 1 Binary percentages…`.

Group comparisons: direction (positive vs negative) then `(P = x)` only.  
Do not write `(median 49.00 versus 55.00 years, P = 0.002)`.

**Table 1** = **training versus test** wide table (group columns under each split, with split-wise *P*). This is the main baseline table.  
Do **not** put the pipeline all-data dump (single-cohort only, no split) as Table 1. A positive-versus-negative all-data table, if kept, is supplementary — not Table 1.

**Do not create these tables** (numbers go in Results prose and/or the matching figure):  
LASSO-feature list · nomogram / clinical logistic-coefficient table · SHAP table · score-correlation table (RadScore × age/group) · mediation (ACME) table.

RadScore formula and nomogram coefficients stay in Results prose. SHAP ranks and mediation paths stay in prose + figures.

Typical Results order: Patient characteristics → model construction (formula) → discrimination (Table of operating characteristics + Figure 2) → incremental value / calibration / utility → optional SHAP / correlation / exploratory mediation. Lead the imaging-only score before a circular clinical score when both exist.

**Incremental value (test set).** Re-read the latest `*-results.html` before writing this sentence. House templates that say *did not improve* are often wrong once the nomogram row is higher than RadScore/Clinical. If the nomogram AUC does not exceed RadScore or Clinical: **no incremental test-set value**. If it is numerically higher but DeLong (or an equivalent paired AUC test) was **not** run: *improved* is allowed **only in the same sentence** as the missing test (`…improved test-set AUC beyond the RadScore, although this difference was not confirmed by a DeLong test.`). Never write *improved* / *incremental* without that caveat. Figure-legend AUCs must match the **nomogram** Results numbers, not a Combined-row leftover.

Impossible or biologically implausible lab cells: shown, not interpreted; *P* = **NC** (not calculated). Say so once in the table note.

---

## Discussion (800–1000 words)

1. Key findings — **no citations, no result numbers**.  
2. One block per finding — new literature; still no copied AUCs.  
3. Clinical application — **one** short use-case sentence. No disclaimer stack (*It is not a replacement… A high score should not…*).  
4. **Limitations: its own paragraph**, First… Second… Put label circularity **First** when a predictor is part of the endpoint. Facts only. No closer *rather than a ready clinical tool*.  
5. **Conclusion** — 2–3 sentences; echo the objective; **no AUC / CI / *n***. If no external cohort exists, *A validation set is required* **once** (here **or** in Limitations, not both; never in Highlights or Figure 1).

---

## Tables

- Three-line (top / header / bottom); **no verticals**; **thin** single lines (`sz` ≈ 4), **not bold**.  
- Title above: `Table 1. ` **bold**; remainder not bold; flush left.  
- Notes below: 12 pt, flush left, no indent (justified allowed). **No** `Source: *-results.html` and **no** file paths.  
- Header cells: **no** `(n = 57)`.  
- Cells: 11 pt, single spacing, header bold.

---

## Figures

- Embed the latest PNGs.  
- Image first, legend below.  
- **Figure 1 (flowchart):** one paragraph. `Figure 1. ` bold; rest not bold; flush left. No inclusion box. Do **not** add “the figure does not depict a validation set.”  
- **Figure 2 and later:**  
  - Line 1 — short title (`Figure 2. ` bold + short name), flush left, no indent.  
  - Next paragraph — what the panel shows, same as body (justified, first-line indent 0.74 cm). Annotate panels **(A)** / **(B)** or left/right sets separately.  
- One figure-specific qualifier is allowed if it is not already in Results (e.g. SHAP is exploratory). Do **not** reprint Discussion caveats or legal disclaimers in legends.  
- Supplementary figures: prefix bold; note flush left, no indent. Unused template nodes on a DAG must be named as unused.  
- Flowchart export: `bbox_inches=tight`, `pad_inches=0`.

---

## No disclaimers, no repetition

SCI full papers have **no disclaimer**. Ban:

- *for research use only* / *not medical advice* / *the authors disclaim*  
- *not a ready clinical tool*  
- parallel negation: *It is not a replacement for… It is not a… A high score should not… A low score should not…*  
- the same *does not demonstrate effect on decisions or outcomes* copied into Results + Discussion + figure legend  

One scientific bound, **one place**. Do not restate the same hedge in Highlights, Abstract, Discussion, figure legend, and Conclusion.

## Banned voice

- `QC_MI_Warn`, `Habitat_Mode`, `Fusion_Channels`, `Align_Verify_NSeq`, “continued after mutual-information registration warnings…”  
- Group / non_Group, clinical matrix, worksheets not re-exported  
- `coded` / `displayed` as an endpoint prefix (`coded stroke`, `coded recurrence`, `displayed Stroke`)  
- `median [interquartile range]` / `median [IQR]`  
- “A sample-size calculation was not performed.”  
- Random seed / 66666  
- “Histology fields were not applicable and were not used.”  
- Result numbers in Discussion (especially paragraph 1) or Conclusion  
- Literature citations in Methods  
- `hold-out` / `holdout` / `hold out` (write **test**)  
- `development set` / `Dev` / `development-fitted` for the fitting split (write **training** / **training-fitted**)  
- `external test set` (write **validation set**)  
- `validation set` for the internal split (that split is **test set**)  
- File paths, `*-results.html`, `pipeline_run.log`, `Supplementary_QC_*.docx`, `STROBE_*.docx`, `TRIPOD_*.docx`, `false_classification.xlsx`, `output/PNG/` in the manuscript body or table notes  
- Subject IDs; “pipeline treated rows as observations”  
- Package lists after `Python 3.13`  
- Disclaimer / CYA stacks listed above  
- `Ethics: Ethics` as a double subtitle (subtitle is `Ethics`)  
- `Reader_1` (write `Reader 1`); `Negstive` / `non_Stroke` (write `Negative` / `non-stroke`)

De-pipeline replacements (second polish pass; do not reorder IMRAD):

| Avoid | Prefer |
|-------|--------|
| `project clinical data` / `matrix` / `HTML` / `export` | `clinical database` / `dataset` / `source` |
| `The pipeline was configured to retain` | `Features … were retained` |
| `outlined with ITK-SNAP` | `segmented using ITK-SNAP` |
| `built inside the tumor mask` | `constructed within the tumor mask` |
| `cases were split` | `patients were analyzed and divided` |
| empty `[]` authors or `(Date: , NO: )` | yellow `[author name to be completed]` / `[Date to be completed]` / `[NO to be completed]` |

Do **not** take later-polish files as license to fuse sentences, add em-dashes, call the internal split a validation set, or stack *It is not a replacement…*.

---

## Reporting defaults

1. Nomogram = Combined model. Incremental wording: see Results (DeLong caveat).  
2. Full-cohort habitat / clustering: say so.  
3. Per-split Youden: write that.  
4. Cloned train/test 2×2: do not cite.  
5. Never mention a random seed.  
6. Specified but not generated (empty radiomics sheet, no nomogram, no calibration, no DCA): write **not generated**. Do not invent figures.  
7. A field that overlaps the endpoint (MMSE in the MCI label; a symptom code that already contains infarction) is a **coding / circular** result, not an independent imaging biomarker.  
8. Worksheet group names (`non_Stroke`, `Negstive`) are cleaned in prose. Do not prefix the endpoint with *coded* / *displayed*. Un-readjudicated labels: one Methods or Limitations sentence, not a running prefix.

---

## QC before done

- No Heading styles  
- Title and all section/subtitle headings **12 pt bold**  
- Affiliation **12 pt, left, not bold**  
- Labels bold **only through the colon**  
- Body 12 / 1.5; table cells 11 / 1.0; thin three-line rules  
- Highlights, abbreviations, references, table notes: flush left, no indent  
- Results subtitles bold, left, no indent  
- Figure 1 one paragraph; later figures = short title + detailed body paragraph  
- Images embedded  
- First Results paragraph has Figure 1 sentence + binary-percentage sentence (period between them)  
- Table 1 = training vs test wide table; no LASSO / logistic-coeff / SHAP / correlation / mediation tables  
- No `hold-out`; training = internal fitting; test = internal evaluation; validation set = external cohort only  
- No results.html / QC / STROBE path footers  
- Highlights do not advertise a missing validation set  
- Circular predictors named as circular  
- No *coded* / *displayed* endpoint prefix  
- Missing products written as not generated
- Intro last paragraph and Discussion first paragraph: no citations  
- Methods: no `[n]`; no seed; `Python 3.13`  
- Sample size: α, β, *p*, *n*, adequacy  
- Discussion / Conclusion: no result numbers  
- Limitations own paragraph; no disclaimer closer  
- No disclaimer / no repeated hedge  
- `95% CI: X–X`; one fact per sentence  
- Incremental *improved* only with same-sentence DeLong caveat  
- Implausible labs: *P* = NC, note once  
- Every blank yellow-highlighted  
- English punctuation  
- Ethics Date/NO yellow if empty; email `dr.yingli@foxmail.com`  
- Numbers match the latest results file (nomogram row, not a Combined-figure leftover)  
