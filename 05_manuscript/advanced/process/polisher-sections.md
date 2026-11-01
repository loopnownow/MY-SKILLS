# Aitor section polishing rules (appendix)

**Canonical entry:** parent `../../SKILL.md` (manuscript advanced upper layer).
Use this file for **section-by-section polish templates** (§1-§9).
If anything conflicts with `Aitor-format.md` or top-level `05_manuscript` hard rules, **prefer Aitor-format / top-level** (e.g. prediction-model CI is `95% CI: X-X` in `Aitor-format.md`; no em-dash; one fact per sentence). Full-paper second pass: de-pipeline + results.html numbers only; do not reorder IMRAD; do not fuse short sentences.

Source: former `ying-li-polisher` skill (merged P1).

---

## Aitor Academic Manuscript Polisher

Polish medical manuscripts to match Aitor's established SCI writing style:
**highly standardized · clinically oriented · quantitatively precise · objectively cautious**.

---

### STEP 0 — Identify what is being polished

Determine the manuscript section(s) submitted:
- **Abstract** → apply §1
- **Introduction** → apply §2
- **Materials and Methods** → apply §3
- **Results** → apply §4
- **Discussion / Conclusion** → apply §5
- **Full manuscript** → apply all sections in order
- **Title / Keywords** → apply §6

If the user provides raw text without labeling the section, infer from content structure.

---

### §1 — Abstract Polishing Rules

**Structure** (4 implicit parts, even if unheaded). Full papers: labels **Objective:** **Methods:** **Results:** **Conclusion:** are **bold and flush left** (`Aitor-format.md`):
1. **Objective sentence** — Keep **three** purpose-sentence families; do not collapse to one: **"This study aimed to…"** / **"The aim of this study was to…"** / bare infinitive **"To investigate/explore/evaluate…"**. Never a rhetorical question. State clinical need immediately. Counts by family: `05_manuscript/base/vocab/L2/preferred.md` §1; the owner's own usage: `05_manuscript/advanced/vocab/L2/preferred-advanced.md`.
2. **Methods sentence(s)** — Lead with population: *"A total of N patients/animals were…"*. Then imaging/analytical pipeline, validation strategy. All abbreviations defined parenthetically at first use.
3. **Results sentence(s)** — Report quantitative metrics in sentence form (not lists): AUC (95% CI), sensitivity, specificity, P values. Explicitly distinguish significant from non-significant findings: *"…but not in the X group."*
4. **Conclusion sentence** — 1-2 sentences. Clinically grounded. Use *"may provide"*, *"could assist [task]"* — never absolute claims, and never `demonstrated potential` (lab-unused stock; `05_manuscript/base/vocab/L1/ban-phrases.md`).

**Characteristic phrase patterns to preserve or introduce:**
- *"A total of N [subjects] were divided into / reviewed / enrolled…"*
- *"The AUC of the [model] was X (95% CI: X-X) in the training set and X (95% CI: X-X) in the test set."* BODY split is training/test; Figure 1 is Training Cohort / Test Cohort, plus Validation Cohort only when Methods states an external cohort (`Aitor-format.md`). Other-hospital only = validation set.
- *"Both A and B play roles in…"*

**Language rules for abstracts:**
- No italics except for gene/species names
- Abbreviations defined at first use, used consistently thereafter
- No citations in abstract
- No colloquial or non-standard terms

---

### §2 — Introduction Polishing Rules

**Structure.** Six elements (`Aitor-format.md`, Introduction). Paragraphs follow the funnel: burden and guideline definition; limits of current practice; related studies with group appraisal; missing piece and method link; aim (last paragraph, no citations).

**Element wording**

- Guideline definition: *"The [year] [body] guideline defines [construct] by [criteria] and uses it to [decision] [n]."* Then one sentence on what the guideline leaves open: *"The same guideline notes that [open issue] [n]."* Definitions are paraphrased, never quoted.
- Limits: *"[Information] is available only after [event], so [decision] is made on [weaker information]."*
- Related studies: give n, design, and effect for the two or three studies that matter most, each inside a sentence that also carries a comparison or a limitation. Then appraise the group: *"Taken together, these models [strength this study keeps], but [weakness this study targets]."* Vary the frame between manuscripts.
- Missing piece: *"Whether [X] adds [Y] beyond [Z] remains unclear."*
- Method link: *"Because [property of the problem], [feature of the method] may [expected benefit]."* One hedged sentence of inference.
- Aim: *"Therefore, the purpose of this study was to [objective]."* Hypothesis: *"We hypothesized that [model] would [effect] on the test set beyond [comparator]."*

