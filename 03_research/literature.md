# 文献

Use this file when searching, screening, or organizing radiology AI literature.

## Search stance

Search for concepts, not only exact titles. Combine:

- disease: lung cancer, HCC, glioma, breast cancer, rectal cancer, stroke, etc.
- modality: CT, MRI, PET/CT, ultrasound, mammography, pathology, multimodal
- task: classification, segmentation, prognosis, response prediction, survival, radiogenomics
- method: radiomics, deep learning, transformer, foundation model, self-supervised,
  multimodal fusion, domain adaptation, calibration
- standard: CLAIM, CLEAR, RQS, IBSI, TRIPOD+AI, PROBAST+AI, STARD-AI, METRICS

## Source hierarchy

1. Primary research articles and official guideline papers.
2. Systematic reviews or scoping reviews for landscape mapping.
3. Publisher pages, PubMed, arXiv, and conference proceedings for discovery.
4. Secondary databases only as discovery aids.

## 2023-2026 evidence layer

When the user asks for "近三年", "前沿", "高水平期刊", "发表规律", "选题依据",
or journal-fit evidence, load:

- `literature-evidence-2023-2026.md`
- `frontier-patterns-2023-2026.md`
- `journal-patterns-2023-2026.md` when target journals are involved

Use this evidence layer as a PubMed-verified seed map. Do not call it exhaustive.
For final manuscript citation lists, run a fresh search and update the search date.

## Screening tiers

| Tier | Meaning |
|---|---|
| `direct` | Same disease, modality, task, and validation need |
| `method-transfer` | Different disease but method can transfer |
| `background` | Helps frame trend or clinical need |
| `weak` | Related keywords but not useful for the project |

## High-impact journal seed map

When a user asks for frontiers or a publishable topic, start with a current search, then
use this seed map to structure the synthesis. Verify details before citing in a final
manuscript because this list is a curated starting point, not an exhaustive review.

### Reporting and standards

| Theme | Example source |
|---|---|
| AI medical imaging reporting | CLAIM 2024 Update, Radiology: Artificial Intelligence, PMID 38809149 |
| Radiomics reproducibility | IBSI standardized convolutional filters, Radiology, PMID 38319168 |
| Generalizable segmentation benchmark | TotalSegmentator, Radiology: Artificial Intelligence, PMID 37795137 |

### Prospective, reader, or workflow studies

| Theme | Example source |
|---|---|
| Mammography screening AI prospective/paired-reader | Lancet Digital Health MASAI-related papers, PMIDs 37690911, 39904652 |
| Mammography real-world implementation | Nature Medicine, PMID 39775040 |
| Breast cancer detection with AI | Nature Medicine, PMID 40346277 |
| Prostate MRI reader comparison/non-inferiority | Lancet Oncology PI-CAI, PMID 38876123 |
| Pancreatic cancer CT AI and radiologists | Lancet Oncology PANORAMA, PMID 41275871 |
| Lung cancer pathway prioritization | Nature Medicine LungIMPACT, PMID 41876649 |

### Multicenter imaging AI and radiomics

| Theme | Example source |
|---|---|
| CT ensemble DL for immunotherapy benefit in NSCLC | Lancet Digital Health, PMID 37268451 |
| CT angiography intracranial aneurysm multicenter validation | Lancet Digital Health, PMID 38519154 |
| Three-phase CT deep learning radiomics for HCC warning | eClinicalMedicine, PMID 39070173 |
| 2D/3D/fusion model comparison for occult lymph node metastasis | eClinicalMedicine, PMID 38261897 |
| Deep learning radiomics for gastric cancer TME/response | Cell Reports Medicine, PMID 37557177 |
| Interpretable multimodal gastric cancer response model | Cell Reports Medicine, PMID 39637859 |
| Synthetic PET from CT for lung cancer | Cell Reports Medicine, PMID 38471502 |

### Multimodal, radiogenomics, and radiopathomics

| Theme | Example source |
|---|---|
| Radiology + pathology image features for lung cancer outcome | npj Precision Oncology, PMID 40467921 |
| Radio-multiomic breast cancer outcome | npj Precision Oncology, PMID 39244594 |
| Glioma molecular alterations, grade, and prognosis | npj Precision Oncology, PMID 39152182 |
| MRI transformer/radiomics for IDH-wildtype TERT-mutant glioma | npj Precision Oncology, PMID 40148588 |
| Multi-scale radiomics and deep learning for Ki-67 | npj Precision Oncology, PMID 41353523 |
| PET/CT biomarkers plus multi-omics in lymphoma | Cell Reports Medicine, PMID 41260205 |

### Foundation, generative, and generalist imaging AI

| Theme | Example source |
|---|---|
| Generalist biomedical vision-language model | Nature Medicine, PMID 39112796 |
| Echocardiogram vision-language foundation model | Nature Medicine, PMID 38689062 |
| Self-improving generative foundation model for synthetic medical imaging | Nature Medicine, PMID 39663467 |
| Lung CT vision foundation model | Nature Communications, PMID 41339572 |
| Universal full-body segmentation model | Nature Communications, PMID 41136445 |
| Low-data generative AI segmentation | Nature Communications, PMID 40659619 |
| Distributed medical imaging heterogeneity | Nature Communications, PMID 41136442 |

## Output

```text
Search strategy
- Date searched:
- Query concepts:
- Inclusion logic:
- Evidence seed boundary:

Evidence map
| Theme | Representative papers | Why relevant | Transfer risk |

Actionable gap
- What remains under-addressed:
- What the user's data can test:
```

## Common mistakes

- Listing many papers without explaining how they change the study design.
- Treating arXiv performance as established clinical evidence.
- Ignoring negative, external-validation, or reproducibility papers.
- Using outdated guidelines when the user asks for current reporting standards.
- Equating "published in a high-impact journal" with suitability for the user's data.
