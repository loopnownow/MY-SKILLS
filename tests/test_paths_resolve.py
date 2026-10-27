
"""Documented paths resolve, owners resolve, no external renderer.

Merged from: `test_inline_paths_exist.py`, `test_owner_fields.py`, `test_no_external_renderer.py`.
"""
from __future__ import annotations

from pathlib import Path
import posixpath
import re
import unittest

from tests.support import (
    GATES,
    ONE,
    ROOT,
)

BT = re.compile(r"`([^`]+)`")
TOPS = (
    "00_orchestrator/",
    "02_data-processing/",
    "03_research/",
    "05_manuscript/",
    "06_review/",
    "07_response/",
    "tests/",
    "docs/",
)
ALLOW_MISSING = {
    "docs/",  # optional viz outputs; often regenerated locally
    # Explicit "do NOT create this parallel file" example in coding-qc.md.
    # Not a pointer; keep the token so the ban stays readable.
    "02_data-processing/code-qc.md",
}
SKIP_FILE_PREFIXES = (
    "VERSION.txt",
    "INTEGRATION_MAP.md",
)
FORBIDDEN_BARE_RELATIVE = (
    "qc/local-checks.md",
)
OWNER_RE = re.compile(r"^owner:\s*[\"']?([^\"'\n]+)[\"']?\s*$", re.M)
ALLOW_OWNER_VALUES: set[str] = set()
HIST = re.compile(r"deleted|removed|former|archived|retired|no external renderer", re.I)
ALLOW_FILES = {"INTEGRATION_MAP.md"}
SKIP_DIRS = {".git", "__pycache__", ".pytest_cache"}

class InlinePathsExist(unittest.TestCase):
    def test_backtick_repo_paths_exist_or_allowlisted(self) -> None:
        missing: list[str] = []
        for path in ROOT.rglob("*.md"):
            if any(part in {".git", "__pycache__", ".pytest_cache"} for part in path.parts):
                continue
            if path.parts[0] == "tests":
                continue
            rel = path.relative_to(ROOT).as_posix()
            if rel in SKIP_FILE_PREFIXES or rel.startswith(SKIP_FILE_PREFIXES):
                continue
            text = path.read_text(encoding="utf-8", errors="ignore")
            for m in BT.finditer(text):
                tok = m.group(1).strip()
                if "/" not in tok and "\\" not in tok:
                    continue
                if tok.startswith(
                    ("http://", "https://", "D:", "L:", "C:", "{", "<", "#", "mailto:", "file:")
                ):
                    continue
                clean = tok.split()[0].rstrip(".,);:\"'")
                clean = clean.replace("\\", "/").split("#", 1)[0]
                if clean.startswith("./"):
                    clean = clean[2:]
                if not clean.startswith(TOPS):
                    continue
                if clean in ALLOW_MISSING:
                    continue
                if not (ROOT / clean).exists():
                    missing.append(f"{rel}: `{clean}`")
        self.assertEqual(
            missing,
            [],
            "inline paths missing (add to ALLOW_MISSING only with cause):\n"
            + "\n".join(missing[:50]),
        )
class BareRelativeCites(unittest.TestCase):
    def test_no_forbidden_bare_relative_cites(self) -> None:
        hits: list[str] = []
        for path in ROOT.rglob("*.md"):
            if any(part in {".git", "__pycache__", ".pytest_cache"} for part in path.parts):
                continue
            rel = path.relative_to(ROOT).as_posix()
            if rel.startswith("tests/") or rel in SKIP_FILE_PREFIXES or rel.startswith(SKIP_FILE_PREFIXES):
                continue
            text = path.read_text(encoding="utf-8", errors="ignore")
            for bare in FORBIDDEN_BARE_RELATIVE:
                needle = f"`{bare}`"
                if needle in text:
                    hits.append(f"{rel}: {needle}")
        self.assertEqual(hits, [], "forbidden bare relative cites:\n" + "\n".join(hits[:40]))
