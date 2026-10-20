---
name: medical-research-orchestrator
description: >
  Intent-classify the task, run a skill chain, and close QC (file gates + local
  recovery). Use for end-to-end or multi-stage work. Do not use when a single
  domain skill is enough. Do not do literature, stats, writing, or review here.
---

# Medical Research Orchestrator

00 is the lab dispatcher. The live loop is **intent classify → skill chain → QC gate → local recovery**.
It does not duplicate research, statistical, imaging, writing, or discovery rules.

**唯一官方运行图：** [`runtime-flow.mmd`](runtime-flow.mmd)（读图说明 [`runtime-flow.md`](runtime-flow.md)）。入口 / QC / 局部回退以该图为准；更新流程时**只改这一张 mmd**。Gate 条文真源 [`gates.md`](gates.md)。图节点 `Gate · NN` ↔ `G-NN`。

**Seats (07_response owns response letters):** 03 Victor · 02+04 Loopnow · 05 Aitee · 06 Lee · 00 Aitor (QC) · 投稿+伦理表 Bai（`fill-protocol` 路径仍在 03；不进 00 主环）. Mid-entry allowed. Per-paper channel seats all six (max). Ownership: see `00_orchestrator/references/ownership-contract.md`. Do not mount MedSci `orchestrate` as a third SOP.

**Comments / conflicts:** Word author field always **A**. Prefix rules → `06_review/personal/review.md` §0. Mount vs lab conflict stays in the comment with an edit plan; **the user decides**.

**Citation / G-LIT:** before 05 done and inside every 06, 03 runs `03_research/personal/citation-verify.md`. 05 and 06 call/require 03 citation-verify — do not self-certify lit. Mid-entry does not waive it. On fail: dual plan in comments (revise/weaken/delete + optional further 03 search); prefer `05_manuscript/personal/process/evidence.md`. **00** decides at QC whether further search runs; **05** keeps Accept/Weaken/Delete on wording. Record `manuscript.citation_verify` in `templates/project-state.yaml`.

**Standing delivery:** [`references/standing-delivery.md`](references/standing-delivery.md).
**Project `ref/` layout:** [`references/project-ref-layout.md`](references/project-ref-layout.md).
**External executor monitoring:** [`references/handoff-monitor.md`](references/handoff-monitor.md).

## 1. Intent classify

Pick the smallest skill set. One bounded task → that domain skill, not 00.

### Directory detection (before asking)

Look in the working / 0RAD project folder. Echo one lock line when the artifact is clear.

| Artifact found | Implies |
|---|---|
| `settings.ini` | 0RAD project; 02 or 04, not a new scaffold |
| `*-results.html` | numbers exist; may enter `sci-manuscript` |
| `Manuscript_*_house.docx` | writing underway; 05, then maybe 06 |
| reviewer letter / 审稿意见 | `06_review` (review) or `07_response` (response letter) |
| imaging / ROI / features, no HTML | `radiomics-study` unless the user says otherwise |
| `ref/project-state.yaml` | read `pipeline.stage` and `qc`; do not re-init |

`*-results.html` and a reviewer letter in the same folder, and the user did not name the entry: ask which station. One bounded task still goes to that skill, not the full SOP.

If detection is unclear, ask **one** question or render **one** decision node. Never two in the same turn. (Plan-card exception: [`references/plan-and-grilling.md`](references/plan-and-grilling.md).)

**Plan card / flowchart approval / N1–N4:** [`references/plan-and-grilling.md`](references/plan-and-grilling.md). **Grilling policy:** MY-RULES `My rule.md` §2 (grilling). Never `--e2e`. N2 (PHI) applies before 02 tables or clinical extraction.

### Fast routing (single-skill)

SSOT: [`references/fast-routing.md`](references/fast-routing.md) (must match `route-contract.yaml`).

## 2. Skill chain

### Routing

Ids: `01_skill-integration` · `02_data-processing` · `03_research` · `04_analysis` · `05_manuscript` · `06_review` · `07_response`. Scope = each skill's `SKILL.md`. **Literature enters 03 only.** **Reviewer response enters 07 only** (`07_response`). No archive-as-standalone routes.

### Session mount pick

