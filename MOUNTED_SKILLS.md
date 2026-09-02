# Mounted Skills Boundary

This repository is the personal framework / control layer.

`registry.yaml` currently has `mounts: []`. **No external Skill is mounted.**
`PROPOSED` is not `MOUNTED`. Never auto-mount.

Professional generic capability is supplied by a separately mountable package
[`loopnownow/MY-SKILLS-capabilities`](https://github.com/loopnownow/MY-SKILLS-capabilities)
and/or a future approved external Skill.

## How A mounts B

1. `01_skill-discovery-integration` evaluates a candidate and writes `interface.yaml`.
2. User explicitly approves.
3. Add the id to `registry.yaml` `mounts:` with status `MOUNTED`.
4. Record the id, source, and target layer in this file.
5. Domain SKILL.md files call **mounted ids**, not deleted `bundles/` paths.

Until step 3, keep using personal files plus local generic copies listed in `EXTERNALIZATION_CANDIDATES.md`.

## Mount target ids (capabilities pack; not mounted yet)

| Id | B path | Layer | Role |
|---|---|---|---|
| `02-xlsx` | `02-data-processing/xlsx/` | 02 | Excel/CSV automation |
| `02-imaging-qc` | `02-data-processing/imaging-qc/` | 02 | Imaging preprocessing QC docs |
| `02-radiomics-habitat` | `02-data-processing/radiomics-habitat/` | 02 | Radiomics/habitat preparation |
| `02-impute` | `02-data-processing/impute/` | 02 | Missing/outlier processing |
| `02-generic-docs` | `02-data-processing/generic-docs/` | 02 | Generic imaging/data notes |
| `03-literature` | `03-research/literature/` | 03 | Literature / sources / journals / datasets |
| `03-design` | `03-research/design/` | 03 | Study design / validation / blueprints |
| `03-frontier` | `03-research/frontier/` | 03 | Frontier themes / idea-to-question |
| `04-stats-generic` | `04-analysis/stats-generic/` | 04 | Generic statistical encyclopaedia |
| `04-figure-engine` | `04-analysis/figure-engine/` | 04 | Figure generation (moved out of 05) |
| `05-writing-generic` | `05-manuscript/writing-generic/` | 05 | Generic writing / reporting / citation / journal house style |
| `06-review-generic` | `06-review/review-generic/` | 06 | Generic prereview / response machinery |

## Proposed external candidates (not mounted)

- default-candidate: `https://github.com/Imbad0202/academic-research-skills` (`PROPOSED`)
- backup-candidate: `https://github.com/Aperivue/medsci-skills` (`PROPOSED`)

Rule: mounted Skill owns generic capability; MY-SKILLS owns orchestration, personalization, constraints, and Final QC.
