# 规范

Use this file to choose reporting and risk-of-bias frameworks.

## Quick selector

| Need | Use |
|---|---|
| AI medical imaging manuscript reporting | CLAIM |
| Radiomics reporting quality | CLEAR, RQS, METRICS, IBSI-aware reporting |
| Prediction model reporting | TRIPOD+AI |
| Prediction model risk of bias | PROBAST+AI |
| Diagnostic accuracy study | STARD-AI |
| Clinical trial with AI intervention | CONSORT-AI / SPIRIT-AI |
| Segmentation or image analysis reproducibility | CLAIM plus task-specific metrics and data details |

## Audit stance

- Use checklists as reporting and bias tools, not as decoration.
- Map every missing item to manuscript action or author input.
- If a rule may have changed, verify the current official guideline page before final advice.

## Common missing items

- patient flow and exclusions
- data source and acquisition protocol
- label reference standard
- patient-level split and external validation
- preprocessing and augmentation
- model architecture and hyperparameters
- code, model, and data availability
- uncertainty, calibration, subgroup analysis
- limitations and intended use

## Output

```text
Checklist choice
- Primary checklist:
- Secondary checklist:
- Why:

Major gaps
| Item | Current status | Required fix |
```
