# MY-SKILLS

Personal framework + lab layer for medical / imaging research (Grok and compatible agents).
Generic mountable capabilities live in a separate package: `loopnownow/MY-SKILLS-capabilities`.

Layout mirrors `C:\Users\loopn\.grok\skills`.

## Layout

```
00_orchestrator/
01_skill-discovery-integration/
mounts-cap/   Local cache: full B + on-demand backup skills (gitignored bytes)
02_data-processing/
03_research/
04_analysis/
05_manuscript/
06_review/
skill-harvest/
_medical-research-meta/  Architecture, integration map, tests
ARCHITECTURE.md
MOUNTED_SKILLS.md          stub → 01 registry
EXTERNALIZATION_CANDIDATES.md
```

Skill paths are at most four parts from repo root: `<skill>/<category-or-pack>/<scripts|references|personal>/file`. No `core/`, no `bundles/`, no `merged/`.

| Skill | Role |
|-------|------|
| `00_orchestrator` | Intent classify, skill chain, QC closed loop (file gates + local recovery) |
| `01_skill-discovery-integration` | Discover / evaluate / mount; pointers + `mounts/*.md` live here; default source B; bytes in `mounts-cap/` |
| `02_data-processing` | Raw → analysis-ready; Excel/0RAD; imaging prep; extraction; coding principles; no modeling |
| `03_research` | Research framework + literature (03 only) + **选刊** + personal grant supplement + translational design + ethics forms |
| `04_analysis` | Statistics, prediction, **figures** (`04-fig-flow` / `04-fig-plot`) |
| `05_manuscript` | Personal writing upper layer (de-AI at `personal/`; `05-write-venue` = journal templates / house style, not 选刊) |
| `06_review` | Personal review/response upper layer (reviewer response only here) |
| `skill-harvest` | Governance / ROI / evolution proposals |

A = framework + personal. B = default mounted source. Registry lists **30 coarse ids** as a `MOUNTED` **menu** (`session_mount: ask-each-run`). Pick packs each run; do not auto-load all. Never auto-mount a non-B source. ARS/MedSci/Scientific stay PROPOSED backups.

## Maintenance

This GitHub repo is the source of truth. Updates land here when requested; no local-folder scan.

Maintained by Aitor for [loopnownow](https://github.com/loopnownow).
