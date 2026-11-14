# Aitor-format (Aitor / Jinshan)

Formerly `house-format.md`.

**Owner:** `05_manuscript/advanced/`. Single source for **every English SCI full paper** in this lab.

**Blank manuscript template (new SCI paper: copy, then fill):**
`{doc_root}\templates\SCI-manuscript-scaffold.docx`（**空白 SCI 稿件骨架**，2026-11-04 建于 `_Docs\templates`；A4 + 2.54 cm、TNR 12 / 1.5、comments author **A**、无 Heading 1/2/3、无黄底。新稿起手只用这一份）

Canonical name is **`SCI-manuscript-scaffold.docx`**. An identical alias copy named `SCI-manuscript-blank.docx` may also sit in `{doc_root}\templates` after the local rewrite; it is the same file, not a second template. Point every fill at **scaffold** and do not edit the two apart.

**Gold reference (reply letter: Word typography and page geometry):**
`{doc_root}\templates\Aitor-format-gold-response.docx`（**回复信 / 字体版式金样**；不是新稿起手模板，字号、页边距、批注作者以它为准。原 `_templates\02-layout-template.docx` 已退休，勿再引用）

**Gold reference (reply-letter template, Markdown):**
`{doc_harvest_sources}\0doc-base-absorbed-20261023\_meta\02-response-letter-template.md`
（digest: `07_response/advanced/references/response-letter-template-digest.md`）

**Voice and revision marks (same Aitor-format, do not fork):**
`{doc_root}\templates\Aitor-format-gold-response.docx` (typography reference: A4, 2.54 cm margins, TNR 12, 1.5 spacing, comments author **A**) ·
(HISTORIC 2026-11-08: project sample of circular labels; the sample file is no longer on disk; delete extra tables).

Later-polish live files follow `Manuscript_<project-slug>_V<major>.<minor>.docx` or `_R<round>.<minor>.docx` (Rules SSOT) in the outcome folder. Use them for de-pipeline + number realignment only; **do not copy** sentence fusion, em-dash, internal `development`/`validation`, or disclaimer stacks.

If a rule is unclear, **ask the user**. Do not invent a second Aitor-format.
Letters / short communications: apply only if the user asks.

Voice and de-AI lists stay in `05_manuscript/advanced/route.md` + `05_manuscript/base/vocab/L1/ban-phrases.md` (+ optional `05_manuscript/advanced/vocab/L1/sci-overrides.md`; and `SKILL.md`); stats checklist stays in `02_data-processing/qc/report-checks.md`.

---

## Filename (standing)

`<Stem>_<project-slug>_` + `V<major>.<minor>` or `R<round>.<minor>` (proofs optional `P1` / `P1.1`) with Stem = `Manuscript` | `Comments` | `Response` | `Supplementary` (Supplementary only when supplements exist). Version matches the manuscript revision token. Prefer `.docx`. Rules SSOT → `{RULES}/project-ref-layout.md`.

**Version tokens (2026-11-06 t1698u, Rules SSOT, covers 2026-11-05 V2/V3/V9 map).** `V` = pre-submission, including post-submit edits before reviewer comments (`V1.1`…`V1.10`; no zero-padding; **sort numerically**). Moving `drafting` → `pre-submit` does not renumber; the submitted file keeps its `V` token. After submit, before comments, bump the V minor (e.g. `V1.11`); do not invent `R0`. `R` = after reviewer comments (`R1.1`, `R1.2` same round; next comments start `R2.1`). `P` = optional proofs (`P1` or `P1.1`). `Comments_` / `Response_` / `Supplementary_` share the same R (or P) token as that round’s manuscript; pre-submit V files usually have no Comments/Response. Reject-and-resubmit stays on V (major may bump, e.g. `V2.1`). After acceptance keep the last R; proofs use P.

## How to use

- Write or revise an SCI paper → follow this file.
- **New blank paper** → copy `{doc_root}\templates\SCI-manuscript-scaffold.docx` into the outcome folder as `Manuscript_<slug>_V1.1.docx`, then fill it. Do not invent numbers or ethics Date/NO to fill the skeleton. Fill slots and their order: § Blank SCI manuscript skeleton (below).
- Numbers only from the latest `*-results.html` / fixed tables. **Never invent** *n*, AUC, CI, *P*, ethics Date/NO, DOI, or unmade experiments. Never change an AUC/CI/*P* without re-reading that file. For ROC rows, take the **nomogram** (Combined) line, not a leftover pipeline `Combined` figure label that disagrees with Results.
- Canonical filename (standing, Rules SSOT): `Manuscript_<project-slug>_V<major>.<minor>.docx` (e.g. `Manuscript_lxf_PP_V1.1.docx` pre-submit) or `Manuscript_<project-slug>_R<round>.<minor>.docx` (e.g. `Manuscript_lxf_PP_R1.1.docx` after comments), plus same-token `Comments_` / `Response_` / `Supplementary_` for that R (or P) round. Prefer `.docx`; md/pdf companions share the stem. **Overwrite in place.** Authoritative → `{RULES}/project-ref-layout.md` (SCI 稿件文件名). Legacy `_house` / `_polished` stems are retired for new files.
- Embed current figures from the subproject `PNG/` (the paper must contain images).
- **No yellow fills.** Do not yellow-highlight empty slots (ethics Date/NO, author `[]`, missing *n*/AUC/DOI, unfinished phrases, placeholder cells). Missing method or product facts go in **Word comments only**, never in the body, never as yellow placeholders. Do not fabricate those facts. Same rule for **new writing and revision**.
- Word **Track Changes** and **comments** author: **A**. Never `Grok`.
- Ownership: see `00_orchestrator/references/ownership-contract.md`.
- **Do not change Word format** on an existing `.docx`. If a sentence differs from text 城城 already edited (tracked changes / known owner edits), treat it as the owner’s edit: **ask before overwriting**; do not restore the old sentence. Global stop → `{RULES}` `My rule.md` §5.1. HTML / PDF / scripts are out of scope. See `06_review/advanced/word-edit.md`; `references/writing-rules-hard.md`.
- **Do not overwrite existing front-matter:** if the manuscript already states corresponding author, funding, ethics (Date/NO), or affiliations, keep that text. Never replace it with lab defaults/templates unless the user explicitly asks. Missing items → Word comment / ask; do not fill placeholders with defaults.

