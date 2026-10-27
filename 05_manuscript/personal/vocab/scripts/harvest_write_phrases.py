#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
harvest_write_phrases.py -- count the owner's recurring writing phrases in the 0doc bank.

Offline, stdlib only, read-only on the bank. Default is dry-run: it prints a
summary and the top rows. Add --execute to write the markdown table.

Run:
    python3 harvest_write_phrases.py --bank "{doc_review_bank}\\bank"
    python3 harvest_write_phrases.py --bank review-text.jsonl --min-docs 2 --min-count 3
    python3 harvest_write_phrases.py --bank flattened.jsonl --execute --out phrases.md

Feeds `05_manuscript/personal/vocab/L2/preferred-personal.md`; the tiers in that
file (A / B / C) decide what may be absorbed. This script only counts.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

# =============================================================================
# CONFIG
# =============================================================================

# Field names tried, in order, when a JSONL / TSV row carries the prose.
TEXT_FIELDS = (
    "text", "body", "comment", "content", "reply", "message", "paragraph",
    "quote", "sentence", "unit", "after", "value",
)
# Fields naming the lane of a row (review vs reply vs manuscript draft).
SOURCE_FIELDS = ("source", "kind", "lane", "bucket", "type", "role", "task")
# File types read from --bank when it is a directory.
SUFFIXES = (".jsonl", ".ndjson", ".tsv", ".csv", ".md", ".txt")
# Recursion guard for --bank <dir>.
MAX_DEPTH = 3
# Minimum characters for a document to count (drops headers and stubs).
# 20 chars: one full Chinese comment, or a short English sentence.
MIN_DOC_CHARS = 20

# English n-gram width, and width of the sentence-head / sentence-tail windows.
EN_NGRAM = (2, 6)
EN_EDGE = 5
# A phrase must begin and end on a content word. Modals stay allowed at the
# tail because the lab's closer is "Future research should"; articles,
# prepositions, conjunctions and copulas do not.
EDGE_BAN = frozenset("""
a an the and or but nor so yet for of to in on at by with from into onto over under
as than that this these those there here is are was were be been being am
not no if then thus hence which who whom whose what when where while whereas
although because since until do does did done have has had
""".split())

# Chinese sentence split, and char n-gram width at each edge.
ZH_SPLIT = re.compile(r"[。！？；!?;\n]+")
ZH_NGRAM = (2, 8)
# Punctuation that must not sit at a Chinese phrase edge.
ZH_EDGE_PUNCT = "，、,：:（）()《》“”\"'…—　"

# Sentence split for English prose.
EN_SPLIT = re.compile(r"(?<=[.!?])[\s\u3000]+")
EN_TOKEN = re.compile(r"[A-Za-z][A-Za-z'\-]*")
# A sentence must contain a CJK character to be treated as Chinese.
CJK = re.compile(r"[\u4e00-\u9fff]")
# Heading of every table this script writes; such a file is never re-read as bank prose.
TABLE_TITLE = "Bank phrase harvest"
OUTPUT_MARKER = "# " + TABLE_TITLE
# BOM-safe decode.
ENCODING = "utf-8-sig"


# =============================================================================
# LOAD
# =============================================================================

def _rows_from_jsonl(path: Path):
    with path.open("r", encoding=ENCODING, errors="replace") as handle:
        for line in handle:
            line = line.strip()
            if not line:
                continue
            try:
                row = json.loads(line)
            except json.JSONDecodeError:
                continue
            if isinstance(row, str):
                yield {"text": row}
            elif isinstance(row, dict):
                yield row


def _rows_from_table(path: Path):
    with path.open("r", encoding=ENCODING, errors="replace", newline="") as handle:
        reader = csv.DictReader(handle, delimiter="\t" if path.suffix == ".tsv" else ",")
        for row in reader:
            yield {k: v for k, v in row.items() if k is not None}


def _doc_from_plain(path: Path) -> str:
    text = path.read_text(encoding=ENCODING, errors="replace")
    # Never count this script's own output as bank prose.
    return "" if text.startswith(OUTPUT_MARKER) else text


def _text_of(row: dict) -> str:
    for field in TEXT_FIELDS:
        value = row.get(field)
        if isinstance(value, str) and value.strip():
            return value
    best = ""
    for value in row.values():
        if isinstance(value, str) and len(value.strip()) > len(best.strip()):
            best = value
    return best


