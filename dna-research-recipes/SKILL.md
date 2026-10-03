---
name: dna-research-recipes
description: >-
  Genealogy judgment: failure modes, AI verification, source-grounded reasoning. Use for unknown parentage or adoptees; WATO / DNA Painter hypothesis placement; clustering matches to ancestral couples; Ashkenazi or endogamous matches; families across branches, siblings and generations; segment attribution and targeted relative testing; AI for DNA, citations, records, transcription, translation, FamilySearch Full-Text Search, record hints or photo restoration; Y-DNA haplogroups, SNP no-calls, Y-STR genetic distance; mtDNA matches; X-DNA thresholds, visual or parental phasing, GEDmatch, half-sister versus aunt; relationships, same-name identities, conflicting records, negative evidence, Genealogical Proof Standard, DNA with documents; Russian-Empire Jewish surname or patronymic changes, revision lists, приписка, recruit evasion; JewishGen queries, name variants, wives' natal families or married daughters. Newspapers.com coverage, name/OCR recovery and notice attribution. Read the matching recipe before advising.
---

<!-- SCAFFOLD (repo scaffold step): this public SKILL.md is authored as the skill index. The
     recipe bodies (recipes/<slug>.md + recipes/<slug>.sources.md) are injected by the
     deterministic export step; the maintainer finalizes the sanitized wording before release. -->

# DNA research recipes

Distilled, fact-checked **judgment layers** for genetic-genealogy work. Each recipe targets
what an LLM does *not* reliably know, or does *wrong* by default: the named failure modes, the
delegate-vs-never-trust lines, and the reasoning sequence a human must own. They deliberately
skip well-documented fundamentals (you already hold those) and version-specific UI clicks
(volatile, low value, stale-prone).

The research methods apply across platforms, including work from exported data. Kinprove
authorship does not require a Kinprove account, connector or scoring engine.

## How to use

1. Match the user's task to a recipe below.
2. **Read that recipe file in full before advising** — the value is in the specifics, not the summary.
3. Apply its "never trust / never delegate" boundaries as **hard constraints on your own output** —
   those are the exact places a confident answer goes wrong (e.g. fabricating cM→relationship odds,
   reading a WATO ranking as a verdict, ignoring endogamy).
4. If no recipe matches, answer normally — don't force-fit.

## Recipes

