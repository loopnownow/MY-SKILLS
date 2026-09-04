#!/usr/bin/env python3
"""Local mounts-cap cache: full B, on-demand paths for backups. No bulk backup clone."""
from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.error
import urllib.request
import zipfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
A_ROOT = HERE.parent
ONE = A_ROOT / "01_skill-discovery-integration"
UA = "MY-SKILLS-mounts-cap (loopnownow)"
API = "https://api.github.com"
CODELOAD = "https://codeload.github.com"

DIRS = {
    "my-skills-capabilities": "b",
    "academic-research-skills": "ars",
    "med-sci-skills": "medsci",
    "scientific-agent-skills": "scientific",
}
REPOS = {
    "my-skills-capabilities": "loopnownow/MY-SKILLS-capabilities",
    "academic-research-skills": "Imbad0202/academic-research-skills",
    "med-sci-skills": "Aperivue/medsci-skills",
    "scientific-agent-skills": "K-Dense-AI/scientific-agent-skills",
}


def die(msg: str, code: int = 2) -> None:
    print(msg, file=sys.stderr)
    raise SystemExit(code)


def headers() -> dict[str, str]:
    h = {"User-Agent": UA, "Accept": "application/vnd.github+json"}
    token = os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN")
    if token:
        h["Authorization"] = f"Bearer {token}"
    return h


def http_json(url: str) -> object:
    req = urllib.request.Request(url, headers=headers())
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.load(r)


def http_bytes(url: str) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=180) as r:
        return r.read()


def load_state() -> dict:
    p = HERE / "STATE.yaml"
    if not p.is_file():
        return {}
    out: dict = {}
    cur = None
    for line in p.read_text(encoding="utf-8").splitlines():
        if not line.strip() or line.strip().startswith("#"):
            continue
        if line.startswith("  ") and cur:
            k, _, v = line.strip().partition(":")
            out[cur][k.strip()] = v.strip().strip('"')
        elif ":" in line and not line.startswith(" "):
            cur = line.split(":", 1)[0].strip()
            out[cur] = {}
    return out


def save_state(state: dict) -> None:
    lines = ["# gitignored. Recorded SHAs of what is on disk.\n"]
    for sid, rec in state.items():
        lines.append(f"{sid}:\n")
        for k, v in rec.items():
            lines.append(f"  {k}: {v}\n")
    (HERE / "STATE.yaml").write_text("".join(lines), encoding="utf-8")


def _state_lock():
    """Best-effort exclusive lock so parallel ensure --id does not clobber STATE."""
    lock_path = HERE / ".state.lock"
    lock_path.touch(exist_ok=True)
    fh = open(lock_path, "a+", encoding="utf-8")
    try:
        import fcntl
        fcntl.flock(fh.fileno(), fcntl.LOCK_EX)
    except Exception:
        pass  # Windows / no fcntl: merge-on-write below still helps
    return fh


def merge_source_state(source_id: str, updates: dict) -> dict:
    """Reload STATE, merge updates into source_id, write back under lock."""
    fh = _state_lock()
    try:
        state = load_state()
        rec = dict(state.get(source_id, {}))
        rec.update(updates)
        state[source_id] = rec
        save_state(state)
        return state
    finally:
        try:
            import fcntl
            fcntl.flock(fh.fileno(), fcntl.LOCK_UN)
        except Exception:
            pass
        fh.close()


def repo_head(owner_repo: str) -> str:
    data = http_json(f"{API}/repos/{owner_repo}/commits/HEAD")
    if not isinstance(data, dict) or "sha" not in data:
        die(f"no sha for {owner_repo}")
    return str(data["sha"])[:40]


def parse_paths(raw: str) -> list[str]:
    return [p.strip().strip("/") + "/" for p in raw.split(";") if p.strip()]