**Language rules**

- Hedged language for unknowns: *remains unclear*, *remains controversial*, *has not been established*. Never *elucidate / elucidating / elucidated*.
- Sentences 10-30 words. Prefer one main proposition per sentence; if a sentence runs past 20 words, check that it holds one.
- No hyperbole (*groundbreaking*, *novel*, *first ever*) without evidence. Scarcity is worded as what the search found.
- No enumeration of studies, no parallel frames, no more than one triplet per paragraph (`05_manuscript/advanced/vocab/L1/sci-overrides.md`, structure-level tells).
- Do not name reporting guidelines (TRIPOD and others) in the Introduction.
- Active or mixed voice is acceptable.


### §3 — Materials and Methods Polishing Rules

This is the most technically precise section. Follow all sub-rules below.

**Section order for full papers is not this 3.1-3.5 list.** Use `Aitor-format.md` (Ethics → design/N → patients → eligibility → criteria → endpoints → labs → imaging → processing → model → stats). The subsections below are wording templates only.

#### 3.1 Patient / Subject Selection
- Report enrollment window, institution, IRB approval number, retrospective vs. prospective label.
- Template: *"This [retrospective/prospective] study was approved by the Institutional Review Board of Jinshan Hospital of Fudan University (No. XXX)."*
- Inclusion/exclusion criteria: full papers use inline `follows: (1) x; (2) y; and (3) z` (`Aitor-format.md`). Numbered lists only for non-full-paper fragments.
- - Outcomes: clinical names only (positive/negative, present/absent). Never `Positive = 1, Negative = 0` or other raw 0/1 coding dumps (`Aitor-format.md`).
Group sizes: always parenthetical — *(n = 158)*; two groups in running text: `(A, n = 89; B, n = 187)`

#### 3.2 Imaging Protocol
- Scanner model, field strength, institution.
- Sequence parameters in parentheses: *"DWI (b = 0 and 1,000 s/mm²)"*, *"T2WI (TR/TE = X/X ms, slice thickness X mm)"*
- Abbreviations: T2WI, DWI, ADC, DCE, IVIM, 4D flow — full name once, then abbreviation only.

#### 3.3 ROI / Segmentation
- Reader qualifications (years of experience), blinding status.
- Inter-/intra-observer agreement: ICC values required.
- Software named explicitly: *"ITK-SNAP (version X.X)"*, *"3D Slicer"*, *"pyradiomics (version X.X)"*

#### 3.4 Radiomics / AI Pipeline
- Feature extraction: IBSI compliance stated if applicable.
- Dimensionality reduction: *"LASSO regression with 10-fold cross-validation was used to select the most predictive features."*
- Feature categories listed: first-order, shape, GLCM, GLRLM, GLSZM, etc.
- Final feature count stated.

#### 3.5 Statistical Analysis (always final subsection)
- Normality test stated (Shapiro-Wilk or Kolmogorov-Smirnov).
- Appropriate test selection: t-test (normal) vs. Wilcoxon signed-rank (non-normal) — spelled out fully, never abbreviated as "Wilcoxon."
- DeLong test for AUC comparison.
- Decision curve analysis (DCA) for clinical net benefit.
- Closing sentence invariant: *"All statistical analyses were performed using [software]. Differences with a P-value less than 0.05 were considered statistically significant."*

**Voice:** Passive throughout Methods — *"Images were imported"*, *"Features were extracted"*, *"Patients were divided"*

---

### §4 — Results Polishing Rules

**Core principle:** Tables lead, prose annotates.

- Do not redundantly restate every number from tables in prose.
- Prose states direction and magnitude of key findings only.
- Subgroup results follow the exact Methods order.

