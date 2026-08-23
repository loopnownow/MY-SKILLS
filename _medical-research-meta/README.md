# MedicalResearch Skills — Integrated 7-Skill Architecture (v1.1.0)

Deliberately compact **seven-skill** architecture for medical / imaging research,
now **integrated with the Ying Li lab skill library** (`ly-*`, `radiology-skills`,
office adapters) and the standalone packs from `files.zip`.

## Seven skills

| # | Skill | Primary role | Integrated sources |
|---|--------|--------------|--------------------|
| 00 | `00_orchestrator` | Route & coordinate | Lab workflow map |
| 01 | `01_research` | Literature, design, evidence | `ly-literature`, radiology design/frontier, literature-review, pubmed, citation-management |
| 02 | `02_analysis` | Stats, survival, ML, validation | `ly-stats-ml`, `data-impute` |
| 03 | `03_imaging` | Radiomics, MRI, DL, DICOM/ops | radiology modules, `ly-imaging-ops`, `ly-dl-libs`, radiomics-pipeline-toolkit |
| 04 | `04_writing` | Manuscript, polish, figures | `ly-sci-writing`, ying-li-polisher, stop-slop, ai-writing-detector, `ly-figures` (PPTX → system `pptx`) |
| 05 | `05_review` | Pre-review, peer review, response | `ly-prereview`, `ly-response`, peer-review |
| 06 | `06_automation` | Code rules, batch, office, ethics forms | `ly-rules`, ethics-application-forms, docx/pdf/xlsx/markitdown |

## Architectural rules (unchanged)

- Software packages are **tools/adapters**, not separate top-level skills.
- Diseases / topics are **knowledge domains**, not separate skills.
- Manuscript sections are **modes** inside `04_writing`.
- Statistical methods are **modes** inside `02_analysis`.
- Imaging modalities are **modes** inside `03_imaging`.
- Complex tasks are routed by `00_orchestrator`.

## Progressive disclosure

Each skill keeps a short `SKILL.md` entrypoint. Heavy material lives under:

- `bundles/<source-skill>/` — full absorbed skill (read its `SKILL.md` first)
- `references/` — domain checklists and radiology refs
- `scripts/` — runnable helpers when present

## Lab defaults (Ying Li / Jinshan Radiology)

When the user is writing imaging SCI papers for this lab:

1. Prose voice → `04_writing` → `bundles/ly-sci-writing` (+ ying-li-polisher)
2. Pre-submission holes → `05_review` → `bundles/ly-prereview`
3. Response letters → `05_review` → `bundles/ly-response`
4. Code style → `06_automation` → `bundles/code-refactoring` (CONFIG on top, dry-run, checkpoint)
5. Imaging methods design (not prose) → `03_imaging` + design bits in `01_research`
6. Stats for Radiology-grade papers → `02_analysis` → `bundles/ly-stats-ml/bundles/radiology-stats`

## Installation

Copy the seven directories under your agent skills path, preserving names:

```
skills/00_orchestrator
skills/01_research
...
skills/06_automation
```

Optional: keep this package root `README.md` / `ARCHITECTURE.md` / `INTEGRATION_MAP.md` nearby for humans.

## See also

- `ARCHITECTURE.md` — handoff contract and typical flows
- `INTEGRATION_MAP.md` — full source → destination map