---

## Page

- A4 (21.0 × 29.7 cm). Margins 2.54 cm all sides.
- Entire document uses Word **Normal** style. **Never** Heading 1/2/3.

---

## DOCX typography

**Times New Roman, 12 pt, black.** Line spacing **1.5**. Alignment **justified**. Direction **left to right**. Space before/after paragraph **0**. Space before/after text **0**. **Special paragraph format: none** (special format: none). Same typography for manuscript, comments shell, and response letter.

**Exception — response-letter reply bodies are blue (owner 2026-11-01 t1588u):** the author reply text under each `Response:` block in the response letter is **blue font** (RGB 0,0,255 or theme `Blue`); quoted reviewer comments stay black. Color overlay only — the font/spacing above still applies. Manuscript body and comments shell stay **black**. Rule SSOT: `07_response/advanced/response.md`. Do not make manuscript body blue.

**Dual track (2026-10-24):** body / legends shell = Times New Roman; **in-figure text (axes, panel labels, flowchart boxes) = Arial**. Do not mix the two inside one surface.

When **revising an existing `.docx`**: do **not** change Word format unless the owner asks this turn. Wording only via **Track Changes**, at **word- or sentence-level** (no large-block overwrite). See `06_review/advanced/word-edit.md`.

Bold is a content mark, not a restyle pass:

| Surface | Bold |
|---------|------|
| Paper title | **yes**, whole title |
| Authors (`Aitor¹`) | no |
| Affiliation | **no** |
| Title-page / abstract **labels** (`Corresponding author:` `Objective:` …) | **label + colon only**; rest of the same paragraph not bold |
| `Highlights` `Abbreviations` `Abstract` and IMRAD section titles | **yes** |
| Methods / Results **subtitles** | **yes** |
| Highlights body, abbreviations body, references, table notes | no |
| Body after abstract | no |
| `Table N.` / `Figure N.` / `Supplementary …` **prefix** | **prefix only** |
| Table **cells** | header row yes |

There is **no 16 pt title** and **no 14 pt section title**. Do not restyle table cells on revision.

- *P* italic. `n = N`. `95% CI: X–X` or `95% CI: X-X` (no spaces). Not `X to X`. **Hard ban** em-dash (U+2014 / spaced `--`); replace with **parentheses**. **En dash allowed** (U+2013): numeric ranges, CIs and page spans may use it (`0.80–0.93`, `5–10 mm`, `123–145`); ASCII hyphen `-` stays fine where already used (owner t1683u, 2026-11-06; reverses the 2026-10-30 en-dash ban). **Unicode minus allowed** (U+2212): signed numbers and difference spans may use it (`−0.32`, `Q3−Q1`); ASCII `-` stays fine (owner t1761u, 2026-11-07). **Hard ban** `≈` (write `about` / exact). Colon and semicolon are **discourage** (不推荐) in running prose — keep label colons (`Objective:` `95% CI:`).
- **English punctuation only.**
- English sentence ≤55 words. **One fact per sentence.** Do not merge adjacent sentences with semicolons (不推荐) or stacked *and*; prefer a period. Related short sentences still belong in the **same paragraph** (as paragraphs); do not lay out one sentence per line or one sentence per paragraph — see `voice-portrait.md` Paragraph lock.
- Software: `Analyses were performed in Python 3.13.` (version after Python; no parentheses unless the user adds a build, e.g. 3.13.9).
- Split names (full paper), three words only:
  - **training set** — internal fitting (never `development set` / `Dev`)
  - **test set** — internal evaluation (never `hold-out`, `holdout`, or `hold out`)
  - **validation set** — the external confirmation cohort (never `external test set`)
  Compound forms: `training-set`, `training-fitted`, `test-set`, `test AUC`, `validation-set`. Sentence start: `Training-set` / `Test-set` / `Validation-set`. Keep `10-fold cross-validation` (algorithm, not a cohort). If no external cohort exists, put `No validation set was available` or `A validation set is required` in a **Word comment only** (author **A**) — never in the body, Conclusion, Limitations, Highlights, or Figure 1. An external file with too few events for a stable AUC stays in a **Word comment** unless the user asks to write it. Still never `hold-out` or `external test set`.

---

## Title page order

Title → Authors → Affiliation →
`Corresponding author:` `Funding:` `Ethics:` `Acknowledgments:` `Author contributions:` `Data availability:` →
`Highlights` (3 bullets) → `Abbreviations` (alphabetized, terms used ≥2 times; expand at first use in the body).

| Field | Default text |
|-------|----------------|
| Affiliation | `1 Department of Radiology, Jinshan Hospital of Fudan University, 1508 Longhang Road, Shanghai 201508, China` |
| Corresponding author | `Aitor, E-mail: `(see mem:corresponding_email) |
| Funding | `This work was funded by Jinshan Hospital (KYQDJJ202501) to Hai-Feng Shi.` |
| Ethics | IRB of Jinshan Hospital of Fudan University (Date:  , NO:  ). Retrospective waiver. Helsinki allowed. |
| Acknowledgments | `None` |
| Author contributions | `[]`: writing original draft, data collection, and statistical analysis. `[]`: data collection and manuscript revision. `Aitor`: conceptualization, writing-review and editing, and correspondence. |
| Data availability | `The raw data of this manuscript are available from the corresponding author on reasonable request.` |

