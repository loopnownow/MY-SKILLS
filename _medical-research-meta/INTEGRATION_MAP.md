# Integration map — existing skills → MedicalResearch 7 skills

## Source inventory

### From `C:\Users\loopn\.grok\skills`

| Source | Destination |
|--------|-------------|
| ly-literature | `01_research/bundles/ly-literature` |
| radiology-skills/modules/radiology-design | `01_research/bundles/radiology-design` |
| radiology-skills/modules/radiology-frontier | `01_research/bundles/radiology-frontier` |
| radiology-skills/references (design/lit subset) | `01_research/references/radiology` |
| ly-stats-ml | `02_analysis/bundles/ly-stats-ml` |
| data-impute | `02_analysis/bundles/data-impute` |
| radiology-skills radiomics/annotation/radiogenomics/translation/reader | `03_imaging/bundles/*` |
| ly-imaging-ops | `03_imaging/bundles/ly-imaging-ops` |
| ly-dl-libs | `03_imaging/bundles/ly-dl-libs` |
| radiology-skills scripts/examples | `03_imaging/scripts|examples` |
| ly-sci-writing | `04_writing/bundles/ly-sci-writing` |
| ly-figures | `04_writing/bundles/ly-figures` |
| ly-slides | archived 2026-08-15 → `D:\0Grok\0RAD\0del\skill_04_ly-slides` (use system `pptx`) |
| ly-prereview | `05_review/bundles/ly-prereview` |
| ly-response | `05_review/bundles/ly-response` |
| ly-rules | `06_automation/bundles/code-refactoring` |
| ethics-application-forms | `06_automation/bundles/ethics-application-forms` |

### From `C:\Users\loopn\.agents\skills`

| Source | Destination |
|--------|-------------|
| docx | archived 2026-08-15 → `D:\0Grok\0RAD\0del\skill_06_docx` (use system `docx`) |
| pdf | archived 2026-08-15 → `D:\0Grok\0RAD\0del\skill_06_pdf` (use system `pdf`) |
| xlsx | `06_automation/bundles/xlsx` |
| markitdown | `06_automation/bundles/markitdown` |
| pua | `06_automation/bundles/pua` |

### From `files.zip`

| Source | Destination |
|--------|-------------|
| literature-review | `01_research/bundles/literature-review` |
| pubmed-database | `01_research/bundles/pubmed-database` |
| citation-management | `01_research/bundles/citation-management` |
| radiomics-pipeline-toolkit | `03_imaging/bundles/radiomics-pipeline-toolkit` |
| ying-li-polisher | `04_writing/bundles/ying-li-polisher` |
| stop-slop | `04_writing/bundles/stop-slop` |
| ai-writing-detector | `04_writing/bundles/ai-writing-detector` |
| peer-review | `05_review/bundles/peer-review` |

## Conflict resolution

When two sources overlap:

1. **Lab voice / Radiology QC** wins for imaging SCI manuscripts (`ly-sci-writing`, `ly-prereview`, `radiology-stats`).
2. **Generic academic packs** (literature-review, peer-review, citation-management) supply broader methodology and scripts.
3. **Never invent** data, ethics IDs, citations, or unrun experiments — all sources agree.

## What stayed outside top-level skills

Nothing critical: all lab capabilities are nested under the seven skills. Future topics must first become a mode/reference/tool adapter, not skill #8.


## skills_export.zip (2026-08-11 merge)

User decisions:

| Export skill | Decision | Destination |
|--------------|----------|-------------|
| code-refactoring | **Overwrite** ly-rules | `06_automation/bundles/code-refactoring` (+ ly-rules redirect) |
| dicom-nifti-conversion | Scripts into ly-imaging-ops | `03_imaging/bundles/ly-imaging-ops/scripts/from_skills_export/dicom-nifti-conversion/` |
| file-batch-processing | Scripts into ly-imaging-ops | `.../from_skills_export/file-batch-processing/` |
| habitat-analysis | Scripts into toolkit | `03_imaging/bundles/radiomics-pipeline-toolkit/scripts/from_skills_export/habitat-analysis/` |
| radiomics-pipeline | Scripts into toolkit | `.../from_skills_export/radiomics-pipeline/` |
| statistical-modeling | Scripts into stats | `02_analysis/scripts/from_skills_export/statistical-modeling/` + data-impute `export_*` |
| paper-writing-review | Templates only | `04_writing/.../methods_template_export.md`, `05_review/.../review_checklist_export.md` |
| clinical-data-extraction | Full bundle | `06_automation/bundles/clinical-data-extraction` |
| fMRI-preprocessing | Full bundle | `03_imaging/bundles/fMRI-preprocessing` |
| tool-environment-setup | Full bundle | `06_automation/bundles/tool-environment-setup` |

## Session harvest (2026-08-19b)

| Fact | Home |
|------|------|
| Table 1 = training vs test wide table (not all-cohort +/− as main table) | `04_writing/bundles/ly-sci-writing/references/Aitor-format.md` |

## Session harvest (2026-08-19)

Nine 0RAD house→later-polish manuscript pairs. User choices: keep one-fact / no em-dash / no disclaimer / training·test (validation = external); **drop *coded*/*displayed* prefix**.

| Fact | Home |
|------|------|
| De-pipeline replacements; group `(A, n = ; B, n = )`; nomogram-row AUC; recheck incremental vs `*-results.html`; no *coded* prefix; later-polish corpus (do not copy fusion/em-dash/internal validation) | `04_writing/bundles/ly-sci-writing/references/Aitor-format.md` |
| Second pass does not reorder IMRAD; inclusion inline; *concerns* / *eventually* | `04_writing/bundles/ly-sci-writing/references/polisher-sections.md` |

Not written (user kept Aitor): sentence fusion, em-dash, disclaimer stacks, internal `development`/`validation`.

## Session harvest (2026-08-15)

Chat-locked lab rules written into existing skills (no new top-level skill):

| Fact | Home |
|------|------|
| 0RAD folders / `0del` / `exc` / false-classification | `06_automation/references/0rad-workspace.md` |
| `VAL_MODE`, pairwise groups, ID columns | `02_analysis/references/0rad-pipeline-rules.md` |

## Session harvest (2026-08-18)

| Fact | Home |
|------|------|
| 除 `dll_OV` 外默认全部组不筛；子结局分组来自该结局列；`FORCE_INTER` 缺键继承公共、结局间不互写；`SUBGROUP_COL` 只评估主列线图 | `02_analysis/references/0rad-pipeline-rules.md` |
| 工程根 `qc.html` 整体数据 QC | `06_automation/references/0rad-workspace.md` |
| Five console palettes | `04_writing/bundles/ly-figures/references/lab-palettes.md` |

Already owned elsewhere — not rewritten: `Aitor-format.md`, `strobe-flowchart`, `ethics-application-forms`, `data-impute` methods.

## Session harvest (2026-08-17)

| Fact | Home |
|------|------|
| IHC from 病理全文; dash = Negative; ER ≠ HER2 | `06_automation/bundles/clinical-data-extraction/MODULE.md` |

User picked only this row. Not written: write-to-xlsx-cln, first-date labs, mice+mode fallback, settings.ini seed, dll_OV handoff memo.

## skill-harvest (2026-08-15)

Maintenance skill at `~/.grok/skills/skill-harvest/` (not a domain skill).  
Scan chats + extra skill packs → classify → user picks → write into 00–06 homes only.  
Slash: `/skill-harvest`. Script: `scripts/harvest_scan.py`.
