"""Every host manifest must carry the same release version."""

import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
JSON_MANIFESTS = (".claude-plugin/plugin.json", "openclaw.plugin.json", "package.json")


class ManifestVersionTests(unittest.TestCase):
    def test_all_manifests_share_one_version(self):
        versions = {
            name: json.loads((ROOT / name).read_text(encoding="utf-8"))["version"] for name in JSON_MANIFESTS
        }
        hermes = re.search(r"^version:\s*(\S+)", (ROOT / "plugin.yaml").read_text(encoding="utf-8"), re.MULTILINE)
        assert hermes is not None, "plugin.yaml has no version"
        versions["plugin.yaml"] = hermes.group(1)

        self.assertEqual(len(set(versions.values())), 1, versions)
        self.assertEqual(versions["package.json"], "1.1.1")


if __name__ == "__main__":
    unittest.main()
