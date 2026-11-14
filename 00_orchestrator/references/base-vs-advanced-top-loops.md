# Three-layer contract: base thin protocol -> QC gate -> advanced revision

**Layer SSOT for this repo.** Diagram: [`../runtime-flow.mmd`](../runtime-flow.mmd) (reading guide [`../runtime-flow.md`](../runtime-flow.md)). Gates: [`../gates.md`](../gates.md). Ids / paths / counts: [`../registry.yaml`](../registry.yaml).
Owner lock 2026-10-30 (t1408u / t1409u); three-layer rewrite 2026-11-14 (t20261114d).

## 0 Scope and SSOT boundary

This file defines the three layers, the normative run order, and the handoffs. It restates nothing else:

- ids, paths, statuses, counts -> [`../registry.yaml`](../registry.yaml)
- routing rules -> [`fast-routing.md`](fast-routing.md) + [`../route-contract.yaml`](../route-contract.yaml)
- gate WHEN / PASS-FAIL / who repairs -> [`../gates.md`](../gates.md)
- harvest extraction procedure -> [`../harvest/SKILL.md`](../harvest/SKILL.md)

00 classifies, routes, gates, and re-gates. Domain rules live in 02-07; gate ownership lives in `qc/` standards plus 00. Neither side restates the other.

## 1 The three layers

| Layer | Role | Holds | Does not hold | Evolution rate |
|---|---|---|---|---|
| **base** (`NN_slug/base/`) | Thin protocol for one fine id | Mission; scope and out-of-scope; required inputs and what must be asked; workflow decision nodes; constraints (never rules); output and handoff card; LLM Discretion Envelope; pointers | Step recipes, tutorials, word bands, typography, full command blocks, lab numbers, personal voice, dated journal snapshots | Slow: only a framework defect or a genuinely superseded professional method |
| **qc** (`NN_slug/qc/`) | Gate standard: independently verifies base output | Check ids (QCS science / QCV style / QCP process); applicability; condition; required evidence; severity; verdict vocabulary; repair owner; recheck scope; the `advanced/` anchor to fix at | Task execution, capability teaching, a second fix recipe, personal style inside a science score | Fastest: driven by real missed checks, false positives, rework and new risk; one occurrence never becomes a general rule |
| **advanced** (`NN_slug/advanced/`) | Advanced revision authority | The owner's voice, personal structure locks, banned/preferred personal expressions, and confirmed personal working method; each row carries scope, priority (hard lock / default / optional) and source | General professional knowledge, full procedure manuals, science rules already in base or qc | Slow: repeat occurrence -> harvest candidate -> owner lock or task-verified |

Base is stable: an LLM capability upgrade replaces detail, not the contract. A base pack that grows a recipe has drifted. A hard constraint is never dropped for thinness: keep hard constraints verbatim and turn everything else into a pointer.

Discretion Envelope (inside every base contract): **Locked** (research definitions, raw data, ethics, PHI/patient isolation, data leakage, an already accepted analysis plan - never changed unilaterally); **Reasoned** (statistical method, evidence synthesis, mechanism explanation, model evaluation - derived from the current design with the reasoning written down); **Adaptive** (article structure, figure mix, analysis depth, presentation form - may follow the task).

## 2 Normative run order

`S0 -> S1 -> S2 -> (S3 as needed) -> S4 -> S5`. Do not merge S1 with S3 and do not run S3 before S2.

