---
name: medical-scientific-writing
description: >
  Ying Li / Jinshan Radiology SCI original-article prose and journal figures. Use for
  按我的风格写, 我的风格, SCI写作, 润色, 去AI, 去除AI, 英文论著, Aitor-format, Aitor格式,
  写引言, 写讨论, 补文献, 核对引用, 查文献, 流程图, 配色, 色板.
  Figures: figure-engine. Slides / .pptx → system pptx.
  Do not use for 评阅, 审稿, 投稿前预审, or 回复审稿人 → 06_review.
---

# Medical Scientific Writing — SCI 论著

## Purpose

Convert **validated** research information into precise, publication-ready original-article prose and figures.
**Never invent** sample sizes, P values, effects, CIs, procedures, ethics IDs, citations, or claims.

**Lab priority:** data truth > journal format > Ying Li voice > generic ornate English.

**Every SCI full paper uses `bundles/manuscript-core/references/Aitor-format.md` as the only Aitor-format.**  
If an Aitor-format rule is unclear, **ask the user**. Do not invent a second format.

## Capability map

| Task | Path |
|------|------|
| **Writing / polish / de-AI / TRIPOD full paper（唯一真源）** | `bundles/manuscript-core/MODULE.md` |
| **Aitor-format** (title page, IMRAD order, DOCX, citation quotas) | `bundles/manuscript-core/references/Aitor-format.md` |
| **引言/讨论文献检索**（为写 I/D，不是系统综述） | `bundles/manuscript-core/references/intro-discussion-evidence.md` |
| Section polish templates | `bundles/manuscript-core/references/polisher-sections.md` |
| de-AI pack（禁词 / slop / 检测） | `bundles/manuscript-core/references/de-ai/ai-isms-checklist.md` |
| Methods template (export) | `bundles/manuscript-core/references/methods_template_export.md` |
| ROC / calibration / DCA / multi-panel figures | `bundles/figure-engine/MODULE.md` |
| 0RAD 五套画图色板 | `references/lab-palettes.md` |
| Patient / 入组流程图（Figure 1；不画纳入标准） | `bundles/figure-engine/MODULE.md` |
| matplotlib 细调 | `bundles/figure-engine/MODULE.md` |
| Conference / defense PPTX（偶发） | system `pptx` |
| Radiology writing notes | `references/radiology/writing.md` |
| Radiology figure notes | `references/radiology/figures.md` |

## Core rule

Write from evidence and supplied results. Missing info → Word comment (author **A**); never yellow fill; never invent.

## Lab voice (Ying Li) — summary

- Highly standardized · clinically oriented · quantitatively precise · objectively cautious
- Numbers attached to claims (`n`, AUC, 95% CI, *P*)
- Observational → avoid causal overclaim (*associated with*)
- Forbidden fluff: see `bundles/manuscript-core/references/de-ai/forbidden-phrases.md`
- Methods/Results: short-moderate sentences; Discussion hedges calibrated to evidence
- Prediction-model full papers: patient-level split (**training** / **test**; **validation set** = external only; never hold-out); dual-set main metrics; LASSO+RadScore formula in prose (no LASSO table); `95% CI: X–X`; no em-dash punctuation; no disclaimer / no repeated hedge; no *coded*/*displayed* endpoint prefix; missing facts in Word comments (author **A**), no yellow slots; Vancouver+DOI as required

### Section shapes

**Single source of truth — do not duplicate the numbers here:** word counts, citation
placement, typography, and Table 1 layout for every section (Abstract/Intro/Methods/
Results/Discussion/Conclusion) live only in
**`bundles/manuscript-core/references/Aitor-format.md`**. If that file and any other note
ever disagree, `Aitor-format.md` wins — update it there, not in a summary table elsewhere.
Gold file: `0del/lxf_LG/Response/Manuscript_Response_house.docx`.

Detail: `bundles/manuscript-core/MODULE.md` + `bundles/manuscript-core/references/Aitor-format.md` + `bundles/manuscript-core/references/polisher-sections.md`.

## Modes

- `polish` / `draft-section` / `full-prediction` / `venue-shape` / `experiment-outline` / `academic-outline` / `de-ai` / `intro-discussion`
- `intro-discussion` → `intro-discussion-evidence.md` then polisher §2/§5 + Aitor quotas
- `figures` → `figure-engine` + `references/lab-palettes.md`（不要用 AI schematic）
- `slides` → system `pptx`

**Default polish path:** MODULE hard rules → `Aitor-format.md` if full paper → polisher-sections (by section) → de-ai/forbidden-phrases → `ai-isms-checklist.md` → (optional) stop-slop-core → (only if asked) ai-writing-detector.

**Intro/Discussion with literature:** claim list → `intro-discussion-evidence.md` → `Aitor-format.md` quotas → polisher §2/§5. 选题/选刊 stays in `03_research`.

Full-paper files: overwrite `Manuscript_<结局>_house.docx` in place (or `Manuscript_<结局>_polished.docx` after a polish archive). No `_v2` / `_affil` siblings. Archive to `0del` only if the user asks.

## Not this skill

- Pre-submission hole-finding / 模拟审稿 / 评阅他人稿 → `06_review`
- Response letter / 回复审稿人 → `06_review`

## Final writing QC

terminology · tense · numbers match sources · no unsupported causality · abbreviations at first use · figure/table cites · refs coherent · abstract matches main text · de-AI ban list clean · full-paper Aitor-format QC (`Aitor-format.md`)

## Progressive disclosure

Only this top-level skill is auto-discovered. Writing under `manuscript-core`; figures under `figure-engine` / `lab-palettes.md`. Nested modules are not separate skills.