def registry_entry(skill_id: str) -> tuple[str, str]:
    text = (ONE / "registry.yaml").read_text(encoding="utf-8")
    block = None
    cur: list[str] = []
    for line in text.splitlines():
        if line.startswith("  - id:"):
            if cur and any(x.strip() == f"id: {skill_id}" or x.strip() == f"- id: {skill_id}" for x in cur):
                block = cur
                break
            cur = [line]
        elif cur is not None:
            cur.append(line)
            if line.startswith("proposals:"):
                break
    else:
        if cur and f"id: {skill_id}" in "\n".join(cur):
            block = cur
    if not block:
        # fallback scan
        import re
        m = re.search(
            rf"- id: {re.escape(skill_id)}\n    source: (\S+)\n    path: (.+)",
            text,
        )
        if not m:
            die(f"id not in registry: {skill_id}")
        return m.group(1), m.group(2).strip()
    src = path = ""
    for line in block:
        s = line.strip()
        if s.startswith("source:"):
            src = s.split(":", 1)[1].strip()
        if s.startswith("path:"):
            path = s.split(":", 1)[1].strip()
    if not src or not path:
        die(f"incomplete registry row for {skill_id}")
    return src, path


def source_path_for(source_id: str, skill_id: str) -> str:
    """Prefer the named source yaml (backup pick); else registry."""
    files = {
        "my-skills-capabilities": ONE / "sources" / "b-my-skills-capabilities.yaml",
        "academic-research-skills": ONE / "sources" / "ars.proposed.yaml",
        "med-sci-skills": ONE / "sources" / "medsci.proposed.yaml",
        "scientific-agent-skills": ONE / "sources" / "scientific-agent-skills.proposed.yaml",
    }
    p = files.get(source_id)
    if p and p.is_file():
        import re
        text = p.read_text(encoding="utf-8")
        m = re.search(
            rf"- id: {re.escape(skill_id)}\n    path: (.+)",
            text,
        )
        if m:
            return m.group(1).strip()
    _src, path = registry_entry(skill_id)
    return path


def dest_root(source_id: str) -> Path:
    return HERE / DIRS[source_id]


def legacy_b() -> Path:
    return A_ROOT / "MY-SKILLS-capabilities"


def b_present() -> Path | None:
    b = dest_root("my-skills-capabilities")
    if b.is_dir() and any(b.iterdir()):
        return b
    leg = legacy_b()
    if leg.is_dir() and any(leg.iterdir()):
        return leg
    return None


def fetch_dir_api(owner_repo: str, rel: str, dest: Path, ref: str) -> int:
    """Download one repo directory via Contents API. Returns file count."""
    n = 0
    url = f"{API}/repos/{owner_repo}/contents/{rel.strip('/')}?ref={ref}"
    try:
        data = http_json(url)
    except urllib.error.HTTPError as e:
        # Let caller fall back to zip (esp. 403 rate limit)
        raise
    if isinstance(data, dict) and data.get("type") == "file":
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(http_bytes(data["download_url"]))
        return 1
    if not isinstance(data, list):
        die(f"unexpected contents payload for {rel}")
    for item in data:
        name = item.get("name")
        typ = item.get("type")
        child = dest / name
        if typ == "dir":
            n += fetch_dir_api(owner_repo, f"{rel.strip('/')}/{name}", child, ref)
        elif typ == "file":
            child.parent.mkdir(parents=True, exist_ok=True)
            child.write_bytes(http_bytes(item["download_url"]))
            n += 1
    return n


def unzip_prefix(zbytes: bytes, prefix: str, dest: Path) -> int:
    n = 0
    prefix = prefix.strip("/") + "/"
    with zipfile.ZipFile(__import__("io").BytesIO(zbytes)) as zf:
        names = zf.namelist()
        # strip top folder MY-SKILLS-sha/
        for name in names:
            parts = name.split("/", 1)
            rest = parts[1] if len(parts) == 2 else name
            if prefix != "/" and not rest.startswith(prefix) and rest != prefix[:-1]:
                continue
            if name.endswith("/"):
                continue
            rel = rest[len(prefix) :] if prefix != "/" else rest
            if not rel:
                rel = Path(rest).name
            out = dest / rel
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_bytes(zf.read(name))
            n += 1
    return n


