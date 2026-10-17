# L2 preferred phrases + patterns

## Part A — corpus phrase bank

# Corpus Phrase Bank (rebuilt from source manuscripts)

**Status:** purpose / methods / results openers refreshed 2026-08-28 from
**389 unique drafts** (414 candidates → 409 extracted → 20 exact duplicates
removed; English ≈ **324**). Counts in §1–§1c are full-text grep on those
English drafts (Methods/Results repeats included), not abstract-only.
Discussion / limitations / ethics slots below still carry the earlier
96-manuscript grep where this harvest did not re-count. §2 and §2b carry a
further, smaller 2026-08-29 50-draft spot-check addition (marked inline) —
these are provisional and sit below even the 96-draft baseline in sample
size; re-confirm against the full 389-draft harvest before treating them as
settled.

Do **not** vendor unpublished full texts, title dumps, `corpus-raw/`, or
patient identifiers into this file. Templates are generic slots only.

Use this file alongside `polisher-sections.md` and `sentence-templates.md`.
Where a pattern here disagrees with either of those files, **this file wins**
for anything the corpus can settle (it's verbatim evidence); `Aitor-format.md`
still wins for hard formatting/QC rules (CI dashes, banned voice, etc.).

---

## 1. Objective-sentence openers — keep THREE families

Do **not** collapse purpose sentences to one default. Three families are all
in active use (harvest 2026-08-28, 324 English unique drafts):

| Family | Hits | Papers | Role |
|---|---:|---:|---|
| This study aimed to … | 45 | 44 | family 1 |
| To explore/investigate/evaluate/determine/assess/compare/develop … | 35 | 34 | family 2 (bare infinitive) |
| The aim of this study was to … | 22 | 14 | family 3 |
| The purpose of this study was to … | 12 | 12 | minority, not a fourth family |
| We aimed to / We sought to … | 5 | 5 | rare |
| The objective of this study was to … | — | — | not used as a template |

Templates (generic slots only):
- `This study aimed to [objective] using [method] in [population].`
- `The aim of this study was to [objective].`
- `To [investigate/explore/evaluate/…] whether [technique] could [outcome] in [population].`

Purpose sentences often sit mid-abstract, not in the file's first 30 lines.

## 1b. Methods / radiomics narrative (2026-08-28)

| Pattern | Hits | Papers |
|---|---:|---:|
| A total of N … | 180 | 123 |
| randomly divided / split into | 217 | 124 |
| training … test/validation | 404 | 53 |
| retrospectively enrolled/reviewed/collected | 22 | 21 |
| prospectively enrolled/collected/recruited | 16 | 15 |
| LASSO | 185 | 40 |
| radiomics nomogram | 1039 | 52 |

Retrospective far outnumbers prospective. Radiomics prediction papers default
to **training/test + LASSO + nomogram**.

Templates:
- `A total of N patients with [condition] who underwent [imaging] were retrospectively enrolled.`
- `Patients were randomly divided into a training set (n = N) and a test set (n = N).`
- `Radiomics features were reduced using LASSO, and a radiomics nomogram was constructed.`

**Split wording:** manuscript BODY internal split is training/test. Figure 1
labels **Training Cohort / Test Cohort**, plus **Validation Cohort** only when
Methods states an external cohort (`Aitor-format.md`). Only an other-hospital
cohort is a validation set. Never `Development set`.

## 1c. Results default + lab-unused stock (2026-08-28)

| Pattern | Hits | Papers |
|---|---:|---:|
| 95% CI | 1080 | 123 |
| AUC … 95% CI | 264 | 80 |
| DeLong | 81 | 52 |
| was/were associated with | 44 | 33 |
| outperformed | 12 | 7 |
| `demonstrated good performance` | **0** | 0 |
| `suggesting its potential` | **0** | 0 |

**Results default:** report `AUC of X (95% CI: X–X)` for **both** training
and test.

- `The AUC of the [model] was X (95% CI: X–X) in the training set and X (95% CI: X–X) in the test set.`
- `The nomogram exhibited good discrimination in the training set (AUC X [95% CI, X–X]) and the test set (AUC X [95% CI, X–X]).`

Direct side-by-side AUCs are more common than `outperformed`.

**Do not use** as recommended stock: `suggesting its potential`,
`demonstrated good performance` (0 hits in 389 unique drafts). Listed in
`../vocab/L1/ban-phrases.md`.

---

## 2. Discussion openers (¶1 — summary of key finding)

- *"In this study, we hypothesize[d] that…"* — 31 occurrences of the
  "In this study, we…" opener overall.
- *"In this study, we identified Ki-67 expression as an independent clinical predictor for distinguishing between WDLPS and DDLPS…"*
- *"The main finding[s] of [this/the present] study…"* pattern also occurs but
  is rare (1 instance) — don't over-rely on it as a default template; "In
  this study, we…" is the workhorse opener.
- *"[This/Our] study showed that…"* — secondary opener alongside "In this
  study, we…"; 8/50 in a smaller 2026-08-29 spot-check subset (not yet
  re-counted against the full 389-draft harvest — treat as provisional
  until confirmed at full scale).

