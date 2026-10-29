# Intake

Use this file first when the user gives an incomplete, mixed, or high-level radiology
AI request.

Writing / figures → `05_manuscript`. Pre-submission / **journal** peer review / reviewer response → `06_review`.
Reviewing someone else's NSFC → Voice A `grant-review.md` (this skill, not 06_review). Writing your own → Voice B `grant-writing.md`. Do not mix the two voice habits.
Clinical translation / reader studies → `clinical-translation/` (under `advanced/`). Ethics form packs → `fill-protocol`.

## Task modes

| Mode | Use when | Default next module |
|---|---|---|
| `guideline-first` | Project start: endpoint/grouping needs a named guideline definition before search/design/stats/writing | 项目启动前置 → `route.md` (guideline-first); then study card |
| `frontier` | User wants new research directions, hotspots, or innovation points | Frontier |
| `literature` | User wants recent papers, evidence maps, or search terms | Literature |
| `evidence` | User wants 2023-2026 high-impact literature patterns, representative PMID/DOI seed papers, or journal publication patterns behind topic selection | Evidence |
| `public-datasets` | User asks about TCIA, TCGA, GEO, CPTAC, IDC, public imaging/omics datasets, or public validation cohorts | Public datasets |
| `radiomics` | User describes handcrafted features or Pyradiomics-style workflow | Radiomics |
| `deep-learning` | User describes CNN, transformer, segmentation, classification, foundation models, or multimodal AI | Deep learning |
| `mechanism` | User asks how radiomics/deep learning model scores relate to genomics, transcriptomics, single-cell, spatial transcriptomics, pathways, immune microenvironment, or biological mechanisms | Mechanism |
| `study-design` | User gives data and asks what project can be done | Design |
| `grant-writing` | User asks to **write/polish their own** NSFC/provincial/university proposals, opening, protocol, abstract (Voice B) | Grant (own) → `grant-writing.md` + design skeleton + frontier method upgrade |
| `grant-review` | User asks to **review someone else's** NSFC/general/cross applications (Voice A) | Grant (others) → `grant-review.md` only. Do not use 06_review English boilerplate |
| `annotation` | User asks about ROI, VOI, mask, lesion selection, segmentation annotation, reader agreement, or ICC/Dice | Annotation |
| `statistics` | User asks about statistical analysis, sample size, feature selection, LASSO, Cox, C-index, calibration, DCA, confidence intervals, or survival analysis | Statistics |
| `validation` | User asks whether the model or result is reliable | Validation |
| `multicenter` | User asks about multicenter data, external validation by center, scanner/vendor/protocol differences, center effects, harmonization, or domain shift | Multicenter |
| `checklist` | User asks about CLAIM, CLEAR, RQS, IBSI, TRIPOD+AI, PROBAST+AI, STARD-AI, METRICS | Checklists |
| `data` | User asks about DICOM, NIfTI, masks, labels, privacy, repository, or sharing | Data |
| `ethics` | User asks about ethics approval, IRB, consent waiver, privacy, de-identification, or data-use limits | Ethics |
| `reproducibility` | User asks about code, model weights, feature tables, random seeds, environment, supplementary files, or reproducibility | Reproducibility |
| `writing` | User asks for Methods, Results, Discussion, abstract, title, or translation | Writing |
| `figures` | User asks about figures, tables, graphical abstracts, figure legends, workflows, ROC/calibration/DCA/KM plots, or mechanism diagrams | Figures |
| `pre-submission` | User asks for pre-submission audit, simulated reviewer critique, manuscript risk review, or top-journal readiness | Pre-submission |
| `journal-selection` | User has a draft/manuscript and asks where to submit, whether a journal fits, or how to choose target journals | Journal selection (选刊) → `journal-selection.md` + `find-journal/` |
| `clinical-translation` | User asks about clinical utility, reader study, prospective validation, workflow integration, PACS/RIS, deployment, or real-world evaluation | Translation |
| `response` | User gives reviewer comments or revision notes | Response |

## Study card

Collect these fields when available:

```yaml
disease:
clinical_question:
modality:
data_format:
n_patients:
n_images_or_lesions:
centers:
time_span:
labels:
endpoint:
follow_up:
segmentation:
annotation_strategy:
readers:
reader_agreement:
clinical_variables:
omics_data:
paired_omics:
omics_sample_size:
omics_platform:
split_plan:
external_validation:
center_distribution:
scanner_protocols:
statistics_plan:
main_metrics:
calibration_dca:
figure_needs:
public_dataset_plan:
ethics_approval:
consent_status:
data_sharing_limits:
code_availability:
clinical_use_case:
reader_study_plan:
model_type:
target_journal_or_output:
candidate_journals:
publication_goal:
funding_scheme:
proposal_section:
grant_deadline_or_year:
main_constraint:
```

## Clarifying question rule

Proceed with explicit assumptions when the user wants brainstorming or a rough plan.
Ask before final wording when missing facts would otherwise fabricate:

- sample size or patient/lesion/image unit
- endpoint or label source
- segmentation source and reader agreement
- train/validation/test split unit
- external validation status
- reported performance values
- ethics, consent, code, or data availability

## Fast routing examples

- "我有 200 例 CT 想做预后模型" -> Design + radiomics or DL + validation
- "近三年影像 AI 前沿有哪些" -> Frontier + literature
- "根据近三年高水平期刊发表规律帮我选题" -> Evidence + frontier + literature + design
- "影像组学模型做完了，想结合转录组和单细胞解释机制" -> Mechanism + radiomics + literature + validation
- "帮我润色国自然立项依据" -> Voice B grant (own) + design skeleton + frontier method upgrade. No review tics
- "帮我评这份国自/面上" -> Voice A `grant-review.md` five columns. Do not write justification five steps or CN/EN abstract skeleton
- "ROI 是两位医生勾画的，Methods 怎么写" -> Annotation + radiomics + checklists
- "LASSO、Cox、DCA、C-index 这部分统计对不对" -> Statistics + validation
- "帮我看 Methods 是否符合 CLAIM" -> Checklists + DL + validation
- "帮我规划论文图表和 figure legend" -> Figures + writing + checklists
- "投稿前帮我模拟审稿人预审" -> Pre-submission + validation + checklists + figures
- "代码、特征表和模型参数怎么放补充材料" -> Reproducibility + data + ethics
- "4 家医院数据怎么做外部验证和中心差异分析" -> Multicenter + validation + statistics
- "想用 TCIA/TCGA/GEO 做验证或机制解释" -> Public datasets + literature + mechanism + data
- "伦理、知情同意豁免和数据共享怎么写" -> Ethics + data + reproducibility
- "这个模型怎么做读者研究和临床转化" -> Translation + validation + statistics
- "文章写好了，帮我选刊" -> Journal selection (选刊) + literature + checklists + validation
- "结合近三年类似文章发表情况判断能不能投 Nature Medicine" -> Evidence + journal selection + literature + pre-submission
- "审稿人说没有外部验证怎么回复" -> Response + validation
