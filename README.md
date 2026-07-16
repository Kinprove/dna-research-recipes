# DNA Research Recipes

Distilled, fact-checked **judgment layers** for genetic-genealogy work, packaged as an
[Agent Skill](https://code.claude.com/docs/en/skills). Each recipe targets what an AI assistant
does *not* reliably know, or does *wrong* by default: the named failure modes, the
delegate-vs-never-trust boundaries, and the reasoning sequence a human must own. They deliberately
skip well-documented fundamentals and volatile UI click-paths.

Authored and maintained by [Kinprove](https://kinprove.io).

## What's inside

A single skill, `dna-research-recipes`, with five recipes:

| Recipe | Use it for |
| --- | --- |
| `unknown-parentage-wato` | Placing an unknown person into a tree with DNA matches + WATO odds; adoptee / unknown-parent search; clustering matches to an ancestral couple. |
| `ai-for-dna-research` | Using an AI assistant reliably on DNA/genealogy work — what to delegate, what to never trust, cM→relationship guardrails. |
| `ydna-mtdna-interpretation` | Reading Y-DNA and mtDNA results (haplogroup, Y-STR genetic distance, mtDNA match) for a genealogical-timeframe relationship. |
| `ai-for-documentary-records` | Using an AI assistant reliably on documentary/records work — handwriting transcription & translation, full-text finding aids, AI record hints, image restoration. |
| `evidence-proof-judgment` | Correlating evidence & proving identity — same-name conflation, conflicting records, negative evidence, combining DNA and documents into one proof. |

Read the recipe file in full before advising; the value is in the specifics.

## Install

The skill folder `dna-research-recipes/` follows the open
[`SKILL.md` Agent Skills](https://code.claude.com/docs/en/skills) standard, so it loads in any
agent that supports skills. Pick your tool below.

### Claude Code (plugin marketplace)

```sh
claude plugin marketplace add Kinprove/dna-research-recipes
claude plugin install dna-research-recipes@kinprove
```

`kinprove` is the marketplace name defined in `.claude-plugin/marketplace.json`. Verify with
`claude plugin validate .` after cloning if you are working on the repo locally.
Docs: <https://docs.claude.com/en/docs/claude-code/plugin-marketplaces>

### Claude.ai (ZIP upload)

Custom skills on Claude.ai are uploaded as a ZIP of the skill folder.

1. Enable code execution in **Settings → Capabilities** (Free/Pro/Max) or **Organization settings → Skills** (Team/Enterprise).
2. Clone this repo and zip the skill folder:

   ```sh
   git clone https://github.com/Kinprove/dna-research-recipes.git
   cd dna-research-recipes
   zip -r dna-research-recipes.zip dna-research-recipes
   ```

3. Go to **Customize → Skills**, click **+**, choose **Create skill → Upload a skill**, and upload `dna-research-recipes.zip`.

Docs: <https://support.claude.com/en/articles/12512180-getting-started-with-skills-on-claude-ai>

### Codex CLI

Codex discovers skills from `.agents/skills/` directories (repo scope) and `~/.agents/skills/`
(user scope). Drop the skill folder into one of them:

```sh
git clone https://github.com/Kinprove/dna-research-recipes.git
mkdir -p ~/.agents/skills
cp -R dna-research-recipes/dna-research-recipes ~/.agents/skills/
```

Docs: <https://developers.openai.com/codex/skills>

### Gemini CLI

Gemini CLI discovers user skills from `~/.gemini/skills/` (or the `~/.agents/skills/` alias) and
workspace skills from `.gemini/skills/` (or `.agents/skills/`):

```sh
git clone https://github.com/Kinprove/dna-research-recipes.git
mkdir -p ~/.gemini/skills
cp -R dna-research-recipes/dna-research-recipes ~/.gemini/skills/
```

Docs: <https://geminicli.com/docs/cli/skills/>

### Cursor

Cursor discovers skills from `.cursor/skills/` (project) and `~/.cursor/skills/` (global), plus the
`.agents/skills/` alias:

```sh
git clone https://github.com/Kinprove/dna-research-recipes.git
mkdir -p ~/.cursor/skills
cp -R dna-research-recipes/dna-research-recipes ~/.cursor/skills/
```

Docs: <https://cursor.com/docs/skills>

## Pair with the Kinprove MCP connector (optional)

These recipes carry judgment; the [Kinprove](https://kinprove.io) platform carries your data. Pair
the skill with the Kinprove MCP connector so your agent can query your own DNA matches, projects,
and ancestral-couple hypotheses while it reasons.

- MCP endpoint: `https://api.kinprove.io/mcp/v1`

Add it as a connector in your agent's MCP settings and authenticate with your Kinprove account.

## License

FSL-1.1-MIT (Functional Source License 1.1, MIT Future License) — see [`LICENSE`](LICENSE).
Copyright 2026 Kinprove. Each version converts to the MIT license two years after its release.
Third-party attributions and any reproduced-data carve-outs are in [`NOTICE`](NOTICE) and each
recipe's `recipes/<slug>.sources.md`.
