# Standing delivery rules (00 pointers)

## HTML

Whenever this lab **creates or edits** `.html`, follow [`html-visual-design.md`](html-visual-design.md) (structure, a11y, no CDN, palette). Full-repo HTML architecture audits are **off** until the user asks. Do **not** vendor lab console / starter HTML pages into MY-SKILLS (rules only).

## Visualization compiler

Archify is a read-only visualization compiler. It is not a skill and not a top-level `07` layer. MY-SKILLS sources stay authoritative. Contract: [`../visualization-architecture.md`](../visualization-architecture.md), [`../archify-version.yaml`](../archify-version.yaml), [`../visualization-source-contract.yaml`](../visualization-source-contract.yaml). Rebuild derived files with `python3 scripts/gen_visualization.py`, which renders the two diagrams through the pinned `archify-v3.0.1.zip`. Generated HTML under `docs/` is disposable and is not a fact source. Mount diagrams use registry and preset metadata. Do not crawl `mounts-cap/` to draw them.
