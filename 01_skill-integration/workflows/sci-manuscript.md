# SOP: sci-manuscript

**Owner:** `00_orchestrator`. Prediction-model SCI from existing HTML, not from scratch stats.

Use when the user picks this SOP, or write manuscript / write in my voice / full-pipeline paper (and this SOP was chosen)，or directory detection finds `*-results.html` and they lock N3 WRITE.

Numbers **only** from that endpoint’s `*-results.html`. Format: `Aitor-format.md`. Missing HTML → do not start this SOP; send back to `statistics` / 04.

If `ref/project-state.yaml` exists, read `manuscript:` (journal, docx paths, reviewer_items) and `pipeline` / `qc`. Do not overwrite `settings.ini`. Set `pipeline.sop: sci-manuscript`.

## Sequence

0. **Session mount pick (`01`)** — every independent run needs a mount decision. If `session_picked_fine_ids` already covers the fine ids this task needs, reuse the session lock. Otherwise enter 01 and ask which registry mounted ids to attach. `PROPOSED` is not pickable. Load only the picked ids. Do not auto-load all mounted ids. Personal layers are not a mount pick. A single-node personal-layer edit with no mounted dependency does not ask. Gate **G0**.
1. **Confirm inputs** — results HTML, PNG, Figure 1 n from text. Missing n → ask, do not invent. Re-check **G-04**.
2. **Methods / Results (`05_manuscript`)** — personal upper layer + Aitor. Table 1 = training vs test. Nomogram not “Combined”.
3. **Figure 1 (`04_analysis`)** — Figure 1 is the study flowchart read from Methods (`Aitor-format.md`). STROBE / patient-flow: mounted `draw-flowchart`. Statistical plots / imaging panels: mounted `plot-figures`. Palette: `04_analysis/personal/figures.md` (lab palettes) / `FIG_PALETTE` in ini. Captions still 05. Do not draw Figure 1 with `plot-figures` and “no inclusion box”.
4. **Introduction / Discussion** — literature via `03_research`; 05 consumes `05_manuscript/personal/process/evidence.md` then polisher §2/§5. Quotas only in Aitor.
5. **De-AI (`05_manuscript`)** — `05_manuscript/base/vocab/L1/ban-phrases.md` then ai-isms. Methods stay passive. File check: `Manuscript_<endpoint>_house.docx`.
5b. **Citation verify (`03_research`)** — semantic label **G-CIT-1** (draft evidence verification). Required before Gate **G-05** and before the house deliverable is done, including mid-entry. `03_research/personal/citation-verify.md`: claim→ref table + spot-check strong claims against sources. call/require 03 citation-verify — do not self-certify lit. Handoff `05 → 06` if N4 PREVIEW only after this pass. G-CIT-1 does not waive G-CIT-2.
5c. **Integrity · pre-06** — after Gate **G-05** / before Lee 06 (also when mid-entering Need06). Composition only: G-FACT (if numbers cited) + G-CIT-1 already required + short AI-failure / manuscript-local-qc spot checklist. **Not** a new gate id. HARD block before 06 if G-FACT/G-CIT fail. See `gates.md` / `runtime-flow.mmd` node `I25`.
6. **Pre-review (`06_review`)** — Lee: statement consistency, then data consistency. Ownership: see `00_orchestrator/references/ownership-contract.md`. 03 citation-verify inside this review is semantic label **G-CIT-2** (post-revision / inside 06) and cannot be skipped; G-CIT-1 does not waive G-CIT-2. Literature accuracy is joint with Victor. Inventable items → questions for the user. Gate **G-06**.
7. **Revise (`05_manuscript`)** after the user answers. Ownership: see `00_orchestrator/references/ownership-contract.md`. Body Track Changes → **`05_manuscript`** (Aitee). If reviewer comments need a response letter → **`07_response`** (Aitee). Do **not** route response to 06.
8. **Re-review / Verify** — re-audit in **`06_review`** (Lee) as **verification only** (frozen Round-1 items). Fill **R&R traceability** (`00_orchestrator/templates/rr-traceability.md`). Response-letter resolution stays in **`07_response`** (`personal/response.md`, Aitee). Then Integrity · post-re-review lite (`I45`). Cap re-review loops at 2, then escalate like `defects[].rounds`. Do not open a new full pre-review.

## Close

Use the `00` close rules. `pipeline.stage: done` when this run's file is in place and the last gate passed, or the user says end. Stopping after the results page, or before step 6, leaves `stage` at `04` or `05`.

## Do not

- Run pipeline unless `04_analysis` is also requested.
- Cite in Methods; cite in Intro last paragraph or Discussion first paragraph.
- Dual-write VAL_MODE into YAML.
- Draw figures inside 05.
- Start from scratch without HTML.

## Output

Overwrite `Manuscript_<endpoint>_house.docx` in place (or `_polished.docx` after an archive pass).
After a 05/06 Word pass, append `ref/manuscript-revision.md` (`06_review/personal/word-edit.md`). Do not re-polish logged sections.

## Project `ref/` layout

Use `00_orchestrator/references/project-ref-layout.md`. Keep `ref/manuscript-revision.md` and `ref/settings.ini` at **ref root**. Put new review/citation/gate/code/results/exec artifacts in the matching subfolders; read manuscript-revision + citation ledger before re-running the same gate/layer.
