---
name: medical-research-design-and-evidence
description: >
  Personal research top layer: study design, literature, evidence, frontier,
  journal/topic selection, grants, translational/reader-study design.
  Triggers: literature, journal select, grants, ethics, study design, translation,
  reader study, lit-search, find-journal, fill-protocol.
  Literature enters here only -- never via 01.
  Personal layer is the A03 top authority (route/handoff/triggers), not a supplement-only folder.
  Manuscript prose -> 05. Review -> 06. Response -> 07. Stats -> 04.
---

# Research Design & Evidence -- personal top layer

## Purpose

Turn a clinical/biomedical idea into a defensible protocol and evidence base.
**A03 is the personal top layer** (like A05/A06): route, handoff, and post-QC triggers.
Capability **bodies** for lit/design mounts stay in **B**.

## Layer model (2026-10-17)

**Flow:** B lit/design fine-ID **first-pass** -> **00 QC** -> **A03** top-layer re-loops
(may trigger `verify-refs` + `retraction-watcher`; bodies executed in B).

| Layer | Owns |
|---|---|
| B | lit-search, design-study mounts, verify-refs, retraction-watcher, other 03-research capability bodies |
| 00 | QC gate; decides whether A03 re-triggers verify/retraction |
| A03 | Personal route/handoff/authority; citation-verify personal protocol; grants/ethics/intake/translation personal files; post-QC trigger of B verify-refs / retraction-watcher |

## Three pillars

See `personal/route.md` for the full pointer table.

| Pillar | Owns |
|---|---|
| Evidence & literature | citation-verify, intro-evidence-pack, journal-selection SOP, lit-search (mounted B) |
| Design & exploration | radiology-design/frontier, ethics, intake, multicenter, grants, clinical-translation; ethics forms -> `fill-protocol/` |
| Journal selection | `find-journal/` (list gates in-repo; runtime pools in 0doc) |

## Literature rule

- Introduction evidence pack: on 05 cards -> `personal/intro-evidence-pack.md`. Candidates only; 05 decides.
- **Literature research -> 03 only.** Do not route literature through 01 or 05.
- **Citation verify (required on writing and review).** G-CIT-1 before Gate 05; G-CIT-2 inside 06. See `personal/citation-verify.md`.
- **Post-QC (A03-triggered, bodies in B):** when refs changed / G-LIT fail / 00 check (c) says needed -> run mounted `verify-refs` and `retraction-watcher`.

## Personal assets (top layer)

| Task | Path |
|---|---|
| Routing / handoff | `personal/route.md`, `personal/handoff.md` |
| Citation verify (personal protocol) | `personal/citation-verify.md` |
| Intro evidence pack | `personal/intro-evidence-pack.md` |
| Journal-selection SOP | `personal/journal-selection.md` |
| Grants / ethics / intake / multicenter / radiology | under `personal/` |
| Clinical translation | `personal/clinical-translation/` |
| Ethics forms | `fill-protocol/` |
| Find-journal pack | `find-journal/` |
| Question-to-reference spine | `workflows/question-to-reference.md` |

Do not rewrite mounted B literature/systematic-review capability bodies inside these files.
Where an A personal file only duplicates a long B procedure, prefer a short pointer to B (no bulk-move this round).

## Mounted capability ids (bodies in B)

**This-run pick:** wait for 01 session-mount pick. Registry MOUNTED = menu.

Live fine ids in `01_skill-integration/registry.yaml` (e.g. `lit-search`, `design-study`, `verify-refs`, `retraction-watcher`).

**Post-QC A03-triggered (bodies stay B):**

- `verify-refs` -- literature verify / cite hygiene
- `retraction-watcher` -- retraction check

## Default research spine

`R1 Question -> R2 Evidence & Mechanism -> R3 Design -> R4 Data need -> R5 Research Brief`

Full rules: `workflows/question-to-reference.md`. 00 chooses mid-chain entry / rollback / STOP.

## Boundaries

- Manuscript prose -> `05_manuscript`
- Review -> `06_review`; Response -> `07_response`
- Statistics / figures -> `04_analysis`
- Data prep -> `02_data-processing`
- Project journal lists -> `<project>/ref/` only
