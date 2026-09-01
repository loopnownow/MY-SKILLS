# Ying Li section polishing rules (appendix)

**Canonical entry:** parent `../MODULE.md` (manuscript-core).
Use this file for **section-by-section polish templates** (§1–§9).
If anything conflicts with `mode-1-sci.md` or top-level `05_manuscript` hard rules, **prefer mode-1 / top-level** (e.g. prediction-model CI is `95% CI: X–X` in `Aitor-format.md`; no em-dash; one fact per sentence). Full-paper second pass: de-pipeline + results.html numbers only; do not reorder IMRAD; do not fuse short sentences.

Source: former `ying-li-polisher` skill (merged P1).

---

# Ying Li Academic Manuscript Polisher

Polish medical manuscripts to match Dr. Ying Li's established SCI writing style:
**highly standardized · clinically oriented · quantitatively precise · objectively cautious**.

---

## STEP 0 — Identify what is being polished

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

## §1 — Abstract Polishing Rules

**Structure** (4 implicit parts, even if unheaded). Full papers: labels **Objective:** **Methods:** **Results:** **Conclusion:** are **bold and flush left** (`Aitor-format.md`):
1. **Objective sentence** — Keep **three** purpose-sentence families; do not collapse to one: **"This study aimed to…"** / **"The aim of this study was to…"** / bare infinitive **"To investigate/explore/evaluate…"**. Never a rhetorical question. State clinical need immediately. See `references/corpus/corpus-phrase-bank.md` §1 (389 unique drafts, 2026-08-28).
2. **Methods sentence(s)** — Lead with population: *"A total of N patients/animals were…"*. Then imaging/analytical pipeline, validation strategy. All abbreviations defined parenthetically at first use.
3. **Results sentence(s)** — Report quantitative metrics in sentence form (not lists): AUC (95% CI), sensitivity, specificity, P values. Explicitly distinguish significant from non-significant findings: *"…but not in the X group."*
4. **Conclusion sentence** — 1–2 sentences. Clinically grounded. Use *"may provide"*, *"could assist"*, *"demonstrated potential"* — never absolute claims.

**Characteristic phrase patterns to preserve or introduce:**
- *"A total of N [subjects] were divided into / reviewed / enrolled…"*
- *"The AUC of the [model] was X (95% CI: X–X) in the training cohort and X (95% CI: X–X) in the test cohort."* BODY split is training/test; Figure 1 is Training Cohort / Validation Cohort; other-hospital only = external validation.
- *"Both A and B play roles in…"*

**Language rules for abstracts:**
- No italics except for gene/species names
- Abbreviations defined at first use, used consistently thereafter
- No citations in abstract
- No colloquial or non-standard terms

---

## §2 — Introduction Polishing Rules

**Structure** (3–4 paragraphs, funnel shape):

**¶1 — Disease-level framing**
- Opens with definition + epidemiological or pathophysiological context, immediately referenced: *"X refers to… [1]."* or *"X is the Nth most common… [1,2]."*
- Precise, factual, not rhetorical.

**¶2 — Knowledge gap identification**
- Hedged language mandatory: *"remains unclear"*, *"remains controversial"*, *"the pathogenesis is complex"*, *"current diagnosis relies on invasive methods"*. Never *elucidate / elucidating / elucidated* (purpose/aim → *exploring*; mechanism-unknown → *remain unclear*, not *explain* / *clarify*).
- Reference existing approaches comparatively without over-citation.

**¶3 — Proposed approach / rationale**
- Transition: *"Recently, [modality/technique] has been applied to…"* or *"Radiomics/MRI/IVIM has demonstrated promise in…"*
- Cite 2–3 key supporting references.

**¶4 (optional) — Clinical unmet need → Study objective**
- Closes with explicit objective statement matching the abstract verbatim or near-verbatim.
- Template: *"Therefore, the purpose/aim of this study was to [objective]."*

**Tone rules:**
- No hyperbole (*"groundbreaking"*, *"novel"*, *"first ever"* without evidence)
- Clinical urgency via factual framing only
- Active or mixed voice acceptable (recent style)

---

## §3 — Materials and Methods Polishing Rules

This is the most technically precise section. Follow all sub-rules below.

**Section order for full papers is not this 3.1–3.5 list.** Use `Aitor-format.md` (Ethics → design/N → patients → eligibility → criteria → endpoints → labs → imaging → processing → model → stats). The subsections below are wording templates only.

### 3.1 Patient / Subject Selection
- Report enrollment window, institution, IRB approval number, retrospective vs. prospective label.
- Template: *"This [retrospective/prospective] study was approved by the Institutional Review Board of Jinshan Hospital of Fudan University (No. XXX)."*
- Inclusion/exclusion criteria: full papers use inline `follows: (1) x; (2) y; and (3) z` (`Aitor-format.md`). Numbered lists only for non-full-paper fragments.
- Group sizes: always parenthetical — *(n = 158)*; two groups in running text: `(A, n = 89; B, n = 187)`

