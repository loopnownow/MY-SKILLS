#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
style_lint.py -- offline AI-tell linter, a sub-check of gate G-05 in the 00 QC layer.

WHAT THIS IS
    A lightweight absorption of the *mechanism* of ItsssssJack/SlopMonster (MIT):
    pattern groups -> a score -> a non-zero exit code when a group fails.

WHAT THIS IS NOT (deliberately left out of the absorption)
    * the rival-model "cleanse" step        (manuscript text must never leave the machine)
    * the marketing-copy rules and the "invented proof" number+noun regex
      (every manuscript sentence has n=, P, AUC; number tracing belongs to G-FACT)
    * the "put a person back in" rewrite pass (conflicts with the ying-li style profile)

HARD RULES (each one is enforced by a test in test_style_lint.py)
    1. Fully offline: stdlib only, no network, no subprocess, no model calls.
    2. Never rewrites the manuscript: it reports hits, the user decides.
    3. Fail closed: empty / unscannable / non-English input exits 2, never "passes".

USAGE
    python3 style_lint.py manuscript.md
    python3 style_lint.py manuscript.md --json
    python3 style_lint.py --text "It's not just a tool, it's a journey."
    python3 style_lint.py manuscript.md --config overrides.json   # override any CONFIG key
    cat manuscript.md | python3 style_lint.py -

EXIT CODES
    0  pass         1  style tells found        2  input error (empty / unreadable / not English)
