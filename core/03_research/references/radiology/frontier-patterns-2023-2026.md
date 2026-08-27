# 2023-2026 前沿规律

Use this file with `literature-evidence-2023-2026.md` when turning recent high-impact
radiomics and imaging AI literature into feasible project ideas.

## Evidence boundary

The patterns below are extracted from a PubMed-verified seed map on 2026-06-18.
They are not exhaustive and must be refreshed for final citation use.

## Frontier pattern 1: workflow and reader evidence beats AUC-only work

Signals:

- prospective or paired-reader mammography screening evidence: PMIDs 37690911, 39904652
- real-world mammography implementation: PMID 39775040
- prostate MRI paired non-inferiority reader study: PMID 38876123
- pancreatic CT paired non-inferiority reader study: PMID 41275871
- lung cancer pathway randomized prioritization: PMID 41876649

Use when:

- the user can involve radiologists or a workflow endpoint;
- the task is screening, detection, triage, prioritization, or report support;
- there is a plausible before/after or unaided/AI-assisted design.

Avoid when:

- the dataset is small and retrospective only;
- there are no readers, workflow timestamps, or clinical action thresholds.

Project translation:

- reader study
- clinician + AI incremental value
- workflow triage
- non-inferiority against standard reading
- prospective locked-model validation

## Frontier pattern 2: multicenter validation is the default credibility upgrade

Signals:

- multicenter intracranial aneurysm CTA validation: PMID 38519154
- multicenter HCC CT deep learning radiomics: PMID 39070173
- multicenter CT 2D/3D/radiomics/fusion comparison: PMID 38261897
- distributed imaging heterogeneity method: PMID 41136442
- image batch-effect method signal: PMID 39661030

Use when:

- the user has multiple hospitals, scanners, protocols, or time periods;
- external validation can be held out at center level;
- center-specific sample sizes are adequate.

Avoid when:

- centers are pooled and randomly split;
- external test centers are used for model tuning;
- labels and treatment protocols differ without harmonization.

Project translation:

- center-held-out validation
- temporal/geographic validation
- scanner/protocol subgroup analysis
- ComBat or harmonization sensitivity analysis
- domain shift assessment

## Frontier pattern 3: treatment response and clinically timed endpoints are stronger than generic classification

Signals:

- CT-based immune-checkpoint inhibitor benefit in NSCLC: PMID 37268451
- gastric cancer treatment response and tumor microenvironment: PMID 37557177
- multimodal gastric cancer neoadjuvant response: PMID 39637859
- HCC early warning in cirrhosis: PMID 39070173

Use when:

- treatment dates, treatment type, response definition, and follow-up are reliable;
- baseline and post-treatment or longitudinal imaging exist;
- the endpoint changes management.

Avoid when:

- response labels are vague;
- imaging time windows are inconsistent;
- there is no treatment or follow-up information.

Project translation:

- pCR/ORR/RECIST/iRECIST prediction
- PFS/OS/recurrence risk
- delta-radiomics
- baseline imaging plus clinical covariates
- decision threshold tied to treatment choice

## Frontier pattern 4: imaging-biology linkage is a major upgrade only with real labels

Signals:

- radiology-pathology outcome integration: PMID 40467921
- radio-multiomic breast cancer outcome and biological connection: PMID 39244594
- glioma molecular/grade/prognosis multi-task model: PMID 39152182
- MRI transformer/radiomics for IDH-wildtype TERT-mutant glioma: PMID 40148588
- PET/CT biomarkers plus multi-omics in lymphoma: PMID 41260205

Use when:

- pathology, molecular marker, bulk RNA, single-cell, spatial transcriptomics, or multi-omics data exist;
- sample matching is known;
- the biological question is prespecified.

Avoid when:

- only public unpaired omics data exist and the user wants direct mechanism proof;
- molecular labels are too sparse;
- multiple testing and batch effects cannot be controlled.

Project translation:

- radiogenomics
- radiopathomics
- imaging transcriptomics
- TME/immune microenvironment interpretation
- paired pathway/cell-state/spatial-niche evidence chain

## Frontier pattern 5: foundation models are a transfer tool for most hospital projects

Signals:

- generalist biomedical vision-language model: PMID 39112796
- echocardiogram vision-language foundation model: PMID 38689062
- generative medical image foundation model: PMID 39663467
- lung CT vision foundation model: PMID 41339572
- generalist radiology foundation model leveraging web-scale 2D/3D data: PMID 40849424

Use when:

- the user has limited labels but enough images for transfer learning or benchmarking;
- paired reports are available for vision-language work;
- the goal is feature extraction, pretraining comparison, or report/image alignment.

Avoid when:

- the user wants to train a foundation model from a small single-center cohort;
- external validation is unavailable;
- the project cannot benchmark against simpler baselines.

Project translation:

- foundation-model feature extractor
- self-supervised pretraining
- report-guided labels
- transfer learning benchmark
- zero/few-shot evaluation with external validation

## Frontier pattern 6: generative imaging is publishable only with strict validation

Signals:

- synthetic PET from CT proof of concept: PMID 38471502
- generative foundation model for synthetic medical image generation: PMID 39663467
- low-data generative AI segmentation: PMID 40659619
- chest X-ray vision-language generation: PMID 39187663

Use when:

- the generated output has a clear clinical or workflow purpose;
- validation includes diagnostic, prognostic, or segmentation utility;
- privacy and hallucination risks are handled.

Avoid when:

- the only evidence is visually plausible images;
- synthetic data are used to inflate performance without external validation;
- patient privacy and memorization risks are ignored.

Project translation:

- cross-modality synthesis
- low-data segmentation support
- synthetic augmentation sensitivity analysis
- reader evaluation of synthetic utility

## Frontier pattern 7: reproducibility and reporting are no longer optional

Signals:

- CLAIM 2024 update: PMID 38809149
- IBSI convolutional filters: PMID 38319168
- TotalSegmentator: PMID 37795137

Use when:

- the user is preparing a high-impact manuscript;
- radiomics extraction, segmentation, AI model reporting, and code/data sharing are incomplete.

Avoid when:

- the user wants to hide weak methods behind polished text.

Project translation:

- CLAIM/CLEAR/RQS/IBSI/TRIPOD+AI audit
- feature extraction parameter table
- model card/supplementary reproducibility package
- segmentation QC and mask availability statement

## Ranking project ideas from these patterns

Prefer project ideas in this order:

1. clinically meaningful endpoint + external/multicenter validation;
2. reader/workflow/prospective logic;
3. paired mechanism or multi-omics evidence;
4. foundation-model transfer with strong baselines;
5. reproducible radiomics with transparent validation;
6. exploratory single-center model only when framed honestly.

## Output rule

When using this file, return:

```text
文献驱动前沿判断
- 证据来源边界：
- 最匹配的近三年前沿规律：
- 代表性 PMID：

适合该数据的方向
| 方向 | 对应文献规律 | 为什么适合 | 最小验证要求 | 风险 |

不建议方向
| 方向 | 不建议原因 |
```

## Red lines

- Do not recommend a frontier because it is popular.
- Do not treat these patterns as proof that the user's specific project is publishable.
- Do not cite a PMID as direct support for another disease or modality without stating transfer risk.
- Do not promote foundation-model training without scale, compute, and validation.
