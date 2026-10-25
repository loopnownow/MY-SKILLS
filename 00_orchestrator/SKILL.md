---
name: medical-research-orchestrator
description: >
  Intent-classify the task, run a skill chain, and close QC (file gates + local
  recovery). Also owns the routing index: fine-id registry, alias table, session
  picks, and composite SOPs. Use for end-to-end or multi-stage work. Do not use
  when a single domain skill is enough. Do not do literature, stats, writing, or
  review here.
---

# Medical Research Orchestrator

00 is the lab dispatcher. The live loop is **intent classify → skill chain → QC gate → local recovery**.
It does not duplicate research, statistical, imaging, writing, or discovery rules.

**Sole official runtime map:** [`runtime-flow.mmd`](runtime-flow.mmd) (how to read the map [`runtime-flow.md`](runtime-flow.md)). Entry / QC / local rollback follow this diagram; when updating the flow **edit only this one mmd**. Gate text SSOT [`gates.md`](gates.md). Diagram nodes `Gate · NN` ↔ `G-NN`.

**Seats (07_response owns response letters):** 03 Victor · 02 Loopnow · 05 Aitee · 06 Lee · 00 Aitor (QC) · portal submit + ethics forms Bai (`fill-protocol` path stays under 03; off 00 main loop). Mid-entry allowed. Per-paper channel seats all six (max). Ownership: see `00_orchestrator/references/ownership-contract.md`. Do not adopt an external `orchestrate` pack as a third SOP.

**Comments / conflicts:** Word author field always **A**. Prefix rules → `06_review/personal/review.md` §0. Assistant vs lab conflict stays in the comment with an edit plan; **the user decides**.

**Citation / G-LIT:** before 05 done and inside every 06, 03 runs `03_research/personal/citation-verify.md`. 05 and 06 call/require 03 citation-verify — do not self-certify lit. Mid-entry does not waive it. On fail: dual plan in comments (revise/weaken/delete + optional further 03 search); prefer `05_manuscript/personal/process/evidence.md`. **00** decides at QC whether further search runs; **05** keeps Accept/Weaken/Delete on wording. Record `manuscript.citation_verify` in `templates/project-state.yaml`.

**Standing delivery:** [`references/standing-delivery.md`](references/standing-delivery.md).
**Project `ref/` layout:** [`references/project-ref-layout.md`](references/project-ref-layout.md).
**External executor monitoring:** [`references/handoff-monitor.md`](references/handoff-monitor.md).

## 0 Index & registry

00 owns the routing index. The former `01_skill-integration` seat retired here on 2026-10-25: **coarse id = execution seat** (`02_data-processing` · `03_research` · `05_manuscript` · `06_review` · `07_response`). A fine id carries **no** coarse field — its bucket is its `a_domain`, so a bucket cannot drift from its seat. Bodies stay in-repo under `NN_slug/base/` (`source: my-skills`); this seat only indexes, routes, and gates.

| File | Role |
|---|---|
| [`registry.yaml`](registry.yaml) | fine-id SSOT: `coarse_ids` = the five seats, `fine_ids` (status `LIVE`), `local_packs` |
| [`legacy_aliases.yaml`](legacy_aliases.yaml) | alias → canonical id; retired fine ids, retired buckets, retired 01 seat |
| [`references/id-rules.md`](references/id-rules.md) | canonical ID rule |
| [`references/session-pick.md`](references/session-pick.md) | this-run pick, resolution order, empty-path protocol |
| [`references/hard-rules.md`](references/hard-rules.md) | forbidden combinations, fine-id expansion |
| [`references/lifecycle-cache.md`](references/lifecycle-cache.md) | deploy sync after merge; one clone, no second runtime tree |
| [`references/capability-contract.example.yaml`](references/capability-contract.example.yaml) | example contract for a new pack (proposal side) |
| [`workflows/`](workflows/README.md) | 5 composite SOPs + README |

Registry edits are propose-only: a proposal here, the user confirms. Never auto-add. Never change `registry.yaml` because one run wanted a path that is not indexed.

## 1. Intent classify

Pick the smallest skill set. One bounded task → that domain skill, not 00.

### Directory detection (before asking)

Look in the working project folder. Echo one lock line when the artifact is clear.

| Artifact found | Implies |
|---|---|
| `settings.ini` | lab project; 02, not a new scaffold |
| `*-results.html` | numbers exist; may enter `sci-manuscript` |
| `Manuscript_*_house.docx` | writing underway; 05, then maybe 06 |
| reviewer letter / reviewer comments | `06_review` (review) or `07_response` (response letter) |
| imaging / ROI / features, no HTML | `statistics` unless the user says otherwise |
| `ref/project-state.yaml` | read `pipeline.stage` and `qc`; do not re-init |

`*-results.html` and a reviewer letter in the same folder, and the user did not name the entry: ask which station. One bounded task still goes to that skill, not the full SOP.

If detection is unclear, ask **one** question or render **one** decision node. Never two in the same turn. (Plan-card exception: [`references/plan-and-grilling.md`](references/plan-and-grilling.md).)

**Plan card / flowchart approval / N1–N4:** [`references/plan-and-grilling.md`](references/plan-and-grilling.md). **Grilling policy:** MY-RULES `My rule.md` §2 (grilling). Never `--e2e`. N2 (PHI) applies before 02 tables or clinical extraction.

### Fast routing (single-skill)

SSOT: [`references/fast-routing.md`](references/fast-routing.md) (must match `route-contract.yaml`).

