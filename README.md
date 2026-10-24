# MY-SKILLS

Personal framework + lab layer for medical / imaging research.
Agents load skills from {skills_runtime} (= this GitHub clone / {skills_git}; former .grok\skills retired 2026-10-23). Compatible with Cursor / Grok Build / Cline when that tree is on the skill path.
Capability bodies for domains 02-07 live in-repo under `NN_slug/base/` (`source: my-skills`).

License: MIT (`LICENSE`). Third-party notices: `NOTICE`.
Path aliases: `00_orchestrator/references/lab-paths.yaml`.

## Layout

```
00_orchestrator/
01_skill-integration/
02_data-processing/          # + base/ capability bodies
03_research/
04_analysis/
05_manuscript/
06_review/
07_response/
ARCHITECTURE.md
```

# mounts-cap lab pack-cache: RETIRED 2026-10-20 — {mounts_cap} = D:/00db/_lab/originals/_leftover-20261024/_by-function/mounts-cap-retired-20261020 (do not use; 0del cleared 2026-10-24)


Skill paths are at most five parts from repo root: `<skill>/<category-or-pack>/<scripts|references|personal>/<optional-leaf>/file`. No `core/`, no `bundles/`, no `merged/`. Vendored third-party libraries may nest deeper (e.g. `02_data-processing/base/clean-data/xlsx-office/scripts/office/**`); they are byte-faithful copies, not skill bodies.

Lab disks (not inside this repo): runnable SSOT `{code_root}`; human-doc SSOT `{doc_root}`. Skills keep rules + pointers — see `ARCHITECTURE.md` · Lab workspace SSOT.

| Skill | Role |
|-------|------|
| `00_orchestrator` | Intent classify, skill chain, QC closed loop (file gates + local recovery) |
| `01_skill-integration` | Registry / index / session-pick only; hybrid deny under `references/`; default source in-repo `my-skills`; bodies in `NN_slug/base/` |
| `02_data-processing` | Raw → analysis-ready; Excel/0RAD; imaging prep; extraction; coding principles; no modeling |
| `03_research` | Research framework + literature (03 only) + **journal selection** + personal grant supplement + translational design + ethics forms |
| `04_analysis` | Statistics, prediction, **figures** (`draw-flowchart` / `plot-figures`) |
| `05_manuscript` | Personal writing upper layer (de-AI at `personal/`; `05_manuscript/base/write-venue/` = journal templates / house style, not journal selection) |
| `06_review` | Personal review upper layer (Lee); reviewer response → `07_response` |
| `07_response` | Response-letter upper layer (Aitee) |
| *(archived)* | Former `skill-harvest` → `{DEL}\00_orchestrator_reorg_20261017\skill-harvest_MY-SKILLS\`; standing policy → MY-RULES `skills.md` (skill-evolution) |

Path depth: under `00`–`07`, at most **five** path parts from repo root (pytest `test_core_max_five_path_parts`; exceptions: `NN_slug/base/**` (in-repo capability bodies; includes former find-journal data years)). A = framework + personal + in-repo `base/` chassis. The menu shape (coarse buckets and fine ids) lives in `01_skill-integration/registry.yaml` only — do not restate the totals here.


## Generated visualization

Generated HTML + JSON IR viz goes to the dir given by `--out` / `MY_SKILLS_VIZ_OUT` (required; former `my-skills-viz` retired 2026-10-20; not a committed `docs/` tree). Rebuild locally via `04_analysis/personal/visualization/scripts/gen_visualization.py` (no in-repo `.github` CI). Tests live under `tests/`; architecture notes in root `ARCHITECTURE.md` (former `docs/` / `.github/` archived under `D:/0del`).
## Maintenance

GitHub MY-SKILLS is the framework + capability-body source of truth. Capability bodies for domains 02-07 live in-repo under `NN_slug/base/` (`source: my-skills`). The former `{mounts_cap}/` lab pack-cache is retired (2026-10-20) and is not a source of truth for live bodies. `registry.yaml` is the routing index. Updates to this framework land here when requested; no local-folder scan.

Maintained by Aitor for [loopnownow](https://github.com/loopnownow).

## Cache ≠ Mount ≠ Active · Registry = index

| Term | Meaning |
|---|---|
| **Cache** | `{mounts_cap}/<pack>/` RETIRED 2026-10-20; bytes moved to `{DEL}/_by-function/mounts-cap-retired-20261020/`. Not a source of truth for live bodies |
| **Registry MOUNTED** | Catalog-approved and session-selectable |
| **session_picked_fine_ids** | Selected this run |
| **Active** | Actually loaded this run |
| **Registry** | Routing index only (`01_skill-integration/registry.yaml`) |

Cache is not mount is not active. In-repo `base/` holds capability bodies. The fine-id ceiling is `fine_id_count_canonical` (merge/sub-capability preferred over a new fine id). Optional `load_priority: P0|P1|P2` is YAML metadata only.

