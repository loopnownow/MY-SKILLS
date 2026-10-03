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

Lab disks (not inside this repo): runnable SSOT `D:\0Grok\0scripts`; human-doc SSOT `D:\0Grok\0doc`. Skills keep rules + pointers — see `ARCHITECTURE.md` · Lab workspace SSOT.

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

A = framework + personal. B = default chassis. The menu shape (coarse buckets and fine ids) lives in `01_skill-discovery-integration/registry.yaml` and the generated index `01_skill-discovery-integration/MOUNTED_SKILLS.md` — do not restate the totals here. `session_mount: ask-each-run`, `session_pick_unit: fine_id`. Every independent run needs a mount decision; reuse `session_picked_fine_ids` when they already cover the task. The pick menu is status MOUNTED only. Never auto-mount a non-B source. Non-B fine ids are mixed PROPOSED/MOUNTED per registry. OpenClaw is not a default mount source.

## Maintenance

GitHub MY-SKILLS is the A framework source of truth. The B repo is the source of truth for B bytes. Non-B upstream is the source of truth for those bytes. `mounts-cap/` is a verified local cache, not a source of truth. `registry.yaml` is the routing index. Updates to this framework land here when requested; no local-folder scan.

Maintained by Aitor for [loopnownow](https://github.com/loopnownow).

## Cache ≠ Mount ≠ Active · Registry = index

| Term | Meaning |
|---|---|
| **Cache** | `mounts-cap/<pack>/` verified local bytes (gitignored pack trees). Not a source of truth |
| **Registry MOUNTED** | Catalog-approved and session-selectable |
| **session_picked_fine_ids** | Selected this run |
| **Active** | Actually loaded this run |
| **Registry** | Routing index only (`01_skill-discovery-integration/registry.yaml`) |

Cache is not mount is not active. B `cross-pack/` stubs are pointers. The fine-id ceiling is `fine_id_count_canonical` (merge/sub-capability preferred over a new fine id). Optional `load_priority: P0|P1|P2` is YAML metadata only.

