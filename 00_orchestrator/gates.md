# QC gates (00)

Integrity moments only. Not a checkpoint after every node.
00 checks; the specialist named in the fail column repairs. Never invent n / AUC / PMID / ethics.

| Id | When | Pass | Fail → node (max 3 recoveries) |
|---|---|---|---|
| G0 | every 00/02–06 run | session mount pick done; only picked ids loaded; empty mount → notify then re-search, never silent fallback | 01 (re-ask pick) |
| G-PHI | before 02 tables or clinical extraction | PHI status known; no HIS host/password in git or skill files; extraction uses env `HIS_USERNAME` / `HIS_PASSWORD` on the hospital machine only | stop; user |
| G-04 | after each `*-results.html` | HTML exists, non-empty; n and AUC taken from HTML; split is training vs test (never Development set); `VAL_MODE` and columns only from `settings.ini`; DeLong is a paired comparison, not a CI | 04 Loopnow |
| G-05 | after `Manuscript_*_house.docx` | docx exists; numbers match that endpoint’s HTML; Methods have no citations; Table 1 = training vs test; nomogram not “Combined”; 00 did not write prose | 05 Aitee |
| G-06 | after pre-review or reviewer response | entry was 06; inventable items are questions to the user; 选刊 not sent to `05-write-venue`; undecidable items include reference-only sentence drafts, not silent manuscript edits; **if this run mounted ARS/MedSci/Scientific/non-personal B, at least one Word comment prefix must name that source** (`[ARS:…]` / `[MedSci:…]` / `[Scientific:…]` / `[B:…]`) — else fail and re-tag prefixes only | 06 Lee |
| G-LIT | literature verify fail (05/06) | comments carry dual plan: sentence revise **and** optional 03 substitute-ref search; no invented PMID/DOI; 00 decides whether to call 03 | 03 Aitee (search) / 05 (wording); user decides which plan |

File-existence (chain, every node): expected output missing or empty → do not start the next skill.

Handoff payload: `templates/handoff.yaml`.
Prose repairs: word/sentence units only. Mount vs lab conflicts: comment with edit plan; user decides.
State: `templates/project-state.yaml` fields `pipeline`, `qc`, `defects`.
