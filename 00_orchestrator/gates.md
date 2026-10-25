# QC gates (00)

Integrity moments only. Not a checkpoint after every node.
00 checks; the specialist named in the fail column repairs. Never invent n / AUC / PMID / ethics.


### Gate class (HARD | QUALITY)

Light metadata on existing gate ids — **do not invent** `G-HARD` / `G-QUALITY` ids.

| class | Gates | On FAIL |
|---|---|---|
| **HARD** | G0, G-PHI, G-FACT | Block the next node until the responsible party clears the fail (or user stops). |
| **QUALITY** | G-STATS, G-05, G-06, G-07, G-LIT, G-CODE | Local rework at the responsible node (existing recovery: max 3, then `unresolved`). Do not restart already-correct stages. |

| Id | class | When | Pass | Fail → node (max 3 recoveries) |
|---|---|---|---|---|
| G0 | HARD | every independent run that loads a mount | mount decision done; loaded ids match `project-state.yaml` `mounts.session_picked_fine_ids` (and `handoff.yaml` `mounted_fine_ids`) — check the field, don't rely on memory; reuse the session lock when it already covers this task; empty mount → notify then re-search, never silent fallback; **if any non-base fine id is loaded, 00 must have provided verified provenance/cache state** (`cache_status` fresh or explicitly accepted stale) — else fail to 00 (00 does not query GitHub). For each selected fine id, G0 should be able to record `mount_provenance` with `fine_id`, `source`, `resolved_commit`, `path`, `content_hash`, `checked_at` (see `templates/project-state.yaml`). Do not invent hashes | 00 (re-ask pick / refresh lifecycle) |
| G-PHI | HARD | before 02 tables or clinical extraction | PHI status known; no HIS host/password in git or skill files; extraction uses env `HIS_USERNAME` / `HIS_PASSWORD` on the hospital machine only | stop; user |
| G-STATS | QUALITY | after each `*-results.html` | HTML exists, non-empty; n and AUC taken from HTML; split is training vs test (never Development set); `VAL_MODE` and columns only from `settings.ini`; DeLong is a paired comparison, not a CI | 02 Loopnow |
| G-FACT | HARD | after 02 HTML and again after 05 house.docx (and before 06 if numbers cited) | same fact chain across 02→05→06: N / train·test split / population / outcome / model name / primary endpoint / cut-off / AUC·CI·P match the responsible upstream artifact (usually `*-results.html` or 02 handoff). Also record, when the study uses them: event count, missing count, exclusion count, analysis population, primary/secondary endpoint, time origin, reference category, OR/HR direction, units, threshold, 95% CI method, model formula. Source must be FILE / UPSTREAM / USER — never LLM guess. Do not auto-pick numbers. One FAIL = one responsible node | 02 Loopnow (stats) or 05 Aitee (prose drift); do not invent the number |
| G-05 | QUALITY | after `Manuscript_*_house.docx` | docx exists; numbers match that endpoint’s HTML; Methods have no citations; Table 1 = training vs test; nomogram not “Combined”; 00 did not write prose; pre-submit checks (`05_manuscript/qc/manuscript-local-qc.md`) are clean or commented; 05 qc standards applied (`reporting-guideline-route.md` + `reporting-guidelines-router.json`, `claim-number-align.md`, `anti-leak-placeholders.md`, `style-spotcheck.md`, `figure-stats-legend.md`, `figure-qa-minima.md`, `refs-verified.md`, `venue-compliance-minima.md`, `venue-currency.md`, `data-code-availability.md`); 03 citation-verify (`03_research/personal/citation-verify.md`) has a claim→ref table and a strong-claim spot-check; 05 did not self-certify lit | 05 Aitee (prose) / 03 Victor (citations) |
| G-06 | QUALITY | after Lee pre-review or re-review only | entry was 06 (pre-review / peer-review / re-review); inventable items are questions to the user; Journal selection via 03 `find-journal`; venue style via `05_manuscript/base/write-paper/`; Ownership: see `00_orchestrator/references/ownership-contract.md`. Do not silently edit the manuscript. **Reviewer response / response letter is not G-06** — enters **07 / `07_response`** (mmd `Need07`); sister-paper and consistency conflicts are commented via `06_review/qc/cross-manuscript-qc.md`, not silently rewritten; 06 qc standards applied (`editorial-decision-matrix.md`, `rr-re-review.md` on re-review, `stats-reporting-spotcheck.md`, `stats-failure-modes.md`, `forensic-consistency.md`, `technical-concern-coverage.md`, `review-release-gates.md`); 03 citation-verify ran and was not skipped (Lee: statement then data consistency; lit accuracy joint with Victor); **if this run mounted external review sources (Nature / peer-review / self-review packs), at least one Word comment on a mount-derived Major/Blocking item must use a skill-level prefix** (`[Nature:simulate-reviewers]`, `[peer-review]`, `[self-review]`, …) — source-only tags like bare `[Nature:]` fail; re-tag prefixes only | 06 Lee (comments) / 05 Aitee (Track Changes) / 03 Victor |
| G-07 | QUALITY | after Aitee response / response letter (Need07) | entry was 07 (`Need07`); response resolves each reviewer point or records deferral with owner; no silent Accept of unresolved items; 07 final authority; revise / tighten-response under `07_response/base/` (tone-polish is on-demand inside tighten-response; structure stays revise); G-LIT when the letter or revised ms cites literature; numbers changed in letter → hand off claim/number audit; Lee does not draft responses | 07 Aitee (letter) / 05 Aitee (Track Changes) / 03 Victor (cites) |
| G-LIT | QUALITY | citation-verify required before 05 done and inside 06; also on a literature verify fail | the verify pass itself is required (`03_research/personal/citation-verify.md`); 05/06 do not self-certify lit; on fail, comments carry dual plan: revise/weaken/delete **and** optional further 03 substitute-ref search; Evidence Request card when used (`05_manuscript/personal/process/evidence.md`); no invented PMID/DOI; 00 decides only whether that further search runs | 03 Victor (verify) / 05 Aitee (wording); user decides which plan |
| G-CODE | QUALITY | when task is code review/deep QC/Deep QC/refactor release-ready processing scripts | code QC per `02_data-processing/qc/coding-qc.md`; no open Critical/P0 | 02 (personal/coding.md / Loopnow) |

