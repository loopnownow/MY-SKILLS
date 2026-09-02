# MY-SKILLS

Personal framework + lab layer for medical / imaging research (Grok and compatible agents).
Generic mountable capabilities live in a separate package: `loopnownow/MY-SKILLS-capabilities`.

Layout mirrors `C:\Users\loopn\.grok\skills`.

## Layout

```
core/          Active skills 00–06 + skill-harvest  (max 3 directory levels)
archive/       Standalone packs kept for reuse (not migrated this round)
_medical-research-meta/  Architecture, integration map, tests
ARCHITECTURE.md
SKILLS_map.html
```

| Skill | Role |
|-------|------|
| `00_orchestrator` | Classification, routing, composite workflows, Final QC + local recovery |
| `01_skill-discovery-integration` | Discover / evaluate / mount external Skills (not Excel) |
| `02_data-processing` | Raw → analysis-ready; Excel/0RAD; imaging prep; no modeling |
| `03_research` | Research framework + literature (03 only) + personal grant supplement |
| `04_analysis` | Statistics, prediction, **figures** |
| `05_manuscript` | Personal writing upper layer (not figure-engine) |
| `06_review` | Personal review/response upper layer (reviewer response only here) |
| `skill-harvest` | Governance / ROI / evolution proposals |

A = framework + personal. B = mountable skills. `registry.yaml` `mounts: []` — nothing is mounted until explicit approval. Never auto-mount.

## Maintenance

This GitHub repo is the source of truth. Updates land here when requested; no local-folder scan.

Maintained by Aitor for [loopnownow](https://github.com/loopnownow).