class OwnerFields(unittest.TestCase):
    def test_base_owner_fields_resolve(self) -> None:
        missing: list[str] = []
        seen = 0
        for path in ROOT.rglob("*"):
            if not path.is_file() or path.name not in ("SKILL.md", "MODULE.md"):
                continue
            rel_parts = path.relative_to(ROOT).parts
            if "base" not in rel_parts and "qc" not in rel_parts:
                continue
            if any(p.startswith(".") for p in rel_parts):
                continue
            text = path.read_text(encoding="utf-8")
            for m in OWNER_RE.finditer(text):
                seen += 1
                owner = m.group(1).strip().strip("\"'")
                if owner in ALLOW_OWNER_VALUES:
                    continue
                # owners are repo-relative posix paths
                target = ROOT / owner
                if not target.exists():
                    rel = path.relative_to(ROOT).as_posix()
                    missing.append(f"{rel}: owner={owner}")
        self.assertGreaterEqual(seen, 20, "expected many owner: fields under base/")
        self.assertEqual(missing, [], "owner paths missing:\n" + "\n".join(missing))
class NoExternalRendererReference(unittest.TestCase):
    def test_no_live_archify_reference(self) -> None:
        hits: list[str] = []
        for path in ROOT.rglob("*"):
            if not path.is_file() or path.suffix not in {".md", ".yaml", ".yml", ".py", ".mmd"}:
                continue
            if set(path.parts) & SKIP_DIRS:
                continue
            rel = path.relative_to(ROOT).as_posix()
            if rel in ALLOW_FILES or rel.startswith("tests/"):
                continue
            text = path.read_text(encoding="utf-8", errors="ignore")
            for i, line in enumerate(text.splitlines(), 1):
                if "archify" not in line.lower():
                    continue
                if HIST.search(line):
                    continue
                hits.append(f"{rel}:{i}: {line.strip()[:110]}")
        self.assertEqual(hits, [], "live external-renderer references:\n" + "\n".join(hits[:20]))


NAME_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_.-]{2,58}\.md$")
TICK_RE = re.compile(r"`([^`]{2,90})`")
HIST_LINE = re.compile(
    r"archived|historical|legacy|former|formerly|merged|absorbed|retired|relocated|"
    r"pruned|not on disk|do not recreate|do not create|distill of|dated snapshot|"
    r"勿建|do not recreate|不另建|do not create separately|归档|archive|archived|已并入|merged into|历史|historical",
    re.I,
)

# Documents that live on the lab disk (0doc), in an upstream skill, in MY-RULES,
# or in a dated snapshot note, not in this repo.
EXTERNAL = {
    "lab-palettes.md",
    "Lab-STE-SPEC.md",
    "acceptance-gate.md",
    "gate_mechanical.md",
    "citation-formats.md",
    "api-documentation.md",
    "experiment-integrity.md",
    "evidence-precheck.md",
    "evidence-request.md",
    "skills.md",
    "coding-principles.md",
    "changelog.md",
    "CHANGELOG_*.md",
    "manuscript-revision.md",
    "EXECUTION.md",
    "workspace-layout.md",
    "structures.md",
    "examples.md",
    "literature-evidence-2023-2026.md",
    "INTEGRATION_MAP-20261007.md",
    "INTEGRATION_MAP.archive.md",
    "INTEGRATION_MAP-YYYYMMDD.md",
    "INDEX-thesis.md",
    "themes.md",
    "HARVEST-STANDARD.md",
    "harvest-projects-cut.md",
    "harvest-verified-links.md",
    "03-002-03-guojiazirankexuejijin-qingnianxiangmu.md",
    "03-003-03-fudandaxue-boshibaokao.md",
    "03-004-03-jinshanquweijianwei.md",
    "03-005-03-jinshanyiyuan-yanjiushengketi.md",
    "03-006-03-jinshanyiyuan-yanjiushengketi-2.md",
    "03-007-03-jinshanyiyuan-yanjiushengketi-3.md",
    "03-008-03-jinshanyiyuan-yuanjikeyanjijin.md",
}

# Report artifacts the running task writes; they are names, not repo files.
ARTIFACTS = {
    "RESUBMIT_REPORT.md",
    "PAPER_CLAIM_AUDIT.md",
    "CLAIMS_FROM_RESULTS.md",
    "figure-manifest.md",
    "journals-submitted.md",
    "house-format.md",
}


def _iter_md():
    for path in ROOT.rglob("*"):
        if path.is_file() and path.suffix == ".md" and not (SKIP_DIRS & set(path.parts)):
            yield path


