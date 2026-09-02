# MedicalResearch Skills — framework A (2026-09-02)

Personal **framework + lab layer**. Generic capabilities mount from `MY-SKILLS-capabilities` (B) or an approved external Skill. Nothing is mounted yet (`mounts: []`).

## Skills

| # | Skill | Primary role |
|---|--------|--------------|
| 00 | `00_orchestrator` | Classify, route, composite workflow, Final QC + local recovery |
| 01 | `01_skill-discovery-integration` | Discover / evaluate / mount external Skills |
| 02 | `02_data-processing` | Raw → analysis-ready; Excel/0RAD; imaging prep; extraction; coding principles; ethics forms (temp) |
| 03 | `03_research` | Design, literature (03 only), grants (personal supplement), translational design |
| 04 | `04_analysis` | Stats, prediction, figures; personal `radiology-stats` |
| 05 | `05_manuscript` | Personal writing upper layer |
| 06 | `06_review` | Personal review/response upper layer |
| — | `skill-harvest` | Evolution governance |

## Rules

- Software packages are tools, not top-level skills.
- Literature → 03 only. Figures → 04. Reviewer response → 06 only. Excel/0RAD/extraction/coding-principles/ethics-forms(temp) → 02. Translational design → 03.
- An A skill path ≤ 3 directories from repo root (`<skill>/<optional-folder>/file`). No `core/`, no `bundles/` in A.
- User approval required to mount or evolve. Never auto-mount.
- Former archive four packs rehomed under 02/03 (CHG-20260902-004).

## Tests

```
python -m unittest discover -s _medical-research-meta/tests -v
```

## See also

- `ARCHITECTURE.md` — handoff / QC / mount contract
- `INTEGRATION_MAP.md` — changelog including CHG-20260902-004
- `../MOUNTED_SKILLS.md`, `../EXTERNALIZATION_CANDIDATES.md`
