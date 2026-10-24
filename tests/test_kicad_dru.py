"""Tests for hooks/kicad-dru.py on the fixture in tests/fixtures/dru.

Run from the repository root: python3 -m unittest discover tests
"""
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
TOOL = os.path.join(HERE, "..", "hooks", "kicad-dru.py")
FIXTURE = os.path.join(HERE, "fixtures", "dru")
MANIFEST = "hardware/demo.dru.toml"
TARGET = "hardware/demo.kicad_dru"
PRODUCT = "hardware/rules/product.kicad_dru"


class KicadDru(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.repo = os.path.join(self.tmp, "repo")
        shutil.copytree(FIXTURE, self.repo, ignore=shutil.ignore_patterns("expected.kicad_dru"))
        subprocess.run(["git", "init", "-q", self.repo], check=True)

    def tearDown(self):
        shutil.rmtree(self.tmp)

    def run_tool(self, *args):
        return subprocess.run([sys.executable, TOOL, *args], cwd=self.repo, capture_output=True, text=True)

    def path(self, rel):
        return os.path.join(self.repo, rel)

    def test_compose_matches_expected(self):
        r = self.run_tool("compose", MANIFEST)
        self.assertEqual(r.returncode, 0, r.stderr)
        want = open(os.path.join(FIXTURE, "expected.kicad_dru")).read()
        self.assertEqual(open(self.path(TARGET)).read(), want)
        self.assertEqual(want.count("(version 1)"), 1)

    def test_check_missing_then_ok_then_stale(self):
        r = self.run_tool("check")
        self.assertEqual(r.returncode, 1)
        self.assertIn("missing", r.stderr)
        self.run_tool("compose", MANIFEST)
        r = self.run_tool("check")
        self.assertEqual(r.returncode, 0, r.stderr)
        with open(self.path(PRODUCT), "a") as f:
            f.write('(rule "Product: extra"\n\t(constraint track_width (min 0.2mm))\n)\n')
        r = self.run_tool("check", "--json")
        self.assertEqual(r.returncode, 1)
        report = json.loads(r.stdout)
        self.assertEqual(report["items"][0]["status"], "stale")

    def test_hand_edit_is_stale(self):
        self.run_tool("compose", MANIFEST)
        with open(self.path(TARGET), "a") as f:
            f.write("# hand edit\n")
        self.assertEqual(self.run_tool("check", MANIFEST).returncode, 1)

    def test_duplicate_rule_name_fails(self):
        with open(self.path(PRODUCT), "a") as f:
            f.write('(rule "Fab: via hole"\n\t(constraint hole_size (min 0.3mm))\n)\n')
        r = self.run_tool("compose", MANIFEST)
        self.assertEqual(r.returncode, 1)
        self.assertIn('duplicate rule name "Fab: via hole"', r.stderr)
        self.assertFalse(os.path.exists(self.path(TARGET)))

    def test_missing_source_fails(self):
        os.remove(self.path("hardware/lib/opendap/design-rules/fab-demo/fab-demo.kicad_dru"))
        r = self.run_tool("compose", MANIFEST)
        self.assertEqual(r.returncode, 1)
        self.assertIn("submodule", r.stderr)

    def test_bad_manifest_fails(self):
        with open(self.path(MANIFEST), "w") as f:
            f.write('version = 1\nsources = ["../outside.kicad_dru"]\n')
        r = self.run_tool("compose", MANIFEST)
        self.assertEqual(r.returncode, 1)
        self.assertIn("inside the repository", r.stderr)

    def test_unbalanced_source_fails(self):
        with open(self.path(PRODUCT), "a") as f:
            f.write('(rule "Product: broken"\n\t(constraint clearance (min 0.2mm))\n')
        r = self.run_tool("compose", MANIFEST)
        self.assertEqual(r.returncode, 1)
        self.assertIn("unbalanced", r.stderr)

    def test_usage_error(self):
        self.assertEqual(self.run_tool("frobnicate").returncode, 2)


if __name__ == "__main__":
    unittest.main()
