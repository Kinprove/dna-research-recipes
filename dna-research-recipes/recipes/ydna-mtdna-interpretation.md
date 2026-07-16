# Recipe: Interpreting Y-DNA and mtDNA — what a haplogroup or STR/sequence match can (and can't) establish

## Goal

Given a Y-DNA or mtDNA result — a **haplogroup assignment**, a **Y-STR genetic-distance match**, or an **mtDNA sequence match** — state what it can genuinely establish about a *genealogical-timeframe* relationship (roughly the last ~500 years, the paper-trail era), and refuse the three places where confident interpretation crosses into fabrication.

## The mental model (get this right or everything downstream breaks)

A haplogroup or a genetic-distance number is a **position on a deep phylogenetic tree, not a relationship estimate.** An LLM recites the inheritance rules and the resolution ladder fluently, then **fabricates a point answer** — a haplogroup, a "generations back" figure, or an NPE verdict — because plausible-sounding phylogenetics is exactly what next-token prediction is good at emitting and bad at being right about.

The anchor case: a tester uploaded their mtDNA to ChatGPT and was **confidently told it was haplogroup A2ex, and that this was also the Anzick-1 haplogroup.** Both wrong. Anzick-1 is **D4h3a** (undisputed — the debunker is a co-author of the reference *Mitotree* phylogeny); D4h3a and A2ex don't share a common ancestor for **~66,000 years** (back at haplogroup L3). The AI ran four pages of authoritative-looking, entirely fabricated detail (it even invented that "ex" means "excluding"). The tester believed it *because* it read fluently. The underlying point, as Roberta Estes has argued: an AI has no capacity to understand the topology or the nuances of a phylogenetic tree — it can only echo back what others have already said about it, whether those statements happen to be right or wrong. (Estes, DNAeXplained, 2026-06)

So: **you do not compute or assign haplogroups, TMRCAs, or NPE verdicts from your own reasoning.** Every such value is a *hypothesis to route to the right tool or corroborate* — never a fact to state. Route haplogroup/tree questions to **FTDNA Discover** (the free, authoritative Y-DNA tree + Mitotree reference), genetic-distance timing to the **FTDNA TiP report / Match Time Tree**, and treat their output as a **range with a confidence band**, never a point.

## Rules of thumb — the resolution → timeframe map (interpretive ceilings, not a tutorial)

What each test level can *bound*, and where confidence collapses:

- **Backbone haplogroup (e.g. R-M269) / a 23andMe or third-party estimate** → resolves **millennia**, not generations: a high-level assignment's MRCA sits **thousands of years back** (R-M269's own TMRCA is ~6,000+ ybp; a 23andMe-level estimate points ~2,000–5,000 years back). Genealogically **inert**: it cannot place a paper-trail-era ancestor, and it is *not* an ethnicity (R1b is common in Europe but not all Europeans are R1b, nor all R1b European). A haplogroup captures one *shrinking* slice of ancestry (½ of one grandparent, ¼, ⅛ …), never "your heritage." (Family History Fanatics, 2026-05; GeneaVlogger, 2026-04)
- **Y-STR panels — Y-37 and Y-111 today** (FTDNA retired Y-25/Y-67 for *new* orders in 2019; legacy Y-67 results, matches, and TiP reports still display, and prior testers can still upgrade to Y-67) → give **matches + a genetic distance (GD)**, mapped by the TiP report to a **time range that widens at lower marker counts**. A GD is *stochastic*, not a clock (below).
- **Terminal SNP via Big Y-700** (~23 million Y positions; tests STRs *and* SNPs — SNPs define the branch, STRs do the matching) → resolves the **most recent, genealogically-relevant branch**; Match Time Tree dates it. This is where "recent surname connection vs deep coincidence" is actually decided. (DNAeXplained, 2026-04; FTDNA, 2026-05)
- **mtDNA HVR1/HVR2** → a match here means a shared maternal ancestor **thousands of years ago**; useless for recent or geographic conclusions. **Full sequence (all 16,569 positions)** is the refined test — but even a full-sequence match is **still not proof of a genealogical-timeframe or geographic relationship** (mtDNA mutates slowly; fewer testers; wide matching ranges). (GeneaVlogger, 2025-09; DNAeXplained, 2026-04)
- **STR vs SNP**: SNPs are stable, long-term branch definers; **STRs mutate faster and can back-/parallel-mutate**, so STR results "change over time" and are *weaker* evidence than a shared SNP. (FTDNA, 2026-05)

## What to trust vs never fabricate (the three failure modes)

### 1 — NEVER emit a Y-STR genetic-distance → generations/TMRCA point estimate

