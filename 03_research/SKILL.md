---
name: medical-research-design-and-evidence
description: >
 Advanced research top layer: study design, literature, evidence, frontier,
 journal/topic selection, grants, translational/reader-study design.
 Triggers: literature, journal select, grants, ethics, study design, translation,
 reader study, lit-search, find-journal, fill-protocol.
 Literature enters here only -- never via another seat.
 Advanced layer is the 03 top authority (route/handoff/triggers), not a supplement-only folder.
 Manuscript prose -> 05. Review -> 06. Response -> 07. Stats -> 02.
---

# Research Design & Evidence -- advanced top layer

## Purpose

Turn a clinical/biomedical idea into a defensible protocol and evidence base.
**03 is the advanced top layer** (like 05/06): route, handoff, and post-QC triggers.
Ownership: see `00_orchestrator/references/ownership-contract.md`.
Capability **bodies** for lit/design fine ids live in **`03_research/base/`** (merged 2026-10-17).

## Layer model (2026-10-30 rebind)

**Flow:** base thin-contract first pass (`03_research/base/`: scope, bans, phase names, pointers) -> **00 QC** (score, cite the `advanced/` anchor) -> post-QC revise **via `03_research/advanced/`** -> re-gate at 00. May trigger `verify-refs` (integrity stage).
Layering and `qc/` invocation SSOT: `00_orchestrator/references/base-vs-advanced-top-loops.md`. Gates: `00_orchestrator/gates.md`. Checks: `qc/README.md`.

| Layer | Owns |
|---|---|
| `base/` | Thin contracts for lit-search, design-study, verify-refs, lit-fulltext, find-journal, fill-protocol; pack data (`rules/`, `data/`, `references/`) |
| 00 | QC gate; decides whether 03 re-triggers verify/retraction |
| `advanced/` | The recipe and the authority: citation-verify protocol, journal-selection SOP, radiology design, grants/ethics/intake/translation, Jinshan fill forms |

## Three pillars

See `advanced/route.md` for the full pointer table.

| Pillar | Owns |
|---|---|
| Evidence & literature | citation-verify, intro-evidence-pack, journal-selection SOP, lit-search (`base/`) |
| Design & exploration | radiology-design/frontier, ethics, intake, multicenter, grants, clinical-translation; ethics forms -> `03_research/base/fill-protocol/` (Bai) |
| Journal selection | 选刊走 03 `find-journal` — Victor seats `03_research/base/find-journal/` (list gates in base/; runtime pools in 0doc) |

## Literature rule

- Introduction evidence pack: on 05 cards -> `advanced/intro-evidence-pack.md`. Candidates only; 05 decides.
- **Literature research -> 03 only.** Do not route literature through 05 or 06.
- **Citation verify (required on writing and review).** G-CIT-1 before Gate 05; G-CIT-2 inside 06. See `advanced/citation-verify.md`. 05 and 06 call/require 03 citation-verify — do not self-certify lit.
- **Post-QC (03-triggered, bodies in `base/`):** when refs changed / G-LIT fail / 00 check (c) says needed -> run live `verify-refs` (integrity stage) and `lit-fulltext` when on the project-start chain.

## Advanced assets (top layer)

| Task | Path |
|---|---|
| Routing / handoff | `advanced/route.md`, `advanced/handoff.md` |
| Citation verify (advanced protocol) | `advanced/citation-verify.md` |
| Intro evidence pack | `advanced/intro-evidence-pack.md` |
| Journal-selection SOP | `advanced/journal-selection.md` |
| Grants / ethics / intake / multicenter / radiology | under `advanced/` |
| Clinical translation | `advanced/clinical-translation/` |
| Ethics forms | Bai seats `03_research/base/fill-protocol/`; Jinshan PHI in `advanced/fill-protocol/` |
| Find-journal pack | engine `03_research/base/find-journal/` |
| Question-to-reference spine | `00_orchestrator/workflows/question-to-reference.md` |

Do not rewrite live literature/systematic-review capability bodies inside these files.
Where a base pack carries a long procedure, the procedure belongs in `03_research/advanced/` and the base pack keeps the scope, bans, phase names, and pointer. A pack data library (`rules/`, `data/`, `references/`) stays where it is and is not the contract.

## Live capability ids (bodies under `NN_slug/base/`)

**This-run pick:** wait for the 00 session-fine-id pick. Registry fine-id menu (SSOT) = pick list.

Live fine ids in `00_orchestrator/registry.yaml` (e.g. `lit-search`, `design-study`, `verify-refs`, `lit-fulltext`).

**Post-QC 03-triggered:**

- `verify-refs` -- literature verify / cite hygiene
- `lit-fulltext` -- OA full-text gate after verify-refs

## Default research spine

`R1 Question -> R2 Evidence & Mechanism -> R3 Design -> R4 Data need -> R5 Research Brief`

Full rules: `00_orchestrator/workflows/question-to-reference.md`. 00 chooses mid-chain entry / rollback / STOP.

## Boundaries

- Manuscript prose -> `05_manuscript`
- Review -> `06_review`; Response -> `07_response`
- Statistics / figures -> `02_data-processing`
- Data prep -> `02_data-processing`
- Project journal lists -> `<project>/ref/` only
