# 02_data-processing personal route -- top layer

## A/B flow (2026-10-17)

1. **base first-pass** data-processing fine-IDs (`clean-data`, `batch-cohort`, `imaging-io`, `preprocess-imaging`, ...)
2. **00 QC**
3. **A02 re-loop** -- personal workspace/extract/coding protocols; may re-trigger B mounts when 00 says needed

## Personal load order

1. Workspace / folders / `exc` / false-classification -> `workspace.md`
2. Clinical / HIS / pathology **extraction** -> `extract.md`
3. Soft-coding / dry-run / refactor / complexity ladder -> `coding.md`
4. Deep code QC (Critical/Required/Optional) -> `../qc/coding-qc.md`
5. Raw numeric table digit / smoothness signals -> `table-signals.md`
6. Cooperation / raw->analysis-ready boundary -> `handoff.md`

**Seat:** Loopnow owns 02 execution. Modeling / feature selection / NHST -> hand off to `04_analysis` (see `handoff.md`).
