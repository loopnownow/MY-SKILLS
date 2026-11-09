# Standing delivery rules (00 pointers)

## HTML

Whenever this lab **creates or edits** `.html`, follow [`html-visual-design.md`](html-visual-design.md) (structure, a11y, no CDN, palette). Full-repo HTML architecture audits are **off** until the user asks. Do **not** vendor lab console / starter HTML pages into MY-SKILLS (rules only).

## Visualization compiler

Visualization is rendered locally from the repository's own IR. It is not a skill and not a top-level `07` layer, and no external renderer runs. MY-SKILLS sources stay authoritative. Contract lives under **`02_data-processing/advanced/visualization/`**: `visualization-architecture.md`, `visualization-source-contract.yaml`. Rebuild: `python3 02_data-processing/advanced/visualization/scripts/gen_visualization.py` (offline; nothing is downloaded or unpacked). Generated HTML under the dir given by `--out` / env `MY_SKILLS_VIZ_OUT` (required; no default; former `my-skills-viz` retired 2026-10-20) is disposable and is not a fact source. It is **not** committed under MY-SKILLS (`docs/` removed). Diagrams use the in-repo registry. Do not crawl outside this repo for skill bodies.

## Deliverable drop points (lab)

| Artifact | Format | Where |
|---|---|---|
| **Final** deliverable (manuscript / final table / final report) | by type | **Subproject root** (under `{lab_root}\<project>`); **no** `0result\` folder; else `{DEL}` unless user names Downloads |
| **Intermediate** (QC / ledger / gate / draft) | by type | Subproject → `ref/` map (`review/`/`citation/`/`refer/` (lit + writing refs)/`code-gates/`/`tmp/` + tables/figures/pipeline; **locks under `ref/pipeline/`**; `submission-*`, base tables; `false_classification*` under the active results folder `<project>/<endpoint>/` (resolved OUT_DIR / outcome subproject, t1660u) per `project-ref-layout.md` (retired shells: `analysis/`/`materials/`/`results/`/`exec/`/`code/`/`gates/`/`writing-refs/`/`raw-pre/`)); else `{DEL}` |
| Report / phase QC | HTML | Subproject → that project `ref` or stage folder (`reviewing\…`); else `{DEL}` unless user names Downloads |
| Manuscript / Track Changes (final) | DOCX | Subproject **root** if any; else `{DEL}` unless user names Downloads |
| Data table / filled form (final) | XLSX | Subproject **root** (do **not** create `0result\`); else same as manuscript |
| Intermediate from derivatives | copy | When final, copy to **subproject root**; originals stay in `derivatives` |
| Notes for an LLM | MD | per task |
| User names a place this run | from the user | from the user |


## New folders (2026-10-24 · t1107u/t1108u/t1109u)

**All new folders** assistants need → only under `{DEL}` (`_by-project` / `_by-function`). **Default: no mkdir under `{doc_root}`**; the **only** exception is when 城城 **explicitly agrees that turn**. Scratch → `{DEL}`. ACCEPT notes → `{DEL}` only. Authority: `{RULES}/My rule.md` §5.1; `{RULES}/workspace-layout.md`; mem `{doc_root}/mem/README.md`.

## New files outside `{DEL}` (2026-10-24 · t1098u)

**Do not create new files** outside `{DEL}`. Editing existing files is OK. New drafts / ACCEPT / digests / notes / intermediates → `{DEL}\_by-function\…` or `{DEL}\_by-project\…`. Final drop points in the table above still apply when the user names a deliverable this turn (prefer overwrite-in-place of an existing final). Authority: `{RULES}/My rule.md` §5.1; `{RULES}/workspace-layout.md`; mem `{doc_root}/mem/README.md`.

- Temporary / non-deliverable → `{DEL}\<task>` only; never delivered as output.
- Downloads **only** when the user names 「下载」 (Downloads) this run.
- Write a project into `_Docs` (or `{doc_root}`) only when the user says 「放 0doc」/「放 _Docs」 (旧名 0doc).
- Never delete. Files removed from a project move into `{DEL}` with the relative path kept.
- No retired workspace classes (former Workspace-A / Workspace-B) or WORK_* path aliases (retired 2026-10-24).
- Subprojects do **not** use a live `0result\` folder as the standard deliverable seat.

## Reporting levels

- Small task (single-file edit) → one line: result + absolute paths.
- Multi-file / pipeline / move / needs verification → four parts: (1) status (2) changes (absolute path + new/modified/moved + reason) (3) verification (mark unverified) (4) next; then a cleanup list (original → `{del_root}` / size / reason) and a keep list. Result first, reason second.
- Report times and ETAs: Asia/Shanghai (UTC+08:00).

## Project `ref/` subfolders

QC/citation/gate ledgers inside a project `ref/` follow [`project-ref-layout.md`](project-ref-layout.md) (map: `review/` `citation/` `refer/` (lit+writing refs) `code-gates/` `tmp/` + tables/figures/pipeline; **hashes/MANIFEST/pipeline_run.log under `ref/pipeline/`**; Cleanup two-tier; retired `analysis/`/`materials/`). Keep `settings.ini` and `manuscript-revision.md` at ref root; `false_classification*` under the active results folder `<project>/<endpoint>/` (resolved OUT_DIR / outcome subproject), not at subproject root (t1660u, 2026-11-05).

## accepted closeout (t1806u / t1809u / t1840u)

Pointer only. **Relations / harvest authorization / divert map** → `{RULES}/workspace-layout.md` 「工作区关系：阶段 · 分流 · harvest · 冷库」 (harvest ≠ closeout; harvest needs same-turn owner auth from drafting / pre-submit / reviewing / accepted / archived / `.Del`; closeout does not replace harvest; harvest does not replace disk moves).

**Landing detail** → `{RULES}/workspace-layout.md` 「accepted 收工」: after authorized harvest (or `skill_ref=none`), slim `accepted\<prefix_suffix>\`, then move into `archived\<family>\<prefix_suffix>\` + `ARCHIVED.md`. Hard-keep: one `Manuscript_<slug>_{V|R|P}…` **file** + `FinalData_<slug>.xlsx` (or data.xlsx pinned in `ref/README`) + optional `ref/settings.ini` → `_DataBase\<family>\<prefix_suffix>\`. Project-tree `R*` / `P*` folders go whole into `_DataBase\<family>\<prefix_suffix>\` (>=20 loose → zip-first); after QC originals → `.Del\_by-project\<slug>\`.

Disease shortcode + family L1 SSOT: `_DataBase\_diseases.csv` (`family` column). archived / `_DataBase` L1 = `<family>` (same-source aggregation; t1829u). Leaf suffix still base shortcode. Shared raw once: family raw pool `<family>\_share\` (`<leaf>` archives / `ethics\<CODE>` / `thesis\<slug>`), or primary leaf + `ref/settings.ini` pointer. Rules: `{RULES}/workspace-layout.md` 「同源聚合」/「按家族分桶」/「archived 冷库」.


## ethics retention (t1849u)

Pointer only. **Retention / retire `_lab\ethics`** → `{RULES}/workspace-layout.md` 「伦理材料留存（t1849u）」:
批件原件 only date ≥ 2023-11-10 into `_DataBase\<family>\_share\ethics\`;
clinical protocol + ICF keep all there; `_DataBase\_lab\ethics` retired → `.Del` (Bai moves disk).
`_library\ethics\approvals` remains library SSOT for indexed 批件 PDF.

