# MedicalResearch Skills — framework A (2026-09-03)

Personal **framework + lab layer**. Generic capabilities mount from `MY-SKILLS-capabilities` (**B**, default chassis) or an approved external Skill. Menu shape is `01_skill-discovery-integration/registry.yaml` and the generated `MOUNTED_SKILLS.md` (do not restate totals here). `session_mount: ask-each-run`, `session_pick_unit: fine_id` — not `mounts: []`. Non-B fine ids are mixed PROPOSED/MOUNTED per registry. OpenClaw is not a default mount source.

## Skills

| # | Skill | Primary role |
|---|--------|--------------|
| 00 | `00_orchestrator` | Classify, route, composite workflow, Final QC + local recovery |
| 01 | `01_skill-discovery-integration` | Discover / evaluate / mount external Skills; default source B |
| 02 | `02_data-processing` | Raw → analysis-ready; Excel/0RAD; imaging prep; extraction; coding principles |
| 03 | `03_research` | Design, literature (03 only), **选刊**, grants (personal supplement), translational design, **ethics forms** |
| 04 | `04_analysis` | Stats, prediction, figures (`make-figures` / `fig-plot`); lab notes in `personal/` |
| 05 | `05_manuscript` | Personal writing upper layer; B `05-manuscript/write-venue/` = journal templates / house style (not 选刊); de-AI at `personal/` |
| 06 | `06_review` | Personal review/response upper layer |
| — | `skill-harvest` | Evolution governance |

## Rules

- Software packages are tools, not top-level skills.
- Literature → 03 only. Figures → 04. Reviewer response → 06 only. Excel/0RAD/extraction/coding-principles → 02. Ethics forms + translational design → 03. 选刊 → `03_research` (not 05). 样本量 → `04_analysis` (`calc-sample-size`).
- An A skill path ≤ 4 directories from repo root (`<skill>/<category-or-pack>/<scripts|references|personal>/file`). No `core/`, no `bundles/` in A.
- User approval required to mount or evolve. Never auto-mount a non-B source. Non-B status is per registry, not an all-PROPOSED backup set.
- Former archive four packs rehomed under 02/03 (CHG-20260902-004). Ethics fill pack is under 03, not 02. Former `radiology-stats/` folder is merged into `04_analysis/personal/`.

## Tests

```
python -m unittest discover -s _medical-research-meta/tests -v
```

## See also

- `ARCHITECTURE.md` — handoff / QC / mount contract (agrees with root `ARCHITECTURE.md`)
- `INTEGRATION_MAP.md` — changelog including CHG-20260903-014
- `../MOUNTED_SKILLS.md`, `../EXTERNALIZATION_CANDIDATES.md`
