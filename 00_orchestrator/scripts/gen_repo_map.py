#!/usr/bin/env python3
"""Generate repo-map.html: an offline, self-contained index of the skill
library for the user (not a recommendation artifact — a read-only map).

Activates the dormant hook noted in
00_orchestrator/references/html-visual-design.md ("full-repo architecture
audit ... keep dormant until the user asks"). Follows that file's hard
rules: no CDN, semantic HTML, one accent, offline-openable, meta line
stating what generated it and when.

Data source: 01_skill-discovery-integration/registry.yaml (single source of
truth — this script never hand-lists coarse/fine ids).

Dependency: PyYAML (`pip install pyyaml`).

Usage:
    python3 00_orchestrator/scripts/gen_repo_map.py [--check]
"""
from __future__ import annotations

import argparse
import datetime as dt
import html
import re
import sys
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
REGISTRY = ROOT / "01_skill-discovery-integration" / "registry.yaml"
OUTPUT = HERE.parent / "repo-map.html"

CSS = """
:root{--bg:#f7f8fa;--surface:#fff;--border:#e2e5ea;--text:#1a1d24;--text-dim:#5b6270;
--accent:#3b5bdb;--ok:#2f9e44;--warn:#e8890c;--radius-s:4px;--radius-m:8px;--radius-l:16px;}
*{box-sizing:border-box;}
body{margin:0;font-family:system-ui,-apple-system,"Segoe UI",sans-serif;background:var(--bg);
color:var(--text);font-size:16px;line-height:1.5;}
header{padding:20px 24px;background:var(--surface);border-bottom:1px solid var(--border);}
header h1{margin:0 0 4px;font-size:1.4rem;font-weight:600;}
.meta{color:var(--text-dim);font-size:.8rem;}
main{padding:20px 24px;max-width:1200px;margin:0 auto;}
#search{width:100%;max-width:420px;padding:8px 12px;font-size:.9rem;border:1px solid var(--border);
border-radius:var(--radius-s);margin-bottom:20px;background:var(--surface);color:var(--text);}
#search:focus-visible{outline:2px solid var(--accent);outline-offset:1px;}
.coarse{margin-bottom:28px;}
.coarse h2{font-size:1.05rem;font-weight:600;margin:0 0 4px;}
.coarse .domain{color:var(--text-dim);font-size:.78rem;margin-bottom:10px;}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:10px;}
.card{background:var(--surface);border:1px solid var(--border);border-radius:var(--radius-m);
padding:12px 14px;transition:border-color .2s;}
.card:hover,.card:focus-within{border-color:var(--accent);}
.card .id{font-family:ui-monospace,monospace;font-size:.82rem;font-weight:600;}
.card .label{font-size:.85rem;color:var(--text-dim);margin:2px 0 8px;}
.card .row{display:flex;justify-content:space-between;font-size:.75rem;color:var(--text-dim);
border-top:1px solid var(--border);padding-top:6px;margin-top:6px;}
.status{padding:1px 8px;border-radius:999px;font-size:.7rem;font-weight:600;}
.status.mounted{background:#ebfbee;color:var(--ok);}
.status.proposed{background:#fff4e6;color:var(--warn);}
.hidden{display:none;}
footer{padding:16px 24px;color:var(--text-dim);font-size:.75rem;}
@media print{#search{display:none;}}
"""

JS = """
const q = document.getElementById('search');
q.addEventListener('input', () => {
  const v = q.value.trim().toLowerCase();
  document.querySelectorAll('.card').forEach(c => {
    c.classList.toggle('hidden', v && !c.dataset.blob.includes(v));
  });
  document.querySelectorAll('.coarse').forEach(section => {
    const anyVisible = [...section.querySelectorAll('.card')].some(c => !c.classList.contains('hidden'));
    section.classList.toggle('hidden', !anyVisible);
  });
});
"""