---

## 2b. Gap-statement / novelty-claim opener (Introduction or Discussion ¶2)

Added 2026-08-29 from a 50-draft spot-check subset (smaller than this
section's existing 96-draft baseline — provisional, not yet confirmed
against the full 389-draft harvest):

- *"However, to our knowledge, [no prior study has / few studies have]…"* —
  classic gap-statement immediately preceding the paper's own contribution.
- *"One of the key challenges/aspects of [X] is…"* — used to frame why the
  study's problem matters before stating the approach.
- *"Given that [established fact], [this study/we] …"* — premise-then-move
  connector, bridges known background into the paper's own rationale.

---

## 3. Literature-comparison transitions (Discussion ¶2)

- *"This finding is consistent with a previous study by [Author] et al."* —
  "consistent with" appears 14 times.
- *"in contrast"* is actually the most frequent contrast connector (41
  occurrences) — more common than "in line with" (6). Don't default to "in
  line with" as the go-to agreement phrase; "consistent with" carries that
  role, and "in contrast" carries disagreement.
- Named-author citation pattern is alive and well, e.g.:
  - *"[Author] et al. found that…"*
  - *"[Author] et al. [ref] reported that…"*
  - *"[Author] et al. demonstrated that a deep neural network could achieve dermatologist-level accuracy in distinguishing…"*
- *"which may be attributed to…"* is used (3 occurrences) for explaining a
  discrepancy with prior literature; *"may be explained by"* does not appear
  in this corpus — prefer *"attributed to"* over *"explained by"* for this
  slot.

---

## 4. Limitations paragraph (own paragraph, First…Second…)

Opening-sentence variants, all attested:
- *"This study has several limitations that need to be considered."* (6)
- *"This study had some limitations."* (5)
- *"This study had several limitations."* (2)
- lower-case "this study has/had…" variants also occur — case is inconsistent
  in the raw corpus; **capitalize** per house style regardless.

Body pattern (verbatim):
- *"This study had several limitations. First, selection bias was inevitable because of the retrospective nature of this study."*
- *"This study had some limitations. First, the present retrospective study included limited samples of single-center data."*
- *"This study has some limitations. First, the study had a limited sample size[,] and the results should be further validated in multi-center larger data-sets."*

---

## 5. Future-work closing (end of Limitations)

Verified counts:

| Closer | Count |
|---|---|
| **"Future research should…"** | **18** |
| "Future studies should…" | 9 |
| "warrant(ed)/(s)" (any use, any sentence) | 14 |

