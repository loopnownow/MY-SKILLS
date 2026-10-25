# Research stage map (W1→W3 · standards only)

**Owner:** domain seat (canonical under `03_research/qc/research-stage-artifacts.md`); 00 calls only, at long research / exploration loops.
**Distill of:** ARIS `research-pipeline` + `acceptance-gate` / `resumable-runs` (wanshuiyin/Auto-claude-code-research-in-sleep). Host-agnostic rewrite — **do not** install ARIS runtime, Codex MCP, or `verify_paper_audits.sh`.
**Compose:** `assurance-verdicts.md` (effort vs assurance; who may ACCEPT) · `06_review/qc/assurance-audit-chain.md` · seats in `../../00_orchestrator/references/ownership-contract.md`.

## Stage map → lab seats

| ARIS-ish stage | Lab alias | Primary artifact (contract) | Seat | Gate / station |
|---|---|---|---|---|
| W1 Idea discovery | Idea | `IDEA` — ranked idea + hypothesis + novelty note (e.g. `IDEA_REPORT`) | Victor (03) / user pick | User approve before W1.5; Type-B ACCEPT not by executor alone |
| W1.5 Experiment bridge | Experiment | `EXPERIMENT` — plan + tracker + results (e.g. `EXPERIMENT_PLAN` / `EXPERIMENT_RESULTS` / `*-results.html`) | Loopnow (02) | **G-STATS** / **G-FACT** on numbers |
| W2 Auto review loop | Internal QC | Round ledger + `REVIEW_STATE` (see `06_review/qc/review-loop-state.md`) | Lee (06) marks; Loopnow/Aitee repair | Compose assurance L1–L5; Lee does not self-revise ms by default |
| Summary / handoff | Narrative | `NARRATIVE` — evidence-bound story from IDEA+EXPERIMENT (e.g. `NARRATIVE_REPORT`) | Aitee (05) drafts; Victor cites | **G-FACT** / **G-LIT** before freeze |
| W3 Paper writing | Paper | `paper` — venue-shaped manuscript (`Manuscript_*_house.docx` / TeX) | Aitee (05); Bai portal | **G-05** → Integrity · pre-06 → **G-06** |

Optional W3: skip when user locks “idea/experiment only.” Do not invent a new `G-*` id for these stages.

## Artifact contracts (minimal)

| Artifact | Must carry | Forbidden |
|---|---|---|
| **IDEA** | Question, hypothesis, novelty/prior gap, pilot or kill criteria | Fabricated citations / stats |
| **EXPERIMENT** | Design, n/split source, primary endpoint, result paths + hashes when assurance ≥ polished | Executor self-ACCEPT of eval honesty (Layer 1) |
| **NARRATIVE** | Claim↔evidence links to EXPERIMENT artifacts; open TODOs listed | Numbers not in EXPERIMENT / HTML |
| **paper** | Venue lock + currency note (`venue-currency.md`); refs RV-* / G-CIT | Silent skip of mandatory assurance layers at `submission` |

## Resumable phase status (idea only)

Persist ordered phases with status. Resume walks to the first **non-terminal** phase.

| status | Meaning | Who may set |
|---|---|---|
| `pending` / `running` / `failed` | Execution | Executor |
| `done` | Artifact written (execution-complete) | Executor |
| **`accepted`** | Quality acquittal recorded | **Only** cross-seat / independent reviewer **or** deterministic verifier — never executor self-report |
| `skipped` | Config says stage `NOT_APPLICABLE` | Executor (config) |

`done` ≠ `accepted`. A `done`-but-unaccepted phase is **re-validated** on resume. See `assurance-verdicts.md` Type-B ACCEPT rule.

## Soft wiring (no new G-*)

- Exploration loop topology: `00_orchestrator/workflows/research-exploration-loop.md` (if mounted).
- Review loop state machine: `06_review/qc/review-loop-state.md`.
- Resubmit text-only constraints: `resubmit-edit-whitelist.md`.

**PASS:** stage artifacts named; seats match ownership-contract; no self-ACCEPT on Type-B.
**FAIL:** missing contract artifact or executor self-acquittal → rollback responsible seat / 00 recovery.

*Attribution: ARIS research-pipeline + resumable-runs + acceptance-gate; lab seats + gates remain authoritative.*
