# MY-SKILLS

Personal framework + lab layer for medical / imaging research (Grok and compatible agents).
Generic mountable capabilities live in a separate package: `loopnownow/MY-SKILLS-capabilities`.

Layout mirrors `C:\Users\loopn\.grok\skills`.

## Layout

```
00_orchestrator/
01_skill-discovery-integration/
02_data-processing/
03_research/
04_analysis/
05_manuscript/
06_review/
skill-harvest/
archive/       Empty of skills; four packs rehomed 2026-09-02 (see archive/README.md)
_medical-research-meta/  Architecture, integration map, tests
ARCHITECTURE.md
SKILLS_map.html
MOUNTED_SKILLS.md
EXTERNALIZATION_CANDIDATES.md
```

Skill paths are at most four parts from repo root: `<skill>/<category-or-pack>/<scripts|references|personal>/file`. No `core/`, no `bundles/`, no `merged/`.

| Skill | Role |
|-------|------|
| `00_orchestrator` | Classification, routing, composite workflows, Final QC + local recovery |
| `01_skill-discovery-integration` | Discover / evaluate / mount external Skills (not Excel) |
| `02_data-processing` | Raw → analysis-ready; Excel/0RAD; imaging prep; extraction; coding principles; no modeling |
| `03_research` | Research framework + literature (03 only) + personal grant supplement + translational design + ethics forms |
| `04_analysis` | Statistics, prediction, **figures** |
| `05_manuscript` | Personal writing upper layer (not figure-engine) |
| `06_review` | Personal review/response upper layer (reviewer response only here) |
| `skill-harvest` | Governance / ROI / evolution proposals |

A = framework + personal. B = mountable skills. `registry.yaml` `mounts: []` — nothing is mounted until explicit approval. Never auto-mount.

## Maintenance

This GitHub repo is the source of truth. Updates land here when requested; no local-folder scan.

Maintained by Aitor for [loopnownow](https://github.com/loopnownow).