### 3.2 Imaging Protocol
- Scanner model, field strength, institution.
- Sequence parameters in parentheses: *"DWI (b = 0 and 1,000 s/mm²)"*, *"T2WI (TR/TE = X/X ms, slice thickness X mm)"*
- Abbreviations: T2WI, DWI, ADC, DCE, IVIM, 4D flow — full name once, then abbreviation only.

### 3.3 ROI / Segmentation
- Reader qualifications (years of experience), blinding status.
- Inter-/intra-observer agreement: ICC values required.
- Software named explicitly: *"ITK-SNAP (version X.X)"*, *"3D Slicer"*, *"pyradiomics (version X.X)"*

### 3.4 Radiomics / AI Pipeline
- Feature extraction: IBSI compliance stated if applicable.
- Dimensionality reduction: *"LASSO regression with 10-fold cross-validation was used to select the most predictive features."*
- Feature categories listed: first-order, shape, GLCM, GLRLM, GLSZM, etc.
- Final feature count stated.

### 3.5 Statistical Analysis (always final subsection)
- Normality test stated (Shapiro-Wilk or Kolmogorov-Smirnov).
- Appropriate test selection: t-test (normal) vs. Wilcoxon signed-rank (non-normal) — spelled out fully, never abbreviated as "Wilcoxon."
- DeLong test for AUC comparison.
- Decision curve analysis (DCA) for clinical net benefit.
- Closing sentence invariant: *"All statistical analyses were performed using [software]. Differences with a P-value less than 0.05 were considered statistically significant."*

**Voice:** Passive throughout Methods — *"Images were imported"*, *"Features were extracted"*, *"Patients were divided"*

---

## §4 — Results Polishing Rules

**Core principle:** Tables lead, prose annotates.

- Do not redundantly restate every number from tables in prose.
- Prose states direction and magnitude of key findings only.
- Subgroup results follow the exact Methods order.

**Statistical reporting format:**
- AUC: *"0.86 (95% CI: 0.80–0.93)"* — always with CI
- P values: exact when ≤0.05 (*P = 0.002*); threshold when >0.05 (*P > 0.05*) or non-significant (*P = 0.12*)
- Sensitivity/specificity: as percentages with 1 decimal place
- Always report both significant AND non-significant findings explicitly

**Metabolomics / metabolite lists:**
- Full chemical name at first mention + abbreviation: *"γ-aminobutyric acid (GABA)"*
- Lists embedded in prose with semicolons, not bullet points:
  - ✓ *"…were significantly increased, and that of myo-inositol, taurine, leucine, isoleucine, arginine, and citrulline were significantly decreased…"*
  - ✗ bullet lists

**Radiomics / model performance:**
- Report AUC in primary + all validation groups in one compact sentence.
- Report calibration (Hosmer-Lemeshow P value) and DCA net benefit.

---

## §5 — Discussion and Conclusion Polishing Rules

**Discussion structure** for full papers: `Aitor-format.md` (key findings → per-finding literature with **new** refs → clinical → limitations → conclusion; 800–1000 words). Sentence templates below still apply.

**Discussion structure** (4–6 paragraphs):

**¶1 — Summary** 
- Restate the main finding in 1–2 sentences. Active voice.
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
- Always present. Never defensive. Standard 3–5 items:
  1. Retrospective design / selection bias
  2. Single-center cohort / limited generalizability
  3. Relatively small sample size
  4. Need for external multicenter validation
  5. (If applicable) manual ROI segmentation variability
- Template: *"This study has several limitations. First,… Second,… Third,… Future research should [focus on / explore / validate]…"* — **"Future research should…" is the corpus-dominant closer (18/96, vs. "Future studies should…" at 9/96, vs. any "warrant(ed)" phrasing at 14/96 total across all uses, not just closers)**. Prefer "Future research/studies should…" over "…are warranted…" as the default closing move. See `references/corpus/corpus-phrase-bank.md` §5.

**¶6 / Conclusion (separate section)**
- 1–2 sentences maximum.
- Mirror the abstract objective + affirm clinical value.
- Template: *"In conclusion, the [model] achieved an AUC of X (95% CI: X–X) in the training cohort and X (95% CI: X–X) in the test cohort."* Do **not** use `demonstrated good performance` or `suggesting its potential` (0 hits; `de-ai/forbidden-phrases.md`).

---

## §6 — Title and Keywords Rules

