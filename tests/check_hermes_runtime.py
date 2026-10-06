"""Exercise real Hermes discovery and skill reads in a disposable profile.

Run with the pinned Hermes runtime on PYTHONPATH and its Python interpreter.
No existing Hermes profile is read or changed.
"""

import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PLUGIN = "genealogy-research-recipes"
QUALIFIED_SKILL = f"{PLUGIN}:{PLUGIN}"


def main():
    with tempfile.TemporaryDirectory(prefix="kinprove-hermes-test-", dir=os.environ.get("TMPDIR")) as directory:
        home = Path(directory)
        package = home / "plugins" / PLUGIN
        package.mkdir(parents=True)
        for name in ("plugin.yaml", "__init__.py"):
            shutil.copy2(ROOT / name, package / name)
        shutil.copytree(ROOT / "skills", package / "skills")
        (home / "config.yaml").write_text(
            f"plugins:\n  enabled: [{PLUGIN}]\n  disabled: []\n"
            "skills:\n  external_dirs: []\n"
            "security:\n  allow_lazy_installs: false\n",
            encoding="utf-8",
        )
        # A colliding bare name must remain a separate, user-owned skill.
        local_skill = home / "skills" / PLUGIN / "SKILL.md"
        local_skill.parent.mkdir(parents=True)
        local_skill.write_text(
            f"---\nname: {PLUGIN}\ndescription: Local collision fixture.\n---\n\n"
            "Local fixture, not the plugin bundle.\n",
            encoding="utf-8",
        )
        os.environ["HERMES_HOME"] = str(home)
        os.environ["HERMES_SAFE_MODE"] = "0"

        # Import only after the temporary profile is selected.
        from hermes_cli.plugins import get_plugin_manager
        from tools.skills_tool import skill_view, skills_list

        manager = get_plugin_manager()
        manager.discover_and_load()
        registered = manager.find_plugin_skill(QUALIFIED_SKILL)
        expected_skill = package / "skills" / PLUGIN / "SKILL.md"
        assert registered == expected_skill, "Native discovery did not register the bundled skill"
        listing = json.loads(skills_list())
        assert listing.get("success"), listing
        assert QUALIFIED_SKILL in {item["name"] for item in listing["skills"]}, listing
        skill = json.loads(skill_view(QUALIFIED_SKILL, preprocess=False))
        assert skill.get("success"), skill
        assert expected_skill.read_text(encoding="utf-8") in skill["content"], "Wrong skill contents"

        for relative in (
            "recipes/ai-for-dna-research.md",
            "sources/ai-for-dna-research.md",
            "scripts/lookup_beider_name.py",
        ):
            served = json.loads(skill_view(QUALIFIED_SKILL, file_path=relative, preprocess=False))
            assert served.get("success"), served
            assert served["content"] == (expected_skill.parent / relative).read_text(encoding="utf-8"), relative

        bare = json.loads(skill_view(PLUGIN, preprocess=False))
        assert bare.get("success"), bare
        assert bare["content"] == local_skill.read_text(encoding="utf-8"), "Plugin replaced the bare skill"
        assert {path.name for path in (home / "skills").iterdir()} == {PLUGIN}, "Plugin copied skills into the user tree"

        lookup = subprocess.run(
            [sys.executable, "-B", str(expected_skill.parent / "scripts" / "lookup_beider_name.py"), "--sex", "male", "--name", "Гершель"],
            cwd=home,
            capture_output=True,
            text=True,
            check=True,
            timeout=30,
        )
        assert json.loads(lookup.stdout)["status"] == "found", "Bundled resource lookup failed"
        print("PASS: native discovery, listing, skill/recipe/source/script reads, bare-name isolation and offline Beider lookup")


class HermesRuntimeTests(unittest.TestCase):
    def test_native_bundle_access_and_namespace_isolation(self):
        main()


if __name__ == "__main__":
    unittest.main()
