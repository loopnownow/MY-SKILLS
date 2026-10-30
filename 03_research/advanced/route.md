# 03_research advanced route -- top layer

Three pillars. Load only what the task needs.

## Top-layer flow (2026-10-30 rebind)

base thin first pass (`03_research/base/`: contracts plus pack data) -> **00 QC** (score, cite the `advanced/` anchor) -> post-QC revise **via `03_research/advanced/`** -> re-gate at 00.

## 项目启动前置（project-start-lit）

Standing pipeline. Run this **before** analysis or deep project work when the project is new or the endpoint / grouping definition is unsettled. Fixed chain (do not skip or reorder):

1. **`design-study`**
   - Light start: keywords; materials prefer `ref/refer/`, else ask owner.
   - Settle clinical question, feasibility, and validation spine.
   - Name the **guideline** that defines the endpoint or clinical decision (issuing body + year; verify in-session).
   - Paraphrase the definition that will drive inclusion, grouping, or outcome coding.
   - Record the adopted definition on the study card / project notes (and in `ref/settings.ini` comments when a RAD pipeline is used).
2. **`lit-search`**
   - About **30** related papers from the last **5 years**.
   - **Must include** diagnostic criteria and international guidelines.
   - If the topic overlaps the owner's prior publications, cite **at most 5** of those.
3. **`verify-refs`**
   - Deliver **NLM citation format + abstract list**.
   - Integrity stage includes retraction / correction scan.
4. **`lit-fulltext`** (gate every run on this chain)
   - If `ref/refer/` already has non-duplicate fulltext (pdf|html|md) >= 5
     covering highly relevant last-5y papers plus latest diagnostic criteria
     and latest international guideline: skip download, ledger only.
   - Else fill gaps; land under `ref/refer/`; dedupe DOI/PMID/hash; OA only.
5. Return to **`design-study`** when full text forces a design change.

**Deliverable path:** store the NLM + abstract list under **`ref/refer/`** (literature + NLM cite lists + abstracts; formerly「参考文献」 / `materials/citation`). Do **not** put this list in `ref/citation/` — that folder remains the audit ledger only (`CITATION_AUDIT`, skip notes, journal / citation logs). Do not conflate the two.

Intake task mode: `project-start-lit` (chains the three fine ids). Mode `guideline-first` remains as the endpoint-definition step inside `design-study` for this chain (see `intake.md`).

Only after this chain may route continue to statistics / writing / deeper analysis modes.


1. **base first-pass** lit/design fine-IDs (`lit-search`, `design-study`,...)
2. **00 QC**
3. **03 re-loop** -- advanced protocols; may **trigger** `verify-refs` (integrity stage includes retraction scan) (bodies under `NN_slug/base/`) when check (c) says needed

## Evidence & literature

| File / fine id | When |
|---|---|
| `citation-verify.md` | Claim-ref table; required before 05 done and inside 06 |
| `intro-evidence-pack.md` | 05 Introduction cards -> Evidence Pack |
| `journal-selection.md` | Topic / fit SOP |
| live `lit-search` | Generic retrieval (first-pass) |
| live `verify-refs` | **Post-QC 03-triggered** verify |
| live `lit-fulltext` | OA full-text gate after verify-refs (project-start) |
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

