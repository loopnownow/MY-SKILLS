# -*- coding: utf-8 -*-
"""
test_style_lint.py -- regression suite for 00_orchestrator/scripts/style_lint.py

DISCIPLINE (borrowed from SlopMonster's regression suite):
    every rule gets a nearby MUST-HIT case and a MUST-STAY-CLEAN case that would
    fail if the rule became too broad. Touch a regex -> run this file.

Run:
    python3 -m unittest _medical-research-meta.tests.test_style_lint
"""
import ast
import contextlib
import importlib.util
import io
import json
import re
import tempfile
import unittest
from pathlib import Path

# =============================================================================
# CONFIG -- paths and shared fixtures (edit here, nowhere else)
# =============================================================================
REPO_ROOT = Path(__file__).resolve().parents[2]
SCRIPT_PATH = REPO_ROOT / "00_orchestrator" / "scripts" / "style_lint.py"

# Modules the linter is allowed to import. Anything else (socket, urllib, http,
# requests, subprocess, ...) would break the "manuscript text never leaves the
# machine" rule and must fail the build. Widening this list needs a reviewer's eye.
ALLOWED_IMPORTS = {"argparse", "copy", "json", "re", "sys", "pathlib"}

# A neutral sentence (>10 words) that triggers no rule; pads fixtures past MIN_SCANNED_WORDS.
FILLER = "We studied a cohort of patients with cirrhosis and recorded outcomes over two years."

# The three words the owner ruled to be AI vocabulary (regression guard for that decision).
DECIDED_AI_WORDS = ("robust", "landscape", "leverage")


def _load_module():
    spec = importlib.util.spec_from_file_location("style_lint_under_test", SCRIPT_PATH)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


sl = _load_module()


def doc(section, body):
    """Build a one-section markdown document; FILLER is appended so the text is long enough."""
    return "## %s\n\n%s %s\n" % (section, body, FILLER)


def failed(result, group):
    return result["groups"][group]["failed"]


def terms(result, group):
    return [h["term"] for h in result["groups"][group]["hits"]]


# =============================================================================
# Vocabulary
# =============================================================================
class VocabularyTests(unittest.TestCase):
    def test_decided_words_are_flagged(self):
        # robust / landscape / leverage: must-hit in every inflection we list
        for sentence in ("This is a robust model.", "The model was robustly validated.",
                         "The immune landscape differed.", "Landscapes vary by cohort.",
                         "We leveraged prior data.", "This leverages prior data.",
                         "Leveraging prior data helps."):
            with self.subTest(sentence=sentence):
                self.assertTrue(failed(sl.lint(doc("Discussion", sentence)), "vocabulary"))

    def test_robustness_is_not_flagged(self):
        # must-stay-clean: "feature robustness" is standard radiomics terminology
        r = sl.lint(doc("Discussion", "Feature robustness was assessed with the ICC."))
        self.assertFalse(failed(r, "vocabulary"))

    def test_near_misses_stay_clean(self):
        for sentence in ("Delivery of care improved.", "The lever arm was measured.",
                         "The landscaper arrived.", "Realistic estimates were used."):
            with self.subTest(sentence=sentence):
                self.assertFalse(failed(sl.lint(doc("Discussion", sentence)), "vocabulary"))

    def test_classic_tells(self):
        for sentence in ("We delved into the data.", "It is worth noting that P was small.",
                         "It\u2019s important to note the limits.", "A rich tapestry emerged.",
                         "This underscores the need.", "That being said, we agree."):
            with self.subTest(sentence=sentence):
                self.assertTrue(failed(sl.lint(doc("Discussion", sentence)), "vocabulary"))

    def test_decided_words_are_in_config_and_config_is_sane(self):
        for word in DECIDED_AI_WORDS:
            self.assertTrue(any(re.search(r"\b(?:%s)\b" % p, word, re.I)
                                for p in sl.CONFIG["VOCAB_ALWAYS"]),
                            "%s must stay in VOCAB_ALWAYS" % word)
        for p in sl.CONFIG["VOCAB_ALWAYS"] + sl.CONFIG["VOCAB_LIMITED"]:
            re.compile(p)                                    # every fragment compiles
        self.assertFalse(set(sl.CONFIG["VOCAB_ALWAYS"]) & set(sl.CONFIG["VOCAB_LIMITED"]))
        self.assertLessEqual(sl.CONFIG["PASS_SCORE"], len(sl.GROUPS))

    def test_limited_words_fine_once_not_twice(self):
        self.assertFalse(failed(sl.lint(doc("Discussion", "This is crucial.")), "vocabulary"))
        self.assertTrue(failed(sl.lint(doc("Discussion", "This is crucial. That is crucial.")),
                               "vocabulary"))

    def test_limited_words_total_cap(self):
        three = doc("Discussion", "It is crucial. It is pivotal. It is compelling.")
        four = doc("Discussion", "It is crucial. It is pivotal. It is compelling. It is innovative.")
        self.assertFalse(failed(sl.lint(three), "vocabulary"))
        self.assertTrue(failed(sl.lint(four), "vocabulary"))

    def test_allow_phrases_exempt_a_term_of_art(self):
        text = doc("Discussion", "A high-leverage point was excluded.")
        self.assertTrue(failed(sl.lint(text), "vocabulary"))                       # default: flagged
        r = sl.lint(text, {"ALLOW_PHRASES": ["high-leverage point"]})
        self.assertFalse(failed(r, "vocabulary"))                                  # opt-in exemption


