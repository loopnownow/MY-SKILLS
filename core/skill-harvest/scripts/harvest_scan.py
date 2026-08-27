# -*- coding: utf-8 -*-
"""Scan Grok sessions + extra skill trees for harvest candidates.

Does not edit skills. Writes a markdown (and optional JSON) report.

  python harvest_scan.py --since 7
  python harvest_scan.py --since 0 --json
  python harvest_scan.py --sessions-root "C:\\Users\\loopn\\.grok\\sessions"
"""
from __future__ import annotations

import argparse
import json
import os
import re
from datetime import datetime, timedelta
from pathlib import Path

# ── CONFIG ──────────────────────────────────────────────────────────
GROK_HOME = Path(os.environ.get("GROK_HOME") or (Path.home() / ".grok"))
SESSIONS_ROOT = GROK_HOME / "sessions"
SKILLS_ROOT = GROK_HOME / "skills"
DEFAULT_OUT_DIR = SESSIONS_ROOT / "_merged_summaries"
DEFAULT_EXTRA_SKILL_ROOTS = [
    Path.home() / ".agents" / "skills",
    Path("D:/skills"),
]
NOISE_PREFIXES = (
    "<system-reminder>",
    "<user_info>",
    "<work_policy>",
    "<rules>",
    "<tool_calling>",
    "This session is being continued",
    "Your previous run ended",
    "You are rebuilding",
    "Rebuild ONE",
    "Rebuild TWO",
    "Rebuild THREE",
    "Rebuild SIX",
    "You are a senior radiology",
)
QUERY_RE = re.compile(r"<user_query>\s*(.*?)\s*</user_query>", re.S | re.I)
# ── end CONFIG ──────────────────────────────────────────────────────


def _text_from_obj(obj: dict) -> tuple[str, str]:
    role = str(obj.get("role") or obj.get("type") or "")
    content = obj.get("content")
    text = ""
    if isinstance(content, str):
        text = content
    elif isinstance(content, list):
        parts = []
        for c in content:
            if isinstance(c, dict):
                parts.append(c.get("text") or "")
            elif isinstance(c, str):
                parts.append(c)
        text = "\n".join(parts)
    elif isinstance(obj.get("message"), dict):
        m = obj["message"]
        if isinstance(m.get("content"), str):
            text = m["content"]
    return role, text


def extract_queries(chat_path: Path, limit: int = 12) -> list[str]:
    out: list[str] = []
    if not chat_path.is_file():
        return out
    try:
        lines = chat_path.read_text(encoding="utf-8", errors="replace").splitlines()
    except OSError:
        return out
    for line in lines:
        if not line.strip():
            continue
        try:
            obj = json.loads(line)
        except json.JSONDecodeError:
            continue
        role, text = _text_from_obj(obj)
        for m in QUERY_RE.finditer(text):
            q = " ".join(m.group(1).split())
            if q and q not in out:
                out.append(q)
        if not QUERY_RE.search(text) and role in ("user", "human"):
            q = " ".join(text.split())
            if q and q not in out:
                out.append(q)
        if len(out) >= limit:
            break
    return [q for q in out if not _is_noise(q)]


def _is_noise(q: str) -> bool:
    s = q.strip()
    if len(s) < 4:
        return True
    if s.startswith(NOISE_PREFIXES):
        return True
    if s.startswith("The following skills are available"):
        return True
    if s.startswith("OS Version:"):
        return True
    return False


def scan_sessions(root: Path, since: datetime | None) -> list[dict]:
    rows = []
    if not root.is_dir():
        return rows
    for cwd_dir in root.iterdir():
        if not cwd_dir.is_dir() or cwd_dir.name.startswith("_"):
            continue
        for sid_dir in cwd_dir.iterdir():
            if not sid_dir.is_dir():
                continue
            mtime = datetime.fromtimestamp(sid_dir.stat().st_mtime)
            if since and mtime < since:
                continue
            title = ""
            summary = sid_dir / "summary.json"
            if summary.is_file():
                try:
                    j = json.loads(summary.read_text(encoding="utf-8", errors="replace"))
                    title = j.get("title") or j.get("name") or ""
                except (json.JSONDecodeError, OSError):
                    pass
            queries = extract_queries(sid_dir / "chat_history.jsonl")
            if not queries and not title:
                continue
            rows.append(
                {
                    "sid": sid_dir.name,
                    "cwd": cwd_dir.name,
                    "title": title,
                    "mtime": mtime.isoformat(timespec="minutes"),
                    "queries": queries,
                }
            )
    rows.sort(key=lambda r: r["mtime"], reverse=True)
    return rows


