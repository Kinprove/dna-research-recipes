"""Offline regression checks for the native OpenClaw plugin manifests."""

import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PLUGIN = "genealogy-research-recipes"


def load(name):
    return json.loads((ROOT / name).read_text(encoding="utf-8"))


class OpenClawPluginTests(unittest.TestCase):
    def test_manifest_ships_the_existing_skill_bundle(self):
        manifest = load("openclaw.plugin.json")

        self.assertEqual(manifest["id"], PLUGIN)
        # OpenClaw rejects a native manifest without a schema, even for a plugin with no config.
        self.assertIsInstance(manifest["configSchema"], dict)
        self.assertEqual(manifest["skills"], ["./skills"])
        self.assertTrue((ROOT / "skills" / PLUGIN / "SKILL.md").is_file())

    def test_package_entry_keeps_the_plugin_native(self):
        # With .claude-plugin/ present, OpenClaw loads the repository as a Claude bundle
        # unless package.json declares a native entrypoint.
        self.assertEqual(load("package.json")["openclaw"]["extensions"], ["./index.js"])
        entrypoint = ROOT / "index.js"
        self.assertTrue(entrypoint.is_file(), "Native OpenClaw entrypoint is missing")
        self.assertIn(f'id: "{PLUGIN}"', entrypoint.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
