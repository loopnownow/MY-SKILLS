---
name: "radiology-design"
description: "Imaging study design and feasibility blueprint (研究设计 / 可行性 / 立项 / 开题): patient-level split, blocking risks. Sample-size numbers → 02_data-processing."
domain: "03_research"
trigger: ["研究设计", "可行性", "imaging feasibility", "样本量", "立项", "开题", "自拟标书"]
inputs: ["clinical_question", "modality", "cohort_sketch"]
outputs: ["design_blueprint", "blocking_risks"]
tools: ["checklist"]
quality_control: "patient-level split; no slice-level external validation"
owner: "03_research/personal/radiology-design.md"
---

The 样本量 trigger only frames the question here. Numbers go to `02_data-processing` / Loopnow (`calc-sample-size`).

# Imaging Study Design & Feasibility

Generic stance, intake questions, workflow steps, and the output contract live in
`03_research/base/design-study/MODULE.md` (single source). This page keeps only the
lab-specific pieces: extra-file map, own-proposal skeleton, and handoffs.

## When to open extra files

| File | Open when |
|---|---|
| live `design-study` → `references/feasibility-triage.md` | Deciding if the data can support a study at all; what's the realistic task ceiling; what's missing |
| live `design-study` → `references/study-blueprints.md` | Picking a design template (diagnostic accuracy, prediction/prognosis, treatment-response, segmentation, radiogenomics, reader study) and its minimum-viable vs stronger version |
| live `design-study` → `references/validation-strategy.md` | Designing internal/temporal/geographic/external/multi-center/federated validation; center & scanner effects; what counts as "external" |
| live `design-study` → `references/endpoints-and-estimands.md` | Choosing the clinical question, target population, endpoint, comparator, and clinical-use scenario |
| live `design-study` → `ai-radiogenomics-12-24-roadmap.md` | The user wants a 12-24 month plan for radiology AI/deep radiomics/radiogenomics, or asks how to turn data into a staged publication and translation program |
| [references/grant-own-skeleton.md](../personal/grant-own-skeleton.md) | **Voice B writing your own proposal**: justification five steps, two innovation columns, three feasibility blocks, verbs 「确定/阐明/探讨」. Do not open this file when reviewing someone else's NSFC |

## Workflow and output contract

Single source: `03_research/base/design-study/MODULE.md` — inventory → feasibility triage → question → blueprint → validation → binding constraint → return, plus the seven-item output contract that goes with it. Do not restate either one here.

Lab deltas when running that flow in this seat:

- Sample size / EPV / power numbers are never computed here → `02_data-processing` (`calc-sample-size`).
- `Method options` are judged against `05_manuscript` live `check-reporting`.

## Own-proposal chapter skeleton (Voice B only)

When the user is **writing their own** NSFC / opening / municipal science / health-commission / hospital-level / clinical protocol, open `grant-own-skeleton.md`. Do not use Voice A review tics.

Compact contract (details in that file):

1. **Justification five steps**: burden + typology → mainstream theory and concrete gap → prior work (literature + own, ≥2 chains) → one-sentence hypothesis → what this study will do. Subsection titles are mechanism nodes, not method names.
2. **Two innovation columns**: academic-idea innovation (one step forward) + technical-method innovation (against the tech gap named in justification). Do not write 「我们用了 MRI」.
3. **Three feasibility blocks**: mature model (name modeling / timepoints) + platform named to instruments + people ([PI], SCI [n] papers, ongoing grants). For clinical, also write case source「每年接诊 [疾病] 超过 [n] 例」.
4. **Three goal verbs**: 确定 (whether change exists / intervention works) / 阐明 (mechanism, spectrum, pathway) / 探讨 (diagnostic grading, translation). Do not make 探讨 the only goal.
5. Sentence bank (CN/EN abstracts, hypothesis, inclusion/exclusion) only from `grant-writing.md`. Method upgrade into justification → `radiology-frontier`.

## Handoffs

- Frontier framing / is this direction novel & publishable → `radiology-frontier`.
- Sample size, EPV, power, Riley minimum sample size → `02_data-processing` / Loopnow (`calc-sample-size`; lab notes `02_data-processing/personal/analysis/methods.md`).
- Hand-crafted radiomics pipeline design → `02_data-processing` (live `stats-analysis`; lab rules `02_data-processing/personal/analysis/pipeline.md`).
- Deep-learning architecture & training design → live `design-study` (`03_research`).
- ROI/mask annotation SOP → `02_data-processing` (live `preprocess-imaging`).
- Which checklist the design must satisfy → `05_manuscript` (live `check-reporting`).
- Ethics/consent/data-sharing feasibility → `03_research/personal/ethics.md`.
- Clinical-use scenario, reader study, prospective plan → `03_research/personal/clinical-translation/README.md`.
- Turning this design into **own** funding proposal (Voice B) → `grant-own-skeleton.md` + `grant-writing.md` (sentence bank). Method upgrades into 立项 → `radiology-frontier` `method-upgrade-into-grant.md`.
- Reviewing **other people's** NSFC/general (Voice A) → `../personal/grant-review.md`. Never mix those tics into own text.
- English journal peer review → `06_review`. Not this module.
- This skill plans research; it does not provide clinical or diagnostic recommendations.
