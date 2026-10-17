---
name: medical-manuscript-response
description: >
  Personal response-letter upper layer. Entry for response letter is 07.
  Final authority for point-by-point response and resolution status.
  Mounted revise / tighten-response / response-tone-polisher stay source=B.
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

Flow: B fine-ID first-pass (`revise` / `tighten-response` / `response-tone-polisher`) -> **00 QC** -> **A07** personal final authority.

Mounted packs may draft; **A 07 personal** owns resolution status and letter voice (`personal/response.md`).

## Personal assets

| Task | Path |
|---|---|
| Response letter voice + resolution protocol | `personal/response.md` |
| Route | `personal/route.md` |
| Handoff | `personal/handoff.md` |

## Mounted capability ids (bodies in B; source=B)

- `revise` -- point-by-point structure (B `06-review/review-response/`)
- `tighten-response` -- tightening principles (B)
- `response-tone-polisher` -- tone only; structure stays `revise` (B)

A07 is final authority for Resolved / Partially resolved / Unresolved / New issue and letter voice.

## Not this skill

- Pre-review / peer-review / re-review -> `06_review`
- Manuscript prose / polish -> `05_manuscript`
- Literature -> `03_research`
- Stats / figures -> `04_analysis`