def scan_skill_tree(root: Path) -> list[dict]:
    found = []
    if not root.is_dir():
        return found
    for p in root.rglob("SKILL.md"):
        found.append(_skill_entry(p, "SKILL"))
    for p in root.rglob("MODULE.md"):
        found.append(_skill_entry(p, "MODULE"))
    return found


def _skill_entry(path: Path, kind: str) -> dict:
    name = ""
    desc = ""
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        text = ""
    fm = re.match(r"^---\s*\n(.*?)\n---", text, re.S)
    if fm:
        block = fm.group(1)
        nm = re.search(r"^name:\s*(.+)$", block, re.M)
        ds = re.search(r"^description:\s*>?\s*(.+)$", block, re.M)
        if nm:
            name = nm.group(1).strip()
        if ds:
            desc = ds.group(1).strip()
    if not name:
        name = path.parent.name
    return {
        "kind": kind,
        "name": name,
        "path": str(path),
        "description": desc[:240],
    }


def render_md(sessions: list[dict], extras: dict[str, list[dict]], since_label: str) -> str:
    lines = [
        "# Skill-harvest scan",
        "",
        f"Generated: {datetime.now().isoformat(timespec='minutes')}",
        f"Since: {since_label}",
        f"Sessions with user text: {len(sessions)}",
        "",
        "Next: classify with `references/keep-vs-skip.md` and route with `references/route-map.md`.",
        "Do not edit skills until the user picks rows.",
        "",
        "## Sessions",
        "",
    ]
    for s in sessions:
        lines.append(f"### `{s['sid']}` · {s['mtime']}")
        lines.append(f"- cwd: `{s['cwd']}`")
        if s["title"]:
            lines.append(f"- title: {s['title']}")
        if s["queries"]:
            lines.append("- user:")
            for q in s["queries"][:8]:
                lines.append(f"  - {q[:300]}")
        lines.append("")
    if extras:
        lines.append("## Extra skill trees")
        lines.append("")
        for root, items in extras.items():
            lines.append(f"### `{root}` ({len(items)} files)")
            for it in items[:80]:
                lines.append(f"- `{it['kind']}` **{it['name']}** — `{it['path']}`")
                if it.get("description"):
                    lines.append(f"  - {it['description']}")
            if len(items) > 80:
                lines.append(f"- … {len(items) - 80} more")
            lines.append("")
    return "\n".join(lines) + "\n"


def main() -> int:
    ap = argparse.ArgumentParser(description="Scan chats and extra skills for harvest.")
    ap.add_argument("--since", type=float, default=7, help="Days back; 0 = all")
    ap.add_argument("--sessions-root", type=Path, default=SESSIONS_ROOT)
    ap.add_argument("--out-dir", type=Path, default=DEFAULT_OUT_DIR)
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--skills-extra", type=Path, action="append", default=[])
    args = ap.parse_args()

    since = None
    since_label = "all"
    if args.since and args.since > 0:
        since = datetime.now() - timedelta(days=args.since)
        since_label = f"last {args.since:g} days ({since.isoformat(timespec='minutes')})"

    sessions = scan_sessions(args.sessions_root, since)
    extra_roots = list(args.skills_extra) + [p for p in DEFAULT_EXTRA_SKILL_ROOTS if p.is_dir()]
    extras: dict[str, list[dict]] = {}
    seen = set()
    for root in extra_roots:
        key = str(root)
        if key in seen:
            continue
        seen.add(key)
        items = scan_skill_tree(root)
        if items:
            extras[key] = items

    args.out_dir.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now().strftime("%Y%m%d_%H%M")
    md_path = args.out_dir / f"harvest_scan_{stamp}.md"
    md_path.write_text(render_md(sessions, extras, since_label), encoding="utf-8")
    print(md_path)
    if args.json:
        js_path = args.out_dir / f"harvest_scan_{stamp}.json"
        js_path.write_text(
            json.dumps(
                {"since": since_label, "sessions": sessions, "extra_skills": extras},
                ensure_ascii=False,
                indent=2,
            ),
            encoding="utf-8",
        )
        print(js_path)
    print(f"sessions={len(sessions)} extra_trees={len(extras)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