# =============================================================================
# Section scoping (Methods passive-voice / terminology convention)
# =============================================================================
class SectionScopeTests(unittest.TestCase):
    def test_methods_and_results_are_skipped(self):
        text = ("## Methods\n\nWe used a robust regression and leveraged prior data.\n\n"
                "## Results\n\nThe landscape of features was robust.\n\n"
                "## Discussion\n\n%s\n" % FILLER)
        r = sl.lint(text)
        self.assertFalse(failed(r, "vocabulary"))
        self.assertIn("methods", r["skipped_sections"])

    def test_same_words_in_discussion_are_flagged(self):
        self.assertTrue(failed(sl.lint(doc("Discussion", "We used a robust regression.")), "vocabulary"))

    def test_subheading_inherits_parent_mode(self):
        skip = ("## Methods\n\n### Statistical analysis\n\nWe used robust regression.\n\n"
                "## Discussion\n\n%s\n" % FILLER)
        self.assertFalse(failed(sl.lint(skip), "vocabulary"))            # stays skipped
        scan = "## Discussion\n\n### Limitations\n\nThis was robust. %s\n" % FILLER
        self.assertTrue(failed(sl.lint(scan), "vocabulary"))             # stays scanned

    def test_bare_and_numbered_headings(self):
        text = "2. Methods\n\nA robust regression was used.\n\nDiscussion\n\n%s\n" % FILLER
        self.assertFalse(failed(sl.lint(text), "vocabulary"))

    def test_no_headings_scans_everything_with_warning(self):
        r = sl.lint("This is a robust model. " + FILLER)
        self.assertTrue(failed(r, "vocabulary"))
        self.assertTrue(r["warnings"])

    def test_code_fences_tables_and_inline_code_are_ignored(self):
        text = ("## Discussion\n\n```\nrobust leverage landscape\n```\n\n"
                "| robust | leverage |\n\nUse `robust` here. %s\n" % FILLER)
        self.assertFalse(failed(sl.lint(text), "vocabulary"))