Delete pipeline banners. Hai-Feng Shi in **Funding only**.

**Highlights (3 bullets).** Report findings, not missing data. Do **not** write “No validation set was available” or “A validation set is required” as a highlight (comments only). A missing **product** (empty radiomics sheet, no RadScore / nomogram) is a **Word comment**, not a highlight and not body text. Typical order: main test-set metric → incremental value when it exists → a later endpoint that was analyzed.

`Highlights` and `Abbreviations` may take a colon; bold through the colon.

---

## Abstract

Same-paragraph labels, **bold through the colon only**:
`Objective:` `Methods:` `Results:` `Conclusion:` `Keywords:`
Flush left, no indent. Objective → Methods (*n*) → Results (AUC, CI) → hedged Conclusion.

Lead Results with **test-set** AUC (training in parentheses if needed). If a nomogram, calibration, NRI, or RadScore was not exported, put that fact in a **Word comment** (author **A**); do not write it in Methods, Results, or Highlights. Do not invent those numbers.

---

## Document order

Title page → Abstract → Keywords → Introduction → Materials and Methods → Results → Discussion → Conclusion → References → Tables → Figures → Supplementary files (if any).

Methods still opens with Ethics even if ethics is on the title page.

---

## Citation

- Vancouver / NLM + DOI on every entry. Number by first appearance.
- Do not cite every sentence. Shared source on neighbouring sentences: cite once.
- Do not reuse an earlier number after a later number has entered.
- No `[1-3]` clusters.
- Introduction 800-1000 words, 10-15 refs. **Last paragraph (aim / hypothesis): no citations.**
- Discussion 800-1000 words, 10-15 **new** refs (no overlap with Introduction). **First paragraph: no citations.**
- Those 10-15 / 10-15-new quotas apply when **writing new** Introduction / Discussion. When **checking an already-written** manuscript, do **not** delete genuine references to hit the quota; note over-quota only.
- When **revising an existing** manuscript, reorder in-text Vancouver numbers to appearance order against the reference list. If the reference list contains a duplicate entry, replace that duplicate with an already-verified substitute (author **A**). This duplicate-list exception only.
- **Methods: no citations.**
- References: flush left, **no hanging indent**.

---

## Introduction (800-1000 words)

Five paragraphs, eight beats, in funnel order (owner 2026-10-30 t1401u/t1402u). Beats in the same paragraph are one to three sentences each; related studies may run longer inside para 3.

1. **Disease / burden** (para 1). Opening cites the verified source when one exists. Zero citations here is a fail (`05_manuscript/qc/manuscript-local-qc.md`, `intro_opening_has_citations`).
2. **Clinical significance** (para 1). Why the disease or decision matters for patients or practice.
3. **Guideline definition** (para 2). Latest edition that defines the endpoint or clinical decision as **diagnostic criteria or examination criteria** (issuing body and year, verified by 03 in the same session; see `05_manuscript/advanced/process/evidence.md`). Paraphrase the definition. State the decision that rests on it.
4. **Current standards / methods** (para 2). Routine standards or tests the guideline relies on, and what they leave open or cannot resolve.
5. **Latest research methods (this study)** (para 3). Name the method family this study uses, as current research practice (hedged), not as a solved problem.
6. **Related studies** (para 3). Main results of the two or three most relevant studies (n, design, effect). Then one or two sentences that appraise them as a group: the strength this study keeps and the weakness this study targets. No study-by-study list.
7. **Gap and method link** (para 4). One open question stated as an unknown, then one sentence on why this study's method may address it. Inference is allowed and must be hedged (*may*, *could*). Never *solves*, *overcomes*, *resolves*.
8. **Aim and hypothesis - no citations** (para 5). One endpoint name, identical in the Abstract, Methods (Outcomes), and here. The hypothesis names the set (test set) and the comparator.

Sentence length (Introduction and Discussion)

- Every sentence 10-30 words. None over 30. None under 10 except a fixed technical expression.

Structure bans (Introduction first; Discussion deferred until explicitly extended)

- In the Introduction: no listing, no parallelism. At most one triplet per paragraph. No two consecutive sentences with the same opening words. No run of three sentences that each carry a number and a citation. No enumeration of studies.
- Do not cite the same paper in consecutive sentences unless the second sentence adds a distinct claim that paper supports.
- Related short sentences stay in one paragraph (Paragraph lock in `voice-portrait.md`). Do not flatten the Introduction into one sentence per paragraph.
- Reporting guidelines (TRIPOD, TRIPOD+AI, CLAIM, CLEAR) are writing standards. Do not name or cite them in the Introduction. A required statement goes in the checklist file or the submission form.
- Claim-source fit outranks citation numbering. Never place or reorder a sentence only to keep numbers ascending. Renumber afterwards by script (appearance order vs reference list). Authenticity: `verify-refs`.
- A scarcity claim ("few studies", "remains uncommon") needs a logged search (two sources, dates, queries) and is worded as what was found, not as what exists.
- No current-study AUC dump. Expand abbreviations at first use.

Evidence handling: `05_manuscript/advanced/process/evidence.md`. Scoring anchors and deduction codes: `05_manuscript/qc/manuscript-local-qc.md`. Pre-submit number, placeholder, and sister-paper checks: `05_manuscript/qc/manuscript-local-qc.md`. Base contract: `05_manuscript/base/write-paper/radiology-writing/introduction.md`.


---

## Methods — fixed order

