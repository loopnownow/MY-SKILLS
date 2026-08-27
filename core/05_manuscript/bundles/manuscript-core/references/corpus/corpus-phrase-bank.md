# Corpus Phrase Bank (rebuilt from source manuscripts)

**Status:** rebuilt on 2026-08-27 after the original file (formerly at
`/mnt/skills/user/ying-li-polisher/references/corpus-phrase-bank.md`) was lost
during the merge of `ying-li-polisher` into `medical-scientific-writing`.
Re-derived directly from the 96 deduplicated manuscripts in the project
corpus (100 files, 4 exact-duplicate revision rounds removed by MD5 hash).
Counts below are raw grep counts on that deduplicated corpus, not estimates.

Use this file alongside `polisher-sections.md` and `sentence-templates.md`.
Where a pattern here disagrees with either of those files, **this file wins**
for anything the corpus can settle (it's verbatim evidence); `Aitor-format.md`
still wins for hard formatting/QC rules (CI dashes, banned voice, etc.).

---

## 1. Objective-sentence openers (Abstract / Intro close)

Verified counts across the corpus:

| Opener | Count |
|---|---|
| **"This study aimed to…"** | **18** |
| "The aim of this study was to…" | 17 |
| Bare infinitive ("To explore/investigate/evaluate/determine/assess…") | 13 |
| "The purpose of this study was to…" | 4 |
| "We aimed to…" | 1 |
| "The objective of this study was to…" | 0 |

**Default / dominant form: "This study aimed to…"** — effectively tied with
"The aim of this study was to…", both far more common than the others. Treat
these two as the primary choices; the rest are acceptable variation, not the
default.

Verbatim examples:
- *"This study aimed to investigate whe[ther reduction of manganese intake improves neuropsychological manifestations in MHE rats]."*
- *"In this study, we hypothesized that reduced EAAT-2 expression could lead to increased plasma glutamate levels…"* (hypothesis-framed variant, also legitimate)

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

Extracted with:
```
# copy manuscripts to text, hash-dedupe revision rounds
md5sum *.txt | awk '{print $1}' -> keep first of each unique hash (96 of 100 kept)
cat deduped/*.txt > full_corpus.txt
grep -ohE '<pattern>' full_corpus.txt | sort | uniq -c | sort -rn
```
Counts are exact grep matches, not samples — re-run against a larger or
updated corpus if these files grow.
