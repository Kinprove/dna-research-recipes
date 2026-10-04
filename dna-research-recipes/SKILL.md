---
name: dna-research-recipes
description: >-
  Genealogy judgment and practical workflows. Use for unknown parentage/adoptees, WATO, ancestral-couple clusters; Ashkenazi/endogamous matches, segments, relative testing; Y-DNA haplogroups/SNP no-calls, Y-STR distance, mtDNA; X-DNA/phasing, GEDmatch, half-sister versus aunt; identity conflicts, negative evidence, Genealogical Proof Standard; transcription, translation, FamilySearch Full-Text Search, record hints, photos; Russian-Empire Jewish names, revision lists, приписка, recruit evasion; JewishGen, Beider names, natal families; MyHeritage records; Newspapers.com coverage/OCR; Ancestry records/DNA, Pro Tools, ThruLines; HebrewBooks OCR, Shafeh, indexes; MyHeritage DNA kits, labels, shared matches, triangulation, Theory of Family Relativity; 23andMe match/matrix exports, permissions, ancestry painting, bucketing, reconstructed ancestors, research trees; FTDNA workflows; DNA Painter painting/transfers, Common/Inferred/Distinct Segment Generators, Coverage Estimator; Geni workflows.
---

# DNA research recipes

Distilled, fact-checked **judgment and practical workflows** for genetic-genealogy work. Each recipe targets
what an LLM does *not* reliably know, or does *wrong* by default: the named failure modes, the
delegate-vs-never-trust lines, the reasoning sequence a human must own, and the records needed
to resume an investigation. Judgment recipes focus on reasoning; platform playbooks provide
ordered actions and investigator-created schemas with dated platform-documentation checks.

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

- **`recipes/geni-practical-research-workflows.md`** — Eight practical Geni workflows:
  recover name variants, preserve relationship focus, cite facts, choose projects, compare
  merge candidates, track tree conflicts, create GEDCOM branches and inspect scoped exports.
  *Use for:* Geni language/alias fields, relationship paths, source documents, public projects
  or private workspaces, merge requests, unmerge requests, GEDCOM imports and tree reports.
  *Core guardrail:* preserve profile URLs and dated scope; distinguish tree assertions,
  source-supported statements, pending requests and completed changes. Draft manager or
  curator requests for human review, and inspect private content before sharing an export.

- **`recipes/ancestry-dna-match-investigation.md`** — Eight practical AncestryDNA workflows:
  use a target's closest relatives, build branch anchor tables, search collateral names,
  organize groups and notes, correct tester links, audit labels and recover missing match rows.
  *Use for:* AncestryDNA match investigation, Pro Tools Enhanced Shared Matches, colored dots,
  linked trees, ThruLines, access-dependent gaps or connecting a match to another testing site.
  *Core guardrail:* preserve dated access and pair-specific observations; shared matches are
  clues rather than segment triangulation, and tree paths need documentary verification.

- **`recipes/myheritage-dna-match-investigation.md`** — Nine practical MyHeritage DNA workflows:
  select the right kit, preserve theories before reassignment, build filtered shortlists, use
  labels and notes, capture pair-specific shared-match values, compare triangulation subsets,
  audit theory connections, recover private-tree leads, contact matches and resume dated packets.
  *Use for:* MyHeritage DNA match investigation, kit relinking, largest-segment sorting,
  labels/favorites, Shared DNA Matches, Theory of Family Relativity or an investigation follow-up.
  *Core guardrail:* keep kit identity, access, filter state, pair-specific values and exact
  comparison sets explicit; an unshown measurement is not zero, and a theory is a path to review.

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

- **`recipes/beider-given-name-variants.md`** — Expanding documentary searches with recorded
  Ashkenazi given-name forms from the male and female J-Roots Beider indexes.
  *Use for:* an unfamiliar or approximate Cyrillic given name, compound names, alternate
  spellings, ambiguous article labels, or documenting a DNA match's family under another name form.
  *Core guardrail:* query offline with `scripts/lookup_beider_name.py --name` for up to 20
  article groups by default, including similar candidates when an exact match exists; then
  retrieve a selected article's recorded variants with `--key`. Comparison ignores spaces
  and supported hyphens/dashes; keep compound component searches separate. Distinguish
  unavailable local data from an absent entry. Approximate matches are spelling suggestions,
  not source-backed synonyms; article membership never proves identity or kinship.

