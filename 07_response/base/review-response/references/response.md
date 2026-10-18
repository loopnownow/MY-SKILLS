# 回复

Use this file for reviewer comments about radiomics and imaging AI.

## Default posture

- Preserve reviewer concerns.
- Map each concern to evidence, analysis, manuscript change, limitation, or missing input.
- Do not claim new experiments, analyses, external validation, code release, line numbers,
  or figures unless supplied.

## Common reviewer issues

| Issue | Better response route |
|---|---|
| No external validation | acknowledge limitation, add available temporal/internal validation, soften generalizability |
| Possible data leakage | explain patient-level split and pipeline order, or flag as blocking |
| Small sample | report event count, confidence intervals, simpler model, limitation |
| Missing segmentation details | add reader/mask/QC/inter-reader information |
| Weak clinical utility | add calibration/DCA or soften deployment claims |
| Missing reporting checklist | add CLAIM/CLEAR/TRIPOD+AI/STARD-AI checklist as appropriate |
| Reviewer asks impossible follow-up | explain study-design boundary and add limitation |

## Response template

```text
We thank the reviewer for raising this important point. We agree that [concern]
is important for assessing [validity/generalizability/reproducibility]. To address
this, we [supplied action]. This change appears in [location]. Because [remaining
limitation], we have also revised the Discussion to state that [boundary].
```

Use placeholders when facts are missing.
