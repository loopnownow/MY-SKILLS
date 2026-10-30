<!-- Engine: 03_research/base/find-journal/; this advanced file is a Victor pointer only. -->
# Journal selection (选刊)

Use this file when a manuscript, abstract, or near-complete study is available and
the user asks where to submit, which journal fits, how to rank target journals, or
how to position the paper for submission.

## Core principles

Journal selection is not IF alone. First match evidence strength to journal preferences, then set stretch / solid / safety tiers.

Do not promise “sure accept” / “easy accept” or decide on stale IF. Scope, APCs, review policy, OA, IF, and article types change; before a final recommendation, verify the journal site, recent papers, and author instructions online, and state the retrieval date.

When the user asks for “patterns from high-tier journals in the last three years” or whether the paper fits Radiology / Lancet Digital Health / Nature Medicine / npj Precision Oncology, first read:

- live `meta-analysis` (`02_data-processing/base/meta-analysis/`) — former `literature-evidence-2023-2026.md` retired 2026-09-22
- this file §「2023-2026 journal patterns」(merged below; stands in for the retired standalone file)

Those files give PubMed-verified seed evidence and journal patterns — not a full systematic review. Final submit advice still needs same-day verification of the journal site and recent similar papers.

## Inputs

Collect when possible:

```yaml
title:
abstract:
study_type:
disease:
modality:
sample_size:
centers:
external_validation:
prospective_or_retrospective:
reader_study:
clinical_endpoint:
main_results:
calibration_or_dca:
code_data_availability:
novelty_claim:
target_region_or_specialty:
article_type:
candidate_journals:
must_avoid:
publication_goal: stretch IF / solid accept / fast publish / specialty impact / OA
```

## Evaluation axes

| Axis | Strong-match signals | Downgrade signals |
|---|---|---|
| Clinical question | Clear pain point, population, use case | “Just build a model” |
| Data strength | Multi-center, external validation, prospective/reader study, clear labels | Single-center, small n, weak labels, no external validation |
| Method reliability | Patient-level split, no leakage, calibration, DCA, subgroups and failure cases | AUC or Dice only |
| Novelty | Clinical workflow, generalization, mechanism, multimodal biology link | Architecture swap only |
| Journal fit | Recent similar topics, section match, reader match | Topic off scope |
| Reproducibility | Usable path to code/model/data/feature tables | Data/code unexplained |

## Tier logic

Give three tiers by evidence strength:

1. **Stretch journals**: need a strong clinical question, strong validation, clear novelty. Usually multi-center, external validation, prospective/reader study, real workflow, or strong mechanism.
2. **Primary targets**: high match on disease, modality, methods, and readers — the realistic submit goal.
3. **Backup journals**: when novelty, n, or validation is weaker, prefer specialty fit with more moderate methods bars.

Imaging-AI candidate pools often start from these classes, then verify per manuscript:

- General medicine and digital medicine: Nature Medicine、The Lancet Digital Health、npj Digital Medicine、JAMA Network Open、eClinicalMedicine、EBioMedicine。
- Oncology and precision medicine: The Lancet Oncology、Cell Reports Medicine、npj Precision Oncology、Clinical Cancer Research、European Journal of Cancer。
- Imaging and radiology: Radiology、Radiology: Artificial Intelligence、European Radiology、Investigative Radiology、American Journal of Roentgenology、Academic Radiology。
- Disease specialty: pick hepatobiliary, lung, breast, neuro-oncology, urology, GI, nuclear medicine, or ultrasound journals by disease.
- Methods and engineering: Medical Image Analysis、IEEE Transactions on Medical Imaging、IEEE Journal of Biomedical and Health Informatics、Computerized Medical Imaging and Graphics。

Do not treat these as a fixed recommendation list. Re-filter by topic, recent publications, section type, length, OA, APC, and submit policy.

## Integrating recent publication patterns

When the user asks to “select journals from existing papers and publication patterns”:

1. Build a query from keywords: disease + modality + task + method + endpoint.
2. Search similar papers in target journals over the last 3-5 years; prefer same disease/modality/task.
3. Extract per paper: journal, year, disease, modality, n, validation, main method, main conclusion.
4. Compare strengths and gaps vs the user's manuscript.
5. Bucket journals as `high match`, `worth trying`, `do not prioritize`.

## Output format

```text
Submit positioning
- Article type:
- Core sell:
- Biggest gap:
- Fit readers:

Journal tiers
| Tier | Journal | Match reason | Need to strengthen | Risk |

Recent publication contrast
| Journal | Recent similar-paper traits | Vs this manuscript |

Evidence-pattern gap
- Vs 2023-2026 high-tier journal patterns:
- Representative PMID seeds:

Pre-submit revision advice
- Title/abstract:
- Methods:
- Results:
- Discussion:
- Data and code:

Journals/directions not recommended
- [journal/direction]: reason

Author must confirm
- [missing facts]
```

## Red lines

- Do not rank by IF alone.
- Do not recommend predatory or unverifiable journals.
- Do not say “this will definitely be accepted.”
- Do not ignore whether the target recently published similar work.
- Do not package no-external-validation / small-n / weak-label studies as top-tier fits unless another design advantage is very strong.


## JCR tiered journal pack (Jinshan)

When the user wants “recommend journals / JCR·JCI tiered selection / ease-of-submit index”, load the advanced pack:

