#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
harvest_write_phrases.py -- count the owner's recurring manuscript wording in the 0doc bank.

Reads the paragraph layer of `_bank` (paras.jsonl), groups it by IMRAD section, and
counts sentence-head / sentence-tail phrases per section. Offline, stdlib only,
read-only on the bank. Default is dry-run: prints the summary and the tables.
`--execute --out FILE` writes the markdown.

Run:
    python3 harvest_write_phrases.py --bank "{doc_review_bank}\\bank\\paras.jsonl"
    python3 harvest_write_phrases.py --bank paras.jsonl --section Discussion --limit 40
    python3 harvest_write_phrases.py --bank paras.jsonl --execute --out phrases.md

Feeds `05_manuscript/advanced/vocab/L2/preferred-advanced.md`. This script only
counts; the tiers in that file decide what may be absorbed.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

# =============================================================================
# CONFIG
# =============================================================================

# Paragraph fields carrying prose, in preference order.
TEXT_FIELDS = ("text_acc", "text_orig", "text")
# Field identifying one manuscript.
DOC_FIELD = "doc_id"
# Field carrying the section ordinal written by the docx extractor.
SECTION_FIELD = "section_idx"
# Paragraphs to skip: table cells and text boxes are not running prose.
SKIP_FLAGS = ("in_table", "in_textbox")
# Section ordinal -> IMRAD label. Unknown ordinals fall back to "other".
SECTIONS = {
    0: "Abstract",
    1: "Introduction",
    2: "Methods",
    3: "Results",
    4: "Discussion",
}
# Paragraphs shorter than this are headings, labels or stubs. Chinese carries more
# information per character, so a 60-char floor would drop whole Chinese paragraphs.
MIN_PARA_CHARS = 60
MIN_PARA_CHARS_ZH = 20

# English phrase width and the sentence-head / sentence-tail window.
EN_NGRAM = (2, 6)
EN_EDGE = 5
# A phrase may not END on a function word ("thank you for the"). The head is left
# alone on purpose: the lab's standard openers start there ("In this study, we",
# "This study has several limitations", "The aim of this study was"), and banning
# head function words silently deleted every one of them.
EDGE_TAIL_BAN = frozenset("""
a an the and or but nor so yet for of to in on at by with from into onto over under
as than that this these those there here is are was were be been being am
not no if then thus hence which who whom whose what when where while whereas
although because since until do does did done have has had
""".split())

# Chinese phrase width at each edge, and the punctuation stripped from an edge.
ZH_NGRAM = (2, 10)
ZH_EDGE_PUNCT = "，、,：:（）()《》“”\"'…—　"
CJK = re.compile(r"[\u4e00-\u9fff]")
ZH_MIN_RATIO = 0.15
# Characters that cannot start a Chinese phrase: they only ever follow another word.
ZH_LEAD_BAN = frozenset("的了着过是在和与及或而但却就都也还很更最将把被从对于其为以之其接并又再才已曾正共约近该此")  # a paragraph at or above this CJK share is counted as Chinese

EN_SPLIT = re.compile(r"(?<=[.!?])[\s\u3000]+")
EN_TOKEN = re.compile(r"[A-Za-z][A-Za-z'\-]*")
ZH_SPLIT = re.compile(r"[。！？；!?;\n，、：,]+")

# First line of any table this script writes; such a file is never re-read.
TABLE_TITLE = "Bank phrase harvest"
OUTPUT_MARKER = "# " + TABLE_TITLE
ENCODING = "utf-8-sig"


# =============================================================================
# LOAD
# =============================================================================

def _text_of(row: dict) -> str:
    for field in TEXT_FIELDS:
        value = row.get(field)
        if isinstance(value, str) and value.strip():
            return value
    return ""


def _section_of(row: dict) -> str:
    raw = row.get(SECTION_FIELD)
    if isinstance(raw, int) and raw in SECTIONS:
        return SECTIONS[raw]
    try:
        return SECTIONS.get(int(raw), "other")
    except (TypeError, ValueError):
        return "other"


def _skipped(row: dict) -> bool:
    return any(bool(row.get(flag)) for flag in SKIP_FLAGS)


