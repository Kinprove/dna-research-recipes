"""Regression checks for the Kinprove native ClawHub package."""

import json
import shutil
import subprocess
import tarfile
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ClawHubPackageTests(unittest.TestCase):
    def test_package_scope_matches_the_publishing_owner(self):
        package = json.loads((ROOT / "package.json").read_text(encoding="utf-8"))
        self.assertEqual(package["name"], "@kinprove/genealogy-research-recipes")

    def test_registry_metadata_preserves_license_and_source(self):
        package = json.loads((ROOT / "package.json").read_text(encoding="utf-8"))
        self.assertEqual(package.get("license"), "FSL-1.1-MIT")
        self.assertEqual(package.get("repository"), {
            "type": "git",
            "url": "https://github.com/Kinprove/genealogy-research-recipes.git",
        })

    def test_package_is_publicly_packable(self):
        package = json.loads((ROOT / "package.json").read_text(encoding="utf-8"))
        self.assertIs(package.get("private", False), False)

    def test_compatibility_starts_at_the_tested_openclaw_release(self):
        package = json.loads((ROOT / "package.json").read_text(encoding="utf-8"))
        self.assertEqual(package["openclaw"].get("compat"), {"pluginApi": ">=2026.9.8"})
        self.assertEqual(package["openclaw"].get("build"), {"openclawVersion": "2026.9.8"})

    def test_npm_artifact_ships_only_native_code_and_complete_skill_resources(self):
        npm = shutil.which("npm")
        assert npm is not None, "npm is required to exercise the real package artifact"
        skill = ROOT / "skills" / "genealogy-research-recipes"
        expected = {
            "package.json", "index.js", "openclaw.plugin.json", "README.md", "LICENSE", "NOTICE",
            "skills/genealogy-research-recipes/SKILL.md",
            "skills/genealogy-research-recipes/LICENSE",
            "skills/genealogy-research-recipes/NOTICE",
        }
        for directory in ("recipes", "sources", "scripts", "resources"):
            resources = {
                path.relative_to(ROOT).as_posix()
                for path in (skill / directory).rglob("*")
                if path.is_file() and "__pycache__" not in path.parts
                and path.suffix != ".pyc" and path.name != ".DS_Store"
            }
            self.assertTrue(resources, f"Missing {directory} resources")
            expected.update(resources)

        with tempfile.TemporaryDirectory(prefix="kinprove-npm-pack-") as directory:
            temporary = Path(directory)
            source = temporary / "source"
            shutil.copytree(ROOT, source, ignore=shutil.ignore_patterns(".git", "node_modules", "__pycache__"))
            (source / "untracked-output.txt").write_text("must not ship\n", encoding="utf-8")
            cache = source / "skills" / "genealogy-research-recipes" / "scripts" / "__pycache__"
            cache.mkdir(parents=True)
            (cache / "lookup_beider_name.pyc").write_bytes(b"must not ship")
            result = subprocess.run(
                [npm, "pack", "--ignore-scripts", "--json", "--pack-destination", str(temporary)],
                cwd=source, stdin=subprocess.DEVNULL, capture_output=True, text=True, timeout=120, check=False,
            )
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            packages = json.loads(result.stdout)
            self.assertEqual(len(packages), 1, packages)
            package = packages[0]
            self.assertEqual(package["name"], "@kinprove/genealogy-research-recipes")
            with tarfile.open(temporary / package["filename"], "r:gz") as archive:
                members = archive.getmembers()
                self.assertTrue(all(member.isfile() for member in members), "Unexpected non-file tar member")
                self.assertEqual({member.name for member in members}, {"package/" + path for path in expected})
                self.assertEqual(len(members), len(expected), "Duplicate tar member")
                self.assertEqual(package["entryCount"], len(expected))
                for relative in expected:
                    with self.subTest(resource=relative):
                        resource = archive.extractfile("package/" + relative)
                        assert resource is not None, relative
                        with resource:
                            self.assertEqual(resource.read(), (ROOT / relative).read_bytes())


if __name__ == "__main__":
    unittest.main()
