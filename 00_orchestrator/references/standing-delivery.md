# Standing delivery rules (00 pointers)

## HTML

Whenever this lab **creates or edits** `.html`, follow [`html-visual-design.md`](html-visual-design.md) (structure, a11y, no CDN, palette). Full-repo HTML architecture audits are **off** until the user asks. Do **not** vendor lab console / starter HTML pages into MY-SKILLS (rules only).

## Visualization compiler

Archify is a read-only visualization compiler. It is not a skill and not a top-level `07` layer. MY-SKILLS sources stay authoritative. Contract lives under **`04_analysis/personal/visualization/`**: `visualization-architecture.md`, `archify-version.yaml`, `visualization-source-contract.yaml`. Rebuild: `python3 04_analysis/personal/visualization/scripts/gen_visualization.py` (pinned Archify via release URL / temp under `D:\0del`; zip not vendored in 00). Generated HTML under `{doc_root}/04-lab-reference/my-skills-viz` (default `D:/0Grok/0doc/04-lab-reference/my-skills-viz`; env `MY_SKILLS_VIZ_OUT` / `--out`) is disposable and is not a fact source. It is **not** committed under MY-SKILLS (`docs/` removed). Mount diagrams use registry and preset metadata. Do not crawl `{mounts_cap}/` (`D:/0Grok/0doc/04-lab-reference/mounts-cap`) to draw them.

## Deliverable drop points (lab)

| Artifact | Format | Where |
|---|---|---|
| Report / phase QC | HTML | A-class → project `ref`; B-class → subproject or `submitting\<project>`; no subproject → `C:\Users\loopn\Downloads` |
| Manuscript / Track Changes | DOCX | subproject if any; else Downloads |
| Data table / filled form | XLSX | A-class final → project `0result`; else same as manuscript |
| Intermediate from derivatives | copy | A-class: copy out of `derivatives` into `0result` when final; originals stay |
| Notes for an LLM | MD | per task |
| User names a place this run | from the user | from the user |

- Temporary / intermediate files → `{DEL}\<task>` only; never delivered as output.
- `Downloads\<task>` only for a final delivery with no subproject, or when the user says so.
- Write `{WORK_B}\0doc` or a project `0doc` only when the user says 「放 0doc」.
- Never delete. Files removed from a project move into `{DEL}` with the relative path kept.

## Reporting levels

- Small task (single-file edit) → one line: result + absolute paths.
- Multi-file / pipeline / move / needs verification → four parts: (1) status (2) changes (absolute path + new/modified/moved + reason) (3) verification (mark unverified) (4) next; then a cleanup list (original → 0del / size / reason) and a keep list. Result first, reason second.
- Report times and ETAs: Asia/Shanghai (UTC+08:00).

## Project `ref/` subfolders

QC/citation/gate/exec ledgers inside a project `ref/` follow [`project-ref-layout.md`](project-ref-layout.md). Keep `settings.ini` and `manuscript-revision.md` at ref root.

