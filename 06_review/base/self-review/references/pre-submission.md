# Pre-submission review

Use this file when the user asks for pre-submission review, simulated reviewer
critique, manuscript risk audit, top-journal readiness, or final checks before
submitting a radiomics or medical imaging AI manuscript.

## Core goal

The pre-submission module works like a reviewer and a methods editor: find hard defects that would cause reject or major revision first, then give actionable fixes.

## First questions

- What is the target journal or journal tier?
- Are title, abstract, Methods, Results, and Discussion already available?
- Is the study single-center, multi-center, externally validated, prospective, or retrospective?
- What are the primary endpoint, sample size, events, model performance, and validation scheme?
- Are ethics, data availability, code availability, and reporting checklists present?
- What do the authors worry about most: external validation, sample size, novelty, clinical value, or mechanism?

## Audit priority

### Level 1: possible rejection-level issues

- no clear clinical question
- no patient-level split
- train/test leakage
- feature selection before splitting
- no independent validation despite strong claims
- unclear endpoint or label source
- unclear segmentation or no mask QC
- very small event count with complex model
- unsupported clinical utility claim
- missing ethics approval/waiver statement
- fabricated or unverifiable data/code availability

### Level 2: major revision issues

- no calibration
- no DCA when clinical decision support is claimed
- no confidence intervals
- no baseline clinical model
- no comparison with combined clinical-imaging model
- weak external validation description
- incomplete image acquisition details
- incomplete radiomics extraction parameters
- incomplete deep learning training details
- no limitations addressing retrospective design and generalizability

### Level 3: polish and positioning

- title overclaims clinical deployment
- abstract conclusion stronger than results
- discussion repeats results without explaining clinical meaning
- figures do not support narrative
- tables missing cohort counts or event counts
- terminology inconsistent
- checklist not cited or incompletely addressed

## Target-journal readiness

For high-impact journals, check whether the manuscript has at least several of:

- clinically meaningful question
- multicenter or external validation
- transparent and leakage-resistant methods
- calibrated prediction and decision-curve analysis
- clinically interpretable comparison to standard variables or radiologists
- prospective, reader-study, or workflow evidence for translation
- data/code/model transparency appropriate to privacy constraints
- careful limitations and no deployment overclaim

Do not promise suitability for a journal based only on AUC.

## Output format

```text
Pre-submission review conclusion
- Current tier:
- Biggest hard defect:
- Easiest strengthen point:

High-risk issues
| Priority | Issue | Why dangerous | Suggested fix |

Methods must-fix
- [data split, segmentation, preprocessing, model, validation, ethics]

Results must-add
- [CI, calibration, DCA, subgroup, external validation, failure cases]

Discussion tone-down
- [overclaims and limitations]

Pre-submission checklist
- [checklist, data/code availability, figures, tables, cover letter points]
```

## Revision language

Use direct wording:

- “This is a likely reviewer concern because...”
- “This claim should be softened unless...”
- “This analysis should be moved from exploratory to supplementary unless...”
- “The manuscript should not claim clinical readiness without...”

## Red lines

- Do not rubber-stamp a manuscript as ready when validation or leakage is unresolved.
- Do not hide limitations by wording.
- Do not invent analyses, ethics approval, external validation, or code availability.
- Do not recommend a top-tier target without explicitly stating validation and clinical-utility gaps.
- Do not treat checklist compliance as a substitute for sound study design.
