# Project `ref/` layout (ledgers + artifacts)

**Owner:** `00_orchestrator`.
**Audience:** any skill that writes QC, citation, Word, gate, or execution artifacts into a project `ref/`.
**Timestamps in EXECUTION / wrap-ups:** Asia/Shanghai (UTC+08:00).

This is the **folder map and skip/idempotent contract**. It does not invent clinical numbers. No PII in filenames or ledger rows beyond what the project already stores for science (paths, DOI, citekeys).

**SSOT:** the authoritative copy is the Chinese `{RULES}\project-ref-layout.md`. This page is the runtime mirror for skills; on conflict the Chinese page wins (2026-10-29; **t1321u/t1322u**: lock artifacts `hashes.tsv`/`ref/MANIFEST.md` (project artifact; not in this repo)/`pipeline_run.log` live under **`ref/pipeline/`** (not ref root); writing refs (pptx/doc/docx) may live under **`ref/refer/`** beside lit lists; analysis `false_classification*` stays at **subproject root** (ASL-class temps), not under ref; t1316u: retire shells `analysis/`/`materials/`, lift tables/figures to `ref/`; literature + NLM+abstract lists under `ref/refer/`; `ref/citation/` audit ledger only; t1309s6268: former `results/` briefly `analysis/`; t1307u: unaccepted packs at `ref/` root or `submission-*`; earlier writing-refs+raw-pre / code+gates merges unchanged in spirit).

## Root invariants (do not relocate)

Keep these at **`ref/` root** (skills and convention hard-require them):

| Path | Role |
|---|---|
| `ref/settings.ini` | RAD / pipeline config only. Do not overwrite casually; do not store secrets. |
| `ref/manuscript-revision.md` | Append-only main change ledger (owner asks + code/results/Word). After a 05/06 Word pass, append here (`06_review/advanced/word-edit.md`). **Do not re-polish logged sections** unless upstream numbers changed, the owner named them, or an unresolved comment was authorized. |
| `ref/README.md` | Short map when this layout is adopted (see below). |
| `ref/qc.html` | QC report (when used) stays at **root**, not under a subfolder. |

Optional at root when already in use: `ref/project-state.yaml` (from `00_orchestrator/templates/project-state.yaml`).

Also under `ref/` (lifted from former `analysis/` / earlier `results/`): `tables/` `figures/` `pipeline/`. **Lock artifacts** `hashes.tsv` `ref/MANIFEST.md` (project artifact; not in this repo) `pipeline_run.log` **must** live under **`ref/pipeline/`** (not ref root). **Writing refs** (pptx/doc/docx used as reference — grant apps, report slides, manuscript tables) may live under **`ref/refer/`** beside lit/NLM lists (do not recreate `writing-refs/` or `materials/`). Unaccepted submission packs (`submission-*`) and data base tables may sit at `ref/` root or under `data/` / `submission-<id>/`; prefer flat; keep a subfolder or prefix only on collision.

## Subfolder map

Keep as few `ref/` subfolders as practical. Standard folders: `review/` `citation/` `refer/` `code-gates/` `tmp/` (create on need; **do not pre-create empty folders**). **Do not create** `analysis/` or `materials/` shells anew.

