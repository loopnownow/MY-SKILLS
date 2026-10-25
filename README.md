# MY-SKILLS

Live medical and imaging research skill library for Grok Bot seats `00`–`07`.

| Seat | Folder | Role |
|------|--------|------|
| 00 orchestrator | `00_orchestrator` | Intent, skill chain, QC closed loop; registry / index / session-pick |
| 02 data-processing | `02_data-processing` | Raw → analysis-ready; Excel and batch workspace; imaging prep; extraction; coding principles; statistics, prediction, figures (`draw-flowchart` / `plot-figures`) |
| 03 research | `03_research` | Study design, literature, journal selection, grants, ethics forms |
| 05 manuscript | `05_manuscript` | Scientific writing and de-AI |
| 06 review | `06_review` | Peer review (Lee) |
| 07 response | `07_response` | Reviewer response (Aitee) |

Capability bodies for seats 02–07 live in-repo under `NN_slug/base/`. The routing index is `00_orchestrator/registry.yaml`. Lab path aliases (`{code_root}`, `{doc_root}`, `STATS_ROOT`, and the rest) are in `00_orchestrator/references/lab-paths.yaml`. Runnable code stays on `{code_root}`; human docs stay on `{doc_root}`. This repo is not a vendor of `0doc\_code`.

Paths under `00`–`07` are at most five parts from the repo root, except `NN_slug/base/**`.

License: MIT (`LICENSE`). Third-party notices: `NOTICE`. Release notes: `VERSION.txt`.

Tests: `python -m unittest discover -s tests`.

Maintained by Aitor for [loopnownow](https://github.com/loopnownow).
