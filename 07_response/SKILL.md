---
name: medical-manuscript-response
description: >
  Personal response-letter upper layer. Entry for response letter is 07.
  Final authority for point-by-point response and resolution status.
  Mounted revise / tighten-response use source my-skills under A `07_response/base/`.
  Tone-only polish is an on-demand mode of tighten-response. Point-by-point structure stays revise.
  Re-review stays in 06. Prose Track Changes to 05. Literature to 03.
---

# Manuscript Response -- personal upper layer

**Route:** `personal/route.md`. **Handoff:** `personal/handoff.md`.

## Purpose

Draft and adjudicate point-by-point response letters and resolution status.
Never invent rescue experiments, missing AUCs, ethics IDs, or unrun analyses.
Do not rewrite the manuscript here -- changed sentences go to `05_manuscript`.
Ownership: see `00_orchestrator/references/ownership-contract.md`.

**Response enters through `07_response` only** (not 06).

## Layer model

Flow: fine-ID first-pass (`revise` / `tighten-response`; bodies in A `07_response/base/`) -> **00 QC** -> **A07** personal final authority.

**QC standards:** live in `qc/` and are invoked only by `00_orchestrator` at Gate time (not by the specialist during first-pass). See `qc/README.md`.

Mounted packs may draft; **A 07 personal** owns resolution status and letter voice (`personal/response.md`).

## Personal assets

| Task | Path |
|---|---|
| Response letter voice + resolution protocol | `personal/response.md` |
| Route | `personal/route.md` |
| Handoff | `personal/handoff.md` |

## Mounted capability ids (bodies in A `base/`; source my-skills)

- `revise` -- point-by-point structure (A `07_response/base/revise/`)
- `tighten-response` -- tightening plus on-demand tone-polish (A `07_response/base/tighten-response/`). Legacy alias `response-tone-polisher` was absorbed here; structure stays `revise`.

A07 is final authority for Resolved / Partially resolved / Unresolved / New issue and letter voice.

**Exit gate: G-07** (defined in `00_orchestrator/gates.md`; class QUALITY). Every response point is either resolved with a traced manuscript change or recorded as unresolved; the letter must not claim a fix that the manuscript does not contain. 00 runs the gate; a FAIL loops back here for local rework.

## Not this skill

- Pre-review / peer-review / re-review -> `06_review`
- Manuscript prose / polish -> `05_manuscript`
- Literature -> `03_research`
- Stats / figures -> `04_analysis`
