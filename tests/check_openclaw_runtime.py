"""Exercise a real OpenClaw install and skill discovery in a disposable profile.

Run with the pinned OpenClaw CLI on PATH. No existing OpenClaw profile is read or changed.
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


def main():
    openclaw = shutil.which("openclaw")
    assert openclaw, "The openclaw CLI is not on PATH"
    with tempfile.TemporaryDirectory(prefix="kinprove-openclaw-test-", dir=os.environ.get("TMPDIR")) as directory:
        home = Path(directory).resolve()
        state = home / ".openclaw"
        # Drop inherited OPENCLAW_* selectors so only the temporary profile is used.
        env = {name: value for name, value in os.environ.items() if not name.startswith("OPENCLAW_")}
        env.update(HOME=str(home), OPENCLAW_STATE_DIR=str(state))

        def run_openclaw(*arguments, **options):
            return subprocess.run(
                [openclaw, *arguments], cwd=home, env=env, stdin=subprocess.DEVNULL, check=True, timeout=300, **options
            )

        def openclaw_json(*arguments):
            return json.loads(run_openclaw(*arguments, "--json", stdout=subprocess.PIPE, text=True).stdout)

        run_openclaw("plugins", "install", str(ROOT), "--force", "--accept-capabilities")

        report = openclaw_json("plugins", "inspect", PLUGIN, "--runtime")
        plugin = report["plugin"]
        manifest = json.loads((ROOT / "openclaw.plugin.json").read_text(encoding="utf-8"))
        assert plugin["format"] == "openclaw", f"Loaded as a {plugin.get('bundleFormat')} bundle, not a native plugin"
        assert plugin["status"] == "loaded" and plugin["imported"], plugin
        assert not report["diagnostics"], report["diagnostics"]
        assert plugin["version"] == manifest["version"], plugin["version"]

        listed = {item["name"]: item for item in openclaw_json("skills", "list")["skills"]}
        assert PLUGIN in listed, "The plugin skill is not listed"
        assert listed[PLUGIN]["eligible"] and listed[PLUGIN]["modelVisible"], listed[PLUGIN]

        source_skill = ROOT / "skills" / PLUGIN
        installed_skill = Path(openclaw_json("skills", "info", PLUGIN)["baseDir"]).resolve()
        assert installed_skill == state / "extensions" / PLUGIN / "skills" / PLUGIN, f"Skill served from {installed_skill}"
        for relative in (
            "SKILL.md",
            "recipes/ai-for-dna-research.md",
            "sources/ai-for-dna-research.md",
            "scripts/lookup_beider_name.py",
        ):
            assert (installed_skill / relative).read_bytes() == (source_skill / relative).read_bytes(), relative

        lookup = subprocess.run(
            [sys.executable, "-B", str(installed_skill / "scripts" / "lookup_beider_name.py"), "--sex", "male", "--name", "Гершель"],
            cwd=home,
            stdout=subprocess.PIPE,
            text=True,
            check=True,
            timeout=30,
        )
        assert json.loads(lookup.stdout)["status"] == "found", "Bundled resource lookup failed"
        print("PASS: native install, load, skill listing, skill/recipe/source/script files and offline Beider lookup")


class OpenClawRuntimeTests(unittest.TestCase):
    def test_native_install_and_skill_discovery(self):
        main()


if __name__ == "__main__":
    unittest.main()