1. **Ethics** — subtitle is `Ethics` (never `Ethics: Ethics`).
2. **Study design and sample size** — honest split. Estimation **was performed** (post hoc allowed). State **α = 0.05**, **β = 0.20** (power 80%), observed event proportion *p*, required events ≥ 10 per fitted nomogram coefficient, and whether this sample met that threshold — **once here**. Do **not** keep re-elaborating sample size / power / adequacy across Abstract, Results, Discussion, Highlights, or Limitations. Patients *n* and group counts appear in Patients / Results tables; do not restack the calculation narrative. Never write that a calculation “was not performed.” **Never mention a random seed.**
3. **Patients** — Jinshan default **1 August 2024 to 1 August 2026** (not ADNI). Analyzed *n*. Group counts: `(Stroke, n = 89; non-stroke, n = 187)`, not `(Stroke 89, non_Stroke 187)`. Prefer *patients were analyzed and divided* over *cases were split*. No subject IDs. No “pipeline treated rows as observations.” Do **not** narrate dataset-build / QC filters as eligibility (e.g. *Eligibility required a complete binary outcome label and a complete … feature row*; *Records matching a predefined exclusion list were removed*). Write clinical inclusion/exclusion only; row-completeness and feature-matrix filters stay in the analysis pipeline, not Methods prose. Secondary ADNI / non-Jinshan extracts: say so here or in Limitations, not as a worksheet dump.
4. **Inclusion and exclusion** — one paragraph each; inline `follows: (1) x; (2) y; and (3) z`, not a vertical list.
5. **Diagnostic and treatment criteria**
6. **Outcomes** — pathology **positive versus absent** (e.g. LVSI) or a **follow-up / RECIST** event (e.g. ORR = CR/PR versus SD/PD). Use the clinical name (stroke, recurrence, dedifferentiated). **Do not write *coded* or *displayed*** as an endpoint prefix. **Never put raw pre-stats coding in prose or tables** (e.g. `Positive = 1, Negative = 0`; `1 = event, 0 = none`). That encoding lives only in the analysis dataset; the manuscript uses clinical names (positive / negative, present / absent, event / no event). If labels were not locally re-adjudicated, say so **once** in Outcomes or Limitations (*labels followed the source field; they were not re-read against a local protocol*). Do not claim local re-adjudication.
7. **Laboratory tests** — pathologic endpoint: labs within **30 days** of pathology. Do not apply that sentence to pure survival / response-horizon papers.
8. **Imaging examinations** — MRI: primarily 3.0 T Magnetom Verio (Siemens Healthineers, Erlangen, Germany). CT: primarily Canon Aquilion (Canon Medical Systems, Otawara, Japan). Minority-of-scanners sentence allowed.
9. **Image processing** — method only. No QC field dumps. Lead-in fragments allowed (`Tumor segmentation.` `Preprocessing.`). Write method choices that were actually decided (e.g. no ICC filter, no IBSI phantom). An **empty radiomics sheet** or other missing product is a **Word comment**, not body text. Habitats are imaging constructs, not histologic maps. Spatial ratios / subfield percentages are not a texture-radiomics panel unless that matrix exists.
10. **Model building** — patient-level split; **training-set** selection only; **test set** for evaluation only. Primary model = **nomogram** (the Combined / combined logistic model; do not use those pipeline names). Youden is **split-specific** unless a training threshold was actually fixed. A predictor that is part of the label (MMSE in MCI, a symptom field that already contains infarction) is **not** an independent imaging biomarker — say so here. Variables that were recorded but **not** used as candidate predictors (e.g. treatment type, chemotherapy agent) go in a **Word comment only** — never Methods/Results body (“recorded … but were not included…”).
11. **Statistical analysis** — start with `Analyses were performed in Python 3.13.` (no package list). Write **median and interquartile range**. If calibration, DCA, NRI, IDI, or mediation were not exported, put **not generated / not exported** in a **Word comment only**. Do not invent them. Do not write that sentence in the body.

Fill slots for each of these subtitles, in this order: § Blank SCI manuscript skeleton (`SCI-manuscript-scaffold.docx`). Owner slot names there map onto these subtitles; they never add a new subtitle.

### Methods subtitle packs (corpus-derived, 2026-11-05)

The 11-row order above **is** pack `A_imaging-radiomics`. Four further families exist in the corpus and keep the same anchors (Ethics → Study design and sample size → Patients → Inclusion and exclusion criteria → Diagnostic and treatment criteria → Outcomes → … → Statistical analysis last). Pick one pack per paper; only the **mid block** changes.

| Pack | Use when | Mid block, in order |
|---|---|---|
| `A_imaging-radiomics` | imaging + radiomics / habitat features + a model, one `Model building` | `Imaging examinations` → `Image processing` → `Model building` |
| `A2_radiomics-granular` | same content, pipeline split step by step | `Clinical feature selection` → `Imaging examinations` → `Image processing` → `Model building` (development) → `Model building` (evaluation) → optional `Clinical usefulness` |
| `B_imaging-only` | imaging reading (US / CT / MRI), no feature matrix, no model | `Imaging examinations` → `Image processing` (image analysis) |
| `C_clinical-lab` | no imaging model; the study's own assay / intervention / bench chain | assay, trial, bench, or measurement chain (see reference below) |
| `D_neuroimaging-multimetric` | per-metric brain imaging (ASL / VBM / SBM / ALFF / ReHo / FC / DMN / Fazekas / SPM-LST) | `Imaging examinations` → `Image processing` → one subtitle per metric → optional correlation / mediation |

Pack rules:

