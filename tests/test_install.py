"""Behavioral checks for the no-overwrite installer using temporary directories."""

import hashlib
import importlib.util
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

KIT = Path(__file__).resolve().parents[1]
SCRIPT = KIT / "scripts/install.py"
NAMES = json.loads((KIT / "kit.json").read_text())["skills"]


def digest_tree(root):
    return {str(p.relative_to(root)): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in root.rglob("*") if p.is_file()}


class InstallTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="clickup-kit-test-")
        self.root = Path(self.temp.name)
        self.destination = self.root / "skills with spaces"

    def tearDown(self):
        self.temp.cleanup()

    def run_installer(self, *flags, script=SCRIPT, runtime="codex"):
        return subprocess.run([sys.executable, str(script), "--runtime", runtime,
                               "--destination", str(self.destination), *flags],
                              capture_output=True, text=True, timeout=15)

    def test_preview_creates_nothing(self):
        result = self.run_installer()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout)["action"], "preview")
        self.assertFalse(self.destination.exists())

    def test_copy_matches_every_source_byte(self):
        result = self.run_installer("--apply")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(digest_tree(self.destination), digest_tree(KIT / "skills"))

    def test_repeat_refuses_without_changing_installed_files(self):
        self.assertEqual(self.run_installer("--apply").returncode, 0)
        before = digest_tree(self.destination)
        result = self.run_installer("--apply")
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(digest_tree(self.destination), before)

    def test_one_collision_prevents_all_copies(self):
        existing = self.destination / NAMES[-1]
        existing.mkdir(parents=True)
        (existing / "sentinel.md").write_text("existing skill remains")
        before = digest_tree(self.destination)
        self.assertNotEqual(self.run_installer("--apply").returncode, 0)
        self.assertEqual(digest_tree(self.destination), before)
        self.assertEqual(sorted(p.name for p in self.destination.iterdir()), [NAMES[-1]])

    def test_dangling_skill_symlink_is_a_collision(self):
        self.destination.mkdir()
        link = self.destination / NAMES[-1]
        link.symlink_to(self.root / "absent")
        self.assertNotEqual(self.run_installer("--apply").returncode, 0)
        self.assertTrue(link.is_symlink())
        self.assertEqual(len(list(self.destination.iterdir())), 1)

    def test_destination_symlink_is_refused(self):
        real = self.root / "real"
        real.mkdir()
        self.destination.symlink_to(real, target_is_directory=True)
        self.assertNotEqual(self.run_installer("--apply").returncode, 0)
        self.assertEqual(list(real.iterdir()), [])

    def test_unrelated_skill_is_preserved(self):
        unrelated = self.destination / "unrelated-skill"
        unrelated.mkdir(parents=True)
        sentinel = unrelated / "SKILL.md"
        sentinel.write_text("unrelated content")
        self.assertEqual(self.run_installer("--apply").returncode, 0)
        self.assertEqual(sentinel.read_text(), "unrelated content")
        self.assertEqual(len(list(self.destination.iterdir())), len(NAMES) + 1)

    def test_linked_source_is_refused_before_destination_creation(self):
        copied = self.root / "copied-kit"
        shutil.copytree(KIT, copied, ignore=shutil.ignore_patterns(".git", "__pycache__"))
        (copied / "skills" / NAMES[0] / "linked.md").symlink_to(self.root / "absent")
        self.assertNotEqual(self.run_installer("--apply", script=copied / "scripts/install.py").returncode, 0)
        self.assertFalse(self.destination.exists())

    def test_unsupported_runtime_creates_nothing(self):
        result = subprocess.run([sys.executable, str(SCRIPT), "--runtime", "claude",
                                 "--destination", str(self.destination), "--apply"],
                                capture_output=True, text=True, timeout=15)
        self.assertNotEqual(result.returncode, 0)
        self.assertFalse(self.destination.exists())

    def test_claude_project_layout_and_explicit_invocation(self):
        self.destination = self.root / "project" / ".claude" / "skills"
        self.assert_claude_install()

    def test_claude_personal_layout_and_notices(self):
        self.destination = self.root / "personal-home" / ".claude" / "skills"
        self.assert_claude_install()

    def assert_claude_install(self):
        before = digest_tree(KIT / "skills")
        result = self.run_installer("--apply", runtime="claude-code")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(digest_tree(KIT / "skills"), before)
        for name in NAMES:
            source = KIT / "skills" / name
            target = self.destination / name
            source_text = (source / "SKILL.md").read_text()
            installed_text = (target / "SKILL.md").read_text()
            if name in ["to-prd", "to-issues"]:
                self.assertEqual(installed_text.split("---", 2)[1].count("disable-model-invocation: true"), 1)
            self.assertEqual(installed_text, source_text)
            for p in source.rglob("*"):
                if p.is_file() and p.name != "SKILL.md":
                    self.assertEqual((target / p.relative_to(source)).read_bytes(), p.read_bytes())

    def test_claude_preview_does_not_create_or_transform(self):
        before = digest_tree(KIT / "skills")
        self.assertEqual(self.run_installer(runtime="claude-code").returncode, 0)
        self.assertFalse(self.destination.exists())
        self.assertEqual(digest_tree(KIT / "skills"), before)

    def test_claude_collision_prevents_all_copies(self):
        existing = self.destination / NAMES[-1]
        existing.mkdir(parents=True)
        (existing / "SKILL.md").write_text("keep this")
        before = digest_tree(self.destination)
        self.assertNotEqual(self.run_installer("--apply", runtime="claude-code").returncode, 0)
        self.assertEqual(digest_tree(self.destination), before)

    def test_copy_failure_removes_only_new_skill_folders(self):
        spec = importlib.util.spec_from_file_location("kit_installer", SCRIPT)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        self.destination.mkdir()
        sentinel = self.destination / "existing.txt"
        sentinel.write_text("preserve")
        with patch.object(module.shutil, "copytree", side_effect=OSError("simulated copy failure")):
            with self.assertRaises(OSError):
                module.install(self.destination, apply=True)
        self.assertEqual(list(self.destination.iterdir()), [sentinel])
        self.assertEqual(sentinel.read_text(), "preserve")


if __name__ == "__main__":
    unittest.main()
