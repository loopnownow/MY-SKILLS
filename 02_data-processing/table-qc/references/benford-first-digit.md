# First-digit distribution (Benford)

## Use
Signal when multi-order-of-magnitude continuous measurements diverge from expected leading-digit frequencies.

## Upstream
https://github.com/milcent/benford_py

## Fit
- Counts/concentrations spanning orders of magnitude
- Prefer N >= 30 parseable leading digits

## Poor fit / false alarms
- Narrow clinical reference ranges
- Features already scaled into a fixed interval
- Discrete score instruments

## Reporting
- Report chi-square / p, N, threshold
- Phrase as a QC signal needing human review; do not assert fabrication as proven
