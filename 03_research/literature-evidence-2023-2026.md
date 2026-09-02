# 2023-2026 文献证据

Use this file when the user asks for near-three-year, recent, latest, high-impact,
frontier, journal-fit, or literature-driven advice in radiomics, medical imaging AI,
radiology deep learning, radiogenomics, or clinical translation.

## Scope and status

This is a curated seed evidence map, not an exhaustive systematic review.

- Verification source: PubMed E-utilities.
- Verification date: 2026-06-18.
- Time window: 2023-2026.
- Core journals included: Radiology, Radiology: Artificial Intelligence, The Lancet
  Digital Health, Nature Medicine, Nature Communications, eClinicalMedicine, Cell
  Reports Medicine, The Lancet Oncology, npj Precision Oncology.
- Supplementary method evidence includes selected papers outside the user's original
  journal list when they directly inform foundation models, reader effects, batch effects,
  or multicenter imaging design.

Do not cite this file as a complete review. Use it as a starting evidence layer and
perform a fresh search when the user asks for final manuscript citations, journal policy,
or the latest article list.

## How to use this evidence layer

1. Match the user's disease, modality, task, sample size, labels, and validation data.
2. Load `frontier-patterns-2023-2026.md` for topic selection.
3. Load `journal-patterns-2023-2026.md` for target-journal fit.
4. Use the tables below for representative PMID/DOI-level examples.
5. State the evidence boundary: curated seeds, PubMed-verified on 2026-06-18, not exhaustive.

## Evidence map

### Reporting, standardization, and reproducibility

| PMID | Journal / date | Paper | What it signals for the skill |
|---|---|---|---|
| 38809149 | Radiology: Artificial Intelligence, 2024 Jul | Checklist for Artificial Intelligence in Medical Imaging (CLAIM): 2024 Update | High-level imaging AI manuscripts should be audited against current AI reporting requirements. Use with `规范`, `预审`, and `复现`. |
| 38319168 | Radiology, 2024 Feb | The Image Biomarker Standardization Initiative: Standardized Convolutional Filters for Reproducible Radiomics and Enhanced Clinical Insights | Radiomics papers need reproducible image biomarker settings, filter definitions, and extraction transparency. Use with `组学`, `复现`, and `统计`. |
| 37795137 | Radiology: Artificial Intelligence, 2023 Sep | TotalSegmentator: Robust Segmentation of 104 Anatomic Structures in CT Images | Segmentation/foundation segmentation tools can support workflows, but generated masks still need task-specific QC and validation. Use with `标注` and `深度`. |

### Prospective, reader, workflow, and real-world clinical evidence

| PMID | Journal / date | Paper | What it signals for the skill |
|---|---|---|---|
| 37690911 | The Lancet Digital Health, 2023 Oct | Artificial intelligence for breast cancer detection in screening mammography in Sweden: a prospective, population-based, paired-reader, non-inferiority study | Top clinical AI work often tests workflow and reader impact, not just AUC. Use with `转化`, `预审`, and `选刊`. |
| 39904652 | The Lancet Digital Health, 2025 Mar | Screening performance and characteristics of breast cancer detected in the MASAI trial | Strong screening AI papers report clinical screening behavior and trial design details. Use when evaluating mammography or population screening projects. |
| 39775040 | Nature Medicine, 2025 Mar | Nationwide real-world implementation of AI for cancer detection in population-based mammography screening | Nature Medicine-level clinical AI often includes real-world implementation evidence. Use when judging deployment or top-tier fit. |
| 40346277 | Nature Medicine, 2025 May | Artificial intelligence improves breast cancer detection in mammography screening | Improvement claims need clinical screening evidence and not only retrospective discrimination. |
| 38876123 | The Lancet Oncology, 2024 Jul | Artificial intelligence and radiologists in prostate cancer detection on MRI (PI-CAI) | Paired, confirmatory, non-inferiority reader designs are a high-value route for diagnostic imaging AI. |
| 41275871 | The Lancet Oncology, 2026 Jan | Artificial intelligence and radiologists in pancreatic cancer detection using standard-of-care CT scans (PANORAMA) | High-impact diagnostic AI can be framed around radiologist comparison and standard-of-care imaging. |
| 41876649 | Nature Medicine, 2026 May | AI-based chest X-ray prioritization in the lung cancer diagnostic pathway: the LungIMPACT randomized controlled trial | Workflow prioritization and randomized clinical pathway studies are a high bar for clinical-translation claims. |
| 38504016 | Nature Medicine, 2024 Mar | Heterogeneity and predictors of the effects of AI assistance on radiologists | Reader benefit is heterogeneous; AI assistance should be evaluated by reader, case, workflow, and baseline expertise. |

