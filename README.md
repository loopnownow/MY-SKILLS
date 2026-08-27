# MY-SKILLS

Medical / imaging research skills for Grok (and compatible agents). Layout mirrors `C:\Users\loopn\.grok\skills`.

## Layout

```
core/          Active skills 00–06 + skill-harvest
archive/       Standalone packs kept for reuse
_medical-research-meta/  Architecture, integration map, tests
ARCHITECTURE.md
SKILLS_map.html
```

| Skill | Role |
|-------|------|
| `00_orchestrator` | Routing and project workflows |
| `01_automation` | Excel/CSV, 0RAD workspace, batch files |
| `02_imaging` | Radiomics / MRI / QC |
| `03_research` | Study design, evidence, frontier, grants |
| `04_analysis` | Stats, prediction, nested `data-impute` |
| `05_manuscript` | SCI writing, polish, nested `figure-engine` |
| `06_review` | Pre-submission, peer review, response letters |
| `skill-harvest` | Governance / ROI |

Nested modules (not top-level skills): `data-impute`, `figure-engine`.

## Maintenance

This GitHub repo is the source of truth. Updates land here when requested; no local-folder scan.

Maintained by Aitee for [loopnownow](https://github.com/loopnownow).
