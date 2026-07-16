# Recipe: X-DNA and Visual/Parental Phasing — where confident-sounding analysis silently goes wrong

## Goal

Given a small DNA segment, an X-DNA match, or a chromosome map from visual/parental phasing, state precisely what it can confirm or eliminate about a relationship — and refuse the five places confident-sounding analysis is actually fabrication.

## The mental model (get this right or everything downstream breaks)

X-DNA's restricted inheritance (no male-to-male transmission) is a genuinely powerful **hard constraint** — it can definitively rule a path *out*. But it is a far weaker **confirmation** tool than a model assumes: low SNP density inflates false-match risk, the field has no single agreed cM floor, and being *consistent* with the inheritance rule is not the same as being *caused by* the hypothesized ancestor. Visual phasing is a genuinely powerful data-reduction tool bound by one hard mechanical rule almost no model knows to check. And underneath both sits the small-segment problem: real, *divergent*, company-specific false-positive data that a model will confidently paper over with one clean invented number instead of reporting the actual spread. The unifying failure isn't ignorance of the 101 mechanics — models recite those fluently — it's that fluency gets substituted for the messier, disputed, source-specific reality underneath.

## What to trust vs never fabricate (five failure modes)

### 1 — Small-segment false-positive rates: cite the real, divergent numbers — never invent a round one

There is **no universal definition of "small segment"** — Bettinger's own analysis explicitly notes people mean anything from ≤5 cM to <10 cM, and states 8 cM as *his* working cutoff for the piece while flagging segments up to 10 cM as still problematic. A model asserting one fixed threshold as *the* definition is already fabricating false precision.

The real, company-specific figures — genuinely different methodologies, not one curve:

- **23andMe** (peer-reviewed, 2014, trio-concordance against tested parents): ~70% false at 2 cM, ~15% false at 6 cM.
- **AncestryDNA** (matching white paper, 2020, same trio-concordance method): 50% false at 6 cM, ~30% at 7 cM, ~15% at 10 cM.
- **FamilyTreeDNA** ("Family Finder Matching 5.0" white paper, simulated-pedigree ground truth, not trio data): ~20% false positive rate at 6 cM, which is why FTDNA settled on 6 cM as its reporting floor while explicitly acknowledging many 6–7 cM segments are still false.
- **Anecdotal replications**: Bettinger's own 2017 parent-comparison found 32% of 16,193 AncestryDNA matches unshared with either parent (60% of those <7 cM, 95% <10 cM); Debbie Kennett independently found 36% on the same kind of comparison.

A separate, related but **distinct** statistic shows up in FTDNA's own "Tie-Breaker" class: 6 cM carries "about a 20% chance of matching by chance, and even a 9–10 cM overlap can still have about a 2–3% chance of being random for a fifth-cousin-type match." This is presented as a *theoretical* random-match probability, not the *empirical* false-positive rate above — the two numbers land in a similar ballpark at 6 cM but measure different things (ground-truth trio/simulation concordance vs. population-genetics chance-of-IBS). Don't collapse them into one number as if they're interchangeable.

**None of the following rescues a small segment**, per Bettinger's explicit debunking — and a model asked "does X make this small segment more trustworthy?" should say no to all four:

- **Triangulation** — no evidence it raises validity; a triangulation group can itself be built from close relatives who form one leg, not independent legs, or from segments that are simply old and shared community-wide.
- **An overlapping large segment held by a relative** — this only means the *relative's* segment is real; it says nothing about your own smaller one.
- **SNP density within the small segment** — conceptually plausible, no evidence supports it.
- **Finding a shared ancestor with the match** — sharing recent ancestry and sharing a specific segment are not the same fact; with thousands of sub-10 cM matches, you will *always* be able to find some shared ancestor with almost anyone in a large database — that is not evidence the specific segment came from them, and even a *valid* 7 cM segment can be 10–20 generations old, i.e. genealogically inert either way.

The one genuine exception: a small segment at the **very end of a chromosome** (a recombination hotspot) in a **very close relative comparison** (e.g. grandparent–grandchild, directly or via visual phasing) is much likelier to be real — these small end-segments don't form in the chromosome interior.

