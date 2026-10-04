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

## Recipes

- **DNA reasoning:** [unknown parentage and WATO](genealogy-research-recipes/recipes/unknown-parentage-wato.md), [AI for DNA research](genealogy-research-recipes/recipes/ai-for-dna-research.md), [Y-DNA and mtDNA](genealogy-research-recipes/recipes/ydna-mtdna-interpretation.md), [X-DNA and phasing](genealogy-research-recipes/recipes/xdna-phasing-judgment.md)
- **DNA sites:** [23andMe](genealogy-research-recipes/recipes/23andme-match-research.md), [AncestryDNA](genealogy-research-recipes/recipes/ancestry-dna-match-investigation.md), [FamilyTreeDNA](genealogy-research-recipes/recipes/ftdna-practical-dna-workflows.md), [GEDmatch](genealogy-research-recipes/recipes/gedmatch-practical-dna-workflows.md), [MyHeritage DNA](genealogy-research-recipes/recipes/myheritage-dna-match-investigation.md), [DNA Painter](genealogy-research-recipes/recipes/dnapainter-practical-dna-workflows.md)
- **Evidence:** [evidence and proof](genealogy-research-recipes/recipes/evidence-proof-judgment.md), [AI for documents](genealogy-research-recipes/recipes/ai-for-documentary-records.md)
- **Jewish and Russian Empire:** [name and registration changes](genealogy-research-recipes/recipes/russian-empire-jewish-identity-attribution.md), [emigrant origins](genealogy-research-recipes/recipes/russian-empire-emigrant-origin-recovery.md), [JewishGen](genealogy-research-recipes/recipes/jewishgen-search-family-reconstruction.md), [Beider given names](genealogy-research-recipes/recipes/beider-given-name-variants.md), [HebrewBooks](genealogy-research-recipes/recipes/hebrewbooks-search-recovery.md)
- **Record sites:** [Ancestry](genealogy-research-recipes/recipes/ancestry-record-search-recovery.md), [FamilySearch](genealogy-research-recipes/recipes/familysearch-practical-record-workflows.md), [MyHeritage](genealogy-research-recipes/recipes/myheritage-historical-record-search.md), [Newspapers.com](genealogy-research-recipes/recipes/newspapers-com-search-recovery.md), [Geni](genealogy-research-recipes/recipes/geni-practical-research-workflows.md), [U.S. census](genealogy-research-recipes/recipes/us-census-practical-workflows.md), [U.S. immigration](genealogy-research-recipes/recipes/usa-immigration-search-recovery.md)

Each recipe's sources are in [`sources/`](genealogy-research-recipes/sources/).

## Kinprove MCP (optional)

Add `https://api.kinprove.io/mcp/v1` as an MCP connector so the agent can read your own Kinprove
matches and projects.

## License

[FSL-1.1-MIT](LICENSE), © 2026 Kinprove; each version becomes MIT two years after its release.
Third-party data: [NOTICE](NOTICE).
