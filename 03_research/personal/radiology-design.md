---
name: "radiology-design"
description: "Imaging study design and feasibility blueprint (研究设计 / 可行性 / 立项 / 开题): patient-level split, blocking risks. Sample-size numbers → 04_analysis."
domain: "03_research"
trigger: ["研究设计", "可行性", "imaging feasibility", "样本量", "立项", "开题", "自拟标书"]
inputs: ["clinical_question", "modality", "cohort_sketch"]
outputs: ["design_blueprint", "blocking_risks"]
tools: ["checklist"]
quality_control: "patient-level split; no slice-level external validation"
owner: "03_research/personal/radiology-design.md"
---

The 样本量 trigger only frames the question here. Numbers go to `04_analysis` / Loopnow (`calc-sample-size`).

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
| [references/grant-own-skeleton.md](../personal/grant-own-skeleton.md) | **Voice B 写自己的标书**：立项五步、创新两栏、可行性三块、目标「确定/阐明/探讨」。评别人的国自不要打开本文件 |

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
   `04_analysis` / Loopnow, `calc-sample-size`).
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

When the user is **writing their own** 国自 / 开题 / 市科委 / 卫健委 / 院级 / 临床研究方案, open `grant-own-skeleton.md`. Do not use Voice A 评议口癖.

Compact contract (details in that file):

1. **立项五步**：负担+分型 → 主流学说及具体缺口 → 前期（文献+自己，至少两条链）→ 假说一句 → 本研究要做什么。小节标题用机制节点，不是方法名。
2. **创新两栏**：学术思想创新（往前推一步）+ 技术方法创新（针对立项里点名的技术缺口）。不要写「我们用了 MRI」。
3. **可行性三块**：模型成熟（点名造模/时间点）+ 平台点名到仪器 + 人（[PI]、SCI [n] 篇、在研基金）。临床另写病源「每年接诊 [疾病] 超过 [n] 例」。
4. **目标三档**：确定（有无变化/干预是否有效）/ 阐明（机制、谱、通路）/ 探讨（诊断分级、转化）。不要把探讨当唯一目标。
5. 句库（中英摘要、假说、入排）只从 `grant-writing.md` 取。方法升级写进立项 → `radiology-frontier`.

## Handoffs

- Frontier framing / is this direction novel & publishable → `radiology-frontier`.
- Sample size, EPV, power, Riley minimum sample size → `04_analysis` / Loopnow (`calc-sample-size`; lab notes `04_analysis/personal/methods.md`).
- Hand-crafted radiomics pipeline design → `04_analysis` (mounted `radiomics-ml`; lab rules `04_analysis/personal/pipeline.md`).
- Deep-learning architecture & training design → mounted `architecture-zoo` (`03_research`).
- ROI/mask annotation SOP → `02_data-processing` (mounted `preprocess-imaging`).
- Which checklist the design must satisfy → `05_manuscript` (mounted `check-reporting`).
- Ethics/consent/data-sharing feasibility → `03_research/personal/ethics.md`.
- Clinical-use scenario, reader study, prospective plan → `03_research/personal/clinical-translation/README.md`.
- Turning this design into **own** funding proposal (Voice B) → `grant-own-skeleton.md` + `grant-writing.md`（句库）. Method upgrades into 立项 → `radiology-frontier` `method-upgrade-into-grant.md`.
- Reviewing **other people's** NSFC/面上 (Voice A) → `../personal/grant-review.md`. Never mix those tics into own text.
- English journal peer review → `06_review`. Not this module.
- This skill plans research; it does not provide clinical or diagnostic recommendations.