- **Evaluation splits into its own subtitle only in `A2`** (83% of that pack). In A / B / C / D it stays inside `Model building`.
- Feature extraction and selection fold into `Image processing`; only `A2` keeps clinical feature selection and imaging feature selection as their own subtitles.
- `Clinical usefulness` / diagnostic-performance subtitles are optional extras, never required slots.
- **Results subtitles follow the chosen pack order, not a one-for-one mirror** (owner t1671u). Some Methods steps produce no result. A Methods-only step may have no Results subtitle; do not invent Results to close it. Keep the asymmetric defect: a Results subtitle with no Methods parent is a defect.
- Do not copy these corpus defects: `Ethics: Ethics`, a run-in `Ethics:` label inside the first paragraph, `Study design and sample size` moved into Results, and `Reporting guideline` / `General information` / `None` used as subtitles.

Full tables (per-slot required / optional / absent, corpus aliases, evidence paths, corpus→canonical normalization): `{doc_skill_harvest}\methods-subtitle-variants\methods-subtitle-packs.md`. Heading frequency and the per-paper extraction log sit in the same folder (46 manuscripts, 2026-11-05).

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

**Decimal places (house):**
- **Table 1** continuous / percentage cells: **1 or 2** decimal places (pick one depth per variable family and keep it; do not spray 3+ decimals in baseline tables).
- ***P* values**, **AUC** and AUC-related metrics (95% CI bounds for AUC, DeLong *P*, and the same family), **NRI / IDI**, and **correlation** coefficients (*r* / ρ and their *P*): **3** decimal places (e.g. `P = 0.002`, `AUC of 0.812 (95% CI: 0.745-0.879)`, `NRI = 0.123`).
- Do not round these 3-decimal metrics down to 2 in prose or tables just for neatness.

**Do not create these tables** (numbers go in Results prose and/or the matching figure):
LASSO-feature list · nomogram / clinical logistic-coefficient table · SHAP table · score-correlation table (RadScore × age/group) · mediation (ACME) table.

RadScore formula and nomogram coefficients stay in Results prose. SHAP ranks and mediation paths stay in prose + figures.

Typical Results order: Patient characteristics → model construction (formula) → discrimination (Table of operating characteristics + Figure 2) → incremental value / calibration / utility → optional SHAP / correlation / exploratory mediation. Lead the imaging-only score before a circular clinical score when both exist.

**Incremental value (test set).** Re-read the latest `*-results.html` before writing this sentence. House templates that say *did not improve* are often wrong once the nomogram row is higher than RadScore/Clinical. If the nomogram AUC does not exceed RadScore or Clinical: **no incremental test-set value**. If it is numerically higher but DeLong (or an equivalent paired AUC test) was **not** run: *improved* is allowed **only in the same sentence** as the missing test (`…improved test-set AUC beyond the RadScore, although this difference was not confirmed by a DeLong test.`). Never write *improved* / *incremental* without that caveat. Figure-legend AUCs must match the **nomogram** Results numbers, not a Combined-row leftover.

Impossible or biologically implausible lab cells: shown, not interpreted; *P* = **NC** (not calculated). Say so once in the table note.

---

## Discussion (800-1000 words)

Inverted funnel (owner 2026-10-30 t1404u): key findings (no cites/numbers) → literature contrast per finding → hedged mechanism if any → one clinical use-case → Limitations own paragraph → Conclusion. Every Introduction aim/hypothesis must be answered here (finding, limitation, or explicit deferral); QC: `manuscript-local-qc.md` Part A2 / LOG-5.

Do **not** compress Discussion by page quota (no “cut to 1.5 pages”). Length follows the word band and content need.

1. Key findings — **no citations, no result numbers**.
2. One block per finding — new literature; still no copied AUCs.
3. Clinical application — **one** short use-case sentence. No disclaimer stack (*It is not a replacement… A high score should not…*).
4. **Limitations: its own paragraph**, First… Second… Put label circularity **First** when a predictor is part of the endpoint. Facts only. No closer *rather than a ready clinical tool*. Prefer **no citations** in Limitations; a needed literature contrast belongs in the earlier literature-contrast block, not here (owner t1671u). Check the ordinals: `First` / `Second` / `Third` … must be sequential, complete, and in the actual sentence order; the count of ordinals must match the number of limitation sentences.
5. **Conclusion** — 2-3 sentences; echo the objective; **no AUC / CI / *n***. If no external cohort exists, *A validation set is required* / *No validation set was available* go in a **Word comment only** — never in Conclusion, Limitations, Highlights, or Figure 1.

---

## Blank SCI manuscript skeleton (SCI-manuscript-scaffold.docx)

Fill-slot map for the blank manuscript at `{doc_root}\templates\SCI-manuscript-scaffold.docx`, for radiomics / clinical-plus-imaging prediction papers (owner t1643-t1645u, absorbed t1647u). This is **not** a second format: it is the slot checklist used to enrich that docx from corpus (Cline / agents). Page, typography, bans, quotas, bold marks, and the Methods fixed order above are unchanged and still govern. Spelling: **preprocessing**, **NRI/IDI** (never NIR). **Results subtitles follow the Methods order. Some Methods steps produce no Results; leave those without a Results subtitle (owner t1671u).**

Placeholders are the only fill values allowed in the skeleton: `[PLACEHOLDER: …]`. Never bake a real IRB number, AUC, scanner serial, or DOI into this skill as a required value. Jinshan defaults already in the title-page table and the scanner pair in Methods may stay as defaults; every project-specific value stays a placeholder until verified against the source.

### Paragraph lock when filling the blank

Slots below are a **content checklist, not paragraph units**. Filling a slot never licenses one line per slot. `05_manuscript/advanced/voice-portrait.md` Paragraph lock governs; `05_manuscript/qc/manuscript-local-qc.md` FLU-4 scores it.