**Title format:**
- Structured as: *"[Technique/modality] [± radiomics/nomogram] [for/in predicting/diagnosing/differentiating] [outcome] [in/among] [population]"*
- Examples from corpus:
  - *"An MRI radiomics nomogram improves the accuracy in identifying eligible candidates for fertility-preserving treatment in endometrioid adenocarcinoma"*
  - *"CT-based radiomics for differentiating well-differentiated from dedifferentiated liposarcoma"*
- Avoid colons unless journal style requires them.
- No superlatives (*"a novel"*, *"the first"*) unless factually verified.

**Keywords:**
- 5–8 keywords
- Include: imaging modality, technique (radiomics/nomogram/IVIM/4D flow), pathology name, clinical endpoint
- Abbreviations expanded: write *"magnetic resonance imaging"* not *"MRI"* unless journal specifies otherwise

---

## §7 — Universal Language Rules (apply everywhere)

### Terminology conventions

| Domain | Convention |
|---|---|
| Imaging sequences | Full name once → abbreviation: T2-weighted imaging (T2WI) |
| Statistical tests | Always fully spelled: *"Wilcoxon signed-rank test"* not *"Wilcoxon"* |
| Metabolites | Chemical name (abbreviation): *"γ-aminobutyric acid (GABA)"* |
| Radiomics features | Category terms: first-order, texture (GLCM, GLRLM, GLSZM), shape |
| Clinical entities | Abbreviate from first sentence and maintain throughout |
| Group sizes | Always *(n = N)* in parentheses |
| P values | Italic P, space before operator: *P* < 0.05 (or per journal style) |
| Confidence intervals | 95% CI: X–X (en-dash, no spaces) |

### Hedging vocabulary (use in Discussion only, not in Results)

| Strength | Terms |
|---|---|
| Confirmed | demonstrated, showed, confirmed, revealed |
| Suggested | suggested, indicated, found |
| Speculative | may, might, could, possibly, potentially |
| Future work | **should** (dominant: "Future research/studies should…", 27/96 combined), warrants, is needed, should be validated |

### Forbidden expressions
- *"groundbreaking"*, *"state-of-the-art"* (unless directly cited)
- *"proved"* (use *"demonstrated"*)
- *"superior"* (use *"outperformed"* or *"showed higher AUC than"*)
- *"will"* for predictions (use *"may"* or *"could"*)

**NOT forbidden — corpus-verified, do not re-add:** *"novel"* (59 occurrences),
*"notably"* (21), *"interestingly"* (13), *"importantly"* (9). These appear
in the edited, submission-ready corpus used purposefully and sparingly — e.g.
flagging one genuinely unexpected result or the single most clinically
load-bearing sentence in a paragraph — never as filler repeated throughout.
The editorial rule is "keep if it's doing real work, cut if it's decorative,"
not "delete on sight." See `references/corpus/corpus-phrase-bank.md` §8 for
verified in-context examples before deciding to cut one.

### Sentence structure targets
- **Methods/Results:** 20–30 words average. Short conclusion sentences (≤15 words).
- **Introduction/Discussion:** 25–40 words. Complex sentences with subordinate clauses acceptable.
- No sentence > 55 words anywhere.

### Clinical translation phrases (use in Discussion ¶4)
- *"could assist individualized decision-making"*
- *"may optimize clinical workflow"*
- *"reduce unnecessary [procedures/interventions]"*
- *"provide a non-invasive/preoperative assessment"*
- *"Decision curve analysis showed net benefit over…"*

---

## §8 — Polishing Workflow

For each piece of submitted text:

1. **Identify section** (Abstract / Intro / M&M / Results / Discussion / Conclusion)
2. **Check structure** — does it follow the section template? Reorder if needed.
3. **Apply section-specific rules** (§1–§5)
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

## §9 — Reference Conventions

Search and claim-to-DOI for I/D: `intro-discussion-evidence.md`. Counts and locked paragraphs: `Aitor-format.md` (do not copy here).

- Vancouver/NLM style (numbered, order of appearance)
- No reference inflation — Introductions: follow Aitor (10–15), not a second quota
- Self-citation: functional only (*"as previously described [X]"*)
- Every factual claim in Introduction and Discussion must be cited
- Funding: grant number + granting body always explicit

---

## Quick Reference Card

```
Abstract   : Objective → Methods (n=N) → Results (AUC, 95%CI) → Conclusion (hedged)
Intro      : Disease def [ref] → Gap (hedged) → Existing approaches → Aim
Methods    : Ethics → Cohort (n=N) → Imaging → ROI → Pipeline → Stats (passive voice)
Results    : Table leads → Prose annotates → AUC(95%CI) → P exact → Non-sig explicit
Discussion : Summary → Literature → Mechanism (hedged) → Clinical → Limitations → Future
Conclusion : 1-2 sentences, echo objective, affirm clinical value
```

For extended examples and sentence-level templates, see `references/sentence-templates.md`.
For statistical reporting checklists, see `references/stats-checklist.md`.
