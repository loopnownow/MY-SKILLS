# MedicalResearch Skills — Integrated 7-Skill Architecture (v1.1.0)

Deliberately compact **seven-skill** architecture for medical / imaging research,
now **integrated with the Ying Li lab skill library** (`ly-*`, `radiology-skills`,
office adapters) and the standalone packs from `files.zip`.

## Seven skills

| # | Skill | Primary role | Integrated sources |
|---|--------|--------------|--------------------|
| 00 | `00_orchestrator` | Route & coordinate | shortcut map + `workflows/` + `templates/project-state.yaml` |
| 01 | `01_automation` | Excel/CSV, 0RAD workspace, batch files | `xlsx`, `0rad-workspace.md` |
| 02 | `02_imaging` | Radiomics, MRI, pipeline | radiomics-habitat, imaging-preprocessing-qc |
| 03 | `03_research` | Design, journal, frontier, grant | radiology-design/frontier, grant-writing |
| 04 | `04_analysis` | Stats, survival, ML, validation | `radiology-stats`, `statistical-analysis`, `data-impute` |
| 05 | `05_manuscript` | SCI 论著 writing, polish, I/D literature, figures | `manuscript-core`, `figure-engine`, `lab-palettes.md` |
| 06 | `06_review` | Pre-review, peer review, reviewer response | `manuscript-quality` |

## Architectural rules (unchanged)

- Software packages are **tools/adapters**, not separate top-level skills.
- Diseases / topics are **knowledge domains**, not separate skills.
- Manuscript sections are **modes** inside `05_manuscript`.
- Peer review / pre-submission audit / reviewer response are **modes** inside `06_review`.
- Statistical methods are **modes** inside `04_analysis`.
- Imaging modalities are **modes** inside `02_imaging`.
- Complex tasks are routed by `00_orchestrator`.

## Progressive disclosure

Each skill keeps a short `SKILL.md` entrypoint. Heavy material lives under:

- `bundles/<source-skill>/` — full absorbed skill (read its `SKILL.md` first)
- `references/` — domain checklists and radiology refs
- `scripts/` — runnable helpers when present

## Lab defaults (Ying Li / Jinshan Radiology)

When the user is writing imaging SCI papers for this lab:

1. Prose voice → `05_manuscript` → `bundles/manuscript-core` (+ ying-li-polisher)
2. Intro/Discussion citations → `05_manuscript` → `intro-discussion-evidence.md`
3. Pre-submission holes → `06_review` → `bundles/manuscript-quality`
4. Response letters → `06_review` → `bundles/manuscript-quality`
5. Code style → `archive/code-refactoring` (CONFIG on top, dry-run, checkpoint)
6. Imaging methods design (not prose) → `02_imaging` + design bits in `03_research`
7. Stats for Radiology-grade papers → `04_analysis` → `bundles/radiology-stats`

## Installation

Copy the active directories under your agent skills path, preserving names:

```
skills/core/00_orchestrator
...
skills/core/06_review
skills/archive/code-refactoring
skills/archive/ethics-application-forms
skills/archive/clinical-data-extraction
skills/archive/clinical-translation
```

Optional: keep this package root `README.md` / `ARCHITECTURE.md` / `INTEGRATION_MAP.md` nearby for humans.

## See also

- `ARCHITECTURE.md` — handoff contract and typical flows
- `INTEGRATION_MAP.md` — full source → destination map
- `tests/` — no-LLM skill-file evals (`python -m unittest discover -s _medical-research-meta/tests -v`)
- `benchmarks/` — case table for those evals