| Step | Owner | Does | Hands off (what / what not) |
|---|---|---|---|
| **S0 Classify** | 00 | Resolve fine id(s) from the registry, detect the project folder, list required inputs (data table, results, sources, protocol, manuscript version, target venue) | Routing card + missing-input list. Not a domain judgement or a draft |
| **S1 Base first pass** | specialist | Load the fine id's base contract plus base vocab layer names and load order; produce the first pass and an open-question / evidence map | First pass, unresolved inputs, evidence pointers. Not a self-declared "QC passed", not personal style, not advanced packs |
| **S2 Science QC** | 00 | Run QCS checks against required evidence (data table, results, sources, protocol), not against prose self-consistency | Per-check verdict (PASS / FAIL / WARN / UNVERIFIABLE / NOT_APPLICABLE), severity, evidence, repair owner. Not a rewrite, not a style score, not a merged total |
| **S3 Advanced revision** | specialist, only when needed | Apply the relevant advanced packs (voice, personal locks, confirmed personal method) to the S2 findings | Change list + one-line basis per change. Not a new scientific claim, analysis, or locked definition change |
| **S4 Incremental QC** | 00 | Re-check only the changed sections (recheck scope = row / section); enable **Style QC (QCV)** only when S3 ran or the owner asks for de-AI / polish | Changed-scope verdicts + optional style report. Not a second full-manuscript science review |
| **S5 Re-gate** | 00 | Four final checks: file integrity, number consistency, citation consistency, format; release or return the named node | Release decision + residual WARN / UNVERIFIABLE list |

Local recovery: re-run only the failing node; the same defect may roll back at most 3 times, then it escalates to the owner.

S2 -> S3 is the post-QC revise: base output is scored first, then revised via `advanced/`. Science QC (S2) and Style QC (S4) are separate scores; a style hit never becomes a science FAIL and never blocks a science gate.

## 3 Handoff contract

Every handoff names **to whom / what / what not**. Minimum set:

- S0 -> S1: routing card, inputs, open questions. Not a domain opinion.
- S1 -> S2: draft + evidence map. Not self-certification.
- S2 -> S3: failing checks + the `advanced/` anchor for each. Not a rewrite.
- S3 -> S4: diff + basis per change. Not a new claim.
- S4 -> S5: changed-scope verdicts + a separate style report. Not a merged score.

## 4 What 00 owns

- Owns: intent classification, fine-id pick, routing, the QC gate, local recovery, re-gate.
- Does not own: domain rules (02-07), the harvest extraction procedure ([`../harvest/SKILL.md`](../harvest/SKILL.md)), prose authority, or a second fix recipe.
- Gate ownership stays with the `qc/` standards plus 00: `qc/` says WHAT to check; [`../gates.md`](../gates.md) says WHEN / PASS-FAIL / who repairs. Specialists and the base first pass do not self-invoke `qc/`.

## 5 Drift rules

1. A base pack that carries a recipe, word band, typography detail, command block, lab number, or personal voice has drifted -> move it to that seat's `advanced/` (or delete it when it is generic knowledge) and leave a pointer.
2. A QC check that scores personal style as science has drifted -> split it into QCS and QCV; style never enters a science total and never blocks a science gate.
3. An advanced pack that teaches general professional knowledge has drifted -> it belongs in base or is simply deleted; "every medical researcher needs this" means it is not personal.
4. A check without `Evidence_required` cannot pass: use `UNVERIFIABLE`, never a silent PASS.
5. One occurrence never becomes a rule: base and QC changes need a repeated defect or a locked method; advanced needs repetition plus owner confirmation.
6. Layer names are `base`, `qc`, `advanced`. Do not reintroduce the retired `personal` layer name; "personal revision authority" is a role phrase only.

## 6 Pointers

- Acceptance matrix for this split (A/B/C arms, fixtures, metrics, pre-registered verdicts): `three-layer-acceptance-matrix.md`.

- Diagram: [`../runtime-flow.mmd`](../runtime-flow.mmd); reading guide [`../runtime-flow.md`](../runtime-flow.md).
- Gates: [`../gates.md`](../gates.md). Registry: [`../registry.yaml`](../registry.yaml). Run selection: [`session-pick.md`](session-pick.md). Harvest: [`../harvest/SKILL.md`](../harvest/SKILL.md).
- Base contracts: each `NN_slug/base/<fine-id>/MODULE.md`. QC standards: each `NN_slug/qc/`. Advanced packs: each `NN_slug/advanced/`.
