---
name: research-exploration-loop
description: >
  00 sub-component (not a fine id): state-aware exploration under the orchestrator.
  Detect completed / uncertain / missing work; dispatch existing 03/04 (and 05/06 when needed);
  forbid pointless re-runs of reusable completed work. Structural QC only in 00;
  content judgment stays with specialists / fine ids.
triggers: ["这个研究还能做什么", "这个结果怎么解释", "还缺哪些文献", "研究空白", "选题探索"]
owner: 00_orchestrator
type: 00-sub-component
---

# research-exploration-loop

## 0. Positioning

Belongs under `00_orchestrator`. **Not** a registry fine id (v4 52-id ceiling). **Not** a new coarse id.

> **00 = State + Gate (structural) + Route + Resume + Loop counts**  
> **00 never judges medical content** — only whether required fields exist, trace pointers are present, and reported confidence clears a threshold.

Content (claim fidelity, population/endpoint differences, hedge wording) is delegated to 03/04/05/06. 00 only consumes `pass|fail + confidence` and continues routing.

Do **not** invent fine ids such as `pubmed-search` / `literature-review` / `hypothesis-generation`. Use live mounts: `lit-search`, `frontier-hypothesize`, `find-cohort-gap`, `verify-refs`, and 04 stats fine ids.

```text
00_orchestrator
│
├── workflows/radiomics-study.md
├── workflows/sci-manuscript.md
└── workflows/research-exploration-loop.md   ← this SOP
       │
       ├── detect-entry
       ├── detect-gap
       ├── resume-from-state
       ├── reuse-completed-work
       ├── dispatch-existing-skills
       ├── local-rework (L1 = existing gate recovery, max 3)
       ├── cross-stage-loop (L2)
       └── stop-or-handoff
```

## 1. Entry — detect-entry

Read `<project>/ref/project-state.yaml` (template: `../templates/project-state.yaml`). Do not assume the user starts at day one.

Structural fields 00 may compute itself:

- `trace_ok` — every claim in that stage has a PMID/DOI/path pointer (presence only; not correctness).
- `classification_confidence` — numeric confidence reported by a specialist for a gap/novelty classification (threshold check only).

**Resume point** = first stage with `status != complete`, or `trace_ok == false`, or `classification_confidence` below threshold (default **0.6**, calibrate later).

Optional sketch (illustrative):

```yaml
project_state:   # existing file; exploration uses exploration_state below
  study_design:
    question: { status: complete }   # or keep as free text + derive status in exploration_state
exploration_state:
  stages:
    literature_search: { status: complete }
    evidence_extraction: { status: complete, trace_ok: true }
    synthesis: { status: complete, trace_ok: true }
    gap: { status: partial, classification_confidence: 0.42 }
    hypothesis: { status: not_started }
    method: { status: not_started }
    data: { status: not_started }
    writing: { status: not_started }
    review: { status: not_started }
```

Prefer mapping onto existing `pipeline.stage` / `study_design` / `manuscript` when possible; use `exploration_state` for loop-specific counters only.

## 2. Gap detect + evidence types

From evidence extraction onward, each evidence row should carry:

```yaml
evidence_type: guideline | primary_study | review | meta_analysis
```

**Freshness (locked):**

- Only `guideline` enters freshness checks. `primary_study` / `review` / `meta_analysis` stay `reusable`; old ≠ wrong.
- Freshness is **just-in-time**: verify once when that guideline is about to be used for method advice or Discussion — no polling.
- Guideline refresh is a single-item replace and **does not** spend L1/L2 budget unless the new version invalidates downstream hypothesis/Discussion (then one L1 rework counts toward the 3-cap).
- Non-guideline "outdated" never triggers. A `primary_study` is invalidated only by **contradiction** (new conflicting evidence) — a separate back-edge, not "outdated".

## 3. Reuse completed work

```yaml
exploration_state:
  completed: []
  uncertain: []
  missing: []
  invalidated: []
  reusable: []
```

Rule: `completed + trace_ok + reusable` → **do not** re-run without cause.

Unlock re-call of upstream skills only on:  
`QC failure` | `evidence outdated (guideline only)` | `new question` | `contradiction` | `new result` | `reviewer request` | `novelty failure` (reported by 03, not a new gate id).

## 4. Dispatch existing skills (no new pipeline nodes)

When the missing work is **research content** (question / evidence / design / data need / planning brief), dispatch **03** on [`../../03_research/workflows/question-to-reference.md`](../../03_research/workflows/question-to-reference.md) at the right **R1–R5** stage. 00 still chooses entry and STOP; 03 fills the cards.


| Gap type | Layer | Live fine ids / paths (examples) | Question answered |
|---|---|---|---|
| Evidence Discovery | 03 | `lit-search` (P1); optional `paper-lookup` if session-picked | What literature is still missing? |
| Evidence Reasoning | 03 | `verify-refs` + Victor evidence cards; consistency via **G-FACT** / **G-LIT** | What do these studies claim (claim→source→population→endpoint→effect→conflict)? |
| Gap / Hypothesis | 03 | `frontier-hypothesize`, `find-cohort-gap` | What new question is worth asking? |
| Methodological Feasibility | 04 | existing 04 stats / sample-size / design personal | Can this idea be studied with our methods? |

Writing / review exploration handoffs use 05 / 06 only when the gap is wording or reviewer-facing — not for inventing methods.

**No new external source in this CHG.** Absorbing third-party scoring (e.g. idea-generation) requires license + grilling and must land inside existing `frontier-hypothesize` / B scripts — **not** a new fine id.

## 5. QC — structural in 00, content in specialists

00 structural checks only (field presence / pointer presence / confidence threshold).

If `classification_confidence < 0.6` → do not dispatch; ask the user.

Content checks (claim fidelity, population/endpoint/mechanism differences, hedges) → package context to 03/04 (or 05/06). 00 routes on their `pass|fail + confidence`. **Do not invent gate ids** `G-NOVEL` / `G-CONSIST`; use existing `G-FACT`, `G-LIT`, and specialist validators.

## 6. Loop control

### L1 — local QC (existing)

Same as `gates.md` QUALITY recovery: fail → responsible node only → max **3** → `unresolved`. No full-chain rerun.

### L2 — cross-stage exploration (new)

```yaml
exploration_state:
  l2_iteration_count: 0
  hop_history: []
  status: running | stalled | resolved
```

1. **One global counter** for any cross-stage hop (population / endpoint / mechanism / methodology) — no per-branch counters.
2. **Oscillation warning before budget burn:** if the same pair appears twice in `hop_history` (e.g. `gap→evidence→gap→evidence`), warn / prefer early stop — do not wait for the third spend.
3. **Cap 3.** Then `status: stalled`, partial closed-loop report, human decide whether to add budget or change direction.

## 7. Stop or handoff

- `resolved` — return to the calling Main Pipeline node (03→04→05→06 as appropriate).
- `stalled` — L2 cap or oscillation; partial report; human.
- `handoff` — missing work outside this loop → normal coarse routing (02–06).

## 8. Interfaces

- Extend `project-state.yaml` with optional top-level `exploration_state` (see template). Do not fork a second state schema.
- Record changes with `CHG-YYYYMMDD-NNN`.
- External absorb still: license → file diff → extract action/rules only → no whole-pack mount; respect Cache ≠ Mount ≠ Active and the 52 fine-id ceiling.