def ensure_b(force: bool = False) -> None:
    sid = "my-skills-capabilities"
    owner_repo = REPOS[sid]
    remote = repo_head(owner_repo)
    present = b_present()
    state = load_state()
    rec = state.get("b", {})
    if present and rec.get("sha", "").startswith(remote[:7]) and not force:
        print(f"B ok {present} @{rec.get('sha', remote)[:7]}")
        return
    if present and not force:
        print(f"B present {present}; remote {remote[:7]} local {rec.get('sha', 'unknown')[:7]} — updating")
    dest = dest_root(sid)
    dest.mkdir(parents=True, exist_ok=True)
    url = f"{CODELOAD}/{owner_repo}/zip/{remote}"
    print(f"fetch full B {owner_repo}@{remote[:7]}")
    zbytes = http_bytes(url)
    n = unzip_prefix(zbytes, "", dest)
    if n == 0:
        die("B zip extracted 0 files")
    merge_source_state("b", {"sha": remote, "files": str(n)})
    print(f"B cached {dest} ({n} files)")


def ensure_id(skill_id: str, source_id: str | None = None, force: bool = False) -> None:
    if source_id is None:
        source_id, path = registry_entry(skill_id)
    else:
        path = source_path_for(source_id, skill_id)
    if source_id == "my-skills-capabilities":
        ensure_b(force=force)
        return
    if source_id not in DIRS:
        die(f"unknown source {source_id}")
    owner_repo = REPOS[source_id]
    remote = repo_head(owner_repo)
    dest_base = dest_root(source_id)
    state = load_state()
    rec = dict(state.get(source_id, {}))
    n_total = 0
    zbytes_cache: bytes | None = None

    def zip_bytes() -> bytes:
        nonlocal zbytes_cache
        if zbytes_cache is None:
            print(f"codeload zip {owner_repo}@{remote[:7]}")
            zbytes_cache = http_bytes(f"{CODELOAD}/{owner_repo}/zip/{remote}")
        return zbytes_cache

    for rel in parse_paths(path):
        dest = dest_base / rel
        key = rel
        if dest.is_dir() and any(dest.iterdir()) and rec.get(key, "").startswith(remote[:7]) and not force:
            print(f"skip {source_id}:{rel} @{remote[:7]}")
            continue
        # Prefer zip/codeload for backup packs (avoids Contents API rate limits).
        print(f"fetch {source_id}:{rel} @{remote[:7]} via zip")
        try:
            n = unzip_prefix(zip_bytes(), rel, dest)
        except Exception as e:
            print(f"zip failed ({e}); trying Contents API")
            try:
                n = fetch_dir_api(owner_repo, rel, dest, remote)
            except urllib.error.HTTPError as he:
                if he.code == 403:
                    die(f"GitHub 403 for {owner_repo}:{rel} after zip+API — empty-mount protocol")
                raise
        if n == 0:
            # last chance: API then die
            try:
                print(f"zip empty; retry API for {rel}")
                n = fetch_dir_api(owner_repo, rel, dest, remote)
            except urllib.error.HTTPError as he:
                die(f"empty fetch {source_id}:{rel} (HTTP {he.code}) — empty-mount protocol")
        if n == 0:
            die(f"empty fetch {source_id}:{rel} — empty-mount protocol")
        rec[key] = remote
        n_total += n
    rec["sha"] = remote
    # Merge under lock so parallel `ensure --id` does not drop sibling keys.
    merge_source_state(source_id, rec)
    print(f"cached {skill_id} from {source_id} ({n_total} new files)")


def cmd_check() -> None:
    print(f"cache {HERE}")
    b = b_present()
    print(f"B: {b if b else 'MISSING'}")
    state = load_state()
    for sid, d in DIRS.items():
        p = HERE / d
        print(f"  {d}/ exists={p.is_dir()} state={state.get(sid) or state.get('b' if sid.startswith('my') else sid)}")


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="mounts-cap: full B, on-demand backups")
    sub = p.add_subparsers(dest="cmd", required=True)
    sub.add_parser("ensure-b", help="download or update the full B tree")
    e = sub.add_parser("ensure", help="one skill id; backups fetch only that path")
    e.add_argument("--id", required=True)
    e.add_argument("--source", default=None, help="override source id (still path-only for non-B)")
    e.add_argument("--force", action="store_true")
    sub.add_parser("check", help="show what is on disk")
    args = p.parse_args(argv)
    if args.cmd == "ensure-b":
        ensure_b()
    elif args.cmd == "ensure":
        ensure_id(args.id, args.source, force=getattr(args, "force", False))
    elif args.cmd == "check":
        cmd_check()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