def _lane_of(row: dict, fallback: str) -> str:
    for field in SOURCE_FIELDS:
        value = row.get(field)
        if isinstance(value, str) and value.strip():
            return value.strip().lower()[:40]
    return fallback


def collect_docs(bank: Path, skip: Path | None = None) -> list[tuple[str, str, str]]:
    """Return (lane, origin, text) for every document under --bank."""
    if not bank.exists():
        print("bank path not found: %s" % bank, file=sys.stderr)
        raise SystemExit(2)
    skip = skip.resolve() if skip is not None else None
    docs: list[tuple[str, str, str]] = []
    files = [bank] if bank.is_file() else sorted(
        p for p in bank.rglob("*")
        if p.is_file() and p.suffix.lower() in SUFFIXES
        and len(p.relative_to(bank).parts) <= MAX_DEPTH
        and p.resolve() != skip
    )
    for path in files:
        fallback = path.stem if (bank.is_dir() and path.parent == bank) else path.parent.name
        if path.suffix.lower() in (".jsonl", ".ndjson", ".tsv", ".csv"):
            for row in (_rows_from_jsonl(path) if path.suffix.lower() in (".jsonl", ".ndjson")
                        else _rows_from_table(path)):
                text = _text_of(row)
                if len(text.strip()) >= MIN_DOC_CHARS:
                    docs.append((_lane_of(row, fallback), path.name, text))
        else:
            text = _doc_from_plain(path)
            if len(text.strip()) >= MIN_DOC_CHARS:
                docs.append((fallback, path.name, text))
    return docs


# =============================================================================
# EXTRACT
# =============================================================================

def en_phrases(text: str):
    """Sentence-head and sentence-tail windows only.

    Mid-sentence windows of one long sentence all carry the same counts, so they
    would bury the table in fragments. The recurring *wording* sits at the head
    (`This study has several limitations`) or the tail (`... in the test set`).
    """
    for sentence in EN_SPLIT.split(text):
        tokens = [t.lower() for t in EN_TOKEN.findall(sentence)]
        if len(tokens) < EN_NGRAM[0]:
            continue
        for size in range(EN_NGRAM[0], min(EN_NGRAM[1], EN_EDGE, len(tokens)) + 1):
            windows = [tuple(tokens[:size])]
            # In a short sentence the head and tail windows overlap; emitting both
            # counts the same text twice and manufactures suffixes such as
            # "you for the suggestion". Keep the head alone when they touch.
            if len(tokens) - size > size:
                windows.append(tuple(tokens[-size:]))
            for gram in windows:
                if gram[0] in EDGE_BAN or gram[-1] in EDGE_BAN:
                    continue
                if all(t in EDGE_BAN for t in gram):
                    continue
                yield " ".join(gram)


def zh_phrases(text: str):
    for sentence in ZH_SPLIT.split(text):
        sentence = re.sub(r"\s+", "", sentence).strip(ZH_EDGE_PUNCT)
        if len(sentence) < ZH_NGRAM[0] or not CJK.search(sentence):
            continue
        for size in range(ZH_NGRAM[0], ZH_NGRAM[1] + 1):
            if len(sentence) < size:
                break
            spans = [sentence[:size]]
            # Same overlap rule as the English side.
            if len(sentence) - size > size:
                spans.append(sentence[-size:])
            for gram in spans:
                gram = gram.strip(ZH_EDGE_PUNCT)
                if len(gram) >= ZH_NGRAM[0] and CJK.search(gram):
                    yield gram


# =============================================================================
# COUNT
# =============================================================================

def _extractors(lang: str):
    """Pick the phrase extractors for --lang."""
    chosen = []
    if lang in ("en", "both"):
        chosen.append(en_phrases)
    if lang in ("zh", "both"):
        chosen.append(zh_phrases)
    return chosen


def harvest(docs, lang: str):
    total = Counter()
    doc_freq = Counter()
    lanes = defaultdict(Counter)
    extractors = _extractors(lang)
    for lane, _origin, text in docs:
        hits = Counter()
        for extract in extractors:
            hits.update(extract(text))
        for phrase, count in hits.items():
            total[phrase] += count
            doc_freq[phrase] += 1
            lanes[phrase][lane] += count
    return total, doc_freq, lanes


