# MedicalResearch Skills

```
skills/
├── core/
│   ├── 00_orchestrator
│   ├── 01_automation
│   ├── 02_imaging
│   ├── 03_research
│   ├── 04_analysis
│   ├── 05_manuscript
│   ├── 06_review
│   └── skill-harvest
├── archive/
│   ├── ethics-application-forms
│   ├── code-refactoring
│   ├── clinical-data-extraction
│   └── clinical-translation
└── _medical-research-meta/
```

## Core (00–06)

1. `00_orchestrator` — routing and project workflows
2. `01_automation` — Excel/CSV, 0RAD workspace, batch files
3. `02_imaging` — MRI/fMRI, radiomics/habitat, QC
4. `03_research` — study design, evidence, frontier, journal/grant
5. `04_analysis` — statistics, prediction, nested `data-impute`
6. `05_manuscript` — SCI writing, nested `figure-engine`
7. `06_review` — pre-submission audit, peer review, reviewer response

`skill-harvest` is governance.

`data-impute` and `figure-engine` stay nested. They are not separate skills.

## Archive (standalone skills)

- `code-refactoring` — 软编码 / dry-run / CONFIG on top
- `ethics-application-forms` — 伦理申请表填报
- `clinical-data-extraction` — 检验 / 病理全文 / HIS
- `clinical-translation` — 转化 / reader study

Removed (not retained): `markitdown`, `tool-environment-setup`, `imaging-omics-ml`.

## Design rule

**One fact → one authoritative home.**
**One task → one entry point.**
**Nested MODULE ≠ discoverable skill.**
