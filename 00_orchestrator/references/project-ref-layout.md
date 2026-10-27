# Project `ref/` layout (ledgers + artifacts)

**Owner:** `00_orchestrator`.
**Audience:** any skill that writes QC, citation, Word, gate, or execution artifacts into a project `ref/`.
**Timestamps in EXECUTION / wrap-ups:** Asia/Shanghai (UTC+08:00).

This is the **folder map and skip/idempotent contract**. It does not invent clinical numbers. No PII in filenames or ledger rows beyond what the project already stores for science (paths, DOI, citekeys).

**SSOT:** the authoritative copy is the Chinese `{RULES}\project-ref-layout.md`. This page is the runtime mirror for skills; on conflict the Chinese page wins (2026-10-26).

## Root invariants (do not relocate)

Keep these at **`ref/` root** (skills and convention hard-require them):

| Path | Role |
|---|---|
| `ref/settings.ini` | RAD / pipeline config only. Do not overwrite casually; do not store secrets. |
| `ref/manuscript-revision.md` | Append-only main change ledger (owner asks + code/results/Word). After a 05/06 Word pass, append here (`06_review/advanced/word-edit.md`). **Do not re-polish logged sections** unless upstream numbers changed, the owner named them, or an unresolved comment was authorized. |

Optional at root when already in use: `ref/project-state.yaml` (from `00_orchestrator/templates/project-state.yaml`). Prefer keeping it at root until a future contract says otherwise.

## Subfolder map

| Subfolder | Put here | Do not put here |
|---|---|---|
| `ref/review/` | Per-round `changelog.md` / `CHANGELOG_*.md`; review handoff YAML; Lee round notes | Main Word change ledger (that stays `manuscript-revision.md`) |
| `ref/citation/` | `CITATION_AUDIT.json` (or `.jsonl`); citation README / skip notes; journal/citation logs (`ref_journal_log.txt`, `CITATION*`) | Full PDF banks |
| `ref/gates/` | `GATE*_report.md`, number-lock, input/output hash reports | Live `settings.ini` |
| `ref/code/` | Script/path notes, patch pointers (no secrets, no tokens) | Raw credentials |
| `ref/results/` | Table/figure lock notes and content hashes | Large binary datasets (stay in derivatives); finals at **subproject root** (do **not** create `0result\`) |
| `ref/exec/` | Optional `EXECUTION.md` wrap-ups; ops notes that are not review-round ledgers | Owner-facing ACCEPT reports unless the owner asked |
| `ref/tmp/` | Project-local **intermediate** Word/PDF/scratch (Claude diffs, superseded TC, `-copy`, merge scratch) held until the owner says clean/close-out | Current finals (stay at project root); closed-round changelogs (`review/`); citation/gates ledgers; secrets |

### `ref/tmp/` cleanup

- Create on first need (copy-on-need with the other subfolders).
- Assistants may stage intermediates here instead of scattering at `ref/` root or project root.
- **Do not** silent-delete. When the owner says clean / clean / close-out for that project, move the whole `ref/tmp/` tree (or named files) into `{DEL}\_by-project\<project>\` (or `_by-function` when cross-project), keeping relative names when useful.
- After cleanup, leave an empty `ref/tmp/` or recreate on next write; do not invent clinical content there.

Also keep a short **`ref/README.md`** map at `ref/` root once a project adopts this layout (subfolder roles above).

## Skip / idempotent rules (read ledgers before re-run)

Assistants **must** read `ref/manuscript-revision.md` and the citation ledger **before** re-running the same gate or layer. Silent skip without a ledger reason is forbidden (see assurance six-state: `NOT_APPLICABLE` ≠ silent skip).

| Domain | Skip when | Else |
|---|---|---|
| Literature / citation L4 | Same key (`DOI` **or** citekey) + same **layer** + same **fine_id** (or skill id) already recorded PASS/KEEP in `ref/citation/CITATION_AUDIT.json` (or `.jsonl`) and input hashes unchanged | Re-run; append/update entry; emit six-state verdict |
| Word / polish | Section or span already logged in `ref/manuscript-revision.md` as revised or review-only | Append new row; do not silent re-polish |
| Review round | Round marked completed in `ref/review/changelog.md` (Implemented / Not implemented closed) | Open a new round file or append; do not rewrite closed rounds without owner ask |
| Gates / assurance | Same gate id + matching `audited_input_hashes` already PASS at required assurance level | Re-run if hashes stale or assurance upgraded (`submission` / `conference-ready` forbid silent skip) |

Citation ledger key shape (internal; not a user-facing slogan): `DOI|citekey` + `layer` + `fine_id`. Prefer JSON array or `{"entries":[]}` envelope.

Cross-links:

- Citation L4 / three-axis + six-state → `05_manuscript/qc/citation-audit-gate.md`
- Assurance six-state → `06_review/qc/assurance-verdicts.md`
- Word append rule → `06_review/advanced/word-edit.md` + `05_manuscript/SKILL.md`
- Deliverable drop points → `00_orchestrator/references/standing-delivery.md`

## What this contract does **not** do

- Does not mass-require empty folders on greenfield projects until first artifact write (create subfolders copy-on-need).
- Does not move ethics locked trees or write `advanced/`.
- Does not install ARIS runtime.

## Pre-edit originals (`-org`) (2026-10-19)

- Files named `*-org` / `*org*` (e.g. `comments-org.docx`, `SARC_CT_MRI_manuscript-org.docx`) are **pre-edit originals**. Keep them in the project — typically `ref/review/`.
- On owner close-out/clean: **do not discard** `-org` originals. Move only true intermediates from `ref/tmp/` to `{DEL}\_by-project\<project>\`. If an `-org` was parked in `tmp/`, promote it to `ref/review/` (or leave at root) before cleaning `tmp/`.