Do **not** say "GD 2 at Y-67 ≈ 5 generations." A GD is a count of differing markers (GD 5 at Y-111 = 5 of 111 differ, 106 match), and **STR mutation is random, marker-specific, and roughly ~1 per 5 transmissions** — a rule-of-thumb, *not* a constant. So the *same* GD 5 can mean five separate mutations across five generations (a recent shared ancestor — second-great-grandparents) **or** slow accumulation across many more; and a line can go generations with **zero** new mutations. (GeneaVlogger, 2026-06/2026-05)

The honest output is a **resolution-dependent probability distribution**, which is exactly what FTDNA's **TiP report** (Y-37/Y-111, plus legacy Y-67) and **Match Time Tree** (Big Y-700) produce. Concrete shape: a real TiP estimate of "common ancestor born **1500–1850**" contained the documented truth (**1798**) inside the range; the vendor's single "1650"-type figure is just *the mean of a wide band*, not an answer. (FTDNA, 2026-03; GeneaVlogger, 2026-06)

- **Trust / route:** the TiP report or Match Time Tree, quoted **as a range that widens at lower marker counts**. Recommend upgrading Y-37→Y-111→Big Y-700 to *narrow* it.
- **Never:** a self-computed point estimate, or treating the vendor's midpoint as the relationship.

### 2 — NEVER read an exact match at low resolution as "recent"

A **GD-0 at Y-37**, or an **HVR1/HVR2 mtDNA match**, is frequently a **ceiling artifact**: the panel has run out of resolution, so "identical" only means "indistinguishable *at this level*," and the shared ancestor can be **deep-time**. An exact Y-37 match can sit thousands of years back; the same pair often shows real genetic distance once tested at Y-111 or Big Y-700. Think of each level as a **window**: Y-37 is a small pane (wide, blurry timeframe); Big Y-700 is a bay window (a much tighter view). Upgrading routinely makes **distant, irrelevant "matches" disappear** as the allowed-difference thresholds tighten — in one real Schultz project, 37-marker matches (closest still 3 steps away) vanished entirely at 67 and 111. (Your DNA Guide, 2025-10; GeneaVlogger, 2026-04; Family Locket, 2024-01)

- **Trust:** "exact at low resolution ⇒ *unresolved*, could be recent or ancient — upgrade to find out." For mtDNA, only the **full sequence** is worth interpreting, and even then not for recent/geographic claims. A Romanian mtDNA peak that also lights up Hungary may just be a **sibling line** — "not really much you can tell with that." (GeneaVlogger, 2025-09)
- **Never:** "you match exactly, so you're closely related," or an mtDNA HVR/region match as evidence of a specific place or recent maternal ancestor.

### 3 — NEVER assert a non-paternity event (NPE) from a haplogroup contradiction or absent surname-matches

A haplogroup/terminal-SNP that **contradicts** the documented paternal line, or an **absence of surname-matching Y-testers**, is a **FLAG that needs corroboration — never PROOF of an NPE.** *(This is the Y/mt-specific instantiation of flag-vs-proof; it is not the general proof-standard lesson.)* Competing explanations that produce the identical signal:

- **Relevant descendants simply never Y-tested.** So few men Y-test that you can have many autosomal-confirmed same-surname cousins and *still* no Y-match — the host knows (via autosomal DNA, conclusively) he descends from Goldbergs, yet **not one Goldberg cousin has Y-tested**, so his own Y-haplogroup looks "disconnected." Absence of a co-tester is also just a **"haplogroup in waiting"** — a private variant needs a *second* tester before it forms a branch. (GeneaVlogger, 2026-05; DNAeXplained, 2026-04)
- **A sequencing / read-interpretation error, or a newly-defined SNP** re-shuffling the assignment. (GeneaVlogger, 2026-05)
- **Same-name-different-man, a stepparent/illegitimacy on a *different* generation than assumed, or a surname that predates hereditary surnames.** The Woodall project split one presumed family into **four** groups: one carried the surname via his *mother* (illegitimacy), one had a Native American paternal line, and two descended from different 1600s sons with different haplogroups — "we don't know if it was misattributed paternity, a stepparent situation, or two different men with the same name." (Legacy Tree, 2026-01)

Base rate cuts **both** ways: a commonly-cited **~5% per generation** misattributed-paternity estimate (a rule-of-thumb; formal studies usually land lower, ~1–2%) means a *deep* paper trail almost certainly contains a break **somewhere** — so a contradiction is *plausible* — but that same statistic **cannot tell you which generation**, so it never localizes the event. (Legacy Tree, 2026-01)