- **`recipes/unknown-parentage-wato.md`** — Placing an unknown person (an unknown parent, an
  adoptee's bio-parent, an unplaced ancestor) into a tree using DNA matches + WATO odds.
  *Use for:* "who is my unknown grandfather/father", adoptee bio-family search, WATO hypothesis
  scoring, clustering matches to an ancestral couple, tied hypotheses, choosing a discriminating
  tester, or deciding which observations to withhold from a calculation.
  *Core guardrail:* WATO ranks placements on a tree **you already built**, gives **relative** odds
  among competing hypotheses (never a verdict), and breaks **silently** under endogamy / pedigree
  collapse / any multi-path match.

- **`recipes/ai-for-dna-research.md`** — Using an AI assistant *reliably* on DNA/genealogy work:
  what to delegate freely, what to never trust, and the prompt patterns that work. Includes
  endogamous match prioritization, segment attribution, targeted testing of outmarrying branches,
  and coherent family comparisons across tested ancestors, siblings and descendants.
  *Also use for:* "how are these two families connected", multiple related focal testers,
  repeated descent paths, a long segment in a relative that is shorter/absent in a descendant,
  mixed-origin segment overhangs, fused clusters, or validating a match's own pedigree.
  *Use for:* any "can AI/ChatGPT/Claude help me with my DNA / tree / citations", **or** whenever
  you (the assistant) are about to compute or assert something in this domain.
  *Core guardrail:* never fabricate cM→relationship odds (route to the Shared cM Project / DNA
  Painter WATO); every AI output is a **hypothesis to verify**, never a fact to file.

- **`recipes/ydna-mtdna-interpretation.md`** — Interpreting Y-DNA and mtDNA results (a haplogroup
  assignment, a Y-STR genetic-distance match, an mtDNA sequence match): what each can actually
  establish about a *genealogical-timeframe* relationship, and where confident interpretation
  crosses into fabrication. The Y-STR/mtDNA complement to `ai-for-dna-research.md` (autosomal cM).
  *Use for:* "what does my haplogroup / Y-STR match / mtDNA match mean", "how many generations back
  is genetic distance N", "does this haplogroup contradiction prove a non-paternity event",
  differing Y labels, measured versus inferred SNP results, choosing a tester to split an
  unresolved SNP block, TMRCA disagreement with a dated pedigree, or a pair matching on both
  autosomal DNA and Y-DNA/mtDNA through potentially different ancestral lines.
  *Core guardrail:* never assign a haplogroup or compute a GD→generations/TMRCA point estimate from
  memory (route to FTDNA Discover / TiP report / Match Time Tree, quote a resolution-dependent
  **range**); an exact match at low resolution is **unresolved**, not recent; a haplogroup
  contradiction or absent surname-match is a **flag needing corroboration**, never proof of an NPE.

- **`recipes/xdna-phasing-judgment.md`** — X-DNA matches and visual/parental phasing: what a
  segment, an X match, or a phased chromosome map can actually confirm or eliminate, and where
  confident-sounding analysis is actually fabrication.
  *Use for:* "is this X-DNA match trustworthy", "what's the minimum X cM threshold", "phase my kit
  against a parent or siblings", "half-sister or aunt", "does this X match rule out a father",
  reconstructed-kit quality, artificial homozygosity, or interpreting matches to a synthetic kit.
  *Core guardrail:* never invent a small-segment or X-DNA false-positive rate or cM threshold — cite
  the specific company/study, since they diverge by design and by pair-sex; phasing reduces but never
  eliminates pseudosegments on either side; an X-DNA result consistent with a hypothesis is a
  **veto only**, never confirmation.

- **`recipes/ai-for-documentary-records.md`** — Using an AI assistant *reliably* on DOCUMENTARY / records
  work (NOT DNA): handwriting transcription & translation, AI full-text / OCR finding aids (FamilySearch
  Full-Text Search), reviewing & correcting AI-indexed records, evaluating AI record hints, and image
  restoration / colorization / generation & evidentiary trust.
  *Use for:* any "can AI/ChatGPT/Gemini transcribe or translate this handwriting", "full-text search for
  unindexed deeds/probate", "correct AI-indexed records", "evaluate an AI record hint", "colorize/restore
  an old photo".
  *Core guardrail:* every AI output is a **hypothesis to verify** against the ORIGINAL image; a bare LLM is
  not a search engine; never use an AI-restored/generated face for identification.

- **`recipes/evidence-proof-judgment.md`** — Correlating evidence & proving identity: the judgment an AI gets
  WRONG when it recites the Genealogical Proof Standard but misapplies it — same-name conflation, conflict-
  flattening, over-reading a document, negative-evidence errors, DNA/documentary siloing, de-novo fabrication,
  and sycophancy toward the answer you want.
  *Use for:* separating same-named people, resolving conflicting records, weighing indirect vs negative evidence,
  or combining DNA with documents into ONE proof — **and** whenever you (the assistant) are about to state a
  genealogical conclusion.
  *Core guardrail:* the human owns every ruling (merge/separate, conflict resolution, exhaustiveness, the final
  "therefore proven"); the model assembles and drafts but NEVER concludes.
- **`recipes/russian-empire-jewish-identity-attribution.md`** — A Russian-Empire Jewish ancestor who turns up
  under a given name, patronymic or surname that fits neither candidate branch: the inverse of same-name
  collapse (one person, several names), read through the imperial record system — revision lists (ревизские
  сказки), family lists (посемейные списки), metrical books and recruit files as ledgers of *registration*
  (приписка), not vital records — with the naming and re-registration mechanisms (double names, head-of-household
  patronymics, heir naming, stepchild, fostered orphan, levy evasion, son-in-law surname, surname split,
  conversion) carried as competing hypotheses, and the "prediction must differ" test before any DNA is asked to
  choose between branches of one endogamous family.
  *Use for:* "which brother was his father", a boy registered in a relative's household, a wife's child from a
  first marriage, a family hiding a son from the recruit levy / cantonists, brothers under different surnames,
  a patronymic that is the grandfather's or the husband's name, a person missing from a revision list, or
  DNA that "can't tell the two branches apart" under Ashkenazi endogamy plus repeated pedigree collapse.
  *Core guardrail:* chain the household before you judge the name; find the приписка before you search a
  town; write which tester's result would DIFFER under the two hypotheses before touching a match list — if
  none differs, say "undecidable with current testers" and name the tester who would decide it.

- **`recipes/jewishgen-search-family-reconstruction.md`** — Retrieving JewishGen family records when
  names, ages, towns or a woman's surname are uncertain. Build explicit name-variant and mixed-field
  search batches, distinguish registration from residence, and look for wives' natal families or
  married daughters through children's records and household comparisons.
  *Use for:* JewishGen exact, partial, phonetic or fuzzy searches; double names and patronymics;
  conflicting ages or delayed registration; a missing marriage record, unknown maiden name or
  daughter who disappears under a married surname.
  *Core guardrail:* verify each collection's field and search-method semantics; a name, age or
  household match creates a candidate, and a recruitment explanation remains a hypothesis until
  independent records support it.

- **`recipes/newspapers-com-search-recovery.md`** — Recovering newspaper notices when issue
  coverage, printed names or OCR hide an ancestor on Newspapers.com. Search initials, married
  names, associates, occupations and addresses; follow travel, social and legal notices across
  relevant newspapers, then verify the original notice.
  *Use for:* a failed newspaper name search, an unknown maiden name, a missing obituary,
  immigration or family-reconstruction leads, incomplete issue coverage, or unreadable OCR.
  *Core guardrail:* a page-level hit can join different notices; verify each person, relationship,
  event date and place in its actual notice. A failed query is not evidence that an event never
  happened, and a second index of the same newspaper image is not independent corroboration.

## What a recipe is (and isn't)

- **Fact-checked.** Each recipe separates independently verified claims from figures reported by a
  cited source but not independently verified. Honor that line — don't present a source-reported
  transcript figure (a specific cM number, a percentage) as a rule.
- **Judgment, not fundamentals.** Recipes carry the non-obvious judgment an unaided answer gets
  wrong, not the well-documented basics you already produce reliably.
- **Not a manual.** No click-by-click UI. If the user needs the buttons, send them to the tool's
  own docs; the recipe carries the judgment around the tool.

## Attribution

These recipes are original Kinprove-authored distillations, licensed FSL-1.1-MIT (see `LICENSE`).
Third-party facts and methods are credited in each recipe's `recipes/<slug>.sources.md`; any
reproduced third-party data is carved out in `NOTICE`.
