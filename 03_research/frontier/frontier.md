# 前沿

Use this file to convert recent radiomics and imaging deep learning literature into
feasible research directions for the user's data.

## Core principle

Frontier selection is a matching problem: `important trend + user's data can support it
+ validation is credible + clinical question is meaningful`.

Do not recommend a method only because it is fashionable.

## Recency rule

When the user asks for "latest", "recent", "near three years", "frontier", "hotspot",
"前沿", "热点", or "近三年", search current sources before final recommendations.
Use official journal pages, PubMed, arXiv, publisher pages, and high-quality review
articles as discovery sources. State the search date.

For 2023-2026 high-impact imaging AI patterns, load these files before giving
literature-driven project suggestions:

- `literature-evidence-2023-2026.md`
- `frontier-patterns-2023-2026.md`

State that this is a PubMed-verified curated seed map, not an exhaustive systematic
review. Refresh the search for final citations or publication-critical claims.

## Frontier families

| Family | Good fit | Common risk |
|---|---|---|
| Foundation models | Large unlabeled image sets, transfer learning, limited labels | Overclaiming without external validation |
| Self-supervised learning | Many images but sparse labels | Leakage through pretraining or patient overlap |
| Vision-language / report-guided AI | Paired imaging and reports | Noisy report labels and weak ground truth |
| Multimodal fusion | Imaging plus clinical, omics, pathology, or genomics | Missingness, small sample, unclear added value |
| Radiomics + deep fusion | Existing ROI/masks plus image data | Feature leakage, weak harmonization |
| Radiogenomics | Molecular or pathology labels available | Small labeled cohorts and multiple testing |
| Domain adaptation | Multi-center scanner/protocol shift | No true target-domain validation |
| Federated learning | Data cannot leave hospitals | Engineering burden and governance limits |
| Uncertainty/calibration | Clinical decision support or triage | Reporting AUC only, no calibration or DCA |
| Longitudinal imaging | Follow-up scans and treatment response | Timepoint inconsistency and survival bias |
| Weak supervision | Labels exist at patient/report level but masks are limited | Poor localization evidence |
| Generative augmentation | Rare disease or data imbalance | Synthetic data improves appearance but not validity |

## High-impact journal patterns, 2023-2026

Use `frontier-patterns-2023-2026.md` for the detailed evidence-linked version. The
summary below is only the routing layer.

| Pattern | What strong papers tend to do | Project implication |
|---|---|---|
| Prospective or paired-reader evaluation | Breast screening AI, prostate MRI AI, pancreatic cancer CT AI, and lung-cancer pathway AI papers test workflow impact, reader non-inferiority, or triage | If the user has clinical workflow data, frame the study around reader/workflow benefit, not only AUC |
| Multicenter retrospective validation | CT/MRI deep learning radiomics papers in eClinicalMedicine, Lancet Digital Health, Radiology, and npj journals often use multicenter cohorts | For retrospective studies, make center-held-out or external validation a central strength |
| Imaging plus biology | Radiogenomics, radiopathomics, radio-multiomics, tumor microenvironment, Ki-67, IDH/TERT, and immune response papers connect images to biology | Recommend this only when molecular/pathology/omics labels actually exist |
| Longitudinal imaging | CT/MRI/PET studies increasingly use serial scans, treatment response, recurrence, and survival endpoints | If follow-up exists, prioritize temporal dynamics over single-timepoint classification |
| Foundation and generalist models | Nature Medicine and Nature Communications papers emphasize vision-language, synthetic image generation, universal segmentation, and CT foundation models | Use as transfer or benchmarking strategy unless the user has enough scale to train foundation models |
| Reproducible pipelines | Nature Communications-style work highlights end-to-end reproducible radiology AI pipelines and distributed learning | Recommend code, pipeline, container, and split transparency when the project aims high |
| Clinical utility beyond discrimination | High-impact papers often add calibration, decision impact, reader comparison, or real-world deployment | Do not call a study clinically useful from AUC alone |

## Matching workflow

1. Build the study card from `入口`.
2. Identify the clinical bottleneck: diagnosis, staging, subtype, treatment response,
   recurrence, survival, segmentation, workflow efficiency, or report quality.
3. Choose 2-4 frontier families that fit the data.
4. Reject directions that require unavailable data, such as genomics, longitudinal
   follow-up, expert masks, or external cohorts.
5. Return 3-5 project options ranked by feasibility and novelty.

## Output

```text
Frontier map
- Best-fitting frontier:
- Why it fits this dataset:
- What recent work suggests:
- Evidence boundary:
- Representative PMID seeds:

Project option 1
- Title:
- Core question:
- Data needed:
- Method route:
- Validation route:
- Innovation point:
- Main risk:
- Minimum next step:

Directions to avoid
- [direction]: [why unsupported by current data]
```

## Red flags

- "Use a foundation model" without saying what task, data, and validation it improves.
- "Multimodal" when clinical variables are unavailable or too incomplete.
- "Radiogenomics" without molecular/pathology labels.
- "External validation" when test data come from the same center or same patient pool.
- "Clinical utility" without calibration, decision curve, workflow endpoint, or prospective logic.
- "Near-three-year frontier" without current literature search date and journal/source boundary.
