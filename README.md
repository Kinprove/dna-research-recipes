# Genealogy Research Recipes

Fact-checked recipes that keep an AI assistant from the usual genealogy mistakes, for DNA
evidence and for record searches. One [Agent Skill](https://code.claude.com/docs/en/skills) by
[Kinprove](https://kinprove.io); no Kinprove account needed.

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

Start a new Hermes session after enabling. Ask the agent to load
`genealogy-research-recipes:genealogy-research-recipes` with `skill_view`, or discover
it with `skills_list`. To load an individual recipe, use the same qualified name
and a relative `file_path`, for example `recipes/ai-for-dna-research.md`.

Native plugin skills are read-only, namespaced and explicitly loaded; Hermes does
not add them to the automatic system-prompt skill index. Existing skills with the
same bare name remain separate. The plugin needs no Python dependencies, API keys
or Kinprove account and does not configure the optional MCP connector.

Update the installed plugin with:

```sh
hermes plugins update genealogy-research-recipes
```

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