### G-FACT checklist

Record only. Do not auto-pick numbers. Blank stays blank or becomes one question.

- event count
- missing count
- exclusion count
- analysis population
- primary/secondary endpoint
- time origin
- reference category
- OR/HR direction
- units
- threshold
- 95% CI method
- model formula


### Soft-check Hook A — lab RI (detect only)

| Id | When | Fail → comment |
|---|---|---|
| **Hook A** (`LAB-RI` / G-FACT pre-06) | Integrity / G-FACT pre-06; manuscript states a “normal range”, “reference interval” / “reference range” / “normal value”, or a unit for a lab/clinical indicator | `LAB-RI-MISMATCH` or `LAB-UNIT-MISMATCH`: quote claim, cite nearest KB `record_id`, note population/assay caveat. Do **not** insert KB numbers. |

Lab-ref soft-check contract (detect only; **never** auto-edit manuscript numbers): `{doc_root}\03-research\lab-ref-ranges\qc\gate-hooks.md`. Soft only — never auto-rewrite from the lab-ref KB.

G-FACT is fact-lineage completeness after 02 HTML and again after 05 house.docx, and before 06 only if numbers are cited. 02 exit is not a G-FACT. 03 exit is not a G-FACT. There is no G-02 and no G-03. Visualization gates `G-VIZ-01` / `G-VIZ-02` are domain-held by `02_data-processing/personal/visualization/`; 00 does not route them.

File-existence (chain, every node): expected output missing or empty → do not start the next skill.

Handoff payload: `templates/handoff.yaml`.
Prose repairs: word/sentence units only. Ownership: see `00_orchestrator/references/ownership-contract.md`. Mount vs lab conflicts: comment with edit plan; user decides; Aitee applies Track Changes after that decision.
State: `templates/project-state.yaml` fields `pipeline` (stage includes `03`), `qc` (`last_gate` includes G-FACT / G-LIT / G-CODE), `defects` (per-defect `rounds`, max 3), `manuscript.citation_verify` (G-CIT-1 / G-CIT-2).

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
| Stale-ref | meta hygiene / `references/skill-evolution.md` — **not** every manuscript run |
| Code | **G-CODE** / 02 personal/coding.md |

Execution QC is diagnostic only: detect → name responsible node → local re-run. Never auto-edit user files or fill missing numbers.

## Manuscript local QC checklists

Writing-seat scorecard + pre-submit checks: `05_manuscript/qc/manuscript-local-qc.md`. Additional 05 qc standards: `reporting-guideline-route.md` + `reporting-guidelines-router.json`, `claim-number-align.md`, `anti-leak-placeholders.md` (incl. AL-5 disclaimer→comment annotation+suggested rewrite; compose 06/07 `disclaimer-comment-only.md`), `style-spotcheck.md`, `figure-stats-legend.md`, `figure-qa-minima.md`, `refs-verified.md`, `venue-compliance-minima.md`, `venue-currency.md`, `data-code-availability.md`. Cross-manuscript: `06_review/qc/cross-manuscript-qc.md`. Additional 06 qc standards: `editorial-decision-matrix.md`, `rr-re-review.md`, `stats-reporting-spotcheck.md`, `stats-failure-modes.md`, `forensic-consistency.md`, `technical-concern-coverage.md`, `review-release-gates.md`, `appraisal-tool-route.md`. Domain `qc/` holds WHAT to check (standards only; pass/fail + fail→rollback); this file holds WHEN / PASS-FAIL / who repairs. Formal Gate ownership stays here in 00.


