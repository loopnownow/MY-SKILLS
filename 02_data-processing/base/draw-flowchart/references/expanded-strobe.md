# Type A′ — expanded STROBE (pre-split cohorts + downsample)

Same visual contract as type A ([style.md](style.md)): white ground, 1 pt black square
boxes, Arial, arrows on a spine, PDF preferred, 16 cm page width, same caption.
Only the cohort arithmetic is one level deeper.

```
screened ─▶ pre-split arm 1 ─▶ (downsample) ─▶ final cohort 1 ┐
         └▶ pre-split arm 2 ────────────────▶ final cohort 2 ┴▶ analyzed
```

Use it when the study splits **before** resampling: a class-imbalance downsample is
applied inside one arm, so `screened → analyzed` does not close without the dropped n.

Draw with `scripts/draw_strobe_flow_expanded.py --json spec.json --out Figure1_flow.pdf`.
Do not drive type B or C from it, and do not put a pipeline row in the spec.

## Spec

```json
{
  "layout": "expanded-split-downsample",
  "screened": "Patients with [condition] between [dates] (n=458)",
  "inclusion": ["criterion 1", "criterion 2"],
  "presplit": {
    "training": {"n": 320, "pp": 37, "non_pp": 283},
    "test":     {"n": 138, "pp": 16, "non_pp": 122}
  },
  "downsample": {"n": 209, "reason": "Training-set downsampling ...", "class": "non_pp"},
  "analyzed": "249 patients analyzed (53 positive vs 196 negative)",
  "splits": [
    {"label": "Training Cohort", "n": 111, "pp": 37, "non_pp": 74},
    {"label": "Test Cohort",     "n": 138, "pp": 16, "non_pp": 122}
  ],
  "pos_name": "pseudoprogression"
}
```

| Key | Meaning |
|---|---|
| `layout` | Must be `expanded-split-downsample` when present; any other value is refused (type A lives in `draw_strobe_flow`). |
| `presplit` / `arms` | Dict of arms (insertion order = left → right) or list. `n`, `pp`, `non_pp` parse from text as in type A. `label` defaults from the dict key. |
| `downsample` | One dict, or a list with `arm` (index or label) for several arms. `n` is the number **removed**; `class` is `non_pp` (default) or `pp`. `reason` becomes the box text. |
| `splits` / `cohorts` | One entry per pre-split arm, **paired by index**. |
| `analyzed` | Text of the bottom box; the trailing/phrase n is parsed for the audit. |
| `pos_name` | Wording for the `pp` class in generated boxes (default `positive`). Per-box `text` overrides any generated wording. |
| `font_size` | Optional override of the house 8.3 pt. |

Project numbers and sentences belong in the project's own `ref/*.json`; the script
must stay free of group constants.

## n-audit (fail-closed)

Exits nonzero unless all of these close:

- `arm.n == arm.pp + arm.non_pp`
- `arm.n − downsample.n == cohort.n` (arms without a downsample: `arm.n == cohort.n`)
- `cohort.n == cohort.pp + cohort.non_pp`
- `screened n == Σ arm.n`
- `Σ cohort.n == analyzed n`
- `Σ cohort.pp == Σ arm.pp − Σ downsampled pp`
- `Σ cohort.non_pp == Σ arm.non_pp − Σ downsampled non_pp`

Every n must be parseable. Missing n is a failure, not a guess. `--no-audit` is only
for reproducing a historical printed figure whose numbers genuinely do not add up, and
that mismatch must be documented in the manuscript file.
