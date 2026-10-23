# Standing delivery rules (00 pointers)

## HTML

Whenever this lab **creates or edits** `.html`, follow [`html-visual-design.md`](html-visual-design.md) (structure, a11y, no CDN, palette). Full-repo HTML architecture audits are **off** until the user asks. Do **not** vendor lab console / starter HTML pages into MY-SKILLS (rules only).

## Visualization compiler

Visualization is rendered locally from the repository's own IR. It is not a skill and not a top-level `07` layer, and no external renderer runs. MY-SKILLS sources stay authoritative. Contract lives under **`04_analysis/personal/visualization/`**: `visualization-architecture.md`, `visualization-source-contract.yaml`. Rebuild: `python3 04_analysis/personal/visualization/scripts/gen_visualization.py` (offline; nothing is downloaded or unpacked). Generated HTML under the dir given by `--out` / env `MY_SKILLS_VIZ_OUT` (required; no default; former `my-skills-viz` retired 2026-10-20) is disposable and is not a fact source. It is **not** committed under MY-SKILLS (`docs/` removed). Mount diagrams use registry and preset metadata. The former `{mounts_cap}/` cache is retired (2026-10-20); do not crawl it.

## Deliverable drop points (lab)

| Artifact | Format | Where |
|---|---|---|
| Report / phase QC | HTML | Subproject → that project `ref` or `in-review\<project>`; else `{DEL}` unless user names Downloads |
| Manuscript / Track Changes | DOCX | Subproject if any; else `{DEL}` unless user names Downloads |
| Data table / filled form | XLSX | Final tables → subproject `0result`; else same as manuscript |
| Intermediate from derivatives | copy | Copy out of `derivatives` into `0result` when final; originals stay |
| Notes for an LLM | MD | per task |
| User names a place this run | from the user | from the user |

- Temporary / intermediate files → `{DEL}\<task>` only; never delivered as output.
- Downloads **only** when the user names 「下载」/「Downloads」 this run.
- Write a project `0doc` (or `{doc_root}`) only when the user says 「放 0doc」.
- Never delete. Files removed from a project move into `{DEL}` with the relative path kept.
- No A-class / B-class / `{WORK_A}` / `{WORK_B}` (retired 2026-10-24).

## Reporting levels

- Small task (single-file edit) → one line: result + absolute paths.
- Multi-file / pipeline / move / needs verification → four parts: (1) status (2) changes (absolute path + new/modified/moved + reason) (3) verification (mark unverified) (4) next; then a cleanup list (original → 0del / size / reason) and a keep list. Result first, reason second.
- Report times and ETAs: Asia/Shanghai (UTC+08:00).

## Project `ref/` subfolders

QC/citation/gate/exec ledgers inside a project `ref/` follow [`project-ref-layout.md`](project-ref-layout.md). Keep `settings.ini` and `manuscript-revision.md` at ref root.