def collect_docs(bank: Path) -> list[tuple[str, str, str]]:
    """Return (section, doc_id, text) for every prose paragraph."""
    if not bank.exists():
        print("bank path not found: %s" % bank, file=sys.stderr)
        raise SystemExit(2)
    docs: list[tuple[str, str, str]] = []
    with bank.open("r", encoding=ENCODING, errors="replace") as handle:
        for line in handle:
            line = line.strip()
            if not line:
                continue
            try:
                row = json.loads(line)
            except json.JSONDecodeError:
                continue
            if not isinstance(row, dict) or _skipped(row):
                continue
            text = _text_of(row)
            stripped = text.strip()
            floor = MIN_PARA_CHARS_ZH if _is_zh(stripped) else MIN_PARA_CHARS
            if len(stripped) < floor:
                continue
            docs.append((_section_of(row), str(row.get(DOC_FIELD) or "?"), text))
    return docs


# =============================================================================
# EXTRACT
# =============================================================================

def _is_zh(text: str) -> bool:
    if not text:
        return False
    return len(CJK.findall(text)) / len(text) >= ZH_MIN_RATIO


def en_phrases(text: str):
    """Sentence-head and sentence-tail windows of an English paragraph.

    Mid-sentence windows of one long sentence all carry the same counts, so they
    would bury the table in fragments; recurring wording sits at a sentence edge.
    """
    for sentence in EN_SPLIT.split(text):
        tokens = [t.lower() for t in EN_TOKEN.findall(sentence)]
        if len(tokens) < EN_NGRAM[0]:
            continue
        seen: set[tuple[str, ...]] = set()
        for size in range(EN_NGRAM[0], min(EN_NGRAM[1], EN_EDGE, len(tokens)) + 1):
            windows = [tuple(tokens[:size])]
            # Head and tail overlap in a short sentence; emitting both counts the
            # same text twice and invents suffixes such as "you for the suggestion".
            if len(tokens) - size > size:
                windows.append(tuple(tokens[-size:]))
            for gram in windows:
                if gram in seen:
                    continue
                if gram[-1] in EDGE_TAIL_BAN:
                    continue
                if all(t in EDGE_TAIL_BAN for t in gram):
                    continue
                seen.add(gram)
                yield " ".join(gram)


def zh_phrases(text: str):
    """Clause-head and clause-tail character windows of a Chinese paragraph.

    Split on every Chinese clause mark, not just the full stop: a clause is the
    unit the owner actually repeats ("样本量偏小" / "建议补充多中心数据"), and
    splitting there also keeps punctuation out of the phrase.
    """
    for clause in ZH_SPLIT.split(text):
        clause = re.sub(r"\s+", "", clause).strip(ZH_EDGE_PUNCT)
        if len(clause) < ZH_NGRAM[0] or not CJK.search(clause):
            continue
        seen: set[str] = set()
        for size in range(ZH_NGRAM[0], ZH_NGRAM[1] + 1):
            if len(clause) < size:
                break
            spans = [clause[:size]]
            if len(clause) - size > size:
                spans.append(clause[-size:])
            # A window that starts or ends mid-compound is noise ("接比较这些指标").
            # Drop it when a one-character shift produces a longer-matching span.
            spans = [s for s in spans if not (s[:1] in ZH_LEAD_BAN)]
            for gram in spans:
                gram = gram.strip(ZH_EDGE_PUNCT)
                if len(gram) < ZH_NGRAM[0] or not CJK.search(gram) or gram in seen:
                    continue
                seen.add(gram)
                yield gram


def _extractors(lang: str):
    chosen = []
    if lang in ("en", "both"):
        chosen.append(en_phrases)
    if lang in ("zh", "both"):
        chosen.append(zh_phrases)
    return chosen


# =============================================================================
# COUNT
# =============================================================================

def harvest(docs, lang: str):
    """Occurrences, document frequency and section, per phrase.

    Occurrences and document frequency are counted separately: using a set for
    both makes "次数" collapse into "篇数". Document frequency counts distinct
    manuscripts, not paragraphs, so one paper repeating a phrase ten times still
    counts as one paper.
    """
    occurrences = Counter()
    sections = defaultdict(Counter)
    docs_with: dict[str, set[str]] = defaultdict(set)
    docs_per_section: dict[str, set[str]] = defaultdict(set)
    extractors = _extractors(lang)
    for section, doc_id, text in docs:
        docs_per_section[section].add(doc_id)
        chosen = zh_phrases if _is_zh(text) else en_phrases
        if chosen not in extractors:
            continue
        hits = Counter(chosen(text))
        for phrase, count in hits.items():
            occurrences[phrase] += count
            sections[phrase][section] += count
            docs_with[phrase].add(doc_id)
    presence = Counter({p: len(ids) for p, ids in docs_with.items()})
    distinct_docs = {s: len(ids) for s, ids in docs_per_section.items()}
    return occurrences, presence, sections, distinct_docs