**Related but distinct mechanism — pileup regions.** A population-shared or human-wide region (often near an immune-system or smell-related gene) produces widespread false-positive matches regardless of segment size; FTDNA's own worked example discarded part of a **42.3 cM** paternal-group overlap because it substantially coincided with a known pileup region. Segment *size* alone doesn't clear this — check against a known pileup map (e.g. DNA Painter's) before trusting even a large overlap in an endogamous context.

### 2 — Phasing yourself does not rescue an unphased match's false positive

Phasing (via a tested parent, SideView-style match alignment, or population-genetics phasing) reduces — but, per Bettinger's own source, does **not** eliminate — pseudosegments **on your own side**: "while phasing is likely to eliminate many or most false small segments, it cannot eliminate all false matches." And even a phase that fully resolved your own side does nothing for the match's side. Bettinger states this directly: "while I may have a valid small segment as a result of phasing… my match may only share this DNA because it is a pseudosegment for them." A model that reasons "I tested a parent / phased myself, so any small segment I still match on is now trustworthy" is fabricating a guarantee the mechanism doesn't provide, on **either** side of the comparison.

This generalizes cleanly to X-DNA, where pseudosegment risk is a **joint, pairwise property of both people's sex** — not something either side fixes alone:

- **Male–male X comparisons** are lowest risk: a male's single X, non-recombining with the Y, cannot itself form a pseudosegment on either side.
- **Male–female** comparisons carry the female side's pseudosegment risk (her two X copies, usually unphased) but not the male's.
- **Female–female** comparisons carry the *highest* risk — both sides can weave between unphased maternal/paternal X copies.

So "is this X match trustworthy" depends on *whose* X chromosomes are being compared, not on whether you personally phased.

### 3 — The mechanical visual-phasing rule most models don't know

In visual phasing (comparing 3+ siblings' recombination points to assign chromosome segments to grandparents), there is a hard structural rule: **a full-match segment (green) can never directly border a no-match segment (red), and vice versa.** Every green or red segment must be flanked by a half-match (yellow) segment on both sides, except at the absolute start or end of the chromosome — because a transition from "both chromosomes match" to "neither matches" without an intermediate "one matches" state is genetically impossible. A model validating or auto-completing a phasing chart that ignores this rule will produce an internally impossible map. A related mechanical gotcha from the same source: downloading "half-match" segments already **includes** all full-match segments (every full match is by definition also a half match) — they're not two disjoint sets to sum.

**Illustrative payoff**, from a worked case using three siblings plus an aunt and a grandmother: whole chromosomes (15, 21, 22 in that case) were assigned *exclusively* to a single paternal grandparent — this is the level of resolution the technique is actually capable of when done right.

**A terminology trap to flag separately**: "phasing" a kit against a *mother's* kit (e.g. GEDmatch's Phasing tool, which produces a binary maternal/paternal composite from a child+parent pair) is a **different** mechanism from both sibling-based visual phasing and from Lazarus reconstruction (which rebuilds a *deceased ancestor's* genome from multiple tested descendants/relatives, not a parent-child binary split). None of these three assigns segments to all four distinct grandparents on its own — only sibling-based visual phasing does that. As one practitioner put it directly: "you don't really use the mother with visual phasing" — because every sibling's corresponding chromosome copy from the mother is, by definition, entirely accounted for by her kit, so comparing to her adds no discriminating recombination-point information the way a third sibling does. A model asked to "phase" a case should first establish which of these two different techniques is actually available (parent-child vs. 3+ siblings, optionally + an aunt/uncle/grandparent to fill gaps) before promising either binary-parent isolation or four-grandparent assignment.

### 4 — Misapplied X-DNA elimination logic on a real discriminating case: half-sister vs. aunt

The clean case first, to calibrate: a father–daughter X-DNA comparison should be **all** (100%, since a daughter gets her father's one X intact) or, for a son, **nothing** (0%, since a son gets a Y). Anything in between rules that man out as the biological father — this is airtight *as a transmission rule*, because male X inheritance is a hard, undivided pass-through: no mechanism transmits X from father to son, full stop. But a *reported* nonzero X match on a son isn't automatically the same claim: the source itself flags one confound specific to the son case — if the candidate father and the child's mother are themselves related (the source's example: third or fourth cousins, or closer), the father can share a real X segment with a son *via the mother's line*, without that meaning paternal transmission occurred, since 100% of the son's X came from her. That doesn't weaken the underlying rule (a father still transmits zero X to a son, unconditionally) — it means a small nonzero X "match" on a son should be checked against parental relatedness before being read as disproof. The daughter case has no equivalent caveat: she inherits the father's whole X regardless of who else he's related to. Shared surnames among X matches do not substitute for this test, and it must be paired with checking all 22 autosomal chromosomes (a real father should share roughly half the child's autosomal DNA on every one).

Now the case where the same instinct **fails**: distinguishing a half-sister from an aunt when total shared cM sits in the fully-overlapping 1600–2000 cM band. Paternal half-sisters *do* have a clean, definitive X-DNA test — they always share a full X chromosome, because their father passes his single intact X to every daughter. But that rule is specific to the **paternal** case. In a real documented case where the relationship in question was **maternal** (a much-younger presumed aunt who might actually be a maternal half-sister), the analyst found "the difference is less clear" — because a mother's X recombines before she passes it on, so an aunt sharing the same mother and a maternal half-sister sharing that mother can both show substantial, non-clean-binary X overlap. A model that recites "paternal half-sisters always share a full X, therefore X-DNA resolves half-sister-vs-aunt" and applies it without first checking *which parent* is the one shared will give a false-confident wrong answer on exactly this kind of case.

What actually discriminates the maternal case, absent a clean X answer:

- **"Not in common" matches**: a half-sibling has large (>200 cM) matches from their *other* parent that the aunt/niece does not share; an aunt's matches should nearly all be shared with the niece (same shared ancestors), aside from the aunt's own generation. GEDmatch's "Match Both or 1 of 2" tool surfaces this directly.
- **Niece-vs-aunt segment-size asymmetry**: nieces show *consistently smaller* matches to the same ancestral lines than aunts do (one extra generation of recombination dilution); half-siblings instead vary *randomly* around similar amounts — consistent-smaller vs. random-variation is the actual signal, not the raw total cM.
- **Known confounds that break the "not in common" method**: endogamy or related parents inflate shared matches on both sides; a sparsely-tested population (the cited example: German, Chinese, French ancestry) removes the comparison matches entirely, in which case ethnicity-estimate differences become the fallback signal instead.
- Note also: ~10% of third cousins won't share enough DNA to register as a match at all (recombination), so an *absent* expected match on one side isn't automatically informative either.

**A second, related trap**: an X-DNA overlap that is *mechanically consistent* with the hypothesized inheritance path (doesn't violate the male-blocker rule) is **not proof** it came from that path. FTDNA's own tutorial flags exactly this: an X overlap that fits the inheritance pattern but traces to an apparently unrelated tree branch may signal either a linking mistake or a genuine *second* true relationship (common in endogamous or Ashkenazi-Jewish contexts) — the elimination logic is airtight as a **veto** (violates the rule → impossible), but its absence is not itself **confirmation**.

### 5 — The X-DNA cM threshold: real, sourced disagreement — never state one confident number

Even within the same company's own materials, the cited "minimum reliable X cM" varies by a factor of ~4 depending on *purpose*:

- **10 cM on a single segment** — FamilyTreeDNA's own display/matching floor (a match won't even show below this, and only ever alongside a qualifying autosomal match).
- **A ~2× SNP-density-equivalence factor** — the same FTDNA presentation states a 15 cM X segment is "approximately equivalent in relevance" to a 7.5 cM autosomal one, because the X has lower SNP density per cM; other sources describe the same lower-density relationship with a slightly different pairing (e.g. "10–15 cM X ≈ roughly 7 cM autosomal"). The exact ratio isn't pinned down across sources — only its direction (X needs materially more cM than autosomal for equivalent confidence) is consistent.
- **15–20 cM as a safer interpretive floor**, per Family Locket — but scaled *up* to 20–30 cM specifically for **female-to-female** comparisons (highest pseudosegment risk), and treated as lower-risk even below that floor for male-to-male pairs (no pseudosegment mechanism possible at all).
- **40 cM instead of 20 cM** — a separate FTDNA tutorial's rule of thumb for chromosome-browser visualization work: "double" whatever autosomal cutoff you'd otherwise use.

None of these is *the* answer; they answer different questions (can it display at all vs. is it safe to interpret vs. is it visually trustworthy), and the safe answer shifts again depending on whether the pair being compared is male–male, male–female, or female–female. A model asked "what's the minimum cM for a trustworthy X match" should surface this spread and ask which of the four questions is actually being asked — not pick one number and state it as settled practice.

## Prompt-craft (how to keep an assistant honest here)

1. **Ban invented small-segment statistics.** Any false-positive-rate or chance-match number must be attributed to a specific company/study (23andMe 2014, AncestryDNA 2020, FTDNA's Family Finder Matching 5.0) — never a smoothed or averaged figure presented as a universal law.
2. **Force the parent-of-origin question before any half-sister/aunt-style X-DNA claim.** "Paternal half-sisters share a full X" is airtight only when the shared parent actually is the father — demand that be established first, not assumed.
3. **Treat X-DNA-consistent-with-inheritance as a veto only, never as confirmation** — a segment that fits the inheritance path can still be misassigned or come from a second true relationship; demand corroboration (documents, "not in common" analysis, or a paper trail) before calling it proof.
4. **Demand the pair-sex before quoting an X-DNA cM threshold** — male-male, male-female, and female-female carry different pseudosegment risk and therefore different safe floors; a single number without that context is incomplete.
5. **Never claim "I phased myself, so this small/X segment is now trustworthy."** Phasing is a per-person operation; the match's own (possibly unphased) side still determines whether the shared segment is real.
6. **Check the mechanical phasing-rule invariant before accepting a visual-phasing chart**: no full-match segment may directly border a no-match segment. A chart or auto-fill that violates this is wrong, not just uncertain.
7. **Distinguish "phasing" from "visual phasing" by name before promising an output** — a parent-child phase yields a binary maternal/paternal composite for one person; visual phasing (3+ siblings, optionally + an aunt/uncle/grandparent) can assign segments to all four distinct grandparents. Don't promise the second with only the first's inputs.