- `03_research/base/find-journal/SKILL.md` (authoritative flow; Victor; version ≥ **1.14**; Gemini+ChatGPT 2026-09)
- `03_research/base/find-journal/references/AGENTS.md` (must stay consistent with SKILL/policy)
- Curated table: `{jcr2026_xlsx}`
- Indices and modules: `03_research/base/find-journal/rules/jesi-model.md` (JESI/JEI / JDI / JCI-C / **MJF=MFI** / PAI), `modules.md`, `query-sources.md`
- Persistence: `03_research/base/find-journal/rules/persistence.md` — **absorb / query / delete** table; submission URLs and advanced priors may be stored; annual IF/quartile/volume/APC etc. **QUERY ONLY** (do not write into `{find_journal_pools}/2026/submission-urls.csv`); **Unknown ≠ Low Risk**; no fixed-weight policy (dynamic weighting)

This file still owns evidence-strength vs journal-preference, stretch/solid/safety narrative, and §「2023-2026 journal patterns」 below / live `meta-analysis` contrast. Tier-table output follows the advanced pack (default **tier2→tier3→tier4, 10 journals each**; tier2≈primary/Target, tier3≈solid/Safety-upper, tier4≈Q3; **tier2 stretch-supplement** is off by default — ask before each use; three blacklist journals never recommended; submitted/选刊 whitelist (`whitelist-submitted.csv`) prioritised within tier; graylist (incl. Frontiers series) skipped when a better match exists (`graylist.csv`)). Within-tier sort: manuscript match → ease-of-submit index → annual volume (weak). Medicine titles demoted within tier; do not mark “suspicious” in the table; yellow highlight only for JESI≥80. External journal-recommenders are query/candidate pools only — not top-level decisions. Phase-2 user short table (per paper): full journal name | JCR quartile | IF | annual volume | submit URL / author instructions (full URL); no ISO/OA/confidence/APC/split-journal detail; details in `03_research/base/find-journal/`.

Journal selection (选刊) routes through 03 `find-journal`; formatting through `05_manuscript/base/write-paper/`.

---

## 2023-2026 journal patterns (merged from journal-patterns-2023-2026.md, 2026-10-16)

> Keep this section with the 选刊 SOP.

Use this section when the user asks where to submit a radiomics,
medical imaging AI, radiogenomics, or imaging deep learning manuscript and wants advice
grounded in recent high-impact publication patterns.

## Evidence boundary

This file only owns the trade-off “evidence strength vs journal preference.” Journal-family pattern tables and disclaimers live in `05_manuscript/base/write-paper/references/journal-patterns-2023-2026.md` (SSOT) — do not duplicate here.

## Journal pattern table

| Journal-family signal table (2023-2026 seeds) | See `05_manuscript/base/write-paper/references/journal-patterns-2023-2026.md` (SSOT; not copied here) |

Representative PMID seeds used for this pattern map include 37690911, 38876123,
39775040, 41876649, 37268451, 38519154, 39070173, 37557177, 39244594, 39112796,
41339572, and 38809149. Use live `meta-analysis` (`02_data-processing/base/meta-analysis/`) for the full seed; `literature-evidence-2023-2026.md` was retired 2026-09-22
table and DOI-level metadata.

## Submission-tier logic

### Tier A: top clinical AI journals

Examples: Nature Medicine, The Lancet Digital Health, The Lancet Oncology for appropriate
oncology questions.

Usually needs at least one of:

- prospective, randomized, real-world, or reader-study evidence;
- strong multicenter external validation;
- clear effect on clinical pathway or decision-making;
- broad disease burden or screening/program-level relevance;
- transparent reporting, calibration, and utility analysis.

### Tier B: strong clinical/translational medical journals

Examples: eClinicalMedicine, EBioMedicine, Cell Reports Medicine, Radiology, npj Digital
Medicine, npj Precision Oncology depending on topic.

Usually needs:

- clinically meaningful endpoint;
- robust retrospective or multicenter validation;
- clear baseline comparison;
- calibration/decision utility if prediction is claimed;
- mechanism or precision oncology link when relevant.

### Tier C: focused radiology AI or specialty journals

Usually suitable when:

- study is retrospective and clinically useful but not broad enough for top-tier;
- external validation is limited or absent but methods are transparent;
- the paper contributes a disease-specific model, workflow, or reproducibility resource.

## Manuscript-positioning rules

- If no external validation: do not recommend top-tier clinical AI journals as realistic
  unless the study has another major strength such as prospective reader evidence.
- If single-center and no reader study: frame as exploratory or model-development work.
- If multicenter but pooled random split: downgrade because this is not external validation.
- If radiogenomics/multi-omics: match to npj Precision Oncology, Cell Reports Medicine,
  or disease-specific translational journals only when pairing and biology are credible.
- If foundation model: Nature Medicine/Nature Communications-level framing requires scale,
  generality, external validation, and reusable contribution.
- If clinical utility is claimed: require calibration, DCA/net benefit, threshold-action logic,
  and ideally reader/workflow evidence.

## Output rule

```text
Literature-pattern-driven journal judgment
- Evidence-source boundary:
- Current evidence grade of the manuscript:
- Gap vs last-three-years high-tier journal patterns:

Journal tiers
| Tier | Journal | Match to last-3y patterns | Current gap | Pre-submit upgrade |

Do not submit directly to
| Journal | Reason |

Must verify same day
- scope, author instructions, data/code policy, article type, similar recent papers
```

## Red lines

- Do not promise acceptance.
- Do not rank only by impact factor.
- Do not use a seed paper as proof that the user's weaker design fits the same journal.
- Do not invent journal policies, APCs, turnaround times, or recent publications.
- Do not hide single-center, no-external-validation, or AUC-only limitations.
