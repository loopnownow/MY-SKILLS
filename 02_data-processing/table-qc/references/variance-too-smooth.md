# Between-group SD smoothness (heuristic)

## Use
Flag when several group SDs look unusually alike / under-noisy.

## Boundary
- This is **not** a full Carlisle Monte Carlo randomization audit.
- CV-of-SDs thresholds (e.g. < 0.02) are draft heuristics only.

## Draft trigger
- At least 3 group SDs
- mean(SD)=0 → constant-data risk
- Very small CV_of_SDs → too-smooth signal

## Reporting
- State "heuristic / not full Carlisle"
- Ask for raw distributions and outlier-handling logs
