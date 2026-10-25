# 02_data-processing personal route -- top layer

## A/B flow (2026-10-17)

1. **base first-pass** data-processing fine-IDs (`clean-data`, `imaging-io`, `preprocess-imaging`, ...)
2. **00 QC**
3. **A02 re-loop** -- personal workspace/extract/coding protocols; may re-trigger base mounts when 00 says needed

**Stats / figures half of 02** (merged 2026-10-25): `analysis/route.md`.

## Personal load order

1. Workspace / folders / `exc` / false-classification -> `{RULES}/workspace-layout.md`
2. Clinical / HIS / pathology **extraction** -> `extract.md`
3. Soft-coding / dry-run / refactor / complexity ladder -> `coding.md`
4. Deep code QC (Critical/Required/Optional) -> `../qc/coding-qc.md`
5. Raw numeric table digit / smoothness signals -> `table-signals.md`
6. Cooperation / raw->analysis-ready boundary -> `handoff.md`

**Seat:** Loopnow owns 02 execution. Modeling / feature selection / NHST stay in 02 -- `analysis/route.md` + `analysis/pipeline.md`.