**Statistical reporting format:**
- AUC: *"0.86 (95% CI: 0.80-0.93)"* — always with CI
- P values: exact when ≤0.05 (*P = 0.002*); threshold when >0.05 (*P > 0.05*) or non-significant (*P = 0.12*)
- Sensitivity/specificity: as percentages with 1 decimal place
- Always report both significant AND non-significant findings explicitly

**Metabolomics / metabolite lists:**
- Full chemical name at first mention + abbreviation: *"γ-aminobutyric acid (GABA)"*
- Lists embedded in prose with semicolons, not bullet points:
  - ✓ *"…were significantly increased, and that of myo-inositol, taurine, leucine, isoleucine, arginine, and citrulline were significantly decreased…"*
  - ✗ bullet lists

**Radiomics / model performance:**
- Report AUC in primary + all validation sets in one compact sentence.
- Report calibration (Hosmer-Lemeshow P value) and DCA net benefit.

---

### §5 — Discussion and Conclusion Polishing Rules

Do **not** compress Discussion by page count. Structure and word band win over “cut to N pages”.

**Discussion structure** for full papers: `Aitor-format.md` (key findings → per-finding literature with **new** refs → clinical → limitations → conclusion; 800-1000 words). Sentence templates below still apply.

**Discussion structure** (4-6 paragraphs):

**¶1 — Summary**
- Restate the main finding in 1-2 sentences. Active voice.
- Template: *"In this study, we found that / demonstrated that / showed that…"* Finding openers may use *"The first finding concerns…"* (verb only; do not weld the next sentence onto it).

**¶2 — Literature contextualization**
- Compare with cited prior work; state agreement OR disagreement explicitly.
- Template: *"This is consistent with the findings of [Author et al.], who reported… However, [Author et al.] found…, which may be attributed to…"*
- Include specific metrics from cited papers when available.

**¶3 — Mechanistic interpretation**
- For imaging: interpret biomarkers in terms of underlying pathophysiology.
- Hedging calibrated to evidence strength:
  - Strong (replicated/validated): *"demonstrated"*, *"confirmed"*, *"showed"*
  - Speculative: *"may be related to"*, *"possibly indicates"*, *"might reflect"*
  - Mechanistic: *"suggesting that"*, *"this could be explained by"*

**¶4 — Clinical implications**
- Frame practical utility: *"The nomogram could be used to guide individualized treatment decisions"*, *"could reduce unnecessary invasive procedures"*, *"may optimize patient selection for…"* Prefer *eventually* over *later* for a future use-case. One sentence. No *It is not a replacement…* stack (`Aitor-format.md`).
- DCA framing: *"Decision curve analysis showed that the radiomics nomogram provided a greater net benefit than…"*

**¶5 — Limitations**
- Always present. Never defensive. Standard 3-5 items:
  1. Retrospective design / selection bias
  2. Single-center cohort / limited generalizability
  3. Relatively small sample size
  4. Need for external multicenter validation
  5. (If applicable) manual ROI segmentation variability
- Template: *"This study has several limitations. First,… Second,… Third,… Future research should [focus on / explore / validate]…"* — **"Future research should…" is the bank-dominant closer (18/96, vs. "Future studies should…" at 9/96, vs. any "warrant(ed)" phrasing at 14/96 total across all uses, not just closers)**. Prefer "Future research/studies should…" over "…are warranted…" as the default closing move. Counts: `05_manuscript/base/vocab/L2/preferred.md` §5.

**¶6 / Conclusion (separate section)**
- 1-2 sentences maximum.
- Mirror the abstract objective + affirm clinical value.
- Template: *"In conclusion, the [model] achieved an AUC of X (95% CI: X-X) in the training set and X (95% CI: X-X) in the test set."* Do **not** use `demonstrated good performance` or `suggesting its potential` (0 hits; `05_manuscript/base/vocab/L1/ban-phrases.md`).

---

### §6 — Title and Keywords Rules

**Title format:**
- Structured as: *"[Technique/modality] [± radiomics/nomogram] [for/in predicting/diagnosing/differentiating] [outcome] [in/among] [population]"*
- Examples from bank:
  - *"An MRI radiomics nomogram improves the accuracy in identifying eligible candidates for fertility-preserving treatment in endometrioid adenocarcinoma"*
  - *"CT-based radiomics for differentiating well-differentiated from dedifferentiated liposarcoma"*
