#!/usr/bin/env python3
"""Check that every English positive example (正例) in Lab-STE-SPEC.md
uses only words from the approved dictionary, the default term lock,
or the project locks assumed by the examples.

Lock forms are matched as whole phrases. Words inside a multi-word lock
are not admitted on their own.

Run from the Lab-STE folder:  python tools/check_spec_examples.py
Exit code 1 if any example fails.
"""
import csv
import re
import sys
from pathlib import Path

# ---------------- CONFIG ----------------
ROOT = Path(__file__).resolve().parent.parent          # Lab-STE folder
SPEC = ROOT / "Lab-STE-SPEC.md"
APPROVED = ROOT / "approved-en.tsv"
DEFAULT_LOCK = ROOT / "term-lock-default.tsv"
RULE_PREFIXES = ("EN-", "AI-L01")
# Spec §4 intro: examples assume these project locks (phrases, not split words).
EXAMPLE_PROJECT_LOCK = [
    "logistic regression",
    "nomogram",
    "AUC",
    "calibrate",
    "covariate",
    "radiomics",
]
IRREGULAR = {"drew": "draw", "drawn": "draw", "fitted": "fit", "had": "have",
             "was": "be", "were": "be", "did": "do", "has": "have",
             "higher": "high", "largest": "large", "larger": "large"}
SUFFIXES = [("ies", "y"), ("ied", "y"), ("ed", ""), ("ed", "e"), ("es", ""),
            ("s", ""), ("ing", ""), ("ing", "e"), ("er", ""), ("est", ""),
            ("d", ""), ("ly", ""), ("n", "")]
# ---------------- END CONFIG ----------------


def _tokens(form):
    return tuple(w.lower() for w in re.findall(r"[A-Za-z]+", form))


def load_lexicon():
    lemmas = set()
    phrases = []
    with open(APPROVED, newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f, delimiter="\t"):
            lemmas.add(r["lemma"].lower())

    def add_form(form):
        tok = _tokens(form)
        if not tok:
            return
        if len(tok) == 1:
            lemmas.add(tok[0])
        else:
            phrases.append(tok)

    with open(DEFAULT_LOCK, encoding="utf-8") as f:
        rows = csv.DictReader((l for l in f if not l.startswith("#")), delimiter="\t")
        for r in rows:
            if r["lang"] != "en":
                continue
            add_form(r["canonical"])
            for a in r["aliases"].split("|"):
                if a.strip():
                    add_form(a)
    for form in EXAMPLE_PROJECT_LOCK:
        add_form(form)
    phrases.sort(key=len, reverse=True)
    return lemmas, phrases


def is_known(word, lem):
    w = word.lower()
    if w in lem or IRREGULAR.get(w) in lem:
        return True
    for suf, rep in SUFFIXES:
        if w.endswith(suf):
            base = w[: -len(suf)] + rep
            if base in lem or (len(base) > 2 and base[-1] == base[-2] and base[:-1] in lem):
                return True
    return False


def unknown_words(ex, lem, phrases):
    words = re.findall(r"[A-Za-z]+", ex)
    low = [w.lower() for w in words]
    covered = [False] * len(words)
    for ph in phrases:
        n = len(ph)
        for i in range(len(low) - n + 1):
            if tuple(low[i:i + n]) == ph:
                for j in range(i, i + n):
                    covered[j] = True
    out = []
    for i, w in enumerate(words):
        if covered[i]:
            continue
        if not is_known(w, lem):
            out.append(w)
    return out


def positive_examples(text):
    rule = None
    for line in text.splitlines():
        m = re.match(r"###\s+([A-Z]+-[A-Z]*\d+)", line)
        if m:
            rule = m.group(1)
        if rule and rule.startswith(RULE_PREFIXES) and "**正例" in line:
            for ex in re.findall(r"`([^`]+)`", line):
                if re.fullmatch(r"[A-Za-z0-9 .,'°/\-]+", ex) and " " in ex:
                    yield rule, ex


def main():
    lem, phrases = load_lexicon()
    text = SPEC.read_text(encoding="utf-8")
    bad = 0
    n = 0
    for rule, ex in positive_examples(text):
        n += 1
        unknown = unknown_words(ex, lem, phrases)
        status = "OK  " if not unknown else "FAIL"
        bad += bool(unknown)
        print(f"{status} {rule:8s} {ex}" + (f"   unknown: {unknown}" if unknown else ""))
    print(f"\n{n} examples checked, {bad} failed")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