- **`recipes/myheritage-historical-record-search.md`** — Recovering MyHeritage historical
  records hidden by collection coverage, query fields, name variants, languages or OCR.
  *Use for:* no-result searches, Collection Catalog, relative pivots, historical jurisdictions,
  newspaper keywords/OldNews or an index that must lead onward to an original record.
  *Core guardrail:* diagnose coverage and field meaning before tightening; change one constraint
  at a time, preserve original text, and treat structured or translated values as search leads.

- **`recipes/newspapers-com-search-recovery.md`** — Recovering newspaper notices when issue
  coverage, printed names or OCR hide an ancestor on Newspapers.com. Search initials, married
  names, associates, occupations and addresses; follow travel, social and legal notices across
  relevant newspapers, then verify the original notice.
  *Use for:* a failed newspaper name search, an unknown maiden name, a missing obituary,
  immigration or family-reconstruction leads, incomplete issue coverage, or unreadable OCR.
  *Core guardrail:* a page-level hit can join different notices; verify each person, relationship,
  event date and place in its actual notice. A failed query is not evidence that an event never
  happened, and a second index of the same newspaper image is not independent corroboration.

- **`recipes/hebrewbooks-search-recovery.md`** — Recover HebrewBooks names or passages
  missed by OCR, catalogue spelling or a query that never reached search.
  *Use for:* Hebrew OCR letter confusions, catalogue versus full-text searches, short
  mobile queries, inaccessible routes, Shafeh title searches, given-name indexes and
  viewer versus printed page numbers.
  *Core guardrail:* distinguish an unsubmitted query or access error from a completed
  search with no hits. Keep OCR test strings separate from historical names, and record
  the book ID, viewer page, printed locator and edition separately.

- **`recipes/ancestry-record-search-recovery.md`** — Recovering archival records missed by an
  Ancestry search. Diagnose scope and coverage before relaxing dates, places or names; use
  collection descriptions, original book indexes, census districts and the holding archive.
  *Use for:* an attached census disappearing from results, narrow Card Catalog matches,
  birthplace/residence confusion, conservative wildcard batches, name-free searches, book
  page versus image numbers, enumeration-district browsing, or index-only records.
  *Core guardrail:* search results generate candidates; a zero-result query does not prove
  absence, and the original document must support identity before filing a relationship.

- **`recipes/23andme-match-research.md`** — Twelve practical workflows for 23andMe
  match research, permitted comparisons, numerical matrices and dated preservation.
  *Use for:* match worksheets, connection permissions, selected-segment painting,
  parent-side information, ancestry confidence/history, legacy bucketing,
  reconstructed ancestors, extension exports/groups, manual shared-match charts,
  or floating research-tree branches.
  *Core guardrail:* verify actual access and quantity scope; keep shared-list
  membership, matching intervals, ancestry estimates and documentary identity separate.

- **`recipes/ftdna-practical-dna-workflows.md`** — Four FTDNA workflows for paired
  match/segment exports, duplicate-name joins, MyHeritage tree links and Family Matching.
  *Use for:* Family Finder CSV scope, opaque note handles, selected-match segment files,
  transferred links that need confirmation, and dated parental-bucket inventories.
  *Core guardrail:* reconcile export scope before joining; hold out ambiguous names;
  confirm each tree link and preserve observed vendor assignments separately from pedigree proof.

- **`recipes/dnapainter-practical-dna-workflows.md`** — Six practical DNA Painter operations:
  paint measured matches, copy or merge maps of one tester, intersect phased inheritance,
  calculate provisional missing intervals, combine coordinate spans and plan descendant tests.
  *Use for:* Paint a new match, map duplication/CSV transfers, Common Segment Generator,
  Inferred Segments Generator, Distinct Segment Generator or Coverage Estimator.
  *Core guardrail:* verify the people, chromosome copy and genome build; keep measured
  comparisons, inferred intervals, coordinate unions and pedigree estimates distinguishable.

## What a recipe is (and isn't)

- **Fact-checked.** Each recipe separates independently verified claims from figures reported by a
  cited source but not independently verified. Honor that line — don't present a source-reported
  transcript figure (a specific cM number, a percentage) as a rule.
- **Judgment, not fundamentals.** Recipes carry the non-obvious judgment an unaided answer gets
  wrong, not the well-documented basics you already produce reliably.
- **Platform procedures are dated.** Playbooks pair concrete actions with source-linked records.
  Verify available controls for the selected kit/account and preserve the actual observation scope.

## Attribution

These recipes are original Kinprove-authored distillations, licensed FSL-1.1-MIT (see `LICENSE`).
Third-party facts and methods are credited in each recipe's `recipes/<slug>.sources.md`; any
reproduced third-party data is carved out in `NOTICE`.
