"""draw-flowchart scripts: expanded STROBE spec, fail-closed n-audit, file written.

Synthetic specs only — no lab paths, no patient data (public repo).
"""
from __future__ import annotations

import copy
import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path

from tests.support import ROOT

SCRIPTS = ROOT / "02_data-processing" / "base" / "draw-flowchart" / "scripts"
EXPANDED_NAME = "draw_strobe_flow_expanded"
BASE_NAME = "draw_strobe_flow"

# 200 screened = 150 + 50 pre-split; training 150 - 40 downsampled = 110;
# cohorts 110 + 50 = 160 analyzed; positives 50 + 20 = 70; negatives 60 + 30 = 90.
SPEC = {
    "layout": "expanded-split-downsample",
    "screened": "Screened patients (n = 200)",
    "inclusion": ["Criterion one", "Criterion two"],
    "presplit": {
        "training": {"n": 150, "pp": 50, "non_pp": 100},
        "test": {"n": 50, "pp": 20, "non_pp": 30},
    },
    "downsample": {
        "n": 40,
        "reason": "Non-case downsampling for class imbalance",
        "class": "non_pp",
    },
    "analyzed": "160 patients analyzed (70 positive vs 90 negative)",
    "splits": [
        {"label": "Training Cohort", "n": 110, "pp": 50, "non_pp": 60},
        {"label": "Test Cohort", "n": 50, "pp": 20, "non_pp": 30},
    ],
}


def _load(name: str):
    if str(SCRIPTS) not in sys.path:
        sys.path.insert(0, str(SCRIPTS))
    path = SCRIPTS / f"{name}.py"
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


class ExpandedStrobeSpec(unittest.TestCase):
    def setUp(self) -> None:
        self.mod = _load(EXPANDED_NAME)
        self.tmp = tempfile.TemporaryDirectory()
        self.out = Path(self.tmp.name) / "flow.png"

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def _spec(self, **overrides):
        spec = copy.deepcopy(SPEC)
        spec.update(overrides)
        return spec

    def test_audit_passes_and_writes_file(self) -> None:
        self.mod.draw_expanded_strobe(SPEC, self.out)
        self.assertTrue(self.out.is_file())
        self.assertGreater(self.out.stat().st_size, 0)

    def test_screened_must_cover_arms(self) -> None:
        spec = self._spec(screened="Screened patients (n = 999)")
        with self.assertRaises(self.mod.AuditError):
            self.mod.draw_expanded_strobe(spec, self.out)

    def test_downsample_must_reconcile_arm_and_cohort(self) -> None:
        spec = copy.deepcopy(SPEC)
        spec["downsample"]["n"] = 30
        with self.assertRaises(self.mod.AuditError):
            self.mod.draw_expanded_strobe(spec, self.out)

    def test_downsample_class_must_match_cohort_counts(self) -> None:
        spec = copy.deepcopy(SPEC)
        spec["downsample"]["class"] = "pp"
        with self.assertRaises(self.mod.AuditError):
            self.mod.draw_expanded_strobe(spec, self.out)

    def test_analyzed_must_equal_cohort_sum(self) -> None:
        spec = self._spec(analyzed="171 patients analyzed")
        with self.assertRaises(self.mod.AuditError):
            self.mod.draw_expanded_strobe(spec, self.out)

    def test_arm_count_must_balance(self) -> None:
        spec = copy.deepcopy(SPEC)
        spec["presplit"]["training"]["non_pp"] = 90
        with self.assertRaises(self.mod.AuditError):
            self.mod.draw_expanded_strobe(spec, self.out)

    def test_no_audit_flag_skips_arithmetic(self) -> None:
        spec = self._spec(analyzed="171 patients analyzed")
        self.mod.draw_expanded_strobe(spec, self.out, audit_n=False)
        self.assertTrue(self.out.is_file())

    def test_refuses_type_a_layout(self) -> None:
        spec = self._spec(layout="strobe")
        with self.assertRaises(ValueError):
            self.mod.draw_expanded_strobe(spec, self.out, audit_n=False)

    def test_refuses_pipeline_row(self) -> None:
        spec = self._spec(pipeline=["imaging", "model"])
        with self.assertRaises(ValueError):
            self.mod.draw_expanded_strobe(spec, self.out, audit_n=False)

    def test_cohort_count_must_match_arms(self) -> None:
        spec = copy.deepcopy(SPEC)
        spec["splits"].append({"label": "External Cohort", "n": 10})
        with self.assertRaises(ValueError):
            self.mod.draw_expanded_strobe(spec, self.out, audit_n=False)

    def test_cli_writes_and_fails_loud(self) -> None:
        good = Path(self.tmp.name) / "spec.json"
        good.write_text(json.dumps(SPEC), encoding="utf-8")
        self.mod.main(["--json", str(good), "--out", str(self.out)])
        self.assertTrue(self.out.is_file())

        bad = Path(self.tmp.name) / "bad.json"
        bad.write_text(json.dumps(self._spec(screened="n = 999")), encoding="utf-8")
        with self.assertRaises(SystemExit) as caught:
            self.mod.main(["--json", str(bad), "--out", str(self.out)])
        self.assertEqual(caught.exception.code, 1)


if __name__ == "__main__":
    unittest.main()
