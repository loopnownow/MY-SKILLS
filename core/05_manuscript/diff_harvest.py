#!/usr/bin/env python3
"""
diff_harvest.py — manuscript-core / harvest tool (Toolize, CHG-20260829-001)

Owner: 05_manuscript / manuscript-core (per route-map.md: SCI original-article
writing, de-AI -> 05_manuscript; figures -> 04_analysis). This does NOT live under
skill-harvest — skill-harvest owns evolution governance, not corpus content.

Purpose
-------
Compare an AI draft against your edited final for one manuscript, and surface:
  1. Which already-documented corpus-phrase-bank.md patterns you actively
     wrote into the final (stronger signal than passive corpus frequency).
  2. Which forbidden-phrases.md words you actively deleted.
  3. Candidate NEW patterns not yet in corpus-phrase-bank.md — printed for
     you to eyeball, never auto-inserted.

Every run appends one row to a local data/diff-evidence-log.csv (create beside this script if needed) so evidence
accumulates across editing sessions before the next full corpus re-harvest.

Usage
-----
    python3 diff_harvest.py \\
        --phrase-bank corpus-phrase-bank.md \\
        --forbidden de-ai/forbidden-phrases.md \\
        --draft ai_draft.txt --final your_edited_final.txt \\
        --title "Manuscript title"

Read-mostly: appends one CSV row plus stdout. Never rewrites
corpus-phrase-bank.md or forbidden-phrases.md.

Known limitation: known-pattern matching is best-effort regex over
prose-quoted spans and will under-match inflected/bracketed variants.
"""

import argparse
import csv
import difflib
import re
from datetime import date
from pathlib import Path

FORBIDDEN_DEFAULT = {"novel", "notably", "interestingly", "importantly"}


def load_forbidden_words(path):
    """Best-effort scrape of single-word forbidden entries from forbidden-phrases.md."""
    words = set()
    try:
        text = Path(path).read_text(encoding="utf-8", errors="ignore")
        for m in re.finditer(r"\|\s*([a-zA-Z]+)\s*\|", text):
            w = m.group(1).lower()
            if 3 <= len(w) <= 20:
                words.add(w)
    except FileNotFoundError:
        pass
    return words or FORBIDDEN_DEFAULT


def extract_known_patterns(phrase_bank_path):
    """Pull verbatim/quoted patterns out of corpus-phrase-bank.md."""
    patterns = []
    try:
        text = Path(phrase_bank_path).read_text(encoding="utf-8", errors="ignore")
    except FileNotFoundError:
        return patterns
    for m in re.finditer(r'\*"([^"]{8,120})"\*', text):
        patterns.append(m.group(1))
    for m in re.finditer(r"\|\s*([A-Za-z][A-Za-z0-9 ,/…\-]{6,60}?)\s*\|\s*\d", text):
        patterns.append(m.group(1).strip())
    cleaned = []
    for p in patterns:
        skeleton = re.sub(r"\[[^\]]+\]", "", p).strip()
        skeleton = re.sub(r"\s+", " ", skeleton)
        if len(skeleton) >= 6:
            cleaned.append(skeleton)
    return list(dict.fromkeys(cleaned))


def split_sentences(text):
    text = re.sub(r"\s+", " ", text)
    protected = re.sub(
        r"\b(e\.g|i\.e|et al|Fig|Table|vs|approx|Dr|Mr|Ms|no)\.",
        r"\1<DOT>",
        text,
        flags=re.IGNORECASE,
    )
    parts = re.split(r"(?<=[.!?])\s+(?=[A-Z])", protected)
    return [p.replace("<DOT>", ".").strip() for p in parts if len(p.strip()) > 5]


def word_diff(draft_sent, final_sent):
    d = re.findall(r"[A-Za-z][A-Za-z\-']*", draft_sent)
    f = re.findall(r"[A-Za-z][A-Za-z\-']*", final_sent)
    sm = difflib.SequenceMatcher(a=[w.lower() for w in d], b=[w.lower() for w in f])
    removed, added = [], []
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag in ("delete", "replace"):
            removed.extend(d[i1:i2])
        if tag in ("insert", "replace"):
            added.extend(f[j1:j2])
    return removed, added


