"""Contract for the paragraph-layer section rebuild and phrasing counter.

Config
------
SCRIPT : `05_manuscript/advanced/vocab/scripts/harvest_sections.py`
BANK   : synthetic JSONL fixtures written into a temporary directory

Run
---
    python -B -m unittest tests.test_vocab_harvest_sections -v
"""
from __future__ import annotations

import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPT = REPO_ROOT / "05_manuscript" / "advanced" / "vocab" / "scripts" / "harvest_sections.py"


def _load_module():
    spec = importlib.util.spec_from_file_location("harvest_sections_under_test", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


hs = _load_module()


def _write_bank(rows) -> Path:
    handle = tempfile.NamedTemporaryFile(
        "w", suffix=".jsonl", delete=False, encoding="utf-8", newline="\n")
    with handle as stream:
        for row in rows:
            stream.write(json.dumps(row, ensure_ascii=False) + "\n")
    return Path(handle.name)


def _row(doc_id, pidx, text, in_table=False, in_textbox=False):
    return {
        "doc_id": doc_id,
        "pidx": pidx,
        "in_table": in_table,
        "in_textbox": in_textbox,
        "text_acc": text,
        "text_orig": text,
    }


EN = "Patients were randomly divided into a training cohort and a validation cohort."
ZH = "本研究比较了三组患者的影像组学特征与临床指标之间的差异。"


class HeadingContract(unittest.TestCase):
    def test_imrad_headings_with_numbering(self):
        self.assertEqual(hs.heading_of("2. Methods"), "Methods")
        self.assertEqual(hs.heading_of("RESULTS"), "Results")
        self.assertEqual(hs.heading_of("Results and Discussion"), "Results")

    def test_chinese_headings(self):
        self.assertEqual(hs.heading_of("材料与方法"), "Methods")
        self.assertEqual(hs.heading_of("结果"), "Results")
        self.assertEqual(hs.heading_of("参考文献"), "References")
        self.assertEqual(hs.heading_of("中文摘要"), "Abstract")

    def test_sentence_is_not_a_heading(self):
        self.assertIsNone(hs.heading_of("图 1-5 相关性分析结果"))
        self.assertIsNone(hs.heading_of(EN))


class SectionContract(unittest.TestCase):
    def test_paragraphs_inherit_and_reset_per_document(self):
        rows = [
            {"doc_id": "05-001", "heading": "Methods"},
            {"doc_id": "05-001", "heading": None},
            {"doc_id": "05-001", "heading": "Results"},
            {"doc_id": "05-001", "heading": None},
            {"doc_id": "05-002", "heading": None},
        ]
        counts = hs.assign_sections(rows)
        self.assertEqual(rows[1]["section"], "Methods")
        self.assertEqual(rows[3]["section"], "Results")
        self.assertEqual(rows[4]["section"], "front")
        self.assertEqual(counts["Methods"], 1)
        self.assertEqual(counts["front"], 1)


class ParagraphFilterContract(unittest.TestCase):
    def test_table_textbox_reference_and_short_rows_are_dropped(self):
        bank = _write_bank([
            _row("05-001", 1, EN),
            _row("05-001", 2, EN, in_table=True),
            _row("05-001", 3, EN, in_textbox=True),
            _row("05-001", 4, "[12] Smith J, et al. Journal of Testing, 2019;3(2):1-9."),
            _row("05-001", 5, "Department of Radiology, Fudan University, Shanghai, China; "
                              "and Department of Radiology, Zhongshan Hospital."),
            _row("05-001", 6, "Short stub."),
            _row("03-001", 7, EN),
        ])
        rows, dropped = hs.load_paragraphs(bank, ("05",))
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]["doc_id"], "05-001")
        self.assertEqual(dropped["table_or_textbox"], 2)
        self.assertEqual(dropped["reference_or_affiliation"], 1)
        self.assertEqual(dropped["too_short"], 2)
        self.assertEqual(dropped["doc_prefix"], 1)

    def test_heading_row_survives_the_length_floor(self):
        bank = _write_bank([_row("05-001", 1, "材料与方法"), _row("05-001", 2, ZH)])
        rows, dropped = hs.load_paragraphs(bank, ("05",))
        self.assertEqual(rows[0]["heading"], "Methods")
        self.assertEqual(dropped["too_short"], 0)


class WindowContract(unittest.TestCase):
    def test_chinese_windows_start_at_three_characters(self):
        windows = list(hs.zh_phrases(ZH))
        self.assertTrue(windows)
        self.assertTrue(all(len(item) >= 3 for item in windows))
        self.assertTrue(all(hs.CJK.search(item) for item in windows))

    def test_short_chinese_sentence_yields_nothing(self):
        self.assertEqual(list(hs.zh_phrases("结果")), [])


class CollapseContract(unittest.TestCase):
    def test_longer_span_absorbs_fragment_within_tolerance(self):
        kept = hs.collapse({"研究方案": (100, 50), "研究方案的": (96, 49)})
        self.assertEqual(list(kept), ["研究方案的"])

    def test_unrelated_spans_survive(self):
        kept = hs.collapse({"研究方案": (100, 50), "临床特征": (40, 20)})
        self.assertIn("研究方案", kept)
        self.assertIn("临床特征", kept)

    def test_english_requires_identical_counts(self):
        kept = hs.collapse({"the training cohort": (20, 10), "training cohort": (18, 9)})
        self.assertIn("training cohort", kept)


class EndToEndContract(unittest.TestCase):
    def test_counts_and_top_section(self):
        bank = _write_bank([
            _row("05-001", 1, "Methods"),
            _row("05-001", 2, EN),
            _row("05-001", 3, EN),
            _row("05-002", 1, "Methods"),
            _row("05-002", 2, EN),
        ])
        rows, _dropped = hs.load_paragraphs(bank, ("05",))
        hs.assign_sections(rows)
        occurrences, presence, sections, docs_per_section = hs.collect(rows)
        table = hs.ranked(occurrences, presence, sections, min_docs=2, min_count=2,
                          limit=10, bans=[])
        self.assertTrue(table)
        docs, count, _phrase, section, banned = table[0]
        self.assertEqual(docs, 2)
        self.assertEqual(count, 3)
        self.assertEqual(section, "Methods")
        self.assertFalse(banned)
        self.assertEqual(set(docs_per_section), {"Methods"})

    def test_ban_flag_is_annotated_not_removed(self):
        rows = [{"doc_id": "05-001", "pidx": 1, "heading": None, "zh": False,
                 "text": "This is a novel approach to the problem of staging."}]
        hs.assign_sections(rows)
        occurrences, presence, sections, _docs = hs.collect(rows)
        table = hs.ranked(occurrences, presence, sections, min_docs=1, min_count=1,
                          limit=50, bans=["novel"])
        flagged = [item for item in table if item[4]]
        self.assertTrue(flagged)
        self.assertTrue(all("novel" in item[2] for item in flagged))


if __name__ == "__main__":
    unittest.main()