# =============================================================================
# Constructions
# =============================================================================
class ConstructionTests(unittest.TestCase):
    def test_not_just_x_but_y(self):
        self.assertTrue(failed(sl.lint(doc("Discussion", "It's not just a tool, it's a method.")),
                               "constructions"))
        self.assertTrue(failed(sl.lint(doc("Discussion", "This is not merely a score but a map.")),
                               "constructions"))

    def test_not_only_but_also_stays_clean(self):
        # ordinary academic parallelism
        r = sl.lint(doc("Discussion", "It reduced mortality not only in adults but also in children."))
        self.assertFalse(failed(r, "constructions"))

    def test_more_than_just(self):
        self.assertTrue(failed(sl.lint(doc("Discussion", "It is more than just a score.")),
                               "constructions"))

    def test_thats_where_x_comes_in(self):
        self.assertTrue(failed(sl.lint(doc("Discussion", "That's where radiomics comes in.")),
                               "constructions"))

    def test_stacked_hedge_vs_calibrated_hedge(self):
        self.assertTrue(failed(sl.lint(doc("Discussion", "This may potentially explain it.")),
                               "constructions"))
        self.assertTrue(failed(sl.lint(doc("Discussion", "This could possibly explain it.")),
                               "constructions"))
        # a single calibrated hedge is house style and must stay clean
        self.assertFalse(failed(sl.lint(doc("Discussion", "This may be associated with the outcome.")),
                                "constructions"))
        self.assertFalse(failed(sl.lint(doc("Discussion", "These data suggest a possible link.")),
                                "constructions"))

    def test_self_answering_question(self):
        self.assertTrue(failed(sl.lint(doc("Discussion", "The result? Faster reads.")), "constructions"))
        self.assertFalse(failed(sl.lint(doc("Discussion", "The result was significant.")), "constructions"))


# =============================================================================
# Dash cadence
# =============================================================================
class DashTests(unittest.TestCase):
    def test_two_em_dashes_in_one_sentence(self):
        self.assertTrue(failed(sl.lint(doc("Discussion", "The model \u2014 trained early \u2014 failed.")),
                               "dash_cadence"))

    def test_single_em_dash_is_fine(self):
        self.assertFalse(failed(sl.lint(doc("Discussion", "The model \u2014 trained early failed.")),
                                "dash_cadence"))

    def test_dashes_in_separate_sentences_are_fine(self):
        self.assertFalse(failed(sl.lint(doc("Discussion", "One \u2014 aside. Two \u2014 aside.")),
                                "dash_cadence"))

    def test_en_dash_ranges_are_fine(self):
        r = sl.lint(doc("Discussion", "Lesions of 5\u201310 mm and 20\u201330 mm were seen."))
        self.assertFalse(failed(r, "dash_cadence"))


# =============================================================================
# Rule-of-three rhythm
# =============================================================================
class TricolonTests(unittest.TestCase):
    FOUR = ("The model was faster, smarter, and better. The design was simple, clear, and useful. "
            "The tool is quick, cheap, and reliable. The method is stable, precise, and accurate.")

    def test_four_triples_fail_three_pass(self):
        self.assertTrue(failed(sl.lint(doc("Discussion", self.FOUR)), "tricolon"))
        three = " ".join(self.FOUR.split(". ")[:3]) + "."
        self.assertFalse(failed(sl.lint(doc("Discussion", three)), "tricolon"))

    def test_parenthetical_covariate_lists_are_not_counted(self):
        body = " ".join("Adjusted for covariates (age, sex, and bmi)." for _ in range(6))
        self.assertFalse(failed(sl.lint(doc("Discussion", body)), "tricolon"))

    def test_acronym_lists_stay_clean(self):
        body = " ".join("We adjusted for age, sex, and BMI." for _ in range(6))
        self.assertFalse(failed(sl.lint(doc("Discussion", body)), "tricolon"))