- Avoid colons unless journal style requires them.
- No superlatives (*"a novel"*, *"the first"*) unless factually verified.

**Keywords:**
- 5-8 keywords
- Include: imaging modality, technique (radiomics/nomogram/IVIM/4D flow), pathology name, clinical endpoint
- Abbreviations expanded: write *"magnetic resonance imaging"* not *"MRI"* unless journal specifies otherwise

---

### §7 — Universal Language Rules (apply everywhere)

#### Terminology conventions

| Domain | Convention |
|---|---|
| Imaging sequences | Full name once → abbreviation: T2-weighted imaging (T2WI) |
| Statistical tests | Always fully spelled: *"Wilcoxon signed-rank test"* not *"Wilcoxon"* |
| Metabolites | Chemical name (abbreviation): *"γ-aminobutyric acid (GABA)"* |
| Radiomics features | Category terms: first-order, texture (GLCM, GLRLM, GLSZM), shape |
| Clinical entities | Abbreviate from first sentence and maintain throughout |
| Group sizes | Always *(n = N)* in parentheses |
| P values | Italic P, space before operator: *P* < 0.05 (or per journal style) |
| Confidence intervals | 95% CI: X-X (en-dash, no spaces) |

#### Hedging vocabulary (use in Discussion only, not in Results)

| Strength | Terms |
|---|---|
| Confirmed | demonstrated, showed, confirmed, revealed |
| Suggested | suggested, indicated, found |
| Speculative | may, might, could, possibly, potentially |
| Future work | **should** (dominant: "Future research/studies should…", 27/96 combined), warrants, is needed, should be validated |

#### Forbidden expressions
- *"groundbreaking"*, *"state-of-the-art"* (unless directly cited)
- *"proved"* (use *"demonstrated"*)
- *"superior"* (use *"outperformed"* or *"showed higher AUC than"*)
- *"will"* for predictions (use *"may"* or *"could"*)

**Banned — the 2026-08-29 reversal stands:** *"novel"*, *"notably"*, *"interestingly"*,
*"importantly"*. The bank does hold old occurrences (59 / 21 / 13 / 9), and that
count is history, not a licence: the ban was decided after those manuscripts were
written. Authority: `05_manuscript/base/vocab/L1/ban-terms.yaml`, human table in
`05_manuscript/base/vocab/L1/ban-phrases.md`. `{code_stats}\tools\orchestrator\style_lint.py`
enforces it. Delete the word and state the fact instead.

#### Sentence structure targets
- **Methods/Results:** 20-30 words average. Short conclusion sentences (≤15 words).
- **Introduction/Discussion:** 10-30 words (align `Aitor-format.md` / `voice-portrait.md`). One fact per sentence, inside a continuous paragraph; no long subordinate stacks. Do not lay the opening out as one sentence per paragraph, and do not leave that opening uncited when a verified source exists (`05_manuscript/qc/manuscript-local-qc.md`).
- No sentence > 55 words anywhere.

#### Clinical translation phrases (use in Discussion ¶4)
- *"could assist individualized decision-making"*
- *"may optimize clinical workflow"*
- *"reduce unnecessary [procedures/interventions]"*
- *"provide a non-invasive/preoperative assessment"*
- *"Decision curve analysis showed net benefit over…"*

---

### §8 — Polishing Workflow

For each piece of submitted text:

1. **Identify section** (Abstract / Intro / M&M / Results / Discussion / Conclusion)
2. **Check structure** — does it follow the section template? Reorder if needed.
3. **Apply section-specific rules** (§1-§5)
4. **Apply universal language rules** (§7)
5. **Check statistical reporting** — every numeric result must include CI or P value
6. **Check hedging calibration** — Results: no hedges; Discussion: calibrated hedges
7. **Check forbidden expressions** — replace per §7 table
8. **Output**:
   - Polished text in full
   - Brief change log (≤5 bullet points) noting major modifications

**Output format:**
```
[Polished text — complete section, ready to paste]

---
**Key changes:**
- [Change 1]
- [Change 2]
- ...
```

---

### §9 — Reference Conventions

