# Recipe: Using AI reliably in DNA genealogy research

## Goal

How an AI assistant (or a genealogist using one) can apply AI to DNA/genealogy work **reliably** — what to delegate freely, what to never trust, and the prompt patterns that actually work.

## The mental model (get this right or everything downstream breaks)

AI is a **language-prediction system, not a reasoning authority** — it produces *plausible* output, which is not the same as *correct* output, and it has no access to records it hasn't been given (or can't retrieve). Therefore: **every AI output is a hypothesis to verify, never a fact to file.** "AI lies" is the wrong frame — it's non-intentional; it confidently fills gaps. (Denyse Allen, 2026-01)

## What to delegate freely (AI is genuinely good at these)

- **Restructuring** scattered notes / transcriptions into tables, outlines, timelines, drafts.
- **Transcription** of documents — genuinely useful, but accuracy depends on the handwriting, language, script, and image quality (and the model); *correct-and-verify* against the image, never trust a transcription blind. (Denyse Allen)
- **Assembling citations from complete inputs** you supply (see prompt-craft). (Family Locket, 2025-02)
- **Brainstorming research strategy**, historical/legal context, and *draft* proof-argument prose. (Denyse Allen; Family Locket)
- **Surfacing hypotheses** — comparing Ancestry vs 23andMe reference panels, or cross-referencing tree surnames against ethnicity regions, to *raise* patterns and anomalies **to investigate** (not to conclude — see the ethnicity never-trust). (Family Locket, 2026-03)
- **Front-ending mechanical prep** — e.g. turning Ancestry match screenshots into a structured cM/relationship table to start a Leeds chart. (Family Locket, 2025-02)

## What to never trust or delegate (verify, or don't)

- **Record retrieval / existence.** A bare LLM (no verified retrieval/browsing) cannot fetch an actual birth record or confirm a source exists; if pushed, it *invents* one. A tool-enabled assistant that *can* browse may surface a real catalog entry — but treat anything it returns as unverified until you inspect the actual record. Supplying the record makes it genuinely useful, but verify the output against the source even then. (Denyse Allen)
- **Citations from a bare link.** Citation format depends on source-specific fields (author, source type, publication, access) that a URL alone doesn't carry — supply the fields or the citation will be wrong. (Family Locket & Denyse Allen)
- **cM → relationship odds.** Never ask the LLM to compute relationship probabilities from a cM number — it *fabricates* them. Route a *single* cM figure to the **Shared cM Project / DNA Painter's Shared cM Tool** (point cM → the *range* of candidate relationships); if you have a tree plus multiple matches to place, that's **WATO** — a *different* DNA Painter tool that scores hypothesis slots, not a cM→relationship lookup. Either way, always ask for **all** candidate relationships, never a single point answer. (Half vs full relationships are frequently indistinguishable by cM alone.)
- **cM as closeness under endogamy.** Endogamy / pedigree collapse **inflates** shared cM, so the same cM implies a closer relationship than reality — the AI has no idea your lines are endogamous unless you tell it, and even then it can't quantify the correction.
- **Ethnicity estimates as conclusions.** They're probabilistic and re-versioned by vendors; let AI surface *hypotheses* about admixture/migration, never conclude an ancestral origin. (Family Locket, 2026-03)
- **DNA-estimated relationships as fact.** A tool's "estimated relationship" is a cM-based guess and routinely differs from the real one — AI parroting it will mis-group matches. (Family Locket, Leeds video)
- **Final evidentiary judgment.** Proof validation is human work; AI drafts, you rule. (Denyse Allen)
- **Source-type classification without explicit rules.** Ask AI to classify sources as *original / derivative / authored* and it will (a) confuse them with *primary / secondary* (which classify the *information*, a different axis), and (b) invent its own logic — unless you define the rules first. (Family Locket, 2026-03; the framework is Elizabeth Shown Mills methodology, so this is a real, checkable failure mode.)

## Prompt-craft that practitioners found works (the reusable core)

1. **Provide complete inputs, don't expect inference.** Give the citation fields / the transcription / the screenshot — not "here's a link, cite it."
2. **Templates + hard constraints.** "Use these exact template fields; do not alter the structure." Generic requests produced partial/non-matching output; explicit template + "apply *this* template" fixed it. (Family Locket, 2025-02)
3. **Prompt-chaining for complex concepts.** Teach it bottom-up: define the terms first (what *is* original vs derivative vs authored), *then* ask it to classify. (Family Locket, 2026-03)
4. **Define the rules or it invents them.** Any domain logic (source analysis, grouping criteria) must be stated explicitly first.
5. **Manage the context window.** Long chats degrade and hit limits even on paid plans — split into fresh chats and reload the current state rather than one endless thread. (Family Locket, Leeds video)
6. **Specificity drives quality.** The more precise the ask and the format, the better the output.

## Worked mini-examples (workflow logic, not clicks)

- **Leeds chart** — AI builds the match table (names, cM, tentative relationship) from Ancestry screenshots; *you* do the color-coding. The Leeds Method uses matches sharing **90–400 cM** to separate the four grandparent groups. The 400 cM ceiling **excludes most first cousins** (who tie to two grandparents) — but it's not a clean guarantee: first cousins do occasionally fall in the 301–400 cM band, so independently exclude any *known* match who shares two grandparents rather than trusting the cap. The human-judgment step is spotting the **removed first-cousin descendants (1C1R, 1C2R)** that fall *inside* the 90–400 window but connect to two lines and skew the four-way split — **second cousins are the foundation you keep, not exclude.** AI front-ends; human judges. (Leeds Method = Dana Leeds, July 2018; 90–400 cM — *verified*.)
- **DNA source citations** — build reusable templates (who/what/where/when + the match's cM & segment fields) → export CSV → hand to AI with "use these exact fields." Then **check every output** for missing fields. (Family Locket, 2025-02)
- **Painting a GEDmatch match** — AI helps translate GEDmatch one-to-one coordinates into DNA Painter segments; the *judgment* step it can't own is assigning the segment to the **paternal vs maternal** side and the right ancestral couple — get that wrong and the whole chromosome map is corrupted. (Family Locket, 2025-04)

## The pitfalls worth internalizing (the least-obvious, most-LLM-usable part)

- Confidently wrong on dates/names/places, and it may *argue* when corrected.
- Loses track across a long multi-turn session.
- Treats a DNA-estimated relationship as the real one; ignores endogamy inflating cM.
- Conflates *original/derivative/authored* (source type) with *primary/secondary* (information type).
- Fabricates citations/records when it lacks the underlying fields.

## Verification & privacy discipline

- Every AI-produced claim → **verify against the relevant evidence** — prefer *original* records and *primary* information where available, and correlate independent sources — before it enters a tree or report. Use AI to *think faster*, never to *decide*.
- **De-identify before you share data with any third-party tool, not just before publishing.** Strip direct identifiers before pasting a third party's DNA or match list into a cloud AI (or any external tool) — though raw DNA is inherently re-identifiable, so this is *pseudonymization*, not true anonymization. **Get the person's consent before processing their genetic data — make it a default, not a step you weigh** (it's the community norm, and legally required in many places). De-identify living individuals in anything public as well.
