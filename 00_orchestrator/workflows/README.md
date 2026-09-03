# Workflows (00)

SOPs that **schedule** 01–06. Not extra top-level skills.
Loop: intent classify → skill chain → QC gate (`../gates.md`).

| SOP | When | File |
|-----|------|------|
| radiomics-study | 图像/ROI/特征 → `04_analysis` 出 HTML | `radiomics-study.md` |
| sci-manuscript | 已有 HTML → Aitor 稿 → 预审/回信 | `sci-manuscript.md` |

On 「全线 / 自主 / 组学（整项）」: **ask which SOP** (node N1) unless directory detection already locked it. Do not infer against files.

**Directory detection:** `settings.ini` → 0RAD; `*-results.html` → may enter sci-manuscript; `Manuscript_*_house.docx` → 05; reviewer letter → 06; imaging without HTML → radiomics-study.

**Session mount pick:** before loading packs, run 01 ask-each-run. Registry `MOUNTED` is the menu. Load only the ids the user picks this run. Do not auto-load all mounted ids.

`radiomics-study` offers `sci-manuscript` when HTML exists (N3). `sci-manuscript` requires HTML.

Project state template: `../templates/project-state.yaml` → copy to `<project>/ref/project-state.yaml` only when starting state tracking. Handoff: `../templates/handoff.yaml`.

01 is Skill Discovery, not Excel. Excel/0RAD → 02. Figures → 04 (`04-fig-flow` / `04-fig-plot`). Literature → 03. 选刊 → `03_research`. 样本量 → `04-stats-power`. Reviewer response → 06.
