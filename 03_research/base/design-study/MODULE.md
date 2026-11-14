---
name: "design-study"
domain: "03_research"
trigger: ["研究设计", "可行性", "imaging feasibility", "样本量"]
inputs: ["clinical_question", "modality", "cohort_sketch"]
outputs: ["design_blueprint", "blocking_risks"]
tools: ["checklist"]
quality_control: "patient-level split; no slice-level external validation"
owner: "03_research/base/design-study/MODULE.md"
---

trigger is documentation only; not independently discoverable.

# Imaging Study Design & Feasibility

Contract only for design-study (protocol spine): scope, bans, phase names, and pointers. The house working method and the revision authority live in `03_research/advanced/`; this file does not restate a procedure. Pack data (`references/`) stays beside it as data.

Former pack names that resolved into this seat are retired aliases only — see `00_orchestrator/legacy_aliases.yaml`; do not reopen those trees.

Use this skill at the **front of the research chain**: someone has imaging data (and maybe clinical/pathology/molecular labels) but no settled study. It triages **feasibility** and converts a feasible idea into a **complete, submittable design**.

## Mission

(1) Decide whether the data can support a credible study at all; (2) turn a feasible idea into a design with clinical question, population, endpoint, methods and a validation strategy. Clinical question and validation are the spine; the algorithm is not the study.

## Scope / Out of scope

In: feasibility verdict, design blueprint, validation plan, pre-stats design lock, roadmap when program-level.
Out: sample size / power (`calc-sample-size`), formal statistics (`stats-analysis`), reporting-guideline checklists (`05_manuscript/qc/check-reporting/`), imaging preprocessing (`preprocess-imaging`).

## Input

Minimum: clinical question, modality, cohort sketch (n patients, centers, label source, event count, follow-up). Read `ref/refer/` first, then project tables. Missing ethics approval dates, n, events, or center counts: ask; never infer. Before fixing the collection window, check `03_research/advanced/ethics.md` § Ethics validity period.

## Workflow (decision nodes)

1. **Inventory the data** — disease, modality, n (patients/lesions), centers/scanners, label source, masks, follow-up/events, time span; mark unknowns.
2. **Feasibility triage** → verdict: `Feasible as designed` / `Feasible with changes` / `Feasibility study only` / `Not yet — collect X first`. Detail: [references/feasibility-triage.md](references/feasibility-triage.md).
3. **Define question and estimand** — question → population → primary endpoint → comparator → clinical-use scenario. House method: `03_research/advanced/design/endpoints-and-estimands.md`.
4. **Pick the blueprint** — minimum-viable vs stronger, with cost; then fidelity check (one design name in four places, case-control's three parts, reporting guideline, sampling window, selection bias, ethics coverage). House templates: `03_research/advanced/design/study-blueprints.md`; fidelity detail: [references/design-fidelity.md](references/design-fidelity.md).
5. **Design validation** — patient-level split, internal scheme, external/temporal/geographic/multi-center plan; define honestly what "external" means. Detail: [references/validation-strategy.md](references/validation-strategy.md).
6. **Name the binding constraint** and hand n/EPV to `calc-sample-size`.
7. **Write results** to `ref/design-study.md` (template: [references/design-study-result.md](references/design-study-result.md)) — never leave the blueprint only in chat.
8. **Write the pre-stats lock** to `ref/design-lock.md` (template: [references/design-lock.md](references/design-lock.md)): keywords, gap pointing at `ref/refer`, testable hypothesis, three citation classes (gold standard / last-5-year work / latest guideline with body+year), inclusion-exclusion, statistical path. Mark unknowns; never invent n, ethics IDs, citations or results. **Formal statistics start only after the owner accepts this file (`done` is not `accepted`).**
9. **Program-level plans** (12–24-month AI/radiogenomics route) follow the house roadmap in `03_research/advanced/design/ai-radiogenomics-12-24-roadmap.md`; do not copy a generic roadmap into base.

## Constraints (never)

- Never invent cohort numbers, event counts, center counts, ethics IDs, citations or results.
- Never call an internal cross-validation "external"; never claim a capability the data cannot support.
- Never start formal statistics before an owner-accepted `ref/design-lock.md`.
- Never retro-fit the question to a result; pre-specify endpoint, primary analysis and split.
- If the honest answer is "not yet — do X first", say that instead of a design.

## Output contract

1. Feasibility verdict + one-line reason. 2. Data read with the binding constraint surfaced. 3. Blueprint (question, population, endpoint/estimand, comparator, clinical-use scenario, design type). 4. Method options (minimum-viable vs stronger, trade-off, reporting guideline). 5. Validation plan with the honest "external" definition. 6. Roadmap when relevant. 7. Next actions in priority order. 8. `ref/design-study.md` written. 9. `ref/design-lock.md` with six sections complete or explicitly unknown, owner acceptance recorded.

## Handoffs

- Pre-stats lock → `stats-analysis` starts only after owner acceptance.
- Sample size / EPV / Riley → `calc-sample-size`.
- Deep-learning architecture → `03_research/advanced/`; clinical translation / reader study → `03_research/advanced/clinical-translation/`.
- Ethics feasibility → `write-paper` radiology-ethics (placeholders only); reporting checklist → `05_manuscript/qc/check-reporting/`.
- English peer review → `peer-review`. This skill plans research; it gives no clinical or diagnostic recommendations.
