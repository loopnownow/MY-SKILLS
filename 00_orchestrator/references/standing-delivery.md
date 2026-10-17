# Standing delivery rules (00 pointers)

## HTML

Whenever this lab **creates or edits** `.html`, follow [`html-visual-design.md`](html-visual-design.md) (structure, a11y, no CDN, palette). Full-repo HTML architecture audits are **off** until the user asks. Do **not** vendor lab console / starter HTML pages into MY-SKILLS (rules only).

## Visualization compiler

Archify is a read-only visualization compiler. It is not a skill and not a top-level `07` layer. MY-SKILLS sources stay authoritative. Contract lives under **`04_analysis/personal/visualization/`**: `visualization-architecture.md`, `archify-version.yaml`, `visualization-source-contract.yaml`. Rebuild: `python3 04_analysis/personal/visualization/scripts/gen_visualization.py` (pinned Archify via release URL / temp under `D:\0del`; zip not vendored in 00). Generated HTML under `{doc_root}/04-lab-reference/my-skills-viz` (default `D:/0Grok/0doc/04-lab-reference/my-skills-viz`; env `MY_SKILLS_VIZ_OUT` / `--out`) is disposable and is not a fact source. It is **not** committed under MY-SKILLS (`docs/` removed). Mount diagrams use registry and preset metadata. Do not crawl `{mounts_cap}/` (`D:/0Grok/0doc/04-lab-reference/mounts-cap`) to draw them.