def load_bans(path: Path | None) -> list[str]:
    """Read probe strings from ban-terms.yaml without a YAML parser."""
    if path is None:
        return []
    probes: list[str] = []
    for line in path.read_text(encoding=ENCODING, errors="replace").splitlines():
        match = re.match(r"\s*-?\s*probe:\s*(.+?)\s*$", line)
        if match:
            probes.append(match.group(1).strip().strip("\"'").lower())
    return probes


def _collapse_chain(kept: dict[str, tuple[int, int]]) -> dict[str, tuple[int, int]]:
    """Keep only the longest phrase inside a group of identical counts.

    Sentence-head and sentence-tail windows of one sentence all carry the same
    count and document frequency, so `这个` / `这个结` / `这个结果`,
    `thank you` / `thank you for`, and `study has several limitations` /
    `several limitations` would otherwise all sit in the table. A phrase is
    dropped when a longer phrase with the same (count, doc_freq) contains it.
    """
    ordered = sorted(kept, key=len, reverse=True)
    dropped: set[str] = set()
    for phrase in ordered:
        if phrase in dropped:
            continue
        counts = kept[phrase]
        for other in ordered:
            if other is phrase or other in dropped or len(other) <= len(phrase):
                continue
            if kept[other] != counts or phrase not in other:
                continue
            dropped.add(phrase)
            break
    return {p: v for p, v in kept.items() if p not in dropped}


def rank(total, doc_freq, lanes, min_docs: int, min_count: int, limit: int, bans):
    kept = {
        phrase: (count, doc_freq[phrase])
        for phrase, count in total.items()
        if doc_freq[phrase] >= min_docs and count >= min_count
    }
    kept = _collapse_chain(kept)
    rows = []
    for phrase, (count, docs) in kept.items():
        banned = any(probe in phrase for probe in bans)
        top_lane = lanes[phrase].most_common(1)[0][0]
        rows.append((docs, count, phrase, top_lane, banned))
    rows.sort(key=lambda r: (-r[0], -r[1], r[2]))
    return rows[:limit] if limit else rows


def as_markdown(title: str, rows, docs, args) -> str:
    lines = [
        "# %s" % title,
        "",
        "docs=%d · min_docs=%d · min_count=%d · langs=%s" % (
            len(docs), args.min_docs, args.min_count, args.lang),
        "",
        "| 表达 | 次数 | 篇数 | 主 lane | 备注 |",
        "|---|---:|---:|---|---|",
    ]
    for doc_freq, count, phrase, lane, banned in rows:
        lines.append("| %s | %d | %d | %s | %s |" % (
            phrase.replace("|", "\\|"), count, doc_freq, lane, "已禁(L1)" if banned else ""))
    lines.append("")
    return "\n".join(lines)


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Count recurring writing phrases in the 0doc bank.")
    parser.add_argument("--bank", required=True, type=Path, help="bank directory or single file")
    parser.add_argument("--out", type=Path, help="markdown output path (needs --execute)")
    parser.add_argument("--bans", type=Path, help="ban-terms.yaml, to flag already-banned phrases")
    parser.add_argument("--lang", choices=("en", "zh", "both"), default="both")
    parser.add_argument("--min-docs", type=int, default=2, help="minimum document frequency")
    parser.add_argument("--min-count", type=int, default=3, help="minimum total occurrences")
    parser.add_argument("--limit", type=int, default=80, help="rows printed per run (0 = all)")
    parser.add_argument("--execute", action="store_true", help="write --out; default is dry-run")
    args = parser.parse_args(argv)

    docs = collect_docs(args.bank, skip=args.out)
    if not docs:
        print("no readable prose found under %s" % args.bank, file=sys.stderr)
        return 2

    total, doc_freq, lanes = harvest(docs, args.lang)
    rows = rank(total, doc_freq, lanes, args.min_docs, args.min_count, args.limit,
                load_bans(args.bans))
    table = as_markdown(TABLE_TITLE, rows, docs, args)

    print("docs=%d phrases=%d kept=%d" % (len(docs), len(total), len(rows)))
    if not args.execute:
        print("dry-run: pass --execute --out FILE to write")
        print(table)
        return 0
    if args.out is None:
        print("--execute needs --out", file=sys.stderr)
        return 2
    args.out.write_text(table + "\n", encoding="utf-8")
    print("wrote %s" % args.out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