Search and claim-to-DOI for I/D: `evidence.md`. Counts and settled paragraphs: `Aitor-format.md` (do not copy here).

- Vancouver/NLM style (numbered, order of appearance)
- No reference inflation — Introductions: follow Aitor (10-15), not a second quota
- Self-citation: functional only (*"as previously described [X]"*)
- Every factual claim in Introduction and Discussion must be cited
- Funding: grant number + granting body always explicit

---

### Quick Reference Card

```
Abstract   : Objective → Methods (n=N) → Results (AUC, 95%CI) → Conclusion (hedged)
Intro      : five paragraphs / eight beats per `../Aitor-format.md` § Introduction (not a four-step card)
Methods    : Ethics → Cohort (n=N) → Imaging → ROI → Pipeline → Stats (passive voice)
Results    : Table leads → Prose annotates → AUC(95%CI) → P exact → Non-sig explicit
Discussion : Summary → Literature → Mechanism (hedged) → Clinical → Limitations → Future
Conclusion : 1-2 sentences, echo objective, affirm clinical value
```

For extended examples and sentence-level templates, see `05_manuscript/base/write-paper/references/section-templates.md`.
For statistical reporting checklists, see `05_manuscript/advanced/references/stat-reporting.md`.

### Bank patterns (2026-10-23)

See `../references/bank-patterns.md` for the tagged revision taxonomy when routing polish edits.

---

## De-AI pass (absorbed retired `humanize` 2026-10-30)

Owner: 05 advanced (advanced-only; no registry fine id). Contract invariants, phase names, and procedure live here. Do not dispatch `write-paper` for de-AI. Pattern catalogue: `05_manuscript/advanced/references/ai_patterns.md`. Scripts: `05_manuscript/advanced/process/scripts/`. Voice/vocab: `05_manuscript/advanced/voice-portrait.md` + `05_manuscript/base/vocab/` + advanced vocab overrides.

### Contract (absorbed from retired base pack)

Phase names: `Scan` -> `Report` -> `Fix` -> `Verify`.

Hard bans (invariants):

1. Numbers, statistics, P values, confidence intervals, and clinical facts come out **identical**.
2. Citations are **never** added, removed, or relocated.
3. No new claim, no removed claim, no reinterpretation. A passage that cannot be fixed without changing meaning is left as it is and flagged for the user.
4. Domain terminology stays intact ("convolutional neural network", "apparent diffusion coefficient", "Fleiss' kappa").
5. Out of scope: journal formatting, house style, scientific judgement, translation (use `write-paper` for venue house style).
6. de-AI ban lists: `05_manuscript/base/vocab/L1/ban-phrases.md` plus advanced overrides in `05_manuscript/advanced/vocab/`.

Also: `05_manuscript/advanced/references/style-guardrails.md` (overclaim / hedging), `05_manuscript/advanced/references/stat-reporting.md` (number formatting; house authority `Aitor-format.md`).
Scored checklist: `05_manuscript/qc/manuscript-local-qc.md`.



### Phases

1. **Scan.** Read `ai_patterns.md` first: definitions, watch words, examples, detection greps, per-pattern fixes, and the per-section priorities for all 27 patterns live only there. Scan the supplied sections; for response letters and cover letters prioritise Patterns 22-24. Record pattern number, name, count, exact passage, location. Output a Pattern Frequency Table (pattern, count, severity, one example per row) plus `Total AI pattern instances` and `AI pattern density (N per 1000 words)`.
2. **Report.** Severity: HIGH (more than 3 occurrences), MEDIUM (1-3), LOW (0, clean). Density is total instances across the 27 patterns per 1000 words; target below 2.0. Present the table and ask which patterns to fix; default is all HIGH and MEDIUM.
3. **Fix.** Rewrite flagged passages with each pattern's fix under the fix rules below. Output the rewritten text as a diff or tracked changes.
4. **Verify.** Keep the pre-rewrite text where the fidelity check can read it before editing in place, otherwise Phase 4 cannot tell whether numbers and citations survived. Re-scan the rewrite on the same 27 patterns, run both detectors, and return a Verification Report (before/after: total instances, density, HIGH, MEDIUM, remaining issues, verdict). Density still above 2.0 means another fix-verify cycle, max 3 rounds. When another skill calls the pass, return the report so the caller can read pass/fail.

