# Terminal-digit preference

## Use
Check whether trailing decimals over-use 0/5 or avoid other digits (manual entry pattern).

## Upstream
https://github.com/lorenz-walthert/scrutiny

## Fit
- Values with enough decimal places from semi-manual entry
- Prefer >= 20 values with a decimal point

## Caution
- Instrument resolution can force non-uniform terminals (false positive) — rule out device step first
- Independent from Benford; may run in parallel

## Reporting
- Uniformity chi-square p; share of digits 0+5
- Label as preference signal, not a clinical conclusion
