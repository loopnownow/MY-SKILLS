# 2023-2026 期刊规律

Use this file with `journal-selection.md` when the user asks where to submit a radiomics,
medical imaging AI, radiogenomics, or imaging deep learning manuscript and wants advice
grounded in recent high-impact publication patterns.

## Evidence boundary

This file summarizes journal-fit signals from PubMed-verified seed papers on 2026-06-18.
It is not a substitute for checking the current author instructions, scope, article type,
APC, word limits, data policy, or recent issue contents.

## Journal pattern table

| Journal family | Recent signal from seeds | What a manuscript usually needs | Caution for ordinary retrospective radiomics |
|---|---|---|---|
| Nature Medicine | real-world mammography implementation, improved screening detection, LungIMPACT randomized pathway trial, biomedical/echo/generative foundation models | clinical or workflow significance, prospective/real-world/reader evidence, broad biomedical impact, strong validation | single-center retrospective AUC-only work is usually not aligned |
| The Lancet Digital Health | prospective mammography MASAI, CT immune-checkpoint benefit, multicenter CTA aneurysm validation | clinically relevant digital health question, validation beyond one center, workflow or patient-impact framing | methods-only novelty without clinical validation is weak |
| The Lancet Oncology | PI-CAI prostate MRI, PANORAMA pancreatic CT | oncology diagnostic/treatment relevance, paired reader or confirmatory validation, standard-of-care imaging | requires oncology relevance and rigorous clinical framing |
| Radiology | IBSI standardization and clinically important radiology evidence | radiology-centered question, methodological rigor, clinical imaging relevance, reproducibility | pure algorithm novelty may fit less well unless radiology impact is clear |
| Radiology: Artificial Intelligence | CLAIM 2024, TotalSegmentator and imaging AI methods | imaging AI method/reporting clarity, datasets, validation, reproducibility | weak reporting or no validation will be exposed |
| Nature Communications | CT/foundation segmentation, lung CT foundation model, distributed heterogeneity, low-data segmentation | broad method novelty, technical contribution, external validation, reusable model/data/pipeline when possible | small single-task retrospective models rarely fit unless method is genuinely novel |
| eClinicalMedicine / EBioMedicine | multicenter HCC early warning, 2D/3D/radiomics/fusion clinical validation | clinically meaningful cohort study with transparent validation and translational framing | needs more than local model performance |
| Cell Reports Medicine | gastric cancer TME/response, multimodal response model, synthetic PET, PET/CT plus multi-omics lymphoma | biological or translational mechanism plus clinical prediction | mechanism claims must be supported, not decorative |
| npj Digital Medicine | digital medicine, AI deployment, clinical evaluation, model generalization | digital health relevance, generalizable methods, transparent validation | narrow radiomics without digital medicine framing may be less aligned |
| npj Precision Oncology | radiology-pathology, radio-multiomics, glioma molecular prediction, Ki-67 and precision oncology markers | oncology precision marker, molecular/pathology/multi-omics link, validation | radiogenomics needs real paired labels and cautious mechanism claims |

Representative PMID seeds used for this pattern map include 37690911, 38876123,
39775040, 41876649, 37268451, 38519154, 39070173, 37557177, 39244594, 39112796,
41339572, and 38809149. Use `literature-evidence-2023-2026.md` for the full seed
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
文献规律驱动的选刊判断
- 证据来源边界：
- 文章当前证据等级：
- 与近三年高水平期刊规律的差距：

期刊梯队
| 梯队 | 期刊 | 近三年规律匹配 | 当前短板 | 投稿前升级动作 |

不建议直接投的期刊
| 期刊 | 原因 |

需要当天核验
- scope, author instructions, data/code policy, article type, similar recent papers
```

## Red lines

- Do not promise acceptance.
- Do not rank only by impact factor.
- Do not use a seed paper as proof that the user's weaker design fits the same journal.
- Do not invent journal policies, APCs, turnaround times, or recent publications.
- Do not hide single-center, no-external-validation, or AUC-only limitations.