- **Stronger corroboration (upgrades a flag toward a finding):** (a) a **known male relative who Y-tested and does *not* match you** — a genuine red flag; (b) the non-surname match also being a **close autosomal (Family Finder) match** ⇒ recent connection, investigate; (c) **Big Y** to date *when* the branch/surname split occurred; (d) testing additional documented direct-line descendants to confirm or eliminate. (Your DNA Guide, 2025-10; GeneaVlogger, 2026-05)
- **Never:** "your haplogroup doesn't match your surname line, so there was an NPE," or "no one with your surname matches, therefore NPE."

## Prompt-craft (how to keep an assistant honest here)

1. **Assign nothing; route it.** For any haplogroup/tree question, output "check FTDNA Discover / Mitotree" — do **not** name a haplogroup or its meaning from memory. (The Anzick failure is precisely a from-memory assignment.)
2. **Demand the range, ban the point.** When asked "how many generations is GD *n*?", answer with the resolution-dependent *range* from the TiP report / Match Time Tree, state the marker level, and say the band **widens at fewer markers** — never a single number.
3. **Name the resolution ceiling before interpreting a match.** First establish the Y-STR level (Y-37, Y-111, or legacy Y-67) vs Big Y-700, or mtDNA HVR vs full-sequence — the same match means different things per level; interpreting without the level invites the exact-match-is-recent fabrication.
4. **Force the alternative-explanations list before any NPE language.** If a contradiction/absence appears, enumerate untested-descendants, sequencing error, same-name, wrong-generation, pre-surname — *then* ask what corroboration exists. Use "flag / needs corroboration," never "proves."
5. **Separate the STR-surname question from the SNP-branch question.** Surname clustering (STR projects) answers "who might share a recent paternal line"; terminal SNP / Big Y answers "how recent." Don't let one stand in for the other.
6. **Every output is a hypothesis to verify** against the actual vendor tools, autosomal DNA, and documents — the shared spine with `ai-for-dna-research.md`.

## Pitfalls worth internalizing (least-obvious, most-LLM-usable)

- **Fluency ≠ correctness on phylogeny.** An LLM will emit a clean, wrong haplogroup story (Anzick/A2ex) and *argue* when corrected. Professional-looking output invites unwarranted confidence — that's the danger, not a tell.
- **Surname timing traps.** "Different surname ⇒ NPE" ignores that hereditary surnames were adopted late and unevenly — as recently as the **1930s** in some regions; Dutch not standardized until **1811**; Normandy by the 14th c. (the 1539 Ordinance of Villers-Cotterêts then required priests to record surnames in parish registers — it fixed name *recording*, it did not mandate hereditary surnames). A shared paternal ancestor may simply predate surnames, or a surname was government-assigned for taxation/conscription. Compare the estimated MRCA date to *when surnames were adopted in that region* before reading a mismatch as an event. (FTDNA, 2026-03/2026-05; GeneaVlogger, 2025-09/2025-12; DNAeXplained, 2026-05)
- **Third-party autosomal-derived haplogroups aren't Y/mt tests.** A haplogroup inferred from autosomal raw data is high-level and can be **thousands of years off** the tester's true paternal-line MRCA — don't treat it as equivalent to an actual Y-DNA/mtDNA result. (GeneaVlogger, 2025-09/2026-04)
- **Phylogenetic trees and migration maps are tester-dependent.** Branch definitions and dates differ between platforms, and geography tools (e.g. Globetrekker) mislead when few relevant men have tested — "additional testers could substantially change the inferred geography." Never present the current tree as fixed truth. (GeneaVlogger, 2026-05; DNAeXplained, 2026-05)
- **mtDNA is a weak genealogical instrument by design** — slow mutation, fewer testers, wide match ranges. Great for *eliminating* a direct-maternal-line hypothesis, poor for *pinning* a relationship.

## Corroboration & cross-check discipline (Y/mt never stands alone)

- **Pair every Y/mt result with autosomal + documents.** Y-DNA/mtDNA prove *a* direct paternal/maternal line and a rough timeframe; autosomal DNA and the paper trail localize *which* ancestor and *when*. A Big-Y or mtDNA finding that isn't reconciled with autosomal matches and records is an untested hypothesis. (GeneaVlogger, 2026-05; Legacy Tree, 2026-06)
- **Hypothesis-test by targeted testing.** To confirm/eliminate an unknown direct-line ancestor, test **known direct-line descendants of candidate families** (paternal → Y; maternal → mtDNA) — a purpose-built corroboration, not a database-luck wait. (Legacy Tree, 2026-06)
- **FTDNA is the only consumer company giving Y-DNA/mtDNA *matches*** (23andMe gives high-level haplogroups, no matching); the **Million Mito Project** sharpened mtDNA dating enough to place some subclade MRCAs in a genealogical window (e.g. K1a9b1 ~early 1600s) — so *some* mtDNA questions are now tractable, but only at full-sequence and only with corroboration. (GeneaVlogger, 2026-04)