```bash
python3 "{code_stats}\tools\manuscript-qc\check_rewrite_fidelity.py" --before /tmp/pre_humanize.md --after manuscript.md --out qc/rewrite_fidelity.json --strict
python3 "{code_stats}\tools\manuscript-qc\check_sentence_variety.py" --manuscript manuscript.md --out qc/sentence_variety.json
```
Both detectors live in `{code_stats}\tools\manuscript-qc\`; this pack keeps the pointer
`scripts/README.md` (moved 2026-11-01, t1521u P3-C). Offline, stdlib only.

`NUMBER_DRIFT`, `NUMBER_REASSIGNED`, `CITATION_DROP` or `CITATION_MOVED` means the rewrite broke an invariant: revert that passage, redo it, flag it for the user. `EDIT_FOOTPRINT_HIGH` is advisory (Patterns 6 and 18 replace whole paragraphs by design); read the diff and confirm the argument survived instead of treating the percentage as a defect. Known limits: the fidelity gate does not check an added or removed negation, a number written in words, a changed unit, or a direction word next to a non-percentage; read the diff for those.

### Fix rules

1. **Preserve technical accuracy.** Every number, statistic, P value, confidence interval, and clinical fact stays identical.
2. **Preserve citations.** Never add, remove, or relocate a citation.
3. **Keep the register.** Formal academic prose from an experienced radiologist writing for peers at a top-tier journal; never casual.
4. **Keep domain terminology intact** ("convolutional neural network", "apparent diffusion coefficient", "Fleiss' kappa").
5. **Never change meaning.** No new claim, no removed claim, no reinterpretation. If a passage cannot be fixed without changing meaning, leave it and flag it for the user.
6. **Active voice** where natural ("We analyzed", not "Analysis was performed").
7. **Vary rhythm.** Keep short declarative sentences (8-12 words) and longer ones (25-35 words). A de-AI pass tends to flatten rhythm, which is itself a tell. `check_sentence_variety.py` verifies this.
8. **Thin antithesis and clefts (Pattern 27).** For each "X rather than Y", "not X but Y", "X, not Y", delete the negative half and rewrite the clause positively: if a fact disappears the contrast was functional and stays; if nothing disappears it was decoration. Judge the manuscript's overall rate, keep two or three for emphasis. Rewrite clefts ("What ... is ...", "It is ... that ...") to plain subject-verb order. Rate checked by hand in Phase 4.

### Gate verdicts

| Gate | Severity | Trigger | Verdict |
|---|---|---|---|
| AI-pattern density target | ADVISORY | density above 2.0 patterns per 1000 words after the sweep | warn; surface remaining flagged passages for manual review |
| Pattern 13 - paren-span corruption after em-dash conversion (U+2014) | ENFORCED · manual | after converting a spaced-U+2014 appositive to parentheses | per-sentence scan by hand; `PAREN_SPAN_ORDINAL` / `PAREN_SPAN_SENTENCE` means a conversion wrapped a sentence or an ordinal inside one parenthesis (paren-balanced but broken). Operate per sentence; never match across a sentence boundary |
| Pattern 19 - `§` symbol | ENFORCED (senior MA reviewer prep) | `grep -c "§" manuscript.md` above 0 | auto-strip; post-rewrite count must be 0 |
| Pattern 20 - `(see Methods §X)` self-reference | ENFORCED | match found | rewrite to a direct section-name reference |
| Pattern 21 - AI disclosure in the wrong place | ENFORCED | a disclosure in the body of a journal that wants it elsewhere, or repeated in several places | move it where the target journal asks (journal profile `Disclosure location`); never reword a required disclosure to hide the tool |
| Pattern 25 - inline-emphasis over-use | ENFORCED · manual | italic-emphasis density over threshold after allowlist | `EMPHASIS_OVERUSE` (Minor): strip inline italics (keep stat symbols, Latin, gene-species); whole-clause italics are the strongest tell |
| Pattern 26 - aphorism density | ENFORCED · manual | negative-definition rate AND short-declarative share both over threshold | `APHORISM_DENSITY` (Minor): absorb most epigrams into the neighbouring sentence and write the explanation back, keep two or three; do not simply delete them |
| Pattern 27 - antithesis / cleft density | ENFORCED · manual | "rather than" / "not X but Y" / "X, not Y" or "What ... is ..." / "It is ... that ..." over a per-1000 threshold AND a raw-count floor | `ANTITHESIS_DENSITY` / `CLEFT_DENSITY` (Minor): apply fix rule 8. A lone functional "rather than" or "instead of" never fires |
| Patterns 22-24 - R2R editing mechanism / draft line number / tooling leak | TRIAGE (response letters); `§` count 0 stays hard | detection greps in the `ai_patterns.md` R2R section | review each hit (analysis narration, quoted additions, and a revised-manuscript page or line reference are NOT tells); rewrite confirmed tells to substantive prose |
| Citation preservation invariant | ENFORCED | a citation item (each key of a multi-key or locator citation, or a numeric marker) removed or changed, or moved out of the sentence of the word it was attached to while that word kept its place | `check_rewrite_fidelity.py --strict` gives `CITATION_DROP` / `CITATION_MOVED` (Major); revert that single rewrite and flag it |
| Numerical preservation invariant | ENFORCED | a numeric token's count changed (sign, inequality sign, and percent direction are part of the token), or values traded places while the words stayed | same script gives `NUMBER_DRIFT` / `NUMBER_REASSIGNED` (Major); revert and flag. Known limits: a negation, a number in words, a unit, or a direction word next to a non-percentage is not checked |
| Rewrite footprint | ADVISORY | word tokens changed above `--warn-pct` (default 70) | `EDIT_FOOTPRINT_HIGH` (Minor); never blocks, read the diff |
| Fix rule 7 - sentence-length uniformity | ADVISORY | prose has no short (12 words or fewer) or no long (25 words or more) sentence | `check_sentence_variety.py` gives `SENTENCE_UNIFORM` (Minor); break up or combine until both bands exist. Silent below 15 sentences |

### Detector status

Two detectors ship with the pack and are its only runnable commands:

| Script | Covers |
|---|---|
| `check_rewrite_fidelity.py` | citation and numerical preservation, rewrite footprint |
| `check_sentence_variety.py` | fix rule 7 sentence-length bands |

**Deliberately not shipped** (owner decision 2026-10-25, do not vendor): `check_paren_spans.py` (Pattern 13), `check_emphasis_density.py` (25), `check_aphorism_density.py` (26), `check_rhetorical_density.py` (27), `check_classical_style.py` (Pattern 21 body disclosure). Those gates stay ENFORCED · manual, checked by hand against `ai_patterns.md`; Pattern 21 detection is a body grep for the disclosure strings plus a journal-profile location check. Detector names are kept only so a verdict code in a report traces to its pattern. Only a new owner decision reopens this; no agent may add them.

### Language lint (report-only)

Run it before Phase 1 and again after Phase 4. Output one table (check, result, sentences affected). The lint never changes numbers or citations.

| Check | Rule |
|---|---|
| Sentence length | Target 10-30 words; list sentences outside it. Bands are short (12 words or fewer) / long (25 or more) / ceiling 70, identical to `check_sentence_variety.py`, so the lint table and fix rule 7 cannot disagree |
| Repeated openers | Same first two words in three or more sentences of a paragraph |
| Triplets | More than one "X, Y, and Z" series in a paragraph |
| Number-and-cite chain | Three consecutive sentences that each carry a number and a citation |
| Connector chain | Consecutive sentences opened by However, Moreover, Therefore, In addition |
| Uniform length | Three consecutive sentences within plus or minus 3 words of each other; the formal verdict is `SENTENCE_UNIFORM`, silent below 15 sentences |
| Reporting standards | TRIPOD, CLAIM, or CLEAR named in the Introduction |
| Abbreviations | Defined at first use in the body |
| Claim coverage | Literature claims with no citation in their sentence or same-source group (listed, not gated) |

Fixes are proposals at sentence unit: merge, split, or restructure. Never rewrite a whole paragraph. The lint reports rhythm; phases 1-4 measure and rewrite it. Do not score the same sentence twice in one round.