## 2. Skill chain

### Routing

Ids: `02_data-processing` · `03_research` · `05_manuscript` · `06_review` · `07_response`; `00_orchestrator` is this control plane (registry, flow order, QC), not a domain seat. Scope = each skill's `SKILL.md`. **Literature enters 03 only.** **Reviewer response enters 07 only** (`07_response`). No archive-as-standalone routes.

### Session fine-id pick

Every independent run needs a fine-id pick. If `fine_ids.session_picked_fine_ids` already covers the fine ids this task needs, reuse the session lock. Otherwise read [`registry.yaml`](registry.yaml) and ask which `LIVE` fine ids to attach, then load only those. `PROPOSED` is not pickable. Do not auto-load all live ids. Personal layers are not a fine-id pick. A single-node personal-layer task with no live dependency does not ask.

**Auto-discovery:** only `00_orchestrator`–`07_response` (including nested packs).

**Review / polish on a `.docx`:** follow [`references/fine-id-review-polish-recipe.md`](references/fine-id-review-polish-recipe.md).

### Composite workflows

SOPs in `workflows/` (ask which on "full-pipeline" / N1 unless directory detection locked it). `statistics` stops at HTML and **offers** `sci-manuscript` (N3). `sci-manuscript` requires HTML. New capability → registry proposal in this seat (§0); never auto-add. Writing/review SOP legs always require 03 citation-verify.

### Data-flow contract

| Node | Writes (must exist before next) | Next reads |
|---|---|---|
| 02 (data) | analysis-ready table / aligned IDs | 02 (stats) |
| 02 (stats) | one `*-results.html` per endpoint | 05 (numbers **only** from HTML) |
| 05 | `Manuscript_<endpoint>_house.docx` | 06 |
| 06 | pre-review / re-review; inventable items = questions | user, then 05 for sentences |
| 07 | response letter / resolution status | user, then 05 for sentences |
| 00 | `ref/project-state.yaml` + last `handoff.yaml` | every later node |

Copy `templates/handoff.yaml` at each skill crossing. Fill only known fields. Never invent n, AUC, PMID, or ethics IDs.

### Post-skill file check

After each node, verify the expected output **file exists and is non-empty**. Missing → do not start the next skill. Log on `qc` / `defects` in `project-state.yaml`. Template: `templates/project-state.yaml`.

## 3. QC closed loop

00 owns the last gate. Fail criteria: [`gates.md`](gates.md). Complete only when the requested deliverable exists, major consistency checks pass, assumptions/limitations are visible, and files are usable.

| Gate | When |
|---|---|
| G0 | every run |
| G-PHI | before 02 tables / extraction |
| G-STATS | after `*-results.html` |
| G-FACT | after 02 HTML; again after 05 house.docx; before 06 if numbers cited |
| G-05 | after house.docx |
| G-06 | after pre-review / re-review (not response; response → 07) |
| G-07 | after the response letter (entry 07); qc standards in `07_response/qc/` |
| G-LIT | citation-verify before 05 done and inside 06; on fail |
| G-CODE | code deep QC / refactor release-ready |

Cross-cut Consistency = **G-FACT**. Evolution QC → [`references/skill-evolution.md`](references/skill-evolution.md) (propose-only; Rules keeps the one-line gate). Harvest intake → that file, section «Harvest task flow»; collection SSOT `{doc_skill_harvest}\HARVEST-STANDARD.md` (extract ≠ promote).

**Local recovery:** re-run **only the broken node**; reuse session fine-id lock. Re-read the registry here only for a missing dependency, stale provenance, or a new capability. Max **3** rounds on the **same defect** (`defects[].rounds`), then `status: unresolved` and stop. Do not advance `pipeline.stage` or rerun correct stages. Prose repair → **word/sentence** units only. Visual: FAIL → Locate → Impact → Local/Rollback → Budget → Resume in [`runtime-flow.mmd`](runtime-flow.mmd).

**Close.** Write `pipeline.stage` from the template (`classify | 02 | 03 | 05 | 06 | qc | done`).

- end / requested file on disk + last gate passed → `done`. Do not open the next SOP.
- pause → leave `stage` at the current station; next session does not re-init.
- Stop after results / before pre-review → `02` or `05` (not `done`).

`intent → chain node → file check → integrity gate → localized defect → responsible skill → re-run that node (max 3) → gate → output`

## Research exploration

Triggers 「这个研究还能做什么」 (what else can this study do) and peers → [`workflows/research-exploration-loop.md`](workflows/research-exploration-loop.md). Not a fine id. 00 stays structural-only.

## Boundaries

**00 owns runtime decisions only:** schedule / route / pointers / flow order / QC. Domain knowledge stays in `02`–`07` (harvest for evolution). **Boundaries:** grilling policy → MY-RULES `My rule.md` §2 (grilling); visualization → `02_data-processing/personal/visualization/`.

**Lab SSOT:** [`references/lab-paths.yaml`](references/lab-paths.yaml). Do not vendor `0doc\_code` / `0doc`. Env: prefer `STATS_ROOT` / `ODOC_CODE`; `OSCRIPT_ROOT` is retired (do not recreate `script_root`). Before adding to `00`: **runtime decision vs domain knowledge?**

Do not create a top-level skill for a disease, package, manuscript section, statistical test, metric, or imaging modality. Load selected `SKILL.md` then only required files. Fine ids: [`registry.yaml`](registry.yaml) — **this-run pick first**. 00 does not write prose, invent numbers, click submission, or absorb harvest implementation.
