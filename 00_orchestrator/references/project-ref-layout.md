# Project `ref/` layout (ledgers + artifacts)

**Owner:** `00_orchestrator`.
**Audience:** any skill that writes QC, citation, Word, gate, or execution artifacts into a project `ref/`.
**Timestamps in EXECUTION / wrap-ups:** Asia/Shanghai (UTC+08:00).

This is the **folder map and skip/idempotent contract**. It does not invent clinical numbers. No PII in filenames or ledger rows beyond what the project already stores for science (paths, DOI, citekeys).

**SSOT:** the authoritative copy is the Chinese `{RULES}\project-ref-layout.md`. This page is the runtime mirror for skills; on conflict the Chinese page wins (2026-10-29; t1303s6243: merge `writing-refs/` + `raw-pre/` into `materials/`; keep `review/` and `citation/` separate; t1300u: drop `exec/`, merge `code`+`gates` into `code-gates/`; two-tier Cleanup, not "clear everything except results"; t1307u: unaccepted submission packs under `materials/`, accepted manuscript stays at subproject root; t1309s6268: retire `ref/results/`, put stats products + lock hashes under ``ref/analysis/`).

## Root invariants (do not relocate)

Keep these at **`ref/` root** (skills and convention hard-require them):

| Path | Role |
|---|---|
| `ref/settings.ini` | RAD / pipeline config only. Do not overwrite casually; do not store secrets. |
| `ref/manuscript-revision.md` | Append-only main change ledger (owner asks + code/results/Word). After a 05/06 Word pass, append here (`06_review/advanced/word-edit.md`). **Do not re-polish logged sections** unless upstream numbers changed, the owner named them, or an unresolved comment was authorized. |

Optional at root when already in use: `ref/project-state.yaml` (from `00_orchestrator/templates/project-state.yaml`). Prefer keeping it at root until a future contract says otherwise.

## Subfolder map

Keep as few `ref/` subfolders as practical. Lean six-folder map: `review/` `citation/` `code-gates/` **`analysis/`** `materials/` `tmp/` (create on need; **do not pre-create empty folders**):

| Subfolder | Put here | Do not put here |
|---|---|---|
| `ref/review/` | Per-round `changelog.md` / `CHANGELOG_*.md`; review handoff YAML; Lee round notes | Main Word change ledger (that stays `manuscript-revision.md`) |
| `ref/citation/` | `CITATION_AUDIT.json` (or `.jsonl`); citation README / skip notes; journal/citation logs (`ref_journal_log.txt`, `CITATION*`) | Full PDF banks; writing-reference drafts and pre-clean tables (see `materials/`) |
| `ref/code-gates/` | Script/path notes, patch pointers (no secrets); `GATE*_report.md`, number-lock, input/output hash reports | Live `settings.ini`; raw credentials. **Former side-by-side `code/` and `gates/` are no longer separate folders** |
| `ref/analysis/` | Stats products + locks: `hashes.tsv`, `MANIFEST.md`, `tables/`, `figures/`, `pipeline/`, `pipeline_run.log` (for manuscript/gates) | Large binary datasets (stay in derivatives); analysis temp trees (see Three zones below); finals at **subproject root** (do **not** create `0result\`); keep `qc.html` at **`ref/` root** (not under this folder) |
| `ref/materials/` | Writing-reference drafts/PDFs (thesis parts, Ding*, QIANG* refs editions) **and** this subproject's pre-clean / import tables (xls/xlsx/csv); **unaccepted** submission packs (cover letter / title page / highlights / declarations / figure files as a set). Distinguish by filename or optional loose subdirs; for a full pack prefer `materials/submission-<id>/` (or `materials/submission-packs/` when many); subdirs not required. Keep human-readable names on move; de-id suffixes `_noName` / `_deid` are OK | **Accepted** final manuscript (stay at subproject root); citation PDF corpus (`citation/` holds audit/logs only); large organized raw (stay in `{RAW}`=`D:\00db`) |
| `ref/tmp/` | Project-local **intermediate** Word/PDF/scratch (Claude diffs, superseded TC, `-copy`, merge scratch) held until the owner says clean/close-out | Current finals (stay at project root); closed-round changelogs (`review/`); citation / code-gates ledgers; secrets |

**Retired (do not create anew):** standalone `ref/exec/`, `ref/code/`, `ref/gates/`, `ref/writing-refs/`, `ref/raw-pre/`, `ref/results/`. If old trees still exist: merge former `results/` into `analysis/`; otherwise move into `code-gates/` or `materials/` or follow Cleanup when the owner names them.

### Three zones / analysis temp area

- **Analysis temp results** (`ASL/`, `DKI/`, `DTI_IVIM/`, ...) sit **beside the subproject root**, **not under `ref/`**.
- `ref/analysis/` = stats products + locked specs/hashes for manuscript/gates; **do not** merge with `ASL/`-class trees.
- **Final manuscript / console finals** stay at the subproject root.
- **Accepted** final manuscript stays at the subproject root; **unaccepted** submission packs go under `ref/materials/` (see Submission packs below). When the owner says so, intermediate xlsx may also stay at the subproject root; do not move them on your own.

### Submission packs (unaccepted vs accepted)

- **Definition**: the journal-ready piece set for one submission (cover letter, title page, highlights, declarations, supplements, figure files, graphical abstract, etc.).
- **Unaccepted** (rejected / historical rounds): live under `ref/materials/`; for a full pack (~5+ files) use `materials/submission-<id>/` (id from original folder or journal short name); single loose files may sit at `materials/` root.
- **Accepted**: final manuscript (and still-active revision files) **stay at the subproject root**; do not park them in `materials/` for tidy.
- **Cleanup**: unaccepted packs under `materials/` may later move to `{DEL}\_by-project\<project>\` after asking; never silent-delete.

### Cleanup (tidy later; two tiers, not "everything except analysis")

**Do not** silent-delete. On tidy, **ask 城城 first, then move**; prefer `{DEL}\_by-project\<project>\` (or `_by-function` when cross-project), keeping relative names when useful. **Do not** treat "everything under `ref/` except `analysis/`" as fair game for 0del.

**Default clearable → 0del** (ask, then move):

- `ref/tmp/` (whole tree or named files)
- Superseded `materials/` (old writing refs / obsolete raw-pre tables)
- Unaccepted submission packs under `materials/` (`submission-*`, etc.; ask, then move)
- Leftover empty shells of pre-merge standalone `exec/` / `code/` / `gates/` / `writing-refs/` / `raw-pre/` (after merge into `code-gates/` / `materials/`)

**Default keep:**

- `ref/analysis/` (current locks and final tables/figures; same KEEP role as former `results/`)
- Live `ref/citation/`
- `ref/code-gates/`
- Current in-use `materials/`
- Root `settings.ini` / `manuscript-revision.md` / `README.md` (and live `project-state.yaml` if present)
- `ref/review/` materials not closed or not named for discard; `-org` pre-edit originals (see below)
- ASL-class analysis trees (at subproject root, not under `ref/`): keep by default; clear a whole tree only when 城城 names it

Create subfolders on first need (copy-on-need); after cleanup leave empty `ref/tmp/` or recreate on next write; do not invent clinical content there.

### `ref/README.md` (when adopting this layout)

Once a project adopts this layout, keep a short **`ref/README.md`** at `ref/` root that names, in one line each:

- `materials/`: writing-reference drafts/PDFs + this subproject's pre-clean/import tables (former `writing-refs/` + `raw-pre/`); distinguish by filename or optional subdir; large raw stays in `{RAW}`.
- `code-gates/`: script notes + gate/hash reports (former `code/`+`gates/`).
- `analysis/`: stats products + lock hashes (former `results/`; `qc.html` stays at `ref/` root).
- And note: "analysis temp results live at subproject root `<Modality>/`, not under ref".

## Skip / idempotent rules (read ledgers before re-run)

Assistants **must** read `ref/manuscript-revision.md` and the citation ledger **before** re-running the same gate or layer. Silent skip without a ledger reason is forbidden (see assurance six-state: `NOT_APPLICABLE` ≠ silent skip).

| Domain | Skip when | Else |
|---|---|---|
| Literature / citation L4 | Same key (`DOI` **or** citekey) + same **layer** + same **fine_id** (or skill id) already recorded PASS/KEEP in `ref/citation/CITATION_AUDIT.json` (or `.jsonl`) and input hashes unchanged | Re-run; append/update entry; emit six-state verdict |
| Word / polish | Section or span already logged in `ref/manuscript-revision.md` as revised or review-only | Append new row; do not silent re-polish |
| Review round | Round marked completed in `ref/review/changelog.md` (Implemented / Not implemented closed) | Open a new round file or append; do not rewrite closed rounds without owner ask |
| Gates / assurance | Same gate id + matching `audited_input_hashes` already PASS at required assurance level under `ref/code-gates/` | Re-run if hashes stale or assurance upgraded (`submission` / `conference-ready` forbid silent skip) |

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
- This turn does not migrate live subproject trees of old `code/`/`gates/`/`exec/`/`writing-refs/`/`raw-pre/`; does not pre-create empty `materials/`.

## Pre-edit originals (`-org`) (2026-10-19)

- Files named `*-org` / `*org*` (e.g. `comments-org.docx`, `SARC_CT_MRI_manuscript-org.docx`) are **pre-edit originals**. Keep them in the project (typically `ref/review/`).
- On owner close-out/clean: **do not discard** `-org` originals. Move only true intermediates from `ref/tmp/` to `{DEL}\_by-project\<project>\`. If an `-org` was parked in `tmp/`, promote it to `ref/review/` (or leave at root) before cleaning `tmp/`.