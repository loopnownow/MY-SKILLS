# Table signals (raw numeric tables)

> Relocated from `table-qc/` → `02_data-processing/personal/table-signals.md` (2026-10-16).

## Purpose

Lightweight **signals** on raw numeric tables. Human review decides; nothing here proves misconduct.

Raw measurement table QC signals: leading-digit distribution, terminal-digit preference, between-group SD smoothness heuristic, optional near-duplicate rows. Use when auditing assay/clinical numeric tables before analysis. Not for code structure QC (`02_data-processing/personal/coding.md` / `../qc/coding-qc.md`), imaging ROI QC, skill-harvest evolution, or reported NHST/Table1 math (`02_data-processing/qc/report-checks.md`).

## Boundaries

- Not `02_data-processing/personal/coding.md` / `02_data-processing/qc/coding-qc.md` (deep code QC)
- Not archived `skill-harvest/qc/` / MY-RULES skills.md (skill-evolution)
- Not `preprocess-imaging`
- Reported stats consistency → `02_data-processing/qc/report-checks.md`
- No vendored checker scripts in this pack; Loopnow/Build may implement runners later

## Upstream (links only)

- https://github.com/milcent/benford_py
- https://github.com/lorenz-walthert/scrutiny
- https://github.com/ekzhu/datasketch

---

## First-digit distribution (Benford)

### Use
Signal when multi-order-of-magnitude continuous measurements diverge from expected leading-digit frequencies.

### Upstream
https://github.com/milcent/benford_py

### Fit
- Counts/concentrations spanning orders of magnitude
- Prefer N >= 30 parseable leading digits

### Poor fit / false alarms
- Narrow clinical reference ranges
- Features already scaled into a fixed interval
- Discrete score instruments

### Reporting
- Report chi-square / p, N, threshold
- Phrase as a QC signal needing human review; do not assert fabrication as proven

---

## Terminal-digit preference

### Use
Check whether trailing decimals over-use 0/5 or avoid other digits (manual entry pattern).

### Upstream
https://github.com/lorenz-walthert/scrutiny

### Fit
- Values with enough decimal places from semi-manual entry
- Prefer >= 20 values with a decimal point

### Caution
- Instrument resolution can force non-uniform terminals (false positive) — rule out device step first
- Independent from Benford; may run in parallel

### Reporting
- Uniformity chi-square p; share of digits 0+5
- Label as preference signal, not a clinical conclusion

---

## Between-group SD smoothness (heuristic)

### Use
Flag when several group SDs look unusually alike / under-noisy.

### Boundary
- This is **not** a full Carlisle Monte Carlo randomization audit.
- CV-of-SDs thresholds (e.g. < 0.02) are draft heuristics only.

### Draft trigger
- At least 3 group SDs
- mean(SD)=0 → constant-data risk
- Very small CV_of_SDs → too-smooth signal

### Reporting
- State "heuristic / not full Carlisle"
- Ask for raw distributions and outlier-handling logs

---

## Near-duplicate row / block screen (optional)

### Use
Fast screen for highly similar row blocks in large measurement tables.

### Upstream
- https://github.com/ekzhu/datasketch
- https://github.com/dedupeio/dedupe

### Fit
Large assay tables or multi-batch concatenations.

### Out of scope this round
Image / blot / micrograph copy-move checks.