- **Continuous paragraphs.** IMRAD body = continuous Word paragraphs. Ban one sentence per `w:p`, and ban soft-return fake breaks (Shift+Enter / `w:br` inside one `w:p`) posing as paragraph breaks.
- **Slots 1-14 are a checklist.** The Methods fill slots 1-14 and the Discussion content checklist are content to cover, not one slot per paragraph. Merge related sentences inside one subsection into the same paragraph.
- **Subsection titles** may be their own paragraph (**bold** Normal); never Heading 1/2/3.
- **Body targets.** Methods 1-3 paragraphs per subsection; Results 1-2; Introduction = **4 real paragraphs**, with aim and hypothesis in the **same** paragraph. § Introduction's eight beats keep their order inside those four; a working draft already on its five-paragraph map is not re-cut for count. Abstract: each labeled block (`Objective:` `Methods:` `Results:` `Conclusion:`) stays one paragraph. Discussion: inverted funnel (§ Discussion), with Limitations as one paragraph using `First… Second…`, never bullet rows.
- **Inclusion / exclusion:** inline `(1)(2)(3)` inside one paragraph each. Vertical `-` drafting bullets are deleted before submission.
- **Teaching labels** (`Paragraph N`, `Move …`, `Context` meta lines) are deleted after fill; comments author **A** drafting notes may stay.
- If the scaffold still shows one-sentence paragraphs, **this lock wins** and the filler merges them.

### Nesting rule (owner names ↔ existing Methods names)

Owner slot names map onto the existing Methods fixed order; they do not add subtitles. Where a name differs, use the existing subtitle.

| Blank slot (owner) | Existing Methods subtitle above |
|---|---|
| Ethics | `Ethics` |
| Study design | `Study design and sample size` |
| Patients | `Patients` |
| Inclusion and exclusion | `Inclusion and exclusion` |
| Outcomes | `Outcomes` (stays after inclusion/exclusion; not relocated) |
| Laboratory tests | `Laboratory tests` |
| Clinical feature selection | slot inside `Model building` |
| Imaging scanning | `Imaging examinations` (one paragraph per modality) |
| Imaging preprocessing | `Image processing` (ROI / ICC / software) |
| Imaging feature extraction | inside `Image processing` |
| Imaging feature selection | inside `Image processing` or `Model building` |
| Model development, model evaluation | `Model building` (+ statistics evaluation slots) |
| Statistical analysis | `Statistical analysis` |

### Front matter slots

Title · Running title · Authors · Affiliations · Corresponding author · Keywords · Abbreviations · structured Abstract. Abstract labels stay `Background:` or `Objective:`, then `Methods:` `Results:` `Conclusion:` per § Abstract, bold through the colon only. The Abstract sentence order follows the **Methods subsection names** written for that project, not a generic order.

### Introduction scaffolds

Beat labels only; the shape is § Introduction above (five paragraphs, eight beats). Each scaffold paragraph is annotated with its intra-paragraph logic: **topic → evidence → gap → bridge**. A corpus extract fills the beat, never a new funnel.

### Methods fill slots