"""

import argparse
import copy
import json
import re
import sys
from pathlib import Path

# =============================================================================
# CONFIG  --  everything you may want to tune lives here (and can be overridden
# per run with --config file.json). Nothing below this block hard-codes a term,
# threshold or section name.
# =============================================================================
CONFIG = {
    # ---- 1. Scope: which manuscript sections are scanned ----------------------
    # Only headings whose normalised text is in one of these lists switch the mode.
    # A heading not in either list (e.g. "Statistical analysis", "Limitations")
    # inherits the mode of its parent, so sub-sections of Methods stay skipped.
    # Methods/Results are skipped on purpose: passive voice, enumerations and
    # numeric reporting are convention there, not AI tells.
    "SCAN_SECTIONS": [
        "abstract", "introduction", "background", "discussion",
        "conclusion", "conclusions", "highlights",
    ],
    "SKIP_SECTIONS": [
        "methods", "materials and methods", "patients and methods", "study design",
        "results", "figure legends", "figure legend", "tables", "table",
        "references", "acknowledgments", "acknowledgements",
        "supplementary", "appendix",
    ],
    # Text before the first heading (title block / unheaded abstract): scan it?
    "SCAN_PREAMBLE": True,

    # ---- 2. Scoring thresholds ------------------------------------------------
    # Score = number of clean groups (max 4). The gate passes at >= PASS_SCORE.
    "PASS_SCORE": 4,
    # Limited vocabulary is "fine once, damning when repeated".
    "TIER2_MAX_PER_TERM": 1,      # the same word may appear this many times
    "TIER2_MAX_TOTAL": 3,         # all limited words together may appear this many times
    "EMDASH_MAX_PER_SENTENCE": 1,  # more than this many em-dashes in one sentence fails
    "TRICOLON_MAX_ALLOWED": 3,    # rule-of-three lists tolerated in the scanned text

    # ---- 3. Input guards (fail closed) ----------------------------------------
    "MIN_SCANNED_WORDS": 10,      # fewer scanned words than this -> exit 2, not a pass
    "MAX_NON_LATIN_RATIO": 0.2,   # catalogue is English-only; CJK-heavy text would "pass" falsely

    # ---- 4. Vocabulary (regex fragments, matched on word boundaries, case-insensitive)
    # ALWAYS = flagged on any occurrence.
    # robust / landscape / leverage / labeled / locked are here by explicit decision (AI vocabulary).
    # NOTE "robustness" is intentionally NOT matched: "feature robustness" is standard
    # radiomics terminology (ICC / test-retest). Widen with r"robust(?:ness|ly)?" if wanted.
    # NOTE elevate/enhance are intentionally not listed: "elevated ALT", "contrast-enhanced".
    # NOTE noun "label" (figure label, reporting label) is NOT matched — only labell?ed.
    "VOCAB_ALWAYS": [
        r"labell?ed",
        r"locked",
        r"delv(?:e|es|ed|ing)",
        r"tapestr(?:y|ies)",
        r"testament to",
        r"underscor(?:e|es|ed|ing)",
        r"seamless(?:ly)?",
        r"robust(?:ly)?",
        r"landscapes?",
        r"leverag(?:e|es|ed|ing)",
        r"realms?",
        r"myriad",
        r"plethora",
        r"ever-evolving",
        r"cutting-edge",
        r"transformative",
        r"paradigm shifts?",
        r"holistic(?:ally)?",
        r"embark(?:s|ed|ing)?",
        r"game-changing",
        r"unlock(?:s|ed|ing)?",
        r"harness(?:es|ed|ing)? the power",
        r"dive(?:s|d)? deep",
        r"it(?:'s|\u2019s| is) (?:important|worth) (?:to )?not(?:e|ing)",
        r"that being said",
        r"at the end of the day",
        r"in today(?:'s|\u2019s) (?:fast-paced|digital|modern) world",
    ],
    # LIMITED = tolerated up to TIER2_MAX_PER_TERM / TIER2_MAX_TOTAL.
    "VOCAB_LIMITED": [
        r"foster(?:s|ed|ing)?",
        r"crucial(?:ly)?",
        r"pivotal",
        r"streamline(?:s|d)?",
        r"empower(?:s|ed|ing)?",
        r"showcase(?:s|d)?",
        r"meticulous(?:ly)?",
        r"compelling",
        r"innovative",
        r"comprehensive",
        r"journeys?",
    ],

    # ---- 5. Constructions ("shapes"), name -> regex, matched per sentence, case-insensitive
    # Calibrated hedging is NOT flagged: a single "may/suggest" is house style.
    # Only *stacked* hedges ("may potentially") are.
    "CONSTRUCTIONS": {
        "not just X, but Y": (
            r"\bnot (?:just|merely|simply)\b[^.;!?]{0,120}?[,;]?\s*"
            r"(?:but(?: also)?|it(?:'s|\u2019s| is)|rather)\b"
        ),
        "more than just": r"\bmore than (?:just|merely|simply)\b",
        "that's where X comes in": r"\bthat(?:'s|\u2019s| is) where [^.;!?]{1,60}? comes? in\b",
        "stacked hedge": (
            r"\b(?:may|might|could|can) (?:potentially|possibly|perhaps)\b"
            r"|\b(?:potentially|possibly|perhaps) (?:may|might|could)\b"
        ),
        "self-answering question": r"^(?:the )?(?:result|catch|answer|upshot|takeaway)\?$",
    },

    # ---- 6. Exemptions --------------------------------------------------------
    # Fixed technical collocations you accept despite the word lists, matched
    # case-insensitively and blanked out before linting. Empty by default:
    # robust / landscape / leverage are treated as AI vocabulary everywhere.
    # Examples if you ever hit a legitimate term of art:
    #   "high-leverage point", "leverage plot", "immune landscape", "robust regression"
    "ALLOW_PHRASES": [],

    # ---- 7. Sentence splitting ------------------------------------------------
    "ABBREVIATIONS": ["et al.", "e.g.", "i.e.", "Fig.", "Figs.", "vs.", "approx.", "No.", "Dr."],

    # ---- 8. Output ------------------------------------------------------------
    "EXCERPT_CHARS": 140,
}

# The four scored groups (order = report order). Each clean group is worth 1 point.
GROUPS = ("vocabulary", "constructions", "dash_cadence", "tricolon")

# Not user-tunable: syntax-level building blocks.
_EMDASH = re.compile(r"\u2014|(?<=\s)--(?=\s)")        # em-dash or spaced "--"; en-dash (ranges) is fine
_TRICOLON = re.compile(r"\b[a-z][a-z-]{2,}, [a-z][a-z-]{2,},? (?:and|or) [a-z][a-z-]{2,}\b")
_MD_HEADING = re.compile(r"^\s{0,3}#{1,6}\s*(.+?)\s*#*\s*$")
_NUMBERING = re.compile(r"^\(?\d+(?:\.\d+)*[.)]?\s+")


class InputError(ValueError):
    """Raised for exit-code-2 situations: the linter cannot give an honest verdict."""


# -----------------------------------------------------------------------------
# Config handling
# -----------------------------------------------------------------------------
def _effective_config(overrides):
    """Return CONFIG merged with overrides. Unknown keys are an error (catches typos)."""
    cfg = copy.deepcopy(CONFIG)
    for key, value in (overrides or {}).items():
        if key not in cfg:
            raise InputError("unknown config key: %r" % key)
        cfg[key] = value
    return cfg


# -----------------------------------------------------------------------------
# Section-aware paragraph collection
# -----------------------------------------------------------------------------
def _norm(name):
    """Normalise a heading: strip markdown emphasis, numbering, trailing colon; lowercase."""
    name = re.sub(r"[*_`]", "", name).strip().rstrip(":").strip()
    name = _NUMBERING.sub("", name)
    return name.lower()


def _classify_heading(line, scan_set, skip_set):
    """
    Return None if `line` is not a heading, else (mode, label) where mode is
    'scan' | 'skip' | 'inherit'.
      * Markdown heading ('## Methods'): known name switches mode, unknown inherits.
      * Bare line ('Methods'): treated as a heading ONLY if it is a known section name,
        so ordinary short sentences are never mistaken for headings.
    """
    md = _MD_HEADING.match(line)
    candidate = md.group(1) if md else line.strip()
    key = _norm(candidate)
    if key in scan_set:
        return "scan", key
    if key in skip_set:
        return "skip", key
    if md:
        return "inherit", key
    return None


def _collect_paragraphs(text, cfg):
    """Yield scanned paragraphs as dicts {text, line, section}; also return meta info."""
    scan_set = {_norm(s) for s in cfg["SCAN_SECTIONS"]}
    skip_set = {_norm(s) for s in cfg["SKIP_SECTIONS"]}
    mode = "scan" if cfg["SCAN_PREAMBLE"] else "skip"
    label = "preamble"
    saw_heading = False
    in_fence = False
    paragraphs, buf, buf_line = [], [], None
    scanned_sections, skipped_sections = [], []

    def flush():
        nonlocal buf, buf_line
        if buf:
            joined = " ".join(buf)
            joined = re.sub(r"`[^`]*`", " ", joined)      # inline code is not prose
            paragraphs.append({"text": joined, "line": buf_line, "section": label})
        buf, buf_line = [], None

    for lineno, raw in enumerate(text.splitlines(), 1):
        stripped = raw.strip()
        if stripped.startswith("```"):                    # fenced code block toggles
            flush()
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        heading = _classify_heading(raw, scan_set, skip_set) if stripped else None
        if heading:
            flush()
            saw_heading = True
            new_mode, label = heading
            if new_mode != "inherit":
                mode = new_mode
            (scanned_sections if mode == "scan" else skipped_sections).append(label)
            continue
        if not stripped or stripped.startswith("|"):      # blank line or markdown table row
            flush()
            continue
        if mode == "scan":
            if not buf:
                buf_line = lineno
            buf.append(stripped)
    flush()
    meta = {"saw_heading": saw_heading, "scanned_sections": scanned_sections,
            "skipped_sections": skipped_sections}
    return paragraphs, meta


def _split_sentences(paragraph, cfg):
    """Sentence split with abbreviation protection ('et al.', 'Fig.' ...)."""
    protected = paragraph
    for abbr in cfg["ABBREVIATIONS"]:
        protected = protected.replace(abbr, abbr.replace(".", "\x00"))
    parts = re.split(r"(?<=[.!?])\s+(?=[A-Z0-9\"'(\[])", protected)
    return [p.replace("\x00", ".").strip() for p in parts if p.strip()]


def _mask_allowed(sentence, cfg):
    """Blank out exempt phrases so they cannot trigger any rule."""
    for phrase in cfg["ALLOW_PHRASES"]:
        sentence = re.sub(re.escape(phrase), " ", sentence, flags=re.I)
    return sentence


# -----------------------------------------------------------------------------
# Core lint
# -----------------------------------------------------------------------------
def lint(text, config=None):
    """
    Lint `text` and return a result dict:
      {score, max_score, passed, groups: {name: {failed, hits: [...]}},
       scanned_words, scanned_sections, skipped_sections, warnings}
    Raises InputError when no honest verdict is possible.
    """
    cfg = _effective_config(config)
    if not isinstance(text, str) or not text.strip():
        raise InputError("empty input (an empty file must never count as clean)")

    paragraphs, meta = _collect_paragraphs(text, cfg)
    scanned_text = " ".join(p["text"] for p in paragraphs)
    words = len(re.findall(r"[A-Za-z][A-Za-z'\u2019-]*", scanned_text))
    if words < cfg["MIN_SCANNED_WORDS"]:
        raise InputError(
            "only %d scannable words (need >= %d); check the section headings and "
            "SCAN_SECTIONS / SKIP_SECTIONS" % (words, cfg["MIN_SCANNED_WORDS"]))
    latin = len(re.findall(r"[A-Za-z]", scanned_text))
    cjk = len(re.findall(r"[\u4e00-\u9fff\u3040-\u30ff\uac00-\ud7af]", scanned_text))
    if cjk / max(1, latin + cjk) > cfg["MAX_NON_LATIN_RATIO"]:
        raise InputError("text is mostly non-English; the catalogue is English-only, "
                         "so a pass would be meaningless")

    warnings = []
    if not meta["saw_heading"]:
        warnings.append("no section headings found; the whole text was scanned "
                        "(Methods/Results are NOT skipped)")

    # Sentence records: (line, section, sentence with exemptions blanked)
    sentences = []
    for para in paragraphs:
        for sent in _split_sentences(para["text"], cfg):
            sentences.append({"line": para["line"], "section": para["section"],
                              "text": _mask_allowed(sent, cfg)})

    def excerpt(s):
        limit = cfg["EXCERPT_CHARS"]
        return s if len(s) <= limit else s[:limit - 3] + "..."

    def mk(group, term, rec):
        return {"group": group, "term": term, "section": rec["section"],
                "line": rec["line"], "excerpt": excerpt(rec["text"])}

    groups = {g: {"failed": False, "hits": []} for g in GROUPS}

    # -- group 1: vocabulary --------------------------------------------------
    always = [re.compile(r"\b(?:%s)\b" % p, re.I) for p in cfg["VOCAB_ALWAYS"]]
    limited = [re.compile(r"\b(?:%s)\b" % p, re.I) for p in cfg["VOCAB_LIMITED"]]
    limited_hits, limited_counts = [], [0] * len(limited)
    for rec in sentences:
        for rx in always:
            for m in rx.finditer(rec["text"]):
                groups["vocabulary"]["hits"].append(mk("vocabulary", m.group(0).lower(), rec))
        for i, rx in enumerate(limited):
            for m in rx.finditer(rec["text"]):
                limited_counts[i] += 1
                limited_hits.append(mk("vocabulary", m.group(0).lower(), rec))
    limited_failed = (any(c > cfg["TIER2_MAX_PER_TERM"] for c in limited_counts)
                      or sum(limited_counts) > cfg["TIER2_MAX_TOTAL"])
    if limited_failed:
        groups["vocabulary"]["hits"].extend(limited_hits)
    groups["vocabulary"]["failed"] = bool(groups["vocabulary"]["hits"])

    # -- group 2: constructions ----------------------------------------------
    shapes = {name: re.compile(rx, re.I) for name, rx in cfg["CONSTRUCTIONS"].items()}
    for rec in sentences:
        for name, rx in shapes.items():
            if rx.search(rec["text"]):
                groups["constructions"]["hits"].append(mk("constructions", name, rec))
    groups["constructions"]["failed"] = bool(groups["constructions"]["hits"])

    # -- group 3: dash cadence ------------------------------------------------
    for rec in sentences:
        if len(_EMDASH.findall(rec["text"])) > cfg["EMDASH_MAX_PER_SENTENCE"]:
            groups["dash_cadence"]["hits"].append(mk("dash_cadence", "em-dash pile-up", rec))
    groups["dash_cadence"]["failed"] = bool(groups["dash_cadence"]["hits"])

    # -- group 4: rule-of-three rhythm ---------------------------------------
    triples = []
    for rec in sentences:
        no_parens = re.sub(r"\([^)]*\)", " ", rec["text"])   # "(age, sex, and BMI)" is a covariate list
        for m in _TRICOLON.finditer(no_parens):
            triples.append(mk("tricolon", m.group(0), rec))
    if len(triples) > cfg["TRICOLON_MAX_ALLOWED"]:
        groups["tricolon"]["hits"] = triples
        groups["tricolon"]["failed"] = True

    score = sum(1 for g in GROUPS if not groups[g]["failed"])
    return {
        "score": score,
        "max_score": len(GROUPS),
        "passed": score >= cfg["PASS_SCORE"],
        "groups": groups,
        "scanned_words": words,
        "scanned_sections": meta["scanned_sections"],
        "skipped_sections": meta["skipped_sections"],
        "warnings": warnings,
    }


# -----------------------------------------------------------------------------
# Reporting / CLI
# -----------------------------------------------------------------------------
def format_report(result):
    """Human-readable report. Hits are advisory: the user decides what to change."""
    lines = ["STYLE-SCORE %d/%d  (%s)   scanned %d words" % (
        result["score"], result["max_score"],
        "PASS" if result["passed"] else "FAIL", result["scanned_words"])]
    if result["skipped_sections"]:
        lines.append("skipped sections: " + ", ".join(result["skipped_sections"]))
    for w in result["warnings"]:
        lines.append("warning: " + w)
    for name in GROUPS:
        grp = result["groups"][name]
        lines.append("[%s] %s" % (name, "FAIL" if grp["failed"] else "ok"))
        for h in grp["hits"]:
            lines.append('  L%s [%s] %s | "%s"' % (h["line"], h["section"], h["term"], h["excerpt"]))
    return "\n".join(lines)


def main(argv=None):
    ap = argparse.ArgumentParser(description="Offline AI-tell linter (G-05 style-lint sub-check).")
    ap.add_argument("path", nargs="?", help="text/markdown file, or '-' for stdin")
    ap.add_argument("--text", help="lint this string instead of a file")
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    ap.add_argument("--config", help="JSON file overriding any CONFIG key")
    args = ap.parse_args(argv)
    try:
        overrides = None
        if args.config:
            overrides = json.loads(Path(args.config).read_text(encoding="utf-8"))
        if args.text is not None:
            text = args.text
        elif args.path == "-":
            text = sys.stdin.read()
        elif args.path:
            text = Path(args.path).read_text(encoding="utf-8")
        else:
            raise InputError("give a file path, '-' for stdin, or --text")
        result = lint(text, overrides)
    except (InputError, OSError, UnicodeDecodeError, json.JSONDecodeError) as exc:
        print("STYLE-LINT INPUT ERROR: %s" % exc, file=sys.stderr)
        return 2
    print(json.dumps(result, ensure_ascii=False, indent=2) if args.json else format_report(result))
    return 0 if result["passed"] else 1


if __name__ == "__main__":
    sys.exit(main())
