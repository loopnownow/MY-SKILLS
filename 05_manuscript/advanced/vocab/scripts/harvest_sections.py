#!/usr/bin/env python
r"""harvest_sections.py -- rebuild IMRAD sections for the paragraph layer and count phrases.

`paras.jsonl` carries `section_idx`, but every row holds `0` (the extractor never wrote the
ordinal), so section-scoped harvest returns nothing. This script rebuilds sections from
heading paragraphs in reading order, then counts sentence-head / sentence-tail phrases per
section. Chinese uses 3-8 character windows; a shorter span is dropped when a longer span
covers it.

Run (PowerShell, Python 3.13.9):

    python .\harvest_sections.py
    python .\harvest_sections.py --doc-prefix 05
    python .\harvest_sections.py --execute --out .\paras-sections.md
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import harvest_write_phrases as hw  # noqa: E402

# ---------------------------------------------------------------- CONFIG
# BANK: paragraph layer of _bank (read-only).
BANK = Path(r"D:\0Grok\0doc\_bank\bank\paras.jsonl")
# DOC_PREFIXES: empty = all 160 documents; --doc-prefix 05 limits to the manuscript layer.
DOC_PREFIXES: tuple[str, ...] = ()
# SKIP_FLAGS: table cells and text boxes are not running prose.
SKIP_FLAGS = ("in_table", "in_textbox")
# MIN_EN / MIN_ZH: minimum paragraph length in characters.
MIN_EN = 60
MIN_ZH = 20
# CJK_RATIO: share of CJK characters that marks a paragraph as Chinese.
CJK_RATIO = 0.15
# ZH_NGRAM: Chinese character windows (3 and up; two characters is a word, not a phrase).
ZH_NGRAM = (3, 8)
# DOMINANCE_ZH: a longer span whose count reaches this share of a shorter span wins.
DOMINANCE_ZH = 0.85
# HEADINGS: heading line -> section label, matched in order (case-insensitive).
HEADINGS = (
    (re.compile(r"^\s*(?:abstract|summary|中文摘要|英文摘要|摘\s*要)", re.IGNORECASE), "Abstract"),
    (re.compile(r"^\s*(?:introduction|background|前\s*言|引\s*言|背\s*景)", re.IGNORECASE), "Introduction"),
    (re.compile(r"^\s*(?:materials? and methods?|patients and methods?|subjects and methods?|methods?|材料与方法|对象与方法|资料与方法|方\s*法)", re.IGNORECASE), "Methods"),
    (re.compile(r"^\s*results?\b|^\s*结\s*果", re.IGNORECASE), "Results"),
    (re.compile(r"^\s*discussion\b|^\s*讨\s*论", re.IGNORECASE), "Discussion"),
    (re.compile(r"^\s*(?:conclusions?|concluding remarks)\b|^\s*(?:结\s*论|小\s*结)", re.IGNORECASE), "Conclusion"),
    (re.compile(r"^\s*(?:references?|bibliography)\b|^\s*参考文献", re.IGNORECASE), "References"),
)
# EXCLUDE_SECTIONS: these sections never enter the counts (a reference list is not wording).
EXCLUDE_SECTIONS = ("References",)
# NUM_PREFIX: numbering or chapter marker stripped before heading matching.
NUM_PREFIX = re.compile(
    r"^\s*(?:第\s*[0-9一二三四五六七八九十]+\s*[章节部分篇]\s*|[0-9]+(?:\s*[.、]\s*[0-9]*)*\s*[.、]?\s*)"
)
# HEADING_MAX: longer lines are treated as body text, not headings.
HEADING_MAX = 60
# SKIP_TEXT_RE: reference entries, affiliations and URLs are not wording.
SKIP_TEXT_RE = re.compile(
    r"^\s*\[\d+\]|\[[JMDCR]\]|https?://|\bdoi\b|\buniversity\b|\bchina\b|r-project\.org",
    re.IGNORECASE,
)
# BANS: machine ban list; a hit is labelled "banned(L1)" and never deleted.
BANS = Path(r"D:\0Grok\0doc\GitHub\MY-SKILLS\05_manuscript\base\vocab\L1\ban-terms.yaml")
# MIN_DOCS / MIN_COUNT / LIMIT: default thresholds and row cap.
MIN_DOCS = 3
MIN_COUNT = 5
LIMIT = 80
# OUT_DIR: default output directory.
OUT_DIR = Path(r"D:\0del\_by-function\vocab-harvest-20261027")

CJK = re.compile(r"[\u4e00-\u9fff]")
WS = re.compile(r"\s+")


def is_zh(text: str) -> bool:
    body = [ch for ch in text if not ch.isspace()]
    if not body:
        return False
    return len(CJK.findall(text)) / len(body) >= CJK_RATIO


def heading_of(text: str) -> str | None:
    body = WS.sub(" ", text).strip()
    if len(body) > HEADING_MAX:
        return None
    stripped = NUM_PREFIX.sub("", body).strip()
    for pattern, label in HEADINGS:
        if pattern.match(body) or (stripped and pattern.match(stripped)):
            return label
    return None


def load_paragraphs(bank: Path, prefixes: tuple[str, ...]) -> tuple[list[dict], Counter]:
    if not bank.is_file():
        raise FileNotFoundError(f"paragraph layer missing: {bank}")
    rows: list[dict] = []
    dropped: Counter = Counter()
    with bank.open(encoding="utf-8") as fh:
        for line in fh:
            if not line.strip():
                continue
            row = json.loads(line)
            doc_id = str(row.get("doc_id") or "")
            if prefixes and not doc_id.startswith(prefixes):
                dropped["doc_prefix"] += 1
                continue
            if any(bool(row.get(flag)) for flag in SKIP_FLAGS):
                dropped["table_or_textbox"] += 1
                continue
            text = WS.sub(" ", row.get("text_acc") or "").strip()
            label = heading_of(text)
            if label is not None:
                rows.append(
                    {
                        "doc_id": doc_id,
                        "pidx": int(row.get("pidx") or 0),
                        "text": text,
                        "zh": is_zh(text),
                        "heading": label,
                    }
                )
                continue
            if len(text) < (MIN_ZH if is_zh(text) else MIN_EN):
                dropped["too_short"] += 1
                continue
            if SKIP_TEXT_RE.search(text):
                dropped["reference_or_affiliation"] += 1
                continue
            rows.append(
                {
                    "doc_id": doc_id,
                    "pidx": int(row.get("pidx") or 0),
                    "text": text,
                    "zh": is_zh(text),
                    "heading": None,
                }
            )
    rows.sort(key=lambda item: (item["doc_id"], item["pidx"]))
    return rows, dropped


def assign_sections(rows: list[dict]) -> Counter:
    counts: Counter = Counter()
    current = "front"
    last_doc = None
    for row in rows:
        if row["doc_id"] != last_doc:
            current = "front"
            last_doc = row["doc_id"]
        if row["heading"] is not None:
            current = row["heading"]
            row["section"] = current
            continue
        row["section"] = current
        counts[current] += 1
    return counts


ZH_SPLIT = re.compile(r"[。！？；!?;\n]+")
ZH_EDGE = "，、,：:（）()《》“”\"'…—　 "


def zh_phrases(text: str):
    for sentence in ZH_SPLIT.split(text):
        body = WS.sub("", sentence).strip(ZH_EDGE)
        if len(body) < ZH_NGRAM[0] or not CJK.search(body):
            continue
        seen: set[str] = set()
        for size in range(ZH_NGRAM[0], ZH_NGRAM[1] + 1):
            if len(body) < size:
                break
            spans = [body[:size]]
            if len(body) - size > size:
                spans.append(body[-size:])
            for span in spans:
                span = span.strip(ZH_EDGE)
                if len(span) < ZH_NGRAM[0] or span in seen or not CJK.search(span):
                    continue
                seen.add(span)
                yield span


def collect(rows: list[dict]) -> tuple[Counter, Counter, dict, dict]:
    occurrences: Counter = Counter()
    docs_of: dict[str, set[str]] = defaultdict(set)
    sections: dict[str, Counter] = defaultdict(Counter)
    docs_per_section: dict[str, set[str]] = defaultdict(set)
    for row in rows:
        if row["heading"] is not None:
            continue
        docs_per_section[row["section"]].add(row["doc_id"])
        grams = Counter(zh_phrases(row["text"]) if row["zh"] else hw.en_phrases(row["text"]))
        for phrase, count in grams.items():
            occurrences[phrase] += count
            docs_of[phrase].add(row["doc_id"])
            sections[phrase][row["section"]] += count
    presence: Counter = Counter({phrase: len(docs) for phrase, docs in docs_of.items()})
    return occurrences, presence, sections, docs_per_section


def collapse(kept: dict[str, tuple[int, int]]) -> dict[str, tuple[int, int]]:
    ordered = sorted(kept, key=len, reverse=True)
    buckets: dict[int, list[str]] = defaultdict(list)
    survivors: dict[str, tuple[int, int]] = {}
    for phrase in ordered:
        count = kept[phrase][0]
        if CJK.search(phrase):
            low = max(1, int(count * DOMINANCE_ZH))
            high = int(count / DOMINANCE_ZH) + 1
            peers = range(low, high + 1)
        else:
            peers = (count,)
        redundant = False
        for value in peers:
            for longer in buckets.get(value, ()):
                if phrase in longer:
                    redundant = True
                    break
            if redundant:
                break
        if redundant:
            continue
        buckets[count].append(phrase)
        survivors[phrase] = kept[phrase]
    return survivors


def ranked(occurrences: Counter, presence: Counter, sections: dict,
           min_docs: int, min_count: int, limit: int, bans: list) -> list:
    kept = {
        phrase: (count, presence[phrase])
        for phrase, count in occurrences.items()
        if presence[phrase] >= min_docs and count >= min_count
    }
    kept = collapse(kept)
    rows = []
    for phrase, (count, docs) in kept.items():
        section = sections[phrase].most_common(1)[0][0]
        banned = any(probe in phrase for probe in bans)
        rows.append((docs, count, phrase, section, banned))
    rows.sort(key=lambda item: (-item[0], -item[1], item[2]))
    return rows[:limit] if limit else rows


def render(rows: list, paragraphs: int, doc_count: int, docs_per_section: dict,
           paras_per_section: Counter, args) -> str:
    ordered = sorted(docs_per_section, key=lambda s: (-len(docs_per_section[s]), s))
    lines = [
        "# Bank phrase harvest (sections rebuilt)",
        "",
        "paragraphs=%d · docs=%d · min_docs=%d · min_count=%d · langs=both"
        % (paragraphs, doc_count, args.min_docs, args.min_count),
        "docs per section: " + ", ".join("%s=%d" % (s, len(docs_per_section[s])) for s in ordered),
        "paragraphs per section: " + ", ".join("%s=%d" % (s, paras_per_section[s]) for s in ordered),
        "",
        "| Phrase | Count | Docs | Top section | Banned |",
        "|---|---:|---:|---|---|",
    ]
    for docs, count, phrase, section, banned in rows:
        lines.append(
            "| %s | %d | %d | %s | %s |"
            % (phrase.replace("|", "\\|"), count, docs, section,
               "banned(L1)" if banned else "")
        )
    lines.append("")
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Rebuild sections and count phrases (dry-run by default)")
    ap.add_argument("--doc-prefix", default=None, help="doc_id prefix filter, e.g. 05")
    ap.add_argument("--section", default=None, help="count this section only")
    ap.add_argument("--min-docs", type=int, default=MIN_DOCS)
    ap.add_argument("--min-count", type=int, default=MIN_COUNT)
    ap.add_argument("--limit", type=int, default=LIMIT)
    ap.add_argument("--execute", action="store_true", help="write the table")
    ap.add_argument("--out", type=Path, default=None)
    args = ap.parse_args(argv)

    prefixes = (args.doc_prefix,) if args.doc_prefix else DOC_PREFIXES
    rows, dropped = load_paragraphs(BANK, prefixes)
    if not rows:
        print("no prose paragraphs found", file=sys.stderr)
        return 2
    paras_per_section = assign_sections(rows)
    if args.section:
        rows = [row for row in rows if row["heading"] is None and row["section"] == args.section]
        if not rows:
            print("no prose paragraphs found in section %s" % args.section, file=sys.stderr)
            return 2

    body_rows = [row for row in rows
                 if row["heading"] is None and row["section"] not in EXCLUDE_SECTIONS]
    excluded_rows = [row for row in rows
                     if row["heading"] is None and row["section"] in EXCLUDE_SECTIONS]
    if excluded_rows:
        dropped["excluded_section"] += len(excluded_rows)
        rows = [row for row in rows if row["section"] not in EXCLUDE_SECTIONS]

    occurrences, presence, sections, docs_per_section = collect(rows)
    bans = hw.load_bans(BANS)
    table = ranked(occurrences, presence, sections, args.min_docs, args.min_count,
                   args.limit, bans)
    doc_count = len({row["doc_id"] for row in rows})
    body = render(table, len(body_rows), doc_count, docs_per_section,
                  paras_per_section, args)

    print("paragraphs=%d docs=%d phrases=%d kept=%d"
          % (len(body_rows), doc_count, len(occurrences), len(table)))
    print("dropped: " + ", ".join("%s=%d" % item for item in dropped.most_common()))
    if not args.execute:
        print(body)
        return 0

    out = args.out or (OUT_DIR / "paras-sections.md")
    out.write_text(body, encoding="utf-8", newline="\n")
    print("written: %s" % out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