## Top-layer QC checks (2026-10-17)

After base fine-ID first-pass and before / during personal/top re-loops, 00 verifies:

| Check | What | Fail -> |
|---|---|---|
| **(a) Isolated dual-review artifacts** | When `simulate-reviewers` / dual engines (`self-review` \|\| `peer-review`) ran: finding sets are **isolated**; artifacts labeled by source prefix before 06 merges | base engines re-run; 06 does not invent isolation |
| **(b) Vocab loaded on first write** | First-pass `write-paper` / `check-reporting` loaded `05_manuscript/base/vocab/` before drafting. `05_manuscript/personal/vocab/` is a pointer only | bounce to base write path |
| **(c) 03 verify-refs / retraction re-run needed?** | Post-QC: if refs changed or G-LIT/G-CIT failed -> 03 triggers `verify-refs` + `retraction-watcher` (bodies under `03_research/base/`); else skip | 03 / base verify-refs |
| **(d) 05 polish / humanize** | Post-QC: `humanize` (report-only lint, then de-AI pass) alongside Aitor-format/voice. Bodies under `05_manuscript/base/`; 05 owns order | 05 Aitee |
| **(e) 07 response** | Response enters **07** (not 06). 07 final authority; revise/tighten-response stay `source: my-skills` under `07_response/base/` (tone-polish is on-demand inside tighten-response) | 07 |

These are checks on the existing gate set, not new gate ids.


## Integrity compositions (named nodes — not new gate ids)

Documented on `runtime-flow.mmd` as **Integrity · pre-06** (`I25`) and **Integrity · post-re-review lite** (`I45`). No new `G-*` row.

| Station | Composes | HARD block? | Notes |
|---|---|---|---|
| **Integrity · pre-06** | **G-FACT** (when numbers cited) + **G-CIT-1** / **G-LIT** + **05 reporting-guideline subset** (`reporting-guideline-route.md` + `reporting-guidelines-router.json`) + claim-number-align / anti-leak / manuscript-local-qc AI-fail lite + **figure-stats-legend** / **figure-qa-minima** / **refs-verified** / **data-code-availability** / **venue-compliance-minima** + **forensic-consistency** / **stats-failure-modes** + **assurance-audit-chain** L1–L4 as applicable (HARD compose with G-FACT on confirmed central numeric/stats P0) | **Yes** before Lee 06 if G-FACT or G-CIT/G-LIT or RG subset FAIL | Runs after Gate · 05 / N4→06 and on mid-entry Need06 before P06 |
| **Integrity · post-re-review lite** | G-FACT spot-check + AI-fail lite after `P06r` | Same HARD recovery if fact/lit broken | Not a full first-pass re-run |

### MANDATORY checkpoints (see also `runtime-flow.md`)

Integrity FAIL (I25/I45), review decision (Rev / re-review verdict), and before `stage: done` are **MANDATORY** user/recorded stops. FULL / SLIM / MANDATORY tiers and the ≥4 consecutive continues → force FULL rule live in `runtime-flow.md`.

### R&R re-review

06 re-review (`P06r`) is **verification only** (frozen Round-1 items). Standards: `06_review/qc/rr-re-review.md` + decision `editorial-decision-matrix.md` + `stats-reporting-spotcheck.md` + `stats-failure-modes.md` + `forensic-consistency.md` + `review-release-gates.md`. Traceability template: `00_orchestrator/templates/rr-traceability.md`. Cap re-review loops at 2, then escalate like `defects[].rounds`.

### Assurance contract (soft)

Effort vs assurance axes and 6-state verdicts: `06_review/qc/assurance-verdicts.md`.
Five-layer audit map (experiment → claim science → paper numbers → citations → kill-argument): `06_review/qc/assurance-audit-chain.md`.
At `assurance: submission`, mandatory layers must emit `PASS | WARN | FAIL | BLOCKED | ERROR | NOT_APPLICABLE` — silent skip forbidden.
Executor must not self-judge integrity (Type-B). Compose with G-FACT / G-LIT / Integrity · pre-06; do not invent gate ids.


### Research stage map + review-loop state (soft · ARIS P1)

Host-agnostic process standards only — do **not** install ARIS runtime / Codex MCP / `verify_paper_audits.sh`.

| Standard | Path |
|---|---|
| W1→W3 stage map + IDEA/EXPERIMENT/NARRATIVE/paper contracts → Victor/Loopnow/Aitee/Lee | `03_research/qc/research-stage-artifacts.md` |
| review→fix→re-review + resumable `REVIEW_STATE` | `06_review/qc/review-loop-state.md` |
| Resubmit edit-whitelist + failure ledger | `07_response/qc/resubmit-edit-whitelist.md` |

Compose with existing Assurance contract soft section above; no new `G-*` ids.