1. **Ethics.** Committee full name; approval number; approval date; approval coverage time range (伦理期 = the approval's validity start–end; see `03_research/advanced/ethics.md` § Ethics validity period / 伦理期); consent or waiver; Helsinki statement; optional registry ID. Missing values → **Word comment**, never a yellow fill.
2. **Study design.** Collection window; retrospective or prospective; single or multicenter; study type; primary objective plus optional secondary objective; split (e.g. `7:3`); independent validation set yes or no; optional stratification note. A seed policy may be logged in the working file, but the seed itself never enters manuscript prose (**no random seed**, ban above).
3. **Patients.** Consecutive or not; department; disease; clinical features list (age, sex, and the rest of the Table 1 baseline set); pointers to the flowchart (`Figure 1`) and `Table 1`.
4. **Inclusion and exclusion.** One paragraph each, inline numbering. Add the **time-alignment rule** for imaging, labs, and outcome versus enrollment.
5. **Outcomes.** Immediately after inclusion and exclusion. Primary definition plus reference standard; follow-up yes or no with its rules; optional secondary outcome. One endpoint name, identical in Abstract, Introduction aim, and here.
6. **Laboratory tests.** Timing slot, e.g. `±7 days of enrollment`, with the existing pathology default of 30 days kept for pathologic endpoints; clustered panels (liver, renal, coagulation, others); optional units and missing-value handling.
7. **Clinical feature selection.** Univariable screen, then multivariable logistic regression; entry *P*; collinearity handling; report OR with `95% CI: X-X`.
8. **Imaging scanning** (one paragraph per modality). Timing; scanner model, company, country; sequences and parameters; contrast yes or no; agent trade name, company, country; injection rate and delay; optional acquisition QC note.
9. **Imaging preprocessing.** Software name, version, URL; ROI yes or no; manual or automatic; intra- and inter-reader ICC with the 30-day re-ROI; optional resampling, normalization, registration, and reader blinding.
10. **Imaging feature extraction.** Software name, version, URL; feature classes; optional IBSI compliance statement and feature count.
11. **Imaging feature selection pipeline.** Fixed order: normalize → ICC filter → remove correlated features → LASSO or logistic selection → linear fit. Thresholds and the λ rule stay `[PLACEHOLDER: …]`.
12. **Model development.** One paragraph each for the clinical model, the radiomics model, and the combined or nomogram model; training-set versus test-set reminder; cross-validation and calibration method placeholders. Primary model is the **nomogram**.
13. **Model evaluation.** ROC with DeLong; calibration (nomogram only); DCA; NRI/IDI; sensitivity, specificity, accuracy, AUC with 95% CI; cutoff rule; bootstrap intervals.
14. **Statistical analysis.** Software name, version, URL; normality check; parametric versus non-parametric choice; *P* adjustment; correlation and partial correlation; subgroup and sensitivity analyses; SHAP; two-sided α; missing-data strategy.

### Results fill slots

Subtitles follow the Methods order, not a one-for-one mirror (owner t1671u). A Methods-only step may have no Results subtitle; do not invent one. A Results subtitle with no Methods parent is still a defect. Fill flowchart counts, then table and figure cross-references in the first body paragraph (`The study flowchart is shown in Figure 1.`). An unfilled Results section keeps its heading and carries `Results pending [PLACEHOLDER: …]`; do not drop the heading in the blank. Never invent a count, AUC, or *P* to close a slot.

### Discussion content checklist (radiomics blank)

The inverted funnel in § Discussion is the **voice and QC rule** (word band 800-1000, first paragraph no citations or numbers, Limitations in its own paragraph with at most five `First…Second…` items, Conclusion with no AUC). The slots below are the **content checklist** for enriching the blank, and they nest inside that funnel:

1. **Context 1** (clinical versus radiomics findings kept separate; contrast with published models and markers; concordant results → disease meaning; discordant results → reasons).
2. **Context 2** (first modality).
3. **Context 3** (second modality).
4. **ROC comparison** paragraph.
5. **Clinical utility** (DCA, NRI/IDI, nomogram) against the literature.
6. **Limitations** (at most five items; prefer no citations; ordinals `First… Second…` sequential and in sentence order).
7. **Conclusion**.

Write a bridge sentence between consecutive Contexts. No number may appear here that is absent from Results.

### Optional end matter

Data availability · Code availability · Acknowledgments · Funding · Conflict of interest · Author contributions. Each is a placeholder line until the project supplies the fact; keep the title-page defaults only where § Title page order lists them.

### Corpus enrich note (Cline / agents)

When enriching `SCI-manuscript-scaffold.docx` from corpus: extract generalized scaffolds only; write an optional `{doc_root}\templates\EXTRACT-LOG.md` beside the templates recording what each extract came from; do not hard-code one project's ethics, device, or results into the blank; keep Aitor-format typography and the bold marks above.

---

## Tables

- Three-line (top / header / bottom); **no verticals**; **thin** single lines (`sz` about 4), **not bold**.
- Title above: `Table 1. ` **bold**; remainder not bold; flush left.
- Notes below: 12 pt, flush left, no indent (justified allowed). **No** `Source: *-results.html` and **no** file paths.
- Header cells: **no** `(n = 57)`.
- Cells: **12 pt**, single spacing, header bold. (2026-10-24 adjudicated; was 11 pt)

---

## Figures

- Figure legends sit **below** the figure (not above).


- Embed the latest PNGs.
- Image first, legend below.
- **Figure 1 (study flowchart):** one paragraph. `Figure 1. ` bold; rest not bold. This is the only flowchart. Do not also draw an enrollment-only figure. Boxes and counts are read from **Materials and Methods** only: collection period and screened *n*; inclusion beside exclusion; patients included with both group counts; **Training Cohort** and **Test Cohort** on one row, each with both group counts; **Validation Cohort** on that same row only when Methods states an external cohort and its counts. Downsample or SMOTE, LASSO, Clinical / Radiomics / Nomogram, and ROC AUC, calibration, DCA, NRI, IDI, DAG, or mediation are drawn only when Methods names them. Downsample is not an exclusion criterion. Do not invent a missing count or a missing step. Canonical file is **PDF** (preferred over PNG), **Arial** 12 pt, black (`bbox_inches=tight`, `pad_inches=0`). (2026-10-24: PDF + figure Arial dual-track.) Do **not** add “the figure does not depict a validation set.”
- **Figure 2 and later:**
  - Line 1 — short title (`Figure 2. ` bold + short name), flush left, no indent.
  - Next paragraph — what the panel shows, same as body. Annotate panels **(A)** / **(B)** or left/right sets separately.
- One figure-specific qualifier is allowed if it is not already in Results (e.g. SHAP is exploratory). Do **not** reprint Discussion caveats or legal disclaimers in legends.
- Supplementary figures: prefix bold; note flush left, no indent. Unused template nodes on a DAG must be named as unused.
- Flowchart export: `bbox_inches=tight`, `pad_inches=0`.

---

## No disclaimers, no repetition

**Process negation / not-done class (owner 2026-10-23):** Process-negation sentences that flag work not done («未做 / 未进行 / 我们未…» or similar CYA) **must not enter the body** (manuscript, revision, response letter). Put them only in Word **批注** (author **A**), and every comment must include **建议修改后内容**; bare flags forbidden. Empirical negative findings of the study itself (e.g. *no significant difference*、*was not associated with*）not banned by this rule。QC：`05_manuscript/qc/anti-leak-placeholders.md` AL-5；`07_response/qc/disclaimer-comment-only.md`。

SCI full papers have **no disclaimer**. Ban (owner 2026-10-21 / 2026-10-23: process-negation / disclaimer/CYA/未做-class → Word 批注 only, with 建议修改后内容 — never body; see `05_manuscript/qc/anti-leak-placeholders.md` AL-5):

- *for research use only* / *not medical advice* / *the authors disclaim*
- *not a ready clinical tool*
- parallel negation: *It is not a replacement for… It is not a… A high score should not… A low score should not…*
- the same *does not demonstrate effect on decisions or outcomes* copied into Results + Discussion + figure legend

One scientific bound, **one place**. Do not restate the same hedge in Highlights, Abstract, Discussion, figure legend, and Conclusion.

## Banned voice

- `QC_MI_Warn`, `Habitat_Mode`, `Fusion_Channels`, `Align_Verify_NSeq`, “continued after mutual-information registration warnings…”
- Group / non_Group, clinical matrix, worksheets not re-exported
- `coded` / `displayed` as an endpoint prefix (`coded stroke`, `coded recurrence`, `displayed Stroke`)
- Raw pre-stats coding dumps: `Positive = 1, Negative = 0`; `1 = event / 0 = none`; `outcome coded as 0/1` — analysis-dataset only, never manuscript body/Methods/tables footnotes
- `median [interquartile range]` / `median [IQR]`
- “A sample-size calculation was not performed.”
- Repeated sample-size / power / adequacy essays outside the single Methods slot
- `was not tested` / `未测` / `未完成` (incomplete work → Word comments; never body)
- “Recorded in the source data but were not included as candidate predictors” (and kin: collected/available but unused) → **Word comment only**, never body
- `No validation set was available` / `A validation set is required` in the body, Conclusion, or Limitations (comments only)
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
- Dataset-build eligibility voice: *complete binary outcome label*; *complete … feature row*; *predefined exclusion list were removed*; *required a complete … row* — clinical inclusion/exclusion only
- Package lists after `Python 3.13`
- Disclaimer / CYA stacks listed above
- `Ethics: Ethics` as a double subtitle (subtitle is `Ethics`)
- `Reader_1` (write `Reader 1`); `Negstive` / `non_Stroke` (write `Negative` / `non-stroke`)

De-pipeline replacements (second polish pass; do not reorder IMRAD):

| Avoid | Prefer |
|-------|--------|
| `project clinical data` / `matrix` / `HTML` / `export` | `clinical database` / `dataset` / `source` |
| `The pipeline was configured to retain` | `Features … were retained` |
| `Eligibility required a complete binary outcome label…` / `complete … feature row` / `predefined exclusion list were removed` | Clinical inclusion/exclusion only; drop row-completeness / feature-matrix filter narration |
| `outlined with ITK-SNAP` | `segmented using ITK-SNAP` |
| `built inside the tumor mask` | `constructed within the tumor mask` |
| `cases were split` | `patients were analyzed and divided` |
| empty `[]` authors or `(Date: , NO: )` | Word comment (author **A**); do **not** yellow-fill `[author name to be completed]` / `[Date to be completed]` / `[NO to be completed]` |

Do **not** take later-polish files as license to fuse sentences, add em-dashes, call the internal split a validation set, or stack *It is not a replacement…*.

---

## Reporting defaults

1. Nomogram = Combined model. Incremental wording: see Results (DeLong caveat).
2. Full-cohort habitat / clustering: say so.
3. Per-split Youden: write that.
4. Cloned train/test 2×2: do not cite.
5. Never mention a random seed.
6. Specified but not generated (empty radiomics sheet, no nomogram, no calibration, no DCA): **Word comment only** (`not generated`). Do not invent figures. Do not put that sentence in the body. Same for predictors/covariates that exist in the source data but were not entered into the model.
7. A field that overlaps the endpoint (MMSE in the MCI label; a symptom code that already contains infarction) is a **coding / circular** result, not an independent imaging biomarker.
8. Worksheet group names (`non_Stroke`, `Negstive`) are cleaned in prose. Do not prefix the endpoint with *coded* / *displayed*. Un-readjudicated labels: one Methods or Limitations sentence, not a running prefix.

---

## QC before done

- No Heading styles
- Title and all section/subtitle headings **12 pt bold** as content marks; do not restyle an existing file
- Affiliation **12 pt, not bold**
- Labels bold **only through the colon**
- Body: TNR 12 / 1.5 / justified / LTR / space 0; do not restyle an existing Word file
- Highlights, abbreviations, references, table notes: TNR 12 / 1.5 / justified / space 0; do not restyle an existing file
- Results subtitles bold as content; do not restyle an existing file
- Figure 1 one paragraph; later figures = short title + detailed body paragraph
- Images embedded
- First Results paragraph has Figure 1 sentence + binary-percentage sentence (period between them)
- Table 1 = training vs test wide table; no LASSO / logistic-coeff / SHAP / correlation / mediation tables
- Decimals: Table 1 → 1-2 places; *P* / AUC(+CI) / NRI/IDI / correlation → 3 places
- No `hold-out`; training = internal fitting; test = internal evaluation; validation set = external cohort only
- No results.html / QC / STROBE path footers
- Highlights do not advertise a missing validation set
- Circular predictors named as circular
- No *coded* / *displayed* endpoint prefix
- No raw pre-stats coding (`Positive = 1, Negative = 0` and kin)
- Missing products / unused recorded variables: Word comment only, not body `not generated` / `not included`
- Intro para 5 (aim/hypothesis) and Discussion first paragraph: no citations
- Methods: no `[n]`; no seed; `Python 3.13`
- Sample size: α, β, *p*, *n*, adequacy — once in Methods; do not re-elaborate elsewhere
- Discussion / Conclusion: no result numbers
- Limitations own paragraph; no disclaimer closer; prefer no citations there; `First… Second…` ordinals sequential and in sentence order
- No disclaimer / no repeated hedge
- `95% CI: X-X`; one fact per sentence
- Incremental *improved* only with same-sentence DeLong caveat
- Implausible labs: *P* = NC, note once
- No yellow empty slots; missing method/product facts in Word comments (author **A**)
- Word comments / Track Changes author **A** (never `Grok`)
- English punctuation
- Ethics Date/NO empty: Word comment, not yellow; email(see mem:corresponding_email)
- Numbers match the latest results file (nomogram row, not a Combined-figure leftover)
- Blank skeleton fill: every project-specific slot is `[PLACEHOLDER: …]` until verified; no real IRB number, AUC, or scanner serial baked in as a required value
- Blank skeleton fill: Results subtitles follow the Methods order; a Methods-only step may have no Results subtitle (no invented Results); a Results subtitle with no Methods parent is a defect; an empty Results section keeps its heading with `Results pending [PLACEHOLDER: …]`
- Blank skeleton fill: owner names stay nested under the existing Methods subtitles (no second format, no extra subtitles)