| Subfolder | Put here | Do not put here |
|---|---|---|
| `ref/review/` | Per-round `changelog.md` / `CHANGELOG_*.md`; review handoff YAML; Lee round notes | Main Word change ledger (that stays `manuscript-revision.md`) |
| `ref/citation/` | **Audit ledger + journal/candidate journals:** `CITATION_AUDIT.json` (or `.jsonl`); citation README / skip notes; **journal/candidate selection only as `journals.csv` (or `.xlsx`) plus merged `_notes.md`** (2026-10-31 t1458u); journal/citation logs (`ref_journal_log.txt`, `CITATION*`) | NLM+abstract lists and literature bodies (see `refer/`); writing-reference drafts; loose journal `.md`/`.json`/`.html` (merge into `_notes.md`; superseded originals go to `ref/tmp/`) |
| `ref/refer/` | Project-start and topic literature: **`DOI_*.md` pointers** (`fulltext:` -> `_library\references`), **NLM citations + abstract lists**, lit inventories (formerly「参考文献」 / `materials/citation` / `materials/refer`); **also** writing refs (pptx/doc/docx) | Full-text entities (PDF/HTML -> `D:\0Grok\0doc\_library\references\<L1>\<L2>\`, t1455u); audit ledger (`CITATION_AUDIT` etc. stay in `citation/`); **journal/candidate journals (always `citation/` from t1458u)**; do not put lock artifacts here |
| `ref/code-gates/` | Script/path notes, patch pointers (no secrets); `GATE*_report.md`, number-lock, input/output hash reports | Live `settings.ini`; raw credentials. **Former side-by-side `code/` and `gates/` are no longer separate folders** |
| `ref/tmp/` | Project-local **intermediate** Word/PDF/scratch (Claude diffs, superseded TC, `-copy`, merge scratch) held until the owner says clean/close-out | Current finals (stay at project root); closed-round changelogs (`review/`); citation / code-gates ledgers; secrets |

**Retired (do not create anew):** `ref/analysis/`, `ref/materials/`, standalone `ref/exec/`, `ref/code/`, `ref/gates/`, `ref/writing-refs/`, `ref/raw-pre/`, `ref/results/`. If old trees still exist: lift `analysis/` children to `ref/` root; move lit/`citation`/`参考文献` under `materials/` into `refer/`, other `materials/` children to `ref/` root; empty shells → `{DEL}` (see Cleanup).

### Three zones / analysis temp area

- **Analysis temp results** (`ASL/`, `DKI/`, `DTI_IVIM/`, ...) sit **beside the subproject root**, **not under `ref/`**.
- Stats **tables/figures** live under `ref/tables/` `ref/figures/`; **lock artifacts** `hashes.tsv` `ref/MANIFEST.md` (project artifact; not in this repo) `pipeline_run.log` live under **`ref/pipeline/`**; **do not** merge with `ASL/`-class trees.
- **Analysis misclassification / temp tables** (e.g. `false_classification*`) stay at the **subproject root** with ASL-class temps; **not under `ref/`**.
- **Final manuscript / console finals** stay at the subproject root.
- **Accepted** final manuscript stays at the subproject root; **unaccepted** submission packs go under `ref/` root or `submission-*` (see Submission packs below). When the owner says so, intermediate xlsx may also stay at the subproject root; do not move them on your own.

### Submission packs (unaccepted vs accepted)

- **Definition:** the set of files prepared for one journal submission (cover letter, title page, highlights, declarations, supplements, figure files, graphical abstract, ...).
- **Unaccepted** (rejected / historical rounds): live under `ref/` root; for a full pack (~5+ files) use `submission-<id>/` (id = former folder or short journal name); loose singles may sit directly at `ref/` root.
- **Accepted:** final manuscript (and still-active revision files) **stay at the subproject root**; do not move them into a `ref/` submission folder for tidy alone.
- **Cleanup:** unaccepted packs under `ref/` may move to `{DEL}\_by-project\<project>\` after asking; never silent-delete.

### Data base tables (D-1)

- Raw / pre-clean base tables may live at `ref/` root or `ref/data/` (keep `data/` when clearer or on collision).
- **Before moving base tables in future, ask 城城 first** (D-1); exception: a migrate round already approved to lift former `materials/` contents. No silent moves.

### Cleanup (afterward; two tiers)

**Never** silent-delete. Ask 城城 before moving; prefer `{DEL}\_by-project\<project>\` (cross-project → `_by-function`); keep relative names when useful.

**Default clear → 0del** (ask first):

- `ref/tmp/` (whole tree or named files)
- Obsolete writing refs / expired pre-clean tables now under `ref/refer/` or formerly at `ref/` root
- **Unaccepted** submission packs (`submission-*`, etc.; ask first)
- Empty shells left after merge: `analysis/`, `materials/`, and earlier `exec/` / `code/` / `gates/` / `writing-refs/` / `raw-pre/` / `results/`

**Default keep:**

- Current final tables/figures (`ref/tables/` `ref/figures/`) and **lock artifacts under `ref/pipeline/`** (`hashes*` `MANIFEST*` `pipeline_run.log`) plus still-used `ref/refer/` writing refs/lit, base tables, `submission-*`
- Live `ref/citation/` (audit ledger) and `ref/refer/` (literature + writing refs)
- `ref/code-gates/`
- Root `settings.ini` / `manuscript-revision.md` / `README.md` / `qc.html` (and live `project-state.yaml`)
- `ref/review/` rounds not closed or not named for discard; `-org` pre-edit originals (see below)
- ASL-class trees at subproject root (not under `ref/`): keep by default; clear whole tree only when 城城 names it

Create subfolders on first need (copy-on-need); after cleanup you may leave an empty `ref/tmp/` or recreate on next write; invent no clinical content here.

### `ref/README.md` (when this layout is adopted)

Once a project adopts this layout, keep a short **`ref/README.md`** at `ref/` root with at least one line each for:

- `refer/`: literature + NLM cite lists and abstracts (formerly「参考文献」 / materials/citation); **also** writing refs pptx/doc/docx; distinct from the `citation/` audit ledger.
- `citation/`: `CITATION_AUDIT*` / skip notes / journal citation logs only.
- `code-gates/`: script notes + gate/hash reports (former `code/`+`gates/`).
- Root `tables/` `figures/` `pipeline/`: stats tables/figures + pipeline folder; **hashes / MANIFEST / pipeline_run.log under `ref/pipeline/`** (former `analysis/`/`results/` locks); `qc.html` stays at `ref/` root.
- Writing refs (may live under `refer/`), `submission-*`, data base tables: former `materials/` children (D-1: ask before moving base tables later).
- Note: "analysis temp results and `false_classification*` live at subproject root (`<Modality>/` or root), not under ref".

## Skip / idempotent rules (read ledgers before re-run)

Before **re**-running the same gate or layer, assistants **must** read `ref/manuscript-revision.md` and the citation ledger. Silent skips without a ledger reason are forbidden (assurance six-state: `NOT_APPLICABLE` ≠ silent skip).

| Domain | Skip when | Else |
|---|---|---|
| Literature / citation L4 | Same key (`DOI` **or** citekey) + same **layer** + same **fine_id** (or skill id) already PASS/KEEP in `ref/citation/CITATION_AUDIT.json` (or `.jsonl`) and input hashes unchanged | Re-run; append/update entry; emit six-state verdict |
| Word / polish | Paragraph or span already logged as edited or review-only in `ref/manuscript-revision.md` | Append a new row; do not silently re-polish |
| Review rounds | `ref/review/changelog.md` marked complete (Implemented / Not implemented closed) | Open a new round file or append; do not rewrite closed rounds without owner ask |
| Gates / assurance | Same gate id + matching `audited_input_hashes` already PASS at the required assurance level under `ref/code-gates/` | Re-run when hashes stale or assurance upgraded (`submission` / `conference-ready` forbid silent skip) |

Citation ledger key shape (internal): `DOI|citekey` + `layer` + `fine_id`. Prefer a JSON array or `{"entries":[]}` envelope.

Cross-links:

- Citation L4 / three-axis + six-state → `05_manuscript/qc/citation-audit-gate.md`
- Assurance six-state → `06_review/qc/assurance-verdicts.md`
- Word append rules → `06_review/advanced/word-edit.md` + `05_manuscript/SKILL.md`
- Delivery drop points → `00_orchestrator/references/standing-delivery.md`

## Out of scope for this contract

- Do not bulk pre-create empty folders on empty projects until the first artifact write (copy-on-need).
- Do not move ethics-locked trees; do not write under `advanced/`.
- Do not install the ARIS runtime.
- Do not silent-delete; empty shells move to `{DEL}` only.

## Pre-edit originals (`-org`) (2026-10-19)

- Files named `*-org` / `*org*` (e.g. `comments-org.docx`, `SARC_CT_MRI_manuscript-org.docx`) are **pre-edit originals**. Keep them in-project (usually `ref/review/`).
- On owner close-out/cleanup: **do not discard** `-org` originals. Only move true intermediates from `ref/tmp/` to `{DEL}\_by-project\<project>\`. If an `-org` sat in `tmp/`, promote it to `ref/review/` (or leave at root) before cleanup.