### Multicenter imaging AI, treatment response, and clinical validation

| PMID | Journal / date | Paper | What it signals for the skill |
|---|---|---|---|
| 37268451 | The Lancet Digital Health, 2023 Jul | Predicting benefit from immune checkpoint inhibitors in NSCLC by CT-based ensemble deep learning | Treatment-benefit imaging AI needs clinically meaningful endpoints and careful retrospective validation. |
| 38519154 | The Lancet Digital Health, 2024 Apr | Deep-learning model for intracranial aneurysm detection on CT angiography in China: stepwise, multicentre, early-stage clinical validation | Multicenter and staged validation can lift an imaging AI paper above ordinary retrospective modeling. |
| 39070173 | eClinicalMedicine, 2024 Aug | Early warning of HCC in cirrhotic patients by three-phase CT-based deep learning radiomics | High-level radiomics/deep learning work often uses multicenter cohorts and clinically timed warning endpoints. |
| 38261897 | eClinicalMedicine, 2024 Jan | 3D vs 2D deep-learning, radiomics, and fusion models for occult lymph-node metastasis in laryngeal squamous cell carcinoma | Comparing 2D/3D/radiomics/fusion routes is useful when the user's data can support multiple modeling baselines. |
| 37557177 | Cell Reports Medicine, 2023 Aug | Non-invasive tumor microenvironment evaluation and treatment response prediction in gastric cancer using deep learning radiomics | Strong radiomics papers increasingly connect prediction to tumor microenvironment or treatment response. |
| 39637859 | Cell Reports Medicine, 2024 Dec | Interpretable multi-modal AI model for gastric cancer response to neoadjuvant chemotherapy | Multimodal and interpretable designs are stronger when linked to treatment decision points. |
| 38471502 | Cell Reports Medicine, 2024 Mar | Synthetic PET from CT improves diagnosis and prognosis for lung cancer: proof of concept | Cross-modality synthesis can be innovative, but proof-of-concept work needs cautious claims and validation. |

### Radiogenomics, radio-multiomics, radiopathomics, and mechanism

| PMID | Journal / date | Paper | What it signals for the skill |
|---|---|---|---|
| 40467921 | npj Precision Oncology, 2025 Jun | Computationally integrating radiology and pathology image features for predicting treatment benefit and outcome in lung cancer | Radiology-pathology integration is a strong route when paired pathology images and clinical outcomes exist. |
| 39244594 | npj Precision Oncology, 2024 Sep | Multicenter radio-multiomic analysis for predicting breast cancer outcome and unravelling imaging-biological connection | Radio-multiomic papers need both prediction and an imaging-biological connection; pairing matters. |
| 39152182 | npj Precision Oncology, 2024 Aug | Biologically interpretable multi-task deep learning pipeline predicts molecular alterations, grade, and prognosis in glioma | Multi-task models can connect molecular labels, grade, and prognosis when labels are available. |
| 40148588 | npj Precision Oncology, 2025 Mar | MRI transformer deep learning and radiomics for predicting IDH-wildtype TERT promoter mutant gliomas | Transformer plus radiomics can be justified for molecular subtype prediction if validation and labels are credible. |
| 41353523 | npj Precision Oncology, 2025 Dec | Integration of multi-scale radiomics and deep learning for Ki-67 prediction in clear cell renal carcinoma | Multi-scale radiomics/deep learning is a route for molecular marker prediction, but marker quality and validation define credibility. |
| 41260205 | Cell Reports Medicine, 2025 Nov | Prognostic index integrating deep learning baseline PET/CT biomarkers and multi-omics profiling in diffuse large B-cell lymphoma | Imaging plus multi-omics can support prognosis when sample matching and omics processing are transparent. |

### Foundation, generative, generalist, and distributed imaging AI