**Dominant closing pattern: "Future research should…"** (with "Future
studies should…" as a close second/interchangeable variant). "…are
warranted…" / "warrants further study" is a minority form and should **not**
be treated as the default — this matches and reconfirms the prior corpus
finding.

Verbatim examples:
- *"Future research should focus on larger, multi-center, longitudinal studies to validate these findings…"* (3 occurrences of this near-exact wording)
- *"Future research should explore whether interventions targeting EAAT-2 expression can prevent or mitigate…"*
- *"future research should validate these findings in larger, multicenter prospective cohorts and across d[iverse populations]…"*
- *"Future studies should employ longitudinal and intervention-based designs to track…"*

---

## 6. Conclusion sentences

- *"In conclusion,…"* — 49 occurrences; the standard opener.
- *"In summary,…"* — 6 occurrences; acceptable alternate, much less common.
- *"Taken together,…"* — 0 occurrences; **not** attested in this corpus,
  don't introduce it as a template default.

Verbatim examples:
- *"In conclusion, this study demonstrates the potential of [the] DL model to assist dermatologists in differentiating BCC from CN to improve diagnostic outcomes."*
- *"In conclusion, lipidomics profiling demonstrates high accuracy in predicting the response to chemo-immunotherapy in NSCLC patients."*
- *"In conclusion, this study provides evidence of significant metabolic alterations in the ovaries of PCOS patients, particularly involving lipid metabolism."*

---

## 7. Ethics statement

All variants seen route through Jinshan Hospital, Fudan University, with the
IRB/Ethics Committee number in parentheses. Do not standardize away from
whichever the source manuscript already uses — both "Institutional Review
Board" and "Ethics Committee" appear as the reviewing body name across
different manuscripts in this corpus:

- *"approved by the Ethics Committee of Jinshan Hospital, Fudan University (No. …)"* (9)
- *"approved by the Institutional Review Board (No. …)"* (7)
- *"approved by the Institutional Review Board of Jinshan Hospital (JIEC 2023-S85)"* (4)
- *"approved by the Institutional Review Board of Jinshan Hospital, Fudan University (No. …)"* (3)
- *"approved by the Institutional Review Board of Jinshan Hospital of Fudan University, Shanghai, China (No. …)"* (3)
- *"approved by the Institutional Review Board of Jinshan Hospital, Fudan University (Shanghai, China; JIEC 2023-S52)"* (2)
- *"approved by the Institutional Review Board of Jinshan Hospital of Fudan University (Approval No. …)"* (2)

---

## 8. Words that ARE banned (policy reversal, 2026-08-29)

As of 2026-08-29 these four words are **Forbidden**. See `vocab/L1/ban-phrases.md`. Counts below describe the old corpus; they do not license the words.

| Word | Count |
|---|---|
| novel | 59 |
| notably | 21 |
| interestingly | 13 |
| importantly | 9 |

---

## Provenance / method

§1–§1c: 2026-08-28 harvest on 389 unique drafts (324 English); phrase
counts only — unpublished full texts and title dumps stay off GitHub.

Older slots (discussion openers, limitations, ethics, §8 word counts)
were grep-counted on the 96-manuscript deduplicated set:

```
md5sum *.txt | awk '{print $1}' -> keep first of each unique hash (96 of 100 kept)
grep -ohE '<pattern>' | sort | uniq -c | sort -rn
```

Re-run against a larger corpus if these files grow. Do not commit `corpus-raw/`.


---

## Part B — sentence templates

# Sentence Templates — Ying Li Style

Purpose / methods / results templates refreshed 2026-08-28 from 389 unique drafts (324 English). Do not collapse the three purpose-sentence families below. Do not vendor unpublished full texts, title dumps, or patient identifiers.

**Split wording (body vs Figure 1):** manuscript BODY internal split is **training / test**. Figure 1 labels **Training Cohort / Test Cohort**, plus **Validation Cohort** only when Methods states an external cohort (`Aitor-format.md`). Only an other-hospital cohort is **validation set**. Never `Development set`. Never call a same-hospital random split external validation.

**Do not use (0 hits in 389 unique drafts):** `suggesting its potential`; `demonstrated good performance`. See `vocab/L1/ban-phrases.md`.

## Abstract Templates

### Objective sentence — keep THREE families (do not collapse to one)

Harvest 2026-08-28, 324 English unique drafts, full-text grep:

| Family | Hits | Papers | Status |
|---|---:|---:|---|
| This study aimed to … | 45 | 44 | family 1 |
| To explore/investigate/evaluate/determine/assess/compare/develop … | 35 | 34 | family 2 |
| The aim of this study was to … | 22 | 14 | family 3 |
| The purpose of this study was to … | 12 | 12 | minority |
| We aimed to / We sought to … | 5 | 5 | rare |

- **"This study aimed to [objective] using [method] in [population]."**
- **"The aim of this study was to [objective]."**
- **"To [investigate/explore/evaluate/determine/assess/compare/develop] whether [technique] could [outcome] in [population]."**
- "The purpose of this study was to [develop/evaluate/compare] [model] for [task]." — minority; not a fourth default family.

### Methods sentence
- "A total of N patients with [condition] who underwent [imaging] were retrospectively enrolled."
- "Patients were randomly divided into a training set (n = N) and a test set (n = N)."
- "Radiomics features were reduced using LASSO, and a radiomics nomogram was constructed."
- "A total of N [subjects] were divided into [N] subgroups: [Group A] (n = N), [Group B] (n = N), [Group C] (n = N), and [Group D] (n = N)."
- Radiomics / prediction papers default to **training/test + LASSO + nomogram**. BODY split is training/test; Figure 1 labels Training Cohort / Test Cohort, plus Validation Cohort only when Methods states an external cohort. Other-hospital only = validation set.

### Results sentence
Default: report **AUC of X (95% CI: X–X)** for **both** training and test.
- "The AUC of the [model] was X (95% CI: X–X) in the training set and X (95% CI: X–X) in the test set."
- "The nomogram exhibited good discrimination in the training set (AUC X [95% CI, X–X]) and the test set (AUC X [95% CI, X–X])."
- Direct side-by-side AUCs are more common than `outperformed` (12 hits / 7 papers).
- "Significant [differences/elevations/reductions] were observed in [Group A] and [Group B], but not in [Group C]."

### Conclusion sentence
Do **not** use `demonstrated good performance` or `suggesting its potential` (0 hits in 389 unique drafts; see `vocab/L1/ban-phrases.md`).
- "The radiomics nomogram could improve [clinical decision/patient selection] for [treatment/procedure] in [population]."
- "In conclusion, the [model] achieved an AUC of X (95% CI: X–X) in the training set and X (95% CI: X–X) in the test set."
- "Both [A] and [B] play roles in [pathophysiology], with [specific conclusion]."

---

## Introduction Templates

### Opening sentences
- "[Condition X] refers to [definition], [epidemiological context] [1]."
- "[Condition X] is the [Nth] most common [tumor/disease] in [population], with an incidence of approximately X per 100,000 [2,3]."
- "[Condition X] is a [clinical challenge] because [reason], affecting approximately N patients annually worldwide [1]."

### Gap identification
- "However, the pathogenesis of [X] remains unclear."
- "Currently, [standard approach] remains the gold standard; however, it is limited by [limitation]."
- "The accurate [preoperative/non-invasive] [prediction/diagnosis] of [X] remains challenging."
- "Although [approach A] has been widely used, [limitation], which may lead to [adverse outcome]."

### Proposed approach
- "Recently, radiomics — a method for high-throughput extraction of quantitative features from medical images — has been applied to [task] and shown promising results [X–X]."
- "[Technique] has been proposed as a [non-invasive/functional] method for assessing [biomarker], enabling [clinical benefit] without [limitation of current approach]."
- "Intravoxel incoherent motion (IVIM) imaging can simultaneously reflect the [diffusion and perfusion] properties of tissue, providing additional [physiological] information beyond conventional DWI."

### Closing aim
Keep the same three purpose-sentence families as the abstract (do not collapse to one).
- "This study aimed to [objective] using [method] in [population]."
- "Therefore, the aim of this study was to [develop/evaluate/compare] [a radiomics nomogram/a combined model] for [task] in [population]."
- "To [investigate/evaluate] whether [technique] could [outcome] in [population]."
- "Thus, we hypothesized that [technique] could serve as a useful non-invasive tool for [task]." — hypothesis-framed variant, not a fourth family.

---

## Methods Templates

### Ethics statement
- "This [retrospective/prospective] study was approved by the Institutional Review Board of Jinshan Hospital of Fudan University (No. XXX), and the requirement for informed consent was waived due to the retrospective nature of the study."
- "Written informed consent was obtained from all patients prior to enrollment."
- "All experimental procedures were approved by the Animal Ethics Committee of [institution] (No. XXX) and conducted in accordance with institutional guidelines."

### Patient selection
- "Inclusion criteria were as follows: (1) [criterion 1]; (2) [criterion 2]; (3) [criterion 3]."
- "Patients were excluded if: (1) [criterion 1]; (2) [criterion 2]."
- "Patients were randomly divided into a training set (n = N) and a test set (n = N) at a ratio of X:X."  BODY: training/test. Figure 1: Training Cohort / Test Cohort, plus Validation Cohort only when Methods states an external cohort. Other-hospital only = validation set.

### Imaging protocol
- "All MRI examinations were performed on a X.X-T MRI scanner ([Manufacturer, Model]) using a [body/pelvic/head] coil."
- "DWI was performed with b values of 0 and 1,000 s/mm², and the corresponding ADC maps were automatically generated by the scanner's built-in software."
- "4D flow MRI was acquired with the following parameters: voxel size X×X×X mm³, temporal resolution X ms, VENC X cm/s."

### ROI delineation
- "Regions of interest (ROIs) were manually delineated on [sequence] images by two radiologists with X and X years of experience in [subspecialty] imaging, blinded to [clinical information]."
- "Inter-observer and intra-observer reproducibility were assessed using the intraclass correlation coefficient (ICC); ICC > 0.75 was considered good agreement."

### Radiomics pipeline
- "Radiomics features were extracted using pyradiomics (version X.X, https://pyradiomics.readthedocs.io) following the Image Biomarker Standardisation Initiative (IBSI) guidelines."
- "A total of N features were initially extracted, comprising first-order statistical features, shape-based features, and texture features (GLCM, GLRLM, GLSZM, and NGTDM)."
- "The least absolute shrinkage and selection operator (LASSO) regression with 10-fold cross-validation was used to select the most informative features and reduce dimensionality."
- "A radiomics score (rad-score) was calculated for each patient as a linear combination of selected features weighted by their respective LASSO coefficients."

### Statistical analysis
- "Continuous variables are presented as mean ± standard deviation (SD) or median (interquartile range [IQR]) according to the results of the Shapiro-Wilk normality test."
- "Categorical variables are expressed as frequencies and percentages."
- "Comparisons between groups were performed using the independent-samples t-test or Mann-Whitney U test for continuous variables, and the chi-square test or Fisher's exact test for categorical variables."
- "Receiver operating characteristic (ROC) curve analysis was performed to assess diagnostic performance, and areas under the ROC curves (AUCs) were compared using the DeLong method."
- "Decision curve analysis (DCA) was performed to evaluate the net clinical benefit of the predictive models."
- "All statistical analyses were performed using R software (version X.X; R Foundation for Statistical Computing, Vienna, Austria) and Python (version X.X). Differences with a P-value less than 0.05 were considered statistically significant."

---

## Results Templates

### Baseline characteristics
- "The clinical characteristics of the study population are summarized in Table 1. There were no significant differences in age, sex, or [variable] between the training and test sets (all P > 0.05)."

### Feature selection
- "After LASSO feature selection, N features with non-zero coefficients were retained and used to construct the radiomics signature (Figure X)."

### Model performance
Radiomics default: **training/test + LASSO + nomogram**. Report AUC of X (95% CI: X–X) for **both** training and test.
- "The AUC of the radiomics nomogram was X (95% CI: X–X) in the training set and X (95% CI: X–X) in the test set, with sensitivity of X% and specificity of X% in the training set."
- "The combination model was compared with the clinical model alone in the training set (AUC: X vs. X; P < 0.001 by DeLong test) and in the test set (AUC: X vs. X)."
- "The Hosmer-Lemeshow test indicated good calibration of the nomogram (P = X)."
- "Decision curve analysis showed that the radiomics nomogram provided greater net benefit than either the clinical model or the treat-all/treat-none strategies across a wide range of threshold probabilities (Figure X)."

### Negative findings
- "No significant difference was observed in [variable] between [group A] and [group B] (P = X)."
- "Significant [X] were observed in [Group A] and [Group B] rats, but not in [Group C] rats."

---

## Discussion Templates

### Opening summary
- "In this study, we demonstrated that [technique/model] could accurately [predict/differentiate/identify] [outcome] in [population], with AUC values of X–X across independent cohorts."
- "The main finding of this study was that [key result], suggesting that [clinical implication]."

### Literature comparison
- "This result is consistent with the findings of [Author et al.] [X], who reported [similar finding] in [similar population]."
- "In contrast, [Author et al.] [X] found [different result], which may be attributed to differences in [patient population/imaging protocol/feature selection method]."

### Mechanistic interpretation
- "The elevated [metabolite/parameter] in [group] may reflect [underlying pathophysiology], which is consistent with the known role of [pathway] in [condition]."
- "The higher ADC values observed in [group] might be related to [biological mechanism], suggesting [interpretation]."
- "Enrichment analysis indicated that abnormal metabolism of [pathway] in [condition] might be affected by [factor]."

### Clinical implications
- "The proposed nomogram could be used to guide individualized treatment decisions, potentially reducing unnecessary [procedures] in low-risk patients while ensuring appropriate management for high-risk cases."
- "Decision curve analysis showed that the radiomics nomogram provided a greater net benefit than the clinical model alone, supporting its potential clinical utility in [context]."
- "This non-invasive imaging-based approach could serve as a preoperative tool for [task], thereby optimizing clinical workflows and reducing the burden of [invasive procedure]."

### Limitations paragraph
- "This study has several limitations. First, the retrospective design may have introduced selection bias. Second, all patients were recruited from a single center, which may limit the generalizability of our findings. Third, the sample size was relatively small, and external validation in larger, multicenter cohorts is needed. Fourth, the manual delineation of ROIs is time-consuming and subject to interobserver variability; automated segmentation methods may improve reproducibility in future studies. **Future research should focus on larger, multicenter, prospective studies to validate and further refine the proposed model.**"
- Closing-sentence default is **"Future research should…" / "Future studies should…"** (18/96 and 9/96 respectively — corpus-dominant), not "…are warranted…" (a minority form, 14/96 total across *any* use of "warrant," not specific to this slot).

### Conclusion sentence
Do **not** close with `demonstrated good performance` or `suggesting its potential`.
- "In conclusion, the radiomics nomogram achieved an AUC of X (95% CI: X–X) in the training set and X (95% CI: X–X) in the test set and could assist [clinical application] in [population]."
- "In summary, both [A] and [B] play roles in [condition], with [specific mechanistic conclusion], providing new insights into the pathogenesis of [disease]."
