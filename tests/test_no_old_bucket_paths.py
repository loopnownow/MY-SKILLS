"""禁止旧桶路径回归。

口径（{RULES}/workspace-layout.md）：家族目录只认 `_PHI` / `__zip` / `_thesis`；
旧名 `_db` / `_share` / `modal_` 只允许出现在历史台账行（含 `PR #` 的说明）里。

匹配只针对「路径形态」：
- `_share/`、`_db/`（后接路径分隔符）
- 裸词 `_db`（前后都不是标识符字符）
- `modal_` 前缀

`verify_db`、`build_code_db.py`、`path_shared` 这类标识符天然不命中（前后是字母）。
"""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCAN_SUFFIX = {".md", ".yaml", ".yml"}
SKIP_PARTS = {".git", "tests", "__pycache__", "node_modules", "_work"}
LEDGER_MARK = "PR #"

PATTERNS = [
    ("_share/", re.compile(r"(?<![A-Za-z0-9_])_share/")),
    ("_db/", re.compile(r"(?<![A-Za-z0-9_])_db/")),
    ("bare _db", re.compile(r"(?<![A-Za-z0-9_])_db(?![A-Za-z0-9_])")),
    ("modal_", re.compile(r"(?<![A-Za-z0-9_])modal_[A-Za-z0-9]")),
]


def _scan_files():
    for path in ROOT.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in SCAN_SUFFIX:
            continue
        if any(part in SKIP_PARTS for part in path.relative_to(ROOT).parts):
            continue
        yield path


def test_no_old_bucket_paths():
    hits = []
    for path in _scan_files():
        try:
            text = path.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        for lineno, line in enumerate(text.splitlines(), 1):
            if LEDGER_MARK in line:
                continue
            for name, rx in PATTERNS:
                if rx.search(line):
                    hits.append(
                        f"{path.relative_to(ROOT).as_posix()}:{lineno}: [{name}] "
                        f"{line.strip()[:140]}"
                    )
                    break
    assert not hits, "旧桶路径残留（改用 _PHI / __zip / _thesis）：\n" + "\n".join(hits)
