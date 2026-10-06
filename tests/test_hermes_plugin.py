"""Offline regression checks for the native Hermes skill registration."""

import importlib.util
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class RegistrationContext:
    """The public register_skill contract, without requiring Hermes in unit tests."""

    def __init__(self):
        self.skills = []

    def register_skill(self, name, path, description=""):
        self.skills.append((name, Path(path), description))


class HermesPluginTests(unittest.TestCase):
    def test_register_exposes_the_existing_skill_bundle(self):
        entrypoint = ROOT / "__init__.py"
        self.assertTrue(entrypoint.is_file(), "Native Hermes entrypoint is missing")
        spec = importlib.util.spec_from_file_location("kinprove_hermes_plugin", entrypoint)
        assert spec is not None and spec.loader is not None
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        context = RegistrationContext()

        module.register(context)

        self.assertEqual(len(context.skills), 1)
        name, skill_md, description = context.skills[0]
        self.assertEqual(name, "genealogy-research-recipes")
        self.assertEqual(
            skill_md,
            ROOT / "skills" / "genealogy-research-recipes" / "SKILL.md",
        )
        self.assertTrue(skill_md.is_file())
        self.assertTrue(description)
        self.assertTrue((skill_md.parent / "recipes" / "ai-for-dna-research.md").is_file())
        self.assertTrue((skill_md.parent / "sources" / "ai-for-dna-research.md").is_file())
        self.assertTrue((skill_md.parent / "resources" / "beider-name-indexes.json").is_file())
        self.assertTrue((skill_md.parent / "scripts" / "lookup_beider_name.py").is_file())


if __name__ == "__main__":
    unittest.main()
