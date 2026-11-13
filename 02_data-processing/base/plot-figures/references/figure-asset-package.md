# Figure asset package — final set vs raw library

For a manuscript whose figures ship as a set. Plotting rules stay in MODULE and the format files;
this file governs **what is shipped and how the set is inventoried**.

## 1 Two-layer layout

| Layer | Role |
|---|---|
| `01_终版/` | What gets submitted: stitched multi-panel figures plus the single panels cited in the text. Physical files, about 2.0 GB in the measured set. |
| `02_原始库/` | Full raw library (every export and version), reached through one directory junction per figure. The canonical library is about 8.9 GB and is **not** duplicated on disk. |

- Junction, not copy: a copy doubles the disk and drifts from the source. A junction keeps the raw
  library reachable from the figure folder without a second tree.
- The canonical raw library is never deleted or renamed — a dangling junction leaves no recoverable set.
- Submission files come only from `01_终版/`. Pulling raw-library files in requires copying them to
  `01_终版/` first and re-running the render QA.

## 2 Per-figure confidence

| Mark | Meaning |
|---|---|
| A | Final figure (or single-gene panel) matches the text and can be used as-is |
| B | Best candidate exists but needs a visual lock before use |

B is a to-do, not a defect. Never upgrade B to A because the file name looks right.

## 3 Inventory sheet

One row per figure or panel: `图 | 目录 | 文件数 | 大小 | 置信 | 文内对应`. The measured set ran to
1,714 rows. The sheet is the map of the deliverable; without it the set cannot be audited later.

- Gaps are explicit: `⚠ 缺 <file>` — measured case: the text cites TYR for Fig 6 while `v3` holds no
  `TYR.pdf`.
- Suspect files carry `[可疑]` and stay as candidates; do not silently pick one. Measured cases:
  `图源\HE D62.ai` is named D62 while the text says D72; `4.7.tif` may belong to Fig 7, so Fig 6
  keeps `4.6.tif` until confirmed.

## 4 Pre-delivery check

1. Every file cited in the text resolves inside `01_终版/`.
2. Every junction resolves and the canonical library still exists under its original name.
3. The inventory sheet is current: row count, sizes, confidence marks.
4. Gap and suspect rows are shown to the user, not resolved silently.
