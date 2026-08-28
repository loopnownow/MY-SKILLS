# Type A — published STROBE patient-selection flowchart

Default Figure 1 for retrospective cohort / radiomics prediction papers.
Gold standard: **2023 BJR POLE Fig.1**, not the 0RAD auto figures.

Draw with `scripts/draw_strobe_flow.py`. Do not mix type B or C into this script.

## Layout (top → bottom)

White ground, black square boxes, Arial. Vertical spine.

1. **Top screened n** — disease + time window + `(n=N)`.
2. **Right inclusion**, horizontal arrow **IN** to the spine (arrowhead on the spine).
3. **Right exclusion**, horizontal arrow **OUT** from the spine (arrowhead on the box). Each reason carries `(n=k)`.
4. **Middle enrolled n** plus class counts (e.g. `35 POLE-mutant vs 103 non-POLE-mutant`).
5. **Bottom split:** Training Cohort / Validation Cohort. Never "Development set".
6. **No pipeline / analysis row.** MRI → habitat → LASSO does not belong on Figure 1.

Caption: `Figure 1. Flowchart of patient selection and study design.`

One endpoint per figure. Do not reuse one flow for several outcomes.

## Spec

```text
screened: "Patients with [condition] between [dates] (n=N)"
inclusion: ["...", "..."]
exclusion: ["reason (n=k)", ...]   OR   [{reason, n}, ...]
analyzed: "N patients enrolled ([A] vs [B])"
splits: [{label: "Training Cohort", n}, {label: "Validation Cohort", n}]
```

Parse n from text when the field is a sentence. Do not invent n.

## n-audit (fail-closed)

The script exits nonzero unless:

- `screened n − Σ exclusion n = analyzed n`
- `Σ splits n = analyzed n`

Every exclusion reason and every split must have a parseable n. Missing n is a fail, not a guess.

The published POLE figure itself is off by 3 (169 − (2+12+9+4+1=28) = 141, not 138). Reproduce that historical figure only with `--no-audit`. New papers must pass the audit; fix the counts in Methods, do not silence the gate.

## Clinical variant — Tao Yongqiong CID/MDD

Treatment / follow-up papers (not radiomics prediction) may use this variant. Still type A (patient flow), **not** a reason to call a methods pipeline.

- Combined **inclusion + exclusion** in the first right-hand box (arrow IN).
- Multi-stage spine: treatment → follow-up → MRI quality, with attrition boxes arrowing OUT at each stage.
- Bottom groups are **outcome arms** (High / Low responder), not Training / Validation.

Do not fold this variant into the default radiomics spec. Encode it only when the manuscript is that clinical design.

## Anti-pattern — 0RAD auto figures

Do not copy the laboratory auto-drawer:

| 0RAD auto | Published POLE |
|---|---|
| `spec.pop("inclusion")` — no inclusion box | Right inclusion, arrow IN |
| Exclusion often without per-reason n | Each reason `(n=k)` |
| Development / Validation | Training Cohort / Validation Cohort |
| Bottom pipeline bar (imaging → processing → model) | No pipeline row |
| Caption mentions "analysis flowchart" / "lower row summarizes imaging" | `Figure 1. Flowchart of patient selection and study design.` |
| One figure reused across endpoints | One figure per endpoint |

Type C methods cartoons (Yan Bicong gene panels, choline cell→mouse→MRS) must not call `draw_strobe_flow`. See `methods-pipeline.md`.
