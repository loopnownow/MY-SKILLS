# 设计

Use this file to turn the user's data and clinical interest into a feasible radiology
AI study.

## Study design contract

```text
Clinical question:
Target population:
Imaging modality:
Prediction/segmentation target:
Label source:
Analysis unit:
Training data:
Internal validation:
External validation:
Primary metric:
Secondary metrics:
Clinical use scenario:
Main risk:
```

## Feasibility ranking

Rank project ideas by:

1. label reliability
2. sample size and event count
3. external or temporal validation availability
4. segmentation burden
5. clinical usefulness
6. method novelty
7. reporting and reproducibility burden

Method novelty cannot rescue weak labels or invalid validation.

## Literature-driven design

When the user asks for near-three-year frontiers or high-impact publication logic,
load:

- `literature-evidence-2023-2026.md`
- `frontier-patterns-2023-2026.md`

Use the evidence patterns to choose an archetype, but never force a trendy direction
onto unsupported data. State the gap between the user's data and the recent high-impact
pattern.

## High-impact study archetypes

Choose the closest archetype instead of inventing a vague "AI prediction model" project.

| Archetype | Best data condition | Strong angle | Minimum validation |
|---|---|---|---|
| Reader/workflow AI | prospective, paired-reader, screening, triage, or reporting workflow data | AI changes sensitivity, workload, time, or non-inferiority | reader comparison or workflow endpoint |
| Multicenter diagnostic model | multi-center CT/MRI/PET/US with reliable reference standard | transportable diagnosis or staging | center-held-out or external test |
| Response/prognosis model | treatment, follow-up, recurrence, survival, or pCR labels | imaging biomarkers predict treatment benefit or risk | temporal/external validation, calibration |
| Radiogenomics/radiopathomics | imaging plus molecular/pathology/omics labels | non-invasive biology surrogate | independent validation and biological interpretation |
| Longitudinal imaging model | serial scans before/during/after therapy | dynamics outperform baseline imaging | time-aware split and fixed prediction landmark |
| Foundation-model adaptation | enough unlabeled images or strong pretrained model access | transfer improves small-label setting | baseline comparison and external/temporal test |
| Reproducible pipeline study | code, containers, public/controlled data, multiple sites | method transparency and portability | fully documented pipeline and held-out test |

## Project option template

```text
Project option
- Title:
- Study type:
- Literature-driven pattern:
- Representative PMID seeds:
- Why this is worth doing:
- Required data:
- Minimum viable method:
- Stronger method:
- Validation:
- Expected manuscript angle:
- Biggest risk:
- How to reduce risk:
```

## Common recommendations

- If sample size is small, prefer a focused clinical question, transparent baseline,
  penalized/simple model, robust CV, and clear limitations.
- If external validation exists, make transportability the main strength.
- If masks are strong, segmentation plus downstream clinical prediction may be viable.
- If follow-up exists, survival or response prediction can be stronger than simple diagnosis.
- If only reports are available, treat labels as weak and build an audit plan.
- If aiming for Radiology, Lancet Digital Health, Nature Medicine, or Lancet Oncology,
  prioritize clinical validation, reader/workflow value, and external evidence over
  architectural novelty alone.
- If aiming for npj Precision Oncology, Cell Reports Medicine, EBioMedicine, or
  eClinicalMedicine, multimodal biology-linked imaging questions can be strong when
  validation and mechanistic interpretation are credible.
