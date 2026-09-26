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
| `04_analysis` | Statistics, prediction, **figures** (`make-figures` / `fig-plot`) |
| `05_manuscript` | Personal writing upper layer (de-AI at `personal/`; B `05-manuscript/write-venue/` = journal templates / house style, not 选刊) |
| `06_review` | Personal review/response upper layer (reviewer response only here) |
| `skill-harvest` | Governance / ROI / evolution proposals |

A = framework + personal. B = default mounted source. Registry (v4, `01_skill-discovery-integration/registry.yaml`) is **10 coarse ids (welded stage buckets) → 52 fine ids (session-pick mount points)**, not a flat menu. `session_mount: ask-each-run`, `session_pick_unit: fine_id`. Pick fine ids each run; do not auto-load all. Never auto-mount a non-B source. MedSci/Scientific/AIPOCH/Nature stay PROPOSED backups; ARS/OpenClaw purged from catalog.

## Maintenance

This GitHub repo is the source of truth. Updates land here when requested; no local-folder scan.

Maintained by Aitor for [loopnownow](https://github.com/loopnownow).

## Cache ≠ Mount ≠ Active · Registry = index

| Term | Meaning |
|---|---|
| **Cache** | `mounts-cap/<pack>/` on-disk bytes (gitignored pack trees) |
| **Mount** | Session fine-id pick (registry pointer) |
| **Active** | Loaded into the agent this run |
| **Registry** | Index only (`01_skill-discovery-integration/registry.yaml`) |

External skill entity SSOT = cache. B `cross-pack/` stubs are pointers. **52 fine ids** is the v4 ceiling (merge/sub-capability preferred over new fine ids). Optional `load_priority: P0|P1|P2` is YAML metadata only.

