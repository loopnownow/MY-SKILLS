# 03_research advanced route -- top layer

Three pillars. Load only what the task needs.

## Top-layer flow (2026-10-17)

## 项目启动前置（guideline-first）

Use this **before** literature search, study design, statistics, or writing when the project is new or the endpoint/grouping definition is unsettled.

1. Name the **guideline** that defines the endpoint or clinical decision (issuing body + year; verify in-session).
2. Paraphrase the definition that will drive inclusion, grouping, or outcome coding.
3. Record the adopted definition on the study card / project notes (and in `ref/settings.ini` comments when a RAD pipeline is used).
4. Only then route to `literature` / `study-design` / `statistics` / `writing` modes.

Intake task mode: `guideline-first` (see `intake.md`).


1. **base first-pass** lit/design fine-IDs (`lit-search`, `design-study`,...)
2. **00 QC**
3. **03 re-loop** -- advanced protocols; may **trigger** `verify-refs` + `retraction-watcher` (bodies under `NN_slug/base/`) when check (c) says needed

## Evidence & literature

| File / fine id | When |
|---|---|
| `citation-verify.md` | Claim-ref table; required before 05 done and inside 06 |
| `intro-evidence-pack.md` | 05 Introduction cards -> Evidence Pack |
| `journal-selection.md` | Topic / fit SOP |
| live `lit-search` | Generic retrieval (first-pass) |
| live `verify-refs` | **Post-QC 03-triggered** verify |
| live `retraction-watcher` | **Post-QC 03-triggered** retraction check |
| `lit-bank.md` | Lab citation bank (NLM store / Vancouver cite; advanced=group SCI; base=DOI-verified 5y or current guideline) |
| `references/grant-fulltext-skeleton.md` | Grant full-text section outlines by scheme (absorbed from `_library/fulltext/`; pairs with `grant-own-skeleton.md`) |
| `references/lab-ref-method-digest.md` | Lab reference-range methodology digest; number-plausibility checks in manuscripts and reviews (not clinical decisions, not an LIS RI replacement) |

## Design & exploration

| File | When |
|---|---|
| `radiology-design.md` / `radiology-frontier.md` | Imaging design / novelty |
| `ethics.md` / `intake.md` / `multicenter.md` | Protocol ethics / triage / multicentre |
| `grant-writing.md` / `grant-review.md` / `grant-own-skeleton.md` / `method-upgrade-into-grant.md` | Grants (review voice vs own-proposal voice, inside each file) |
| `handoff.md` | Layering + advanced-file authority; read before moving advanced files |
| `clinical-translation/` | Reader study / deployment design |
| `03_research/base/fill-protocol/` | Ethics forms (Bai seat; no A stub) |
| `00_orchestrator/workflows/question-to-reference.md` | R1-R5 spine |

## Journal selection

| Location | What |
|---|---|
| `03_research/base/find-journal/` | Victor seats engine (no A stub) |
| Runtime pools | `{find_journal_pools}` (`_library\find-journal\data\2026`) |
| `<project>/ref/` | Per-project submitted lists -- never in MY-SKILLS |

Call order: `journal-selection.md` → `03_research/base/find-journal/SKILL.md`. Format after choice → `03_research/base/find-journal/journal-format-compliance/` (+ companion `05_manuscript/base/write-paper/` styles).

## 0doc document DB (Bai)

| File | When |
|---|---|
| `0doc-db.md` | Owner asks to search/look up/inventory `{doc_root}` (Bai seat; Aitor routes only) |

