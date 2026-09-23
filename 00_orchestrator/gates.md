# QC gates (00)

Integrity moments only. Not a checkpoint after every node.
00 checks; the specialist named in the fail column repairs. Never invent n / AUC / PMID / ethics.


### Gate class (HARD | QUALITY)

Light metadata on existing gate ids — **do not invent** `G-HARD` / `G-QUALITY` ids.

| class | Gates | On FAIL |
|---|---|---|
| **HARD** | G0, G-PHI, G-FACT | Block the next node until the responsible party clears the fail (or user stops). |
| **QUALITY** | G-04, G-05, G-06, G-LIT, G-CODE | Local rework at the responsible node (existing recovery: max 3, then `unresolved`). Do not restart already-correct stages. |

| Id | class | When | Pass | Fail → node (max 3 recoveries) |
|---|---|---|---|---|
| G0 | HARD | every 00/02–06 run | session mount pick done; loaded ids match `project-state.yaml` `mounts.session_picked_fine_ids` (and `handoff.yaml` `mounted_fine_ids`) — check the field, don't rely on memory; empty mount → notify then re-search, never silent fallback; **if any non-B fine id is loaded, 01 must have provided verified provenance/cache state** (`cache_status` fresh or explicitly accepted stale) — else fail to 01 (00 does not query GitHub) | 01 (re-ask pick / refresh lifecycle) |
| G-PHI | HARD | before 02 tables or clinical extraction | PHI status known; no HIS host/password in git or skill files; extraction uses env `HIS_USERNAME` / `HIS_PASSWORD` on the hospital machine only | stop; user |
| G-04 | QUALITY | after each `*-results.html` | HTML exists, non-empty; n and AUC taken from HTML; split is training vs test (never Development set); `VAL_MODE` and columns only from `settings.ini`; DeLong is a paired comparison, not a CI | 04 Loopnow |
| G-FACT | HARD | after 04 HTML and again after 05 house.docx (and before 06 if numbers cited) | same fact chain across 02→04→05→06: N / train·test split / population / outcome / model name / primary endpoint / cut-off / AUC·CI·P match the responsible upstream artifact (usually `*-results.html` or 02 handoff). Source must be FILE / UPSTREAM / USER — never LLM guess. One FAIL = one responsible node | 04 Loopnow (stats) or 05 Aitee (prose drift); do not invent the number |
| G-05 | QUALITY | after `Manuscript_*_house.docx` | docx exists; numbers match that endpoint’s HTML; Methods have no citations; Table 1 = training vs test; nomogram not “Combined”; 00 did not write prose | 05 Aitee |
| G-06 | QUALITY | after pre-review or reviewer response | entry was 06; inventable items are questions to the user; 选刊 not sent to `05-write-venue`; undecidable items include reference-only sentence drafts, not silent manuscript edits; response/re-audit issues use resolution status when `06_review/personal/review-resolution.md` is in play; **if this run mounted MedSci/Scientific/AIPOCH/Nature/non-personal B, at least one Word comment on a mount-derived Major/Blocking item must use a skill-level prefix** (`[Nature:nature-reviewer]`, `[Scientific:scientific-critical-thinking]`, `[B:06-review-peer]`, …) — source-only tags like bare `[Nature:]` fail; re-tag prefixes only | 06 Lee |
| G-LIT | QUALITY | literature verify fail (05/06) | comments carry dual plan: revise/weaken/delete **and** optional 03 substitute-ref search; Evidence Request card when used (`05_manuscript/personal/evidence-request.md`); no invented PMID/DOI; 00 decides whether to call 03 | 03 Victor (search) / 05 Aitee (wording); user decides which plan |
| G-CODE | QUALITY | when task is 代码审/深审/Deep QC/refactor release-ready processing scripts | code-refactoring QC per `02_data-processing/code-refactoring/references/code-qc.md`; no open Critical/P0 | 02 (code-refactoring / Loopnow) |

File-existence (chain, every node): expected output missing or empty → do not start the next skill.

Handoff payload: `templates/handoff.yaml`.
Prose repairs: word/sentence units only. Mount vs lab conflicts: comment with edit plan; user decides.
State: `templates/project-state.yaml` fields `pipeline`, `qc`, `defects`.

### G-05 sub-check: `style-lint`  (CHG-20260920-001)

Runs on the 05 polish output, before hand-off to 06. Export the manuscript to text/markdown first
(keep the headings, so Methods / Results can be skipped).

    python3 00_orchestrator/scripts/style_lint.py <manuscript.md> --json

| exit | meaning | action |
|------|---------|--------|
| 0 | pass (4/4) | continue |
| 1 | tells found | hits -> Word comments, author A, source tag `style-lint`, with an edit plan; **user decides**; local rework at the 05 node only; counts toward the 3-try cap; no full-chain rerun |
| 2 | input error (empty / no scannable text / non-English) | **not a pass**; bounce to the user |

Hard rules: offline only, manuscript text is never sent to any other model or service; the linter never
rewrites; Methods / Results are not scanned. Catalogue and rulings: `00_orchestrator/references/style-tells.md`.

## Transversal map (not a second gate set)

ChatGPT-style Route/Mount/Boundary/Evidence/Consistency/Artifact map onto existing gates — do **not** invent Q0–Q6 ids in runtime output:

| Cross-cut | Lives in |
|---|---|
| Route | 00 dispatch table / specialist roster |
| Mount | **G0** |
| Boundary | each skill Boundaries + specialist roles |
| Evidence | **G-LIT** + 05 Evidence QC; no unknown-source numbers |
| Consistency | **G-FACT** |
| Artifact | file-existence chain (this file) |
| Stale-ref | `skill-harvest` / meta hygiene — **not** every manuscript run |
| Code | **G-CODE** / 02 code-refactoring |

Execution QC is diagnostic only: detect → name responsible node → local re-run. Never auto-edit user files or fill missing numbers.