| PMID | Journal / date | Paper | What it signals for the skill |
|---|---|---|---|
| 39112796 | Nature Medicine, 2024 Nov | Generalist vision-language foundation model for diverse biomedical tasks | Generalist models are a frontier, but most user projects should evaluate transfer or benchmarking rather than train one from scratch. |
| 38689062 | Nature Medicine, 2024 May | Vision-language foundation model for echocardiogram interpretation | Vision-language models are strongest when paired images and reports/text labels are available. |
| 39663467 | Nature Medicine, 2025 Feb | Self-improving generative foundation model for synthetic medical image generation and clinical applications | Generative medical imaging requires careful validation, privacy, and clinical usefulness checks. |
| 41339572 | Nature Communications, 2025 Dec | Lung CT vision foundation model facilitating disease diagnosis and medical imaging | CT foundation models can be used as feature extractors or benchmarks when training scale is limited. |
| 40849424 | Nature Communications, 2025 Aug | Towards generalist foundation model for radiology by leveraging web-scale 2D and 3D medical data | Generalist radiology foundation models require web-scale 2D/3D data; typical clinical projects should not claim this scale without evidence. |
| 41136445 | Nature Communications, 2025 Oct | Modality-projection universal model for comprehensive full-body medical imaging segmentation | Universal segmentation is relevant to annotation acceleration but not a substitute for task-specific validation. |
| 40659619 | Nature Communications, 2025 Jul | Generative AI enables medical image segmentation in ultra low-data regimes | Low-data segmentation innovation may help rare diseases, but evaluation must include external or robust test data. |
| 41136442 | Nature Communications, 2025 Oct | Addressing data heterogeneity in distributed medical imaging with heterosync learning | Distributed and heterogeneous data methods matter when centers cannot share raw data or protocols differ. |
| 39187663 | Nature Biomedical Engineering, 2025 Apr | Vision-language foundation model for realistic chest X-ray image generation | Supplementary method evidence for generative/vision-language radiology work; outside the core journal list. |
| 39661030 | Cancer Research, 2025 Jan | BEEx evaluates batch effects in medical images to enable multicenter studies | Supplementary method evidence: batch effects should be measured, not only assumed corrected. |
| 41013591 | Breast Cancer Research, 2025 Sep | AI-driven MRI biomarker for triple-class HER2 expression classification in breast cancer | Supplementary disease-specific example for multicenter breast MRI biomarker work. |

## Pattern extraction

Use these extracted rules when advising users:

- High-impact clinical imaging AI is moving from retrospective AUC toward reader studies,
  workflow endpoints, real-world implementation, and randomized or confirmatory designs.
- Strong retrospective imaging AI papers usually need multicenter validation, time/center
  separation, transparent splits, calibration, and clinically meaningful endpoints.
- Radiomics remains publishable when reproducibility, standardization, external validation,
  and biological/clinical interpretation are handled rigorously.
- Radiogenomics and radio-multiomics are valuable only when molecular, pathology, or omics
  labels are available and pairing is clear.
- Foundation models are useful as transfer learning, feature extraction, benchmarking,
  segmentation assistance, or report/image-language modeling; training a foundation model
  from scratch is rarely feasible for ordinary hospital datasets.
- Multicenter work must address scanner/protocol/center heterogeneity and not simply pool data.
- Clinical utility claims need calibration, DCA/net benefit, threshold-action logic,
  reader/workflow evidence, or prospective validation.

## Update protocol

When updating this evidence layer:

1. Use PubMed or official journal pages.
2. Limit the first pass to the target years and journal set.
3. Record PMID, DOI, title, journal, date, disease, modality, task, model family,
   validation design, and why it matters.
4. Separate core target-journal evidence from supplementary method evidence.
5. Do not add a paper unless its metadata are verified.
6. Mark inferred design signals as inferred when only title/metadata are available.
7. For final manuscript citation advice, re-check source pages on the same day.

## Red lines

- Do not call this a systematic review.
- Do not invent sample sizes, performance metrics, or methods beyond verified metadata.
- Do not cite a seed paper as directly comparable unless disease, modality, task, and validation are aligned.
- Do not turn a foundation-model trend into a recommendation to train a foundation model without scale.
- Do not use these seeds as a substitute for a fresh search when the user asks for latest or final citations.
