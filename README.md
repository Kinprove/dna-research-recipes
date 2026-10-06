# Genealogy Research Recipes

Fact-checked recipes that keep an AI assistant from the usual genealogy mistakes, for DNA
evidence and for record searches. One [Agent Skill](https://code.claude.com/docs/en/skills),
packaged for Claude, Hermes Agent and OpenClaw, by [Kinprove](https://kinprove.io).
No Kinprove account is needed to read the recipes.

## Install

**Claude Code** — run in a session:

```text
/plugin marketplace add Kinprove/genealogy-research-recipes
/plugin install genealogy-research-recipes@kinprove
```

**Claude.ai and the Claude desktop app** — open **Customize → Plugins → Add → Add marketplace**,
enter `Kinprove/genealogy-research-recipes`, then add `genealogy-research-recipes`.

**Hermes Agent** — install and explicitly enable the native plugin:

```sh
hermes plugins install Kinprove/genealogy-research-recipes --no-enable
hermes plugins enable genealogy-research-recipes
```

After enabling, ask the agent to discover the plugin with `skills_list` and load
`genealogy-research-recipes:genealogy-research-recipes` with `skill_view`. Skill-only
plugins can become available in an open chat; start a new session only if discovery
has not refreshed. A Hermes Gateway restart is not required for this skill bundle.

Agent tool calls (not shell commands):

```python
skills_list(category="plugin")
skill_view(name="genealogy-research-recipes:genealogy-research-recipes")
skill_view(
    name="genealogy-research-recipes:genealogy-research-recipes",
    file_path="recipes/ai-for-dna-research.md",
)
```

Use a relative `file_path` for a recipe, its corresponding `sources/` file, or
another bundled resource. For example, ask: "Load the Kinprove recipes, read
`recipes/xdna-phasing-judgment.md`, and distinguish what my X-DNA evidence can
support from what still needs verification."

Native plugin skills are read-only, namespaced and explicitly loaded; Hermes does
not add them to the automatic system-prompt skill index. Existing skills with the
same bare name remain separate. The plugin needs no Python dependencies, API keys
or Kinprove account and does not configure the optional MCP connector.

Update the installed plugin with:

```sh
hermes plugins update genealogy-research-recipes
```

**OpenClaw** — install the native plugin:

```sh
openclaw plugins install git:github.com/Kinprove/genealogy-research-recipes
```

OpenClaw asks you to confirm the source and the plugin's skills. Restart the Gateway
after installing. The `genealogy-research-recipes` skill then loads like any other
OpenClaw skill, with every recipe file beside it. The plugin registers no tools or
hooks, needs no Node dependencies, API keys or Kinprove account and does not
configure the optional MCP connector.

Update the installed plugin with:

```sh
openclaw plugins update genealogy-research-recipes
```

## Registries and provenance

These are separate distribution surfaces; adding a native adapter does not
register the package in another host's public catalog.

- **Claude:** this repository already supplies its own `kinprove` marketplace in
  [`.claude-plugin/marketplace.json`](.claude-plugin/marketplace.json). It is not a
  claim of inclusion in a separate Anthropic-curated directory.
- **Hermes:** installation by `Kinprove/genealogy-research-recipes` works without
  a catalog entry. The [Hermes plugin catalog](https://hermes-agent.nousresearch.com/docs/plugins)
  accepts a separate, human-reviewed PR pinned to an exact commit. An open PR is
  not admission; use the repository install above until the entry is listed.
  After admission, install by `genealogy-research-recipes` and enable it as above.
  Catalog updates move only to a newly reviewed pin, not to an arbitrary branch tip.
- **OpenClaw:** [ClawHub](https://clawhub.ai) publication is separate from GitHub
  installation. For a published Kinprove release, use the explicit registry source:

  ```sh
  openclaw plugins install clawhub:@kinprove/genealogy-research-recipes
  ```

  Check the publisher, version and source commit on ClawHub before installing.
  If that release is not available, use the GitHub install above. The OpenClaw
  runtime plugin ID and update target remain `genealogy-research-recipes`.

To make a direct Hermes repository install reproducible, add
`--ref <full-commit-sha>` to the install command. Public catalog inclusion does not
mean a package is maintained by the host or has received a full security audit.

The native adapters expose bundled instructions, not automatic access to your
DNA accounts or records. They do not make service calls, install an MCP server,
store credentials, send telemetry, or start background jobs. Individual recipes
can describe optional services and commands; executing those still requires the
host's appropriate tools, permissions and any service-specific credentials.

## Publishing to ClawHub (maintainers)

Use a clean checkout of the reviewed commit, with all host manifest versions
synchronized. Publish under the ClawHub `kinprove` owner using an account with
access to that owner. The `@kinprove/` package scope must match it.

```sh
npx --yes clawhub@0.23.3 package validate . --out ../clawhub-validation --json
npx --yes clawhub@0.23.3 package publish . --family code-plugin --owner kinprove --dry-run --json
```

Check that the dry-run reports `code-plugin`, the intended version and the exact
reviewed commit before making a separately authorized live publication. Keep
`--family code-plugin`: Claude manifests coexist in this repository, so automatic
family detection can choose a Claude bundle instead of the native OpenClaw package.
The npm artifact deliberately includes native OpenClaw code and the complete
skill/resources/license tree, not the other hosts' adapters or development files.

A successful dry-run is not a public release. Authenticate securely, publish the
same clean commit with the same flags (without `--dry-run`), and verify its
ClawHub publication/security-check status before announcing availability. Do not
publish to npm merely because this package uses an npm-style scoped name.

## Recipes

- **DNA reasoning:** [unknown parentage and WATO](skills/genealogy-research-recipes/recipes/unknown-parentage-wato.md), [AI for DNA research](skills/genealogy-research-recipes/recipes/ai-for-dna-research.md), [Y-DNA and mtDNA](skills/genealogy-research-recipes/recipes/ydna-mtdna-interpretation.md), [X-DNA and phasing](skills/genealogy-research-recipes/recipes/xdna-phasing-judgment.md)
- **DNA sites:** [23andMe](skills/genealogy-research-recipes/recipes/23andme-match-research.md), [AncestryDNA](skills/genealogy-research-recipes/recipes/ancestry-dna-match-investigation.md), [FamilyTreeDNA](skills/genealogy-research-recipes/recipes/ftdna-practical-dna-workflows.md), [GEDmatch](skills/genealogy-research-recipes/recipes/gedmatch-practical-dna-workflows.md), [MyHeritage DNA](skills/genealogy-research-recipes/recipes/myheritage-dna-match-investigation.md), [DNA Painter](skills/genealogy-research-recipes/recipes/dnapainter-practical-dna-workflows.md)
- **Evidence:** [evidence and proof](skills/genealogy-research-recipes/recipes/evidence-proof-judgment.md), [AI for documents](skills/genealogy-research-recipes/recipes/ai-for-documentary-records.md)
- **Jewish and Russian Empire:** [name and registration changes](skills/genealogy-research-recipes/recipes/russian-empire-jewish-identity-attribution.md), [emigrant origins](skills/genealogy-research-recipes/recipes/russian-empire-emigrant-origin-recovery.md), [JewishGen](skills/genealogy-research-recipes/recipes/jewishgen-search-family-reconstruction.md), [Beider given names](skills/genealogy-research-recipes/recipes/beider-given-name-variants.md), [HebrewBooks](skills/genealogy-research-recipes/recipes/hebrewbooks-search-recovery.md)
- **Record sites:** [Ancestry](skills/genealogy-research-recipes/recipes/ancestry-record-search-recovery.md), [FamilySearch](skills/genealogy-research-recipes/recipes/familysearch-practical-record-workflows.md), [MyHeritage](skills/genealogy-research-recipes/recipes/myheritage-historical-record-search.md), [Newspapers.com](skills/genealogy-research-recipes/recipes/newspapers-com-search-recovery.md), [Geni](skills/genealogy-research-recipes/recipes/geni-practical-research-workflows.md), [U.S. census](skills/genealogy-research-recipes/recipes/us-census-practical-workflows.md), [U.S. immigration](skills/genealogy-research-recipes/recipes/usa-immigration-search-recovery.md)

Each recipe's sources are in [`sources/`](skills/genealogy-research-recipes/sources/).

## Kinprove MCP (optional)

Add `https://api.kinprove.io/mcp/v1` as an MCP connector so the agent can read your own Kinprove
matches and projects.

## License

[FSL-1.1-MIT](LICENSE), © 2026 Kinprove; each version becomes MIT two years after its release.
Third-party data: [NOTICE](NOTICE).