def _sub_phrases(phrase: str):
    if " " in phrase:
        tokens = phrase.split(" ")
        for start in range(len(tokens)):
            for end in range(start + 2, len(tokens) + 1):
                if end - start == len(tokens):
                    continue
                yield " ".join(tokens[start:end])
    else:
        for start in range(len(phrase)):
            for end in range(start + 2, len(phrase) + 1):
                if end - start == len(phrase):
                    continue
                yield phrase[start:end]


def collapse_chain(kept: dict[str, tuple[int, int]]) -> dict[str, tuple[int, int]]:
    """Keep the longest phrase inside a group of identical counts.

    Head and tail windows of one sentence share the same count, so without this
    the table fills with 这个 / 这个结 / 这个结果 and thank you / thank you for.
    """
    dropped: set[str] = set()
    ordered = sorted(kept, key=len, reverse=True)
    for i, phrase in enumerate(ordered):
        if phrase in dropped:
            continue
        counts = kept[phrase]
        for other in ordered[:i]:
            if other in dropped or kept[other] != counts:
                continue
            if phrase in other:
                dropped.add(phrase)
                break
    return {p: v for p, v in kept.items() if p not in dropped}


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


def rank(occurrences, presence, sections, min_docs, min_count, limit, bans):
    kept = {
        phrase: (count, presence[phrase])
        for phrase, count in occurrences.items()
        if presence[phrase] >= min_docs and count >= min_count
    }
    kept = collapse_chain(kept)
    rows = []
    for phrase, (count, docs) in kept.items():
        section = sections[phrase].most_common(1)[0][0]
        banned = any(probe in phrase for probe in bans)
        rows.append((docs, count, phrase, section, banned))
    rows.sort(key=lambda r: (-r[0], -r[1], r[2]))
    return rows[:limit] if limit else rows


# =============================================================================
# OUTPUT
# =============================================================================

def as_markdown(rows, docs, args) -> str:
    lines = [
        "# %s" % TABLE_TITLE,
        "",
        "paragraphs=%d · docs=%d · min_docs=%d · min_count=%d · langs=%s" % (
            len(docs), len({d for _s, d, _t in docs}), args.min_docs, args.min_count, args.lang),
        "",
        "| 表达 | 次数 | 篇数 | 主要章节 | 禁词 |",
        "|---|---:|---:|---|---|",
    ]
    for doc_freq, count, phrase, section, banned in rows:
        lines.append("| %s | %d | %d | %s | %s |" % (
            phrase.replace("|", "\\|"), count, doc_freq, section,
            "已禁(L1)" if banned else ""))
    lines.append("")
    return "\n".join(lines)


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(
        description="Count recurring manuscript phrases in the 0doc paragraph layer.")
    parser.add_argument("--bank", required=True, type=Path,
                        help="paras.jsonl (or a directory containing it)")
    parser.add_argument("--out", type=Path, help="markdown output path (needs --execute)")
    parser.add_argument("--bans", type=Path, help="ban-terms.yaml, to flag banned phrases")
    parser.add_argument("--lang", choices=("en", "zh", "both"), default="both")
    parser.add_argument("--section", help="only this IMRAD section (e.g. Discussion)")
    parser.add_argument("--min-docs", type=int, default=3, help="minimum document frequency")
    parser.add_argument("--min-count", type=int, default=5, help="minimum occurrences")
    parser.add_argument("--limit", type=int, default=60, help="rows printed (0 = all)")
    parser.add_argument("--execute", action="store_true", help="write --out; default dry-run")
    args = parser.parse_args(argv)

    bank = args.bank
    if bank.is_dir():
        bank = bank / "paras.jsonl"

    docs = collect_docs(bank)
    if args.section:
        docs = [d for d in docs if d[0].lower() == args.section.lower()]
    if not docs:
        print("no prose paragraphs found in %s" % bank, file=sys.stderr)
        return 2
    if bank.read_text(encoding=ENCODING, errors="replace").startswith(OUTPUT_MARKER):
        print("%s is this tool's own output, not a bank file" % bank, file=sys.stderr)
        return 2

    occurrences, presence, sections, distinct = harvest(docs, args.lang)
    rows = rank(occurrences, presence, sections, args.min_docs, args.min_count,
                args.limit, load_bans(args.bans))
    table = as_markdown(rows, docs, args)

    print("paragraphs=%d docs=%d phrases=%d kept=%d" % (
        len(docs), len({d for _s, d, _t in docs}), len(occurrences), len(rows)))
    print("docs per section: " + ", ".join("%s=%d" % (s, n) for s, n in sorted(distinct.items())))
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
