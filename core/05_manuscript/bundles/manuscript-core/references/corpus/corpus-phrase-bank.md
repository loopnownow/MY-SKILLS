# Corpus Phrase Bank (rebuilt from source manuscripts)

**Status:** purpose / methods / results openers refreshed 2026-08-28 from
**389 unique drafts** (414 candidates → 409 extracted → 20 exact duplicates
removed; English ≈ **324**). Counts in §1–§1c are full-text grep on those
English drafts (Methods/Results repeats included), not abstract-only.
Discussion / limitations / ethics slots below still carry the earlier
96-manuscript grep where this harvest did not re-count.

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
- `Patients were randomly divided into a training cohort (n = N) and a test cohort (n = N).`
- `Radiomics features were reduced using LASSO, and a radiomics nomogram was constructed.`

**Split wording:** manuscript BODY internal split is training/test. Figure 1
(figure-engine; already merged) uses published **Training Cohort /
Validation Cohort**. Only an other-hospital cohort is external validation.
Never `Development set`. Do not rewrite figure-engine from this file.

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

- `The AUC of the [model] was X (95% CI: X–X) in the training cohort and X (95% CI: X–X) in the test cohort.`
- `The nomogram exhibited good discrimination in the training cohort (AUC X [95% CI, X–X]) and the test cohort (AUC X [95% CI, X–X]).`

Direct side-by-side AUCs are more common than `outperformed`.

**Do not use** as recommended stock: `suggesting its potential`,
`demonstrated good performance` (0 hits in 389 unique drafts). Listed in
`../de-ai/forbidden-phrases.md`.

---

## 2. Discussion openers (¶1 — summary of key finding)

- *"In this study, we hypothesize[d] that…"* — 31 occurrences of the
  "In this study, we…" opener overall.
- *"In this study, we identified Ki-67 expression as an independent clinical predictor for distinguishing between WDLPS and DDLPS…"*
- *"The main finding[s] of [this/the present] study…"* pattern also occurs but
  is rare (1 instance) — don't over-rely on it as a default template; "In
  this study, we…" is the workhorse opener.

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

## 8. Words that are NOT banned (re-confirmed)

Raw occurrence counts in the deduplicated corpus — these are edited,
submission-ready manuscripts, so their presence is not an oversight:

| Word | Count |
|---|---|
| novel | 59 |
| notably | 21 |
| interestingly | 13 |
| importantly | 9 |

These words show up used purposefully and sparingly (e.g. flagging a genuine
methodological first, or drawing attention to one specific unexpected
result among many) — never as filler in every paragraph. **Do not add these
back to any forbidden-word list.** The right editorial move is not "delete
on sight" but "keep if it's doing real work; cut if it's decorative."

Sample in-context uses kept in the corpus (for calibration, not for copying):
- *"…is a novel procedure."* (describing a genuinely new technique)
- *"Interestingly, in heterozygous MPO-deficient mice with intermediate levels of MPO, there was correspondingly intermediate signal enhancement…"* (flagging one specific unexpected result, not a generic transition)
- *"Notably, the puncture time was reduced, from an average of 53 ± 13.7 min … to 27 ± 14.0 min …"* (flagging the single most important quantitative result, not throat-clearing)
- *"Importantly, these alterations were associated with clinical symptom severity…"* (marking the clinically load-bearing sentence in the paragraph, once)

---

## Provenance / method

§1–§1c: 2026-08-28 harvest on 389 unique drafts (324 English); phrase
counts only — unpublished full texts and title dumps stay off GitHub.

Older slots (discussion openers, limitations, ethics, §8 not-banned words)
were grep-counted on the 96-manuscript deduplicated set:

```
md5sum *.txt | awk '{print $1}' -> keep first of each unique hash (96 of 100 kept)
grep -ohE '<pattern>' | sort | uniq -c | sort -rn
```

Re-run against a larger corpus if these files grow. Do not commit `corpus-raw/`.
