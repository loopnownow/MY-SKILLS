# Type C — methods pipeline (must not use draw_strobe_flow)

Radiomics-step cartoons, mechanism panels, animal/cell pipelines, and "how the model was built" figures.

**Do not call `scripts/draw_strobe_flow.py`.** That script draws type A published STROBE patient selection only. Passing a `pipeline` list is rejected.

Type C is a different figure: boxes for MRI / segmentation / feature extraction / LASSO / nomogram, or cell → mouse → MRS. It has no screened-n audit and no inclusion/exclusion arrows.

If the manuscript also needs patient selection, draw that as a separate type A Figure 1. Do not glue a methods bar under the STROBE spine (the 0RAD auto anti-pattern).

Imaging montages (annotated slices) stay in `imaging-panels.md`; they are not patient-flow and not a STROBE substitute.
