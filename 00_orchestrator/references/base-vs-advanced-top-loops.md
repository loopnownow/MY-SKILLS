# Base thin contract vs advanced detail

Short pointer. Full flow: `../runtime-flow.md`. Gates: `../gates.md`.

Owner lock 2026-10-30 (t1408u / t1409u): **base is a thin contract, detail lives in `advanced/`, `qc/` scores and cites `advanced/`.**

| | **base** | **advanced** | **qc** |
|---|---|---|---|
| Role | Thin contract for one fine id (`NN_slug/base/<pack>/`) | Personal revision authority (lab / Aitor / Jinshan) | Gate standard and scorecard |
| Holds | Purpose, inputs/outputs, hard bans, phase names, handoff card, `{code_*}` and path pointers | The detail: step order, word bands, typography, funnel beats, lab numbers, form fields, voice templates, polish procedures | Check ids, deduction codes, pass/fail, fail to rollback station, and the `advanced/` anchor to fix at |
| Does not hold | Step recipes, word bands, typography, funnel beats, lab numbers, form fields, voice templates, polish procedures | Gate pass/fail ownership (that stays with `qc/` plus 00) | Prose authority, or a second fix recipe |
| Read by | Specialist first pass | Specialist revise loop after QC | 00 at gate time |

**Runtime loop:** base thin first pass -> **00 QC** (score, cite the `advanced/` anchor) -> post-QC revise **via `advanced/`** -> re-gate at 00.

- A base pack that grows a recipe has drifted: the recipe belongs in that seat's `advanced/`, and base keeps the pointer.
- Every `qc/` check id that needs a fix carries a concrete `advanced/` anchor (file path plus heading). No orphan score line.
- `qc/` scores and cites; it does not rewrite prose authority.
- Fine IDs for stats-analysis / figures / data-processing / study-design unchanged.
- Registry rows use `source: my-skills` (in-repo `NN_slug/base/`).

**QC standards:** live in each domain `NN_slug/qc/`; `00_orchestrator/gates.md` decides WHEN / PASS-FAIL. Specialists and base first pass do not self-invoke `qc/`.