# =============================================================================
# Fail-closed guards, scoring, CLI
# =============================================================================
class GuardAndCliTests(unittest.TestCase):
    def run_main(self, argv):
        out, err = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            code = sl.main(argv)
        return code, out.getvalue(), err.getvalue()

    def test_empty_and_blank_input_fail_closed(self):
        for bad in ("", "   \n\t ", None):
            with self.subTest(bad=bad):
                with self.assertRaises(sl.InputError):
                    sl.lint(bad)
        self.assertEqual(self.run_main(["--text", ""])[0], 2)

    def test_only_skipped_sections_fail_closed(self):
        with self.assertRaises(sl.InputError):
            sl.lint("## Methods\n\n%s\n" % FILLER)

    def test_non_english_text_fails_closed(self):
        chinese = "\u8fd9\u662f\u4e00\u4e2a\u7528\u4e8e\u6d4b\u8bd5\u7684\u4e2d\u6587\u6bb5\u843d\u3002" * 20
        with self.assertRaises(sl.InputError) as ctx:
            sl.lint("## Discussion\n\n%s %s\n" % (FILLER, chinese))
        self.assertIn("non-English", str(ctx.exception))

    def test_bad_inputs_exit_2(self):
        self.assertEqual(self.run_main(["/no/such/file.md"])[0], 2)
        self.assertEqual(self.run_main([])[0], 2)
        self.assertEqual(self.run_main(["--text", doc("Discussion", "ok"), "--config", "/no/such.json"])[0], 2)

    def test_unknown_config_key_is_an_error(self):
        with self.assertRaises(sl.InputError):
            sl.lint(doc("Discussion", "ok"), {"NOT_A_KEY": 1})

    def test_config_file_override(self):
        with tempfile.TemporaryDirectory() as tmp:
            cfg = Path(tmp) / "o.json"
            cfg.write_text(json.dumps({"ALLOW_PHRASES": ["robust regression"]}), encoding="utf-8")
            code, _, _ = self.run_main(["--text", doc("Discussion", "We used robust regression."),
                                        "--config", str(cfg)])
            self.assertEqual(code, 0)

    def test_exit_codes_and_score(self):
        clean, dirty = doc("Discussion", "The cohort was small."), doc("Discussion", "A robust model.")
        self.assertEqual(self.run_main(["--text", clean])[0], 0)
        self.assertEqual(self.run_main(["--text", dirty])[0], 1)
        both = doc("Discussion", "A robust model. It is more than just a score.")
        r = sl.lint(both)
        self.assertEqual((r["score"], r["max_score"], r["passed"]), (2, 4, False))

    def test_pass_score_is_configurable(self):
        r = sl.lint(doc("Discussion", "A robust model."), {"PASS_SCORE": 3})
        self.assertTrue(r["passed"])

    def test_json_output_is_parseable(self):
        code, out, _ = self.run_main(["--text", doc("Discussion", "A robust model."), "--json"])
        self.assertEqual(code, 1)
        parsed = json.loads(out)
        self.assertEqual(parsed["groups"]["vocabulary"]["hits"][0]["term"], "robust")

    def test_hits_carry_location(self):
        r = sl.lint("## Discussion\n\nLine one is fine here and long enough.\n\nA robust model.\n")
        hit = r["groups"]["vocabulary"]["hits"][0]
        self.assertEqual((hit["section"], hit["line"]), ("discussion", 5))


# =============================================================================
# Policy tests: the rules that must never regress
# =============================================================================
class PolicyTests(unittest.TestCase):
    def test_script_is_offline_stdlib_only(self):
        tree = ast.parse(SCRIPT_PATH.read_text(encoding="utf-8"))
        imported = set()
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                imported.update(a.name.split(".")[0] for a in node.names)
            elif isinstance(node, ast.ImportFrom) and node.module:
                imported.add(node.module.split(".")[0])
        self.assertLessEqual(imported, ALLOWED_IMPORTS,
                             "unexpected imports: %s" % sorted(imported - ALLOWED_IMPORTS))

    def test_script_never_writes_files(self):
        src = SCRIPT_PATH.read_text(encoding="utf-8")
        for needle in ("write_text", "write_bytes", "open(", "os.remove", "unlink"):
            self.assertNotIn(needle, src, "the linter reports; it must never modify files")


if __name__ == "__main__":
    unittest.main()
