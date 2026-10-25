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
| mounted `design-study` → `references/feasibility-triage.md` | Deciding if the data can support a study at all; what's the realistic task ceiling; what's missing |
| mounted `design-study` → `references/study-blueprints.md` | Picking a design template (diagnostic accuracy, prediction/prognosis, treatment-response, segmentation, radiogenomics, reader study) and its minimum-viable vs stronger version |
| mounted `design-study` → `references/validation-strategy.md` | Designing internal/temporal/geographic/external/multi-center/federated validation; center & scanner effects; what counts as "external" |
| mounted `design-study` → `references/endpoints-and-estimands.md` | Choosing the clinical question, target population, endpoint, comparator, and clinical-use scenario |
| mounted `design-study` → `ai-radiogenomics-12-24-roadmap.md` | The user wants a 12-24 month plan for radiology AI/deep radiomics/radiogenomics, or asks how to turn data into a staged publication and translation program |
| [references/grant-own-skeleton.md](../personal/grant-own-skeleton.md) | **Voice B writing your own proposal**: justification five steps, two innovation columns, three feasibility blocks, verbs 「确定/阐明/探讨」. Do not open this file when reviewing someone else's NSFC |

## Workflow

1. **Inventory the data.** Disease, modality(ies), n (patients and lesions), number of centers
   and scanners, label source and quality, presence of segmentation masks, clinical variables,
   follow-up time and event counts, pathology/molecular labels, time span. Mark every unknown.
2. **Feasibility triage** (mounted `design-study` → `references/feasibility-triage.md`). Decide the realistic task ceiling and flag
   showstoppers (no reference standard, no external cohort, too few events, leakage-prone
   structure). Output a verdict: `Feasible as designed` / `Feasible with changes` / `Feasibility
   study only` / `Not yet — collect X first`.
3. **Define the question** (mounted `design-study` → `references/endpoints-and-estimands.md`). Clinical question → target population →
   primary endpoint/estimand → comparator → intended clinical-use scenario.
4. **Pick the blueprint** (mounted `design-study` → `references/study-blueprints.md`). Choose the design template and give a
   **minimum-viable** version (what's publishable now) and a **stronger** version (what would
   reach a higher tier), with the extra cost of each.
5. **For program-level AI/radiogenomics planning**, open mounted `design-study` → `ai-radiogenomics-12-24-roadmap.md`
   and place the project on the staged route from cohort lock to baselines, fusion, external
   validation, and silent/reader/prospective evidence.
6. **Design the validation** (mounted `design-study` → `references/validation-strategy.md`). Specify the split (patient-level),
   internal scheme, and the external/temporal/geographic/multi-center plan. State what is held
   out and what "external" honestly means here.
7. **Name the binding constraint** and the sample-size / EPV question (hand the numbers to
   `02_data-processing` / Loopnow, `calc-sample-size`).
8. **Return** the blueprint + feasibility verdict + validation plan + the prioritised list of
   what to secure next.

## Output contract

1. **`Feasibility verdict`** — one of the four verdicts above, with the one-line reason.
2. **`Data read`** — the inventory, with the binding constraint surfaced and unknowns listed.
3. **`Study blueprint`** — clinical question, population, primary endpoint/estimand, comparator,
   clinical-use scenario; design type.
4. **`Method options`** — minimum-viable vs stronger, with the trade-off and which reporting
   guideline each will be judged against (→ `05_manuscript`, mounted `check-reporting`).
5. **`Validation plan`** — split scheme, internal + external/temporal/geographic/multi-center
   design, and the honest definition of "external" for this data.
6. **`Roadmap`** — when relevant: staged 0-3, 3-6, 6-9, 9-12, 12-18, and 18-24 month milestones.
7. **`Next actions`** — what to collect, label, or confirm before/while running it, in priority
   order. Questions only the author can answer go here.

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
- Hand-crafted radiomics pipeline design → `02_data-processing` (mounted `radiomics-ml`; lab rules `02_data-processing/personal/analysis/pipeline.md`).
- Deep-learning architecture & training design → mounted `architecture-zoo` (`03_research`).
- ROI/mask annotation SOP → `02_data-processing` (mounted `preprocess-imaging`).
- Which checklist the design must satisfy → `05_manuscript` (mounted `check-reporting`).
- Ethics/consent/data-sharing feasibility → `03_research/personal/ethics.md`.
- Clinical-use scenario, reader study, prospective plan → `03_research/personal/clinical-translation/README.md`.
- Turning this design into **own** funding proposal (Voice B) → `grant-own-skeleton.md` + `grant-writing.md` (sentence bank). Method upgrades into 立项 → `radiology-frontier` `method-upgrade-into-grant.md`.
- Reviewing **other people's** NSFC/general (Voice A) → `../personal/grant-review.md`. Never mix those tics into own text.
- English journal peer review → `06_review`. Not this module.
- This skill plans research; it does not provide clinical or diagnostic recommendations.