def ngrams(words, lo=3, hi=5):
    out = []
    for n in range(lo, hi + 1):
        for i in range(len(words) - n + 1):
            out.append(" ".join(words[i : i + n]))
    return out


def main():
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    ap.add_argument("--phrase-bank", required=True)
    ap.add_argument("--forbidden", required=True)
    ap.add_argument("--draft", required=True)
    ap.add_argument("--final", required=True)
    ap.add_argument("--title", required=True)
    ap.add_argument(
        "--log",
        default=None,
        help="CSV log path (default: ../data/diff-evidence-log.csv next to this script)",
    )
    args = ap.parse_args()

    forbidden_words = load_forbidden_words(args.forbidden)
    known_patterns = extract_known_patterns(args.phrase_bank)
    known_lookup = {
        re.sub(r"[^a-z ]", "", p.lower()).strip(): p for p in known_patterns
    }

    draft_sents = split_sentences(
        Path(args.draft).read_text(encoding="utf-8", errors="ignore")
    )
    final_sents = split_sentences(
        Path(args.final).read_text(encoding="utf-8", errors="ignore")
    )
    sm = difflib.SequenceMatcher(a=draft_sents, b=final_sents)

    reinforced_known = []
    forbidden_removed = []
    new_candidates = []

    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == "equal":
            continue
        for d_sent in draft_sents[i1:i2] or [""]:
            for f_sent in final_sents[j1:j2] or [""]:
                removed, added = word_diff(d_sent, f_sent)
                removed_l, added_l = {w.lower() for w in removed}, {w.lower() for w in added}

                hit = forbidden_words & removed_l - added_l
                if hit:
                    forbidden_removed.append((sorted(hit), d_sent[:80], f_sent[:80]))

                for gram in ngrams(added):
                    key = re.sub(r"[^a-z ]", "", gram.lower()).strip()
                    if key in known_lookup:
                        reinforced_known.append((known_lookup[key], f_sent[:80]))
                    elif 3 <= len(gram.split()) <= 5:
                        new_candidates.append((gram, f_sent[:80]))

    seen = {}
    for gram, ex in new_candidates:
        seen.setdefault(gram, ex)
    new_candidates = list(seen.items())

    print(f"=== diff_harvest: {args.title} ===")
    print(
        f"\n主动写出的已知语料库模式（{len(reinforced_known)}处，强证据 — 你亲自选用了它们）:"
    )
    seen_p = set()
    for pattern, ex in reinforced_known:
        if pattern in seen_p:
            continue
        seen_p.add(pattern)
        print(f'  + {pattern}  例: "{ex}..."')

    print(f"\n主动删除的禁用词（{len(forbidden_removed)}处 — 政策被实际执行的证据）:")
    for words, d, f in forbidden_removed[:15]:
        print(f'  - 删除 {words}: "{d}..." -> "{f}..."')

    print(
        f"\n未收录的新候选（{len(new_candidates)}条，仅打印，不会自动写入 corpus-phrase-bank.md，"
        f"需要人工判断是否值得在下次全量re-harvest时纳入）:"
    )
    for gram, ex in new_candidates[:20]:
        print(f'  ? {gram}  例: "{ex}..."')
    if len(new_candidates) > 20:
        print(f"  ... 还有 {len(new_candidates) - 20} 条")

    log_path = (
        Path(args.log)
        if args.log
        else Path(__file__).parent.parent / "data" / "diff-evidence-log.csv"
    )
    log_path.parent.mkdir(parents=True, exist_ok=True)
    is_new = not log_path.exists()
    with open(log_path, "a", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if is_new:
            w.writerow(
                [
                    "date",
                    "manuscript_title",
                    "n_reinforced_known",
                    "n_forbidden_removed",
                    "n_new_candidates",
                    "new_candidates_sample",
                ]
            )
        w.writerow(
            [
                str(date.today()),
                args.title,
                len(set(p for p, _ in reinforced_known)),
                len(forbidden_removed),
                len(new_candidates),
                "; ".join(g for g, _ in new_candidates[:5]),
            ]
        )
    print(f"\n已追加一行证据到 {log_path}（累积多篇后供下次 corpus-phrase-bank.md 全量刷新参考）")


if __name__ == "__main__":
    main()