class BareMdCites(unittest.TestCase):
    def test_bare_md_names_resolve(self) -> None:
        known = {path.name for path in ROOT.rglob("*") if path.is_file()}
        missing: list[str] = []
        for path in _iter_md():
            rel = path.relative_to(ROOT).as_posix()
            for line_no, line in enumerate(
                path.read_text(encoding="utf-8", errors="ignore").splitlines(), 1
            ):
                if HIST_LINE.search(line):
                    continue
                for match in TICK_RE.finditer(line):
                    token = match.group(1).strip()
                    if not NAME_RE.match(token) or "/" in token:
                        continue
                    if token in known or token in EXTERNAL or token in ARTIFACTS:
                        continue
                    missing.append(f"{rel}:{line_no}: `{token}`")
        self.assertEqual(
            missing,
            [],
            "bare .md cites that resolve nowhere (add the file, fix the cite, or "
            "list it in EXTERNAL/ARTIFACTS):\n" + "\n".join(missing[:40]),
        )

# Bare relative tokens (`references/x.md`, `personal/y.md`) are resolved against the
# citing file's directory first. When that fails they must carry an explicit seat or
# module prefix, name an alias/0doc root, or sit on a line that marks the target as
# history. Guards the 2026-10-26 pointer sweep from regressing.
BARE_SKIP_PREFIXES = (
    "ref/",
    "_library/",
    "_code/",
    "_bank/",
    "_meta/",
    "MY-SKILLS/",
    "~/",
    "templates/",
    "scripts/",
    "archive/",
    "01_skill-integration/",
    "04_analysis/",
    "03-research/",
)
BARE_ALIAS_ROOTS = ("{doc_root}", "{RULES}", "{SKILLS}", "{DEL}", "{RAW}", "{code_")
BARE_HISTORY = re.compile(
    r"former|prior path|moved from|now in park|lived at|not vendored|not on disk|no longer|"
    r"deleted|removed|archived|historical|absorbed|pruned|retired|distill of|used to live|"
    r"renamed|park\b|仓内无此|历史|已吸收|已归档",
    re.I,
)


def _bare_tokens(line: str) -> list[str]:
    tokens: list[str] = []
    for match in TICK_RE.finditer(line):
        raw = match.group(1).strip()
        if raw.startswith(("http", "D:", "C:", "L:", "{", "<", "#", "mailto:", "file:", "~")):
            continue
        token = raw.split()[0].rstrip(".,);:\"'").replace("\\", "/").split("#")[0]
        if not token.endswith(".md") or "/" not in token:
            continue
        if any(ch in token for ch in "<>*"):
            continue
        if token.startswith(TOPS) or token.startswith("./"):
            continue
        tokens.append(token)
    return tokens


class BareRelativeResolves(unittest.TestCase):
    def test_bare_relative_pointers_resolve_from_citing_file(self) -> None:
        files = {
            path.relative_to(ROOT).as_posix()
            for path in ROOT.rglob("*")
            if path.is_file() and not (SKIP_DIRS & set(path.parts))
        }
        problems: list[str] = []
        for path in _iter_md():
            rel = path.relative_to(ROOT).as_posix()
            if rel.startswith("tests/"):
                continue
            base = rel.rsplit("/", 1)[0] if "/" in rel else ""
            for line_no, line in enumerate(
                path.read_text(encoding="utf-8", errors="ignore").splitlines(), 1
            ):
                for token in _bare_tokens(line):
                    if posixpath.normpath(posixpath.join(base, token)) in files:
                        continue
                    if token.startswith(BARE_SKIP_PREFIXES):
                        continue
                    if BARE_HISTORY.search(line) or any(root in line for root in BARE_ALIAS_ROOTS):
                        continue
                    suffix = [name for name in files if name.endswith("/" + token)]
                    if len(suffix) == 1:
                        problems.append(f"{rel}:{line_no}: `{token}` -> write `{suffix[0]}`")
                    else:
                        problems.append(f"{rel}:{line_no}: `{token}` -> no unique target ({len(suffix)})")
        self.assertEqual(
            problems,
            [],
            "bare relative pointers must resolve from the citing file, carry a seat "
            "prefix, or be marked as history:\n" + "\n".join(problems[:40]),
        )