Every independent run needs a mount decision. If `mounts.session_picked_fine_ids` already covers the fine ids this task needs, reuse the session lock. Otherwise enter 01 and ask which `MOUNTED` fine ids to attach, then load only those. `PROPOSED` is not pickable. Do not auto-load all mounted ids. Personal layers are not a mount pick. A single-node personal-layer task with no mounted dependency does not ask.

**Auto-discovery:** only `00_orchestrator`–`07_response` (including nested A packs). `{mounts_cap}/**/SKILL.md` is cache — not a session skill unless its fine id is in `session_picked_fine_ids`. `.gitignore` excludes accidental in-repo `mounts-cap/` copies (SSOT cache outside repo).

**Mount → 评阅/润色 recipe:** when the user says 挂载 + 评阅/润色 on a `.docx`, follow [`references/mount-review-polish-recipe.md`](references/mount-review-polish-recipe.md).

### Composite workflows

SOPs in `workflows/` (ask which on 「全线」 / N1 unless directory detection locked it). `radiomics-study` stops at HTML and **offers** `sci-manuscript` (N3). `sci-manuscript` requires HTML. New capability → 01 skill-integration (registry proposal); never auto-mount. Writing/review SOP legs always require 03 citation-verify.

### Data-flow contract

| Node | Writes (must exist before next) | Next reads |
|---|---|---|
| 02 | analysis-ready table / aligned IDs | 04 |
| 04 | one `*-results.html` per endpoint | 05 (numbers **only** from HTML) |
| 05 | `Manuscript_<结局>_house.docx` | 06 |
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
| G-04 | after `*-results.html` |
| G-FACT | after 04 HTML; again after 05 house.docx; before 06 if numbers cited |
| G-05 | after house.docx |
| G-06 | after pre-review / re-review (not response; response → 07) |
| G-07 | after the response letter (entry 07); qc standards in `07_response/qc/` |
| G-LIT | citation-verify before 05 done and inside 06; on fail |
| G-CODE | code deep QC / refactor release-ready |

Cross-cut Consistency = **G-FACT**. Evolution QC → [`references/skill-evolution.md`](references/skill-evolution.md) (propose-only; Rules keeps the one-line gate).

**Local recovery:** re-run **only the broken node**; reuse session mount lock. Re-enter 01 only for missing dependency, stale provenance, or new capability. Max **3** rounds on the **same defect** (`defects[].rounds`), then `status: unresolved` and stop. Do not advance `pipeline.stage` or rerun correct stages. Prose repair → **word/sentence** units only. Visual: FAIL → Locate → Impact → Local/Rollback → Budget → Resume in [`runtime-flow.mmd`](runtime-flow.mmd).

**Close.** Write `pipeline.stage` from the template (`classify | 02 | 03 | 04 | 05 | 06 | qc | done`).

- 结束 / requested file on disk + last gate passed → `done`. Do not open the next SOP.
- 暂停 → leave `stage` at the current station; next session does not re-init.
- Stop after results / before pre-review → `04` or `05` (not `done`).

`intent → chain node → file check → integrity gate → localized defect → responsible skill → re-run that node (max 3) → gate → output`

## Research exploration

Triggers 「这个研究还能做什么」等 → [`workflows/research-exploration-loop.md`](workflows/research-exploration-loop.md). Not a fine id. 00 stays structural-only.

## Boundaries

**00 owns runtime decisions only:** schedule / route / pointers / flow order / QC. Domain knowledge stays in `02`–`07` (harvest for evolution). **Boundaries:** grilling policy → MY-RULES `My rule.md` §2 (grilling); Archify visualization → `04_analysis/personal/visualization/`.

**Lab SSOT:** [`references/lab-paths.yaml`](references/lab-paths.yaml). Do not vendor `0script` / `0doc`. Before adding to `00`: **runtime decision vs domain knowledge?**

Do not create a top-level skill for a disease, package, manuscript section, statistical test, metric, or imaging modality. Load selected `SKILL.md` then only required files. Mount ids: `MOUNTED_SKILLS.md` / `registry.yaml` — **this-run pick first** (01). 00 does not write prose, invent numbers, click 投稿, or absorb harvest/01 implementation.