SOP_SVG = """
<svg viewBox="0 0 920 200" role="img" aria-label="00 orchestrator full-project SOP flow" style="width:100%;height:auto;">
  <defs>
    <marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 z" fill="var(--text-dim)"/>
    </marker>
  </defs>
  <style>
    .node rect{fill:var(--surface);stroke:var(--border);rx:8;}
    .node text{fill:var(--text);font:600 13px system-ui,sans-serif;text-anchor:middle;}
    .node .sub{fill:var(--text-dim);font:400 10px system-ui,sans-serif;}
    .edge{stroke:var(--text-dim);stroke-width:1.5;fill:none;marker-end:url(#arrow);}
    .gate{fill:var(--warn);font:600 10px ui-monospace,monospace;text-anchor:middle;}
  </style>
  <!-- nodes: 03 -> 02 -> 04 -> 05 -> 06, gates between -->
  <g class="node"><rect x="10" y="70" width="150" height="50"/><text x="85" y="92">03_research</text><text class="sub" x="85" y="108">design · lit · 选刊</text></g>
  <g class="node"><rect x="200" y="70" width="150" height="50"/><text x="275" y="92">02_data-processing</text><text class="sub" x="275" y="108">if data / imaging</text></g>
  <g class="node"><rect x="390" y="70" width="150" height="50"/><text x="465" y="92">04_analysis</text><text class="sub" x="465" y="108">stats · figures</text></g>
  <g class="node"><rect x="580" y="70" width="150" height="50"/><text x="655" y="92">05_manuscript</text><text class="sub" x="655" y="108">prose · de-AI</text></g>
  <g class="node"><rect x="760" y="70" width="150" height="50"/><text x="835" y="92">06_review</text><text class="sub" x="835" y="108">pre-review · response</text></g>
  <path class="edge" d="M160,95 H200"/>
  <path class="edge" d="M350,95 H390"/>
  <path class="edge" d="M540,95 H580"/>
  <path class="edge" d="M730,95 H760"/>
  <text class="gate" x="180" y="60">G-PHI</text>
  <text class="gate" x="370" y="60">G-04</text>
  <text class="gate" x="560" y="60">G-FACT / G-05</text>
  <text class="gate" x="745" y="60">G-06</text>
  <text x="460" y="20" text-anchor="middle" fill="var(--text-dim)" font-size="11">Full project SOP · session mount pick (01) before every node · G0 checks project-state.yaml mounts each run</text>
  <text x="460" y="180" text-anchor="middle" fill="var(--text-dim)" font-size="10">Other entries: 06 alone (reviewer response) · 05 alone (revision) · 01 (new capability, network first)</text>
</svg>
"""


def load_registry() -> dict:
    return yaml.safe_load(REGISTRY.read_text(encoding="utf-8"))


def esc(s: str) -> str:
    return html.escape(str(s), quote=True)


def render(reg: dict) -> str:
    meta = reg["meta"]
    coarse_ids = reg["coarse_ids"]
    mounts = reg["mounts"]

    sections = []
    for coarse in coarse_ids:
        cid = coarse["id"]
        rows = [m for m in mounts if m.get("coarse") == cid]
        if not rows:
            continue
        cards = []
        for m in rows:
            status = m.get("status", "")
            status_class = "mounted" if status == "MOUNTED" else "proposed"
            blob = esc(f"{m['id']} {m['label']} {m['source']} {m['path']} {status}".lower())
            cards.append(f"""
        <div class="card" data-blob="{blob}">
          <div class="id">{esc(m['id'])}</div>
          <div class="label">{esc(m['label'])}</div>
          <div class="row"><span>{esc(m['source'])}</span>
            <span class="status {status_class}">{esc(status)}</span></div>
        </div>""")
        a_domain = coarse.get("a_domain", "")
        sections.append(f"""
      <section class="coarse">
        <h2>{esc(cid)}</h2>
        <div class="domain">a_domain: {esc(a_domain)} · {len(rows)} fine ids</div>
        <div class="grid">{''.join(cards)}</div>
      </section>""")

    now = dt.datetime.now().strftime("%Y-%m-%d %H:%M")
    return f"""<!DOCTYPE html>
<html lang="zh">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>MY-SKILLS repo map</title>
<style>{CSS}</style>
</head>
<body>
<header>
  <h1>MY-SKILLS — repo map</h1>
  <div class="meta">Generated {now} from registry.yaml v{meta['version']}
    ({meta['coarse_id_count']} coarse · {meta['fine_id_count_canonical']} fine) —
    read-only index, not a recommendation artifact. Regenerate with
    <code>00_orchestrator/scripts/gen_repo_map.py</code> after editing registry.yaml.</div>
</header>
<main>
  <section class="coarse">
    <h2>00 orchestrator — full-project SOP</h2>
    <div class="domain">hand-authored from 00_orchestrator/SKILL.md "Composite workflows" — resync manually if that section changes</div>
    {SOP_SVG}
  </section>
  <input id="search" type="search" placeholder="筛选 id / label / source / status…"
    aria-label="Filter skills">
  {''.join(sections)}
</main>
<footer>Source of truth: 01_skill-discovery-integration/registry.yaml. This page never hand-lists ids.</footer>
<script>{JS}</script>
</body>
</html>
"""


def strip_timestamp(text: str) -> str:
    return re.sub(r"Generated \d{4}-\d{2}-\d{2} \d{2}:\d{2} from", "Generated <ts> from", text)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    reg = load_registry()
    generated = render(reg)

    if args.check:
        current = OUTPUT.read_text(encoding="utf-8") if OUTPUT.exists() else ""
        if strip_timestamp(current) != strip_timestamp(generated):
            print("repo-map.html is stale vs registry.yaml. Run without --check to regenerate.")
            return 1
        print("repo-map.html matches registry.yaml.")
        return 0

    OUTPUT.write_text(generated, encoding="utf-8")
    print(f"Wrote {OUTPUT}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
