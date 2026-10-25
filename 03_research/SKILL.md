---
name: medical-research-design-and-evidence
description: >
 Personal research top layer: study design, literature, evidence, frontier,
 journal/topic selection, grants, translational/reader-study design.
 Triggers: literature, journal select, grants, ethics, study design, translation,
 reader study, lit-search, find-journal, fill-protocol.
 Literature enters here only -- never via 01.
 Personal layer is the 03 top authority (route/handoff/triggers), not a supplement-only folder.
 Manuscript prose -> 05. Review -> 06. Response -> 07. Stats -> 02.
---

# Research Design & Evidence -- personal top layer

## Purpose

Turn a clinical/biomedical idea into a defensible protocol and evidence base.
**03 is the personal top layer** (like 05/06): route, handoff, and post-QC triggers.
Ownership: see `00_orchestrator/references/ownership-contract.md`.
Capability **bodies** for lit/design mounts live in **A `03_research/base/`** (merged 2026-10-17).

## Layer model (2026-10-17)

**Flow:** lit/design fine-ID **first-pass** (`base/` bodies) -> **00 QC** -> **03** top-layer re-loops

**QC standards:** live in `qc/` and are invoked only by `00_orchestrator` at Gate time (not by the specialist during first-pass). See `qc/README.md`.
(may trigger `verify-refs` + `retraction-watcher`; bodies under A `03_research/base/`).

| Layer | Owns |
|---|---|
| `base/` | lit-search, design-study mounts, verify-refs, retraction-watcher, other 03 capability bodies under `03_research/base/` |
| 00 | QC gate; decides whether 03 re-triggers verify/retraction |
| 03 | Personal route/handoff/authority; citation-verify personal protocol; grants/ethics/intake/translation personal files; post-QC trigger of verify-refs / retraction-watcher (bodies in `base/`) |

## Three pillars

See `personal/route.md` for the full pointer table.

| Pillar | Owns |
|---|---|
| Evidence & literature | citation-verify, intro-evidence-pack, journal-selection SOP, lit-search (`base/`) |
| Design & exploration | radiology-design/frontier, ethics, intake, multicenter, grants, clinical-translation; ethics forms -> A `03_research/base/fill-protocol/` (Bai) |
| Journal selection | 选刊走 03 `find-journal` — Victor seats A `03_research/base/find-journal/` (list gates in base/; runtime pools in 0doc) |

## Literature rule

- Introduction evidence pack: on 05 cards -> `personal/intro-evidence-pack.md`. Candidates only; 05 decides.
- **Literature research -> 03 only.** Do not route literature through 01 or 05.
- **Citation verify (required on writing and review).** G-CIT-1 before Gate 05; G-CIT-2 inside 06. See `personal/citation-verify.md`. 05 and 06 call/require 03 citation-verify — do not self-certify lit.
- **Post-QC (03-triggered, bodies in `base/`):** when refs changed / G-LIT fail / 00 check (c) says needed -> run mounted `verify-refs` and `retraction-watcher`.

## Personal assets (top layer)

| Task | Path |
|---|---|
| Routing / handoff | `personal/route.md`, `personal/handoff.md` |
| Citation verify (personal protocol) | `personal/citation-verify.md` |
| Intro evidence pack | `personal/intro-evidence-pack.md` |
| Journal-selection SOP | `personal/journal-selection.md` |
| Grants / ethics / intake / multicenter / radiology | under `personal/` |
| Clinical translation | `personal/clinical-translation/` |
| Ethics forms | Bai seats A `03_research/base/fill-protocol/`; Jinshan PHI in `personal/fill-protocol/` |
| Find-journal pack | engine `03_research/base/find-journal/` |
| Question-to-reference spine | `01_skill-integration/workflows/question-to-reference.md` |

Do not rewrite mounted literature/systematic-review capability bodies inside these files.
Where an A personal file only duplicates a long base procedure, prefer a short pointer to base (no bulk-move this round).

## Mounted capability ids (bodies under `NN_slug/base/`)

**This-run pick:** wait for 01 session-mount pick. Registry mount menu (SSOT) = pick list.

Live fine ids in `01_skill-integration/registry.yaml` (e.g. `lit-search`, `design-study`, `verify-refs`, `retraction-watcher`).

**Post-QC 03-triggered:**

- `verify-refs` -- literature verify / cite hygiene
- `retraction-watcher` -- retraction check

## Default research spine

`R1 Question -> R2 Evidence & Mechanism -> R3 Design -> R4 Data need -> R5 Research Brief`

Full rules: `01_skill-integration/workflows/question-to-reference.md`. 00 chooses mid-chain entry / rollback / STOP.

## Boundaries

- Manuscript prose -> `05_manuscript`
- Review -> `06_review`; Response -> `07_response`
- Statistics / figures -> `02_data-processing`
- Data prep -> `02_data-processing`
- Project journal lists -> `<project>/ref/` only
