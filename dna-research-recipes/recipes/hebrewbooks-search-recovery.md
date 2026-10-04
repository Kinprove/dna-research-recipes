# Recipe: Recovering HebrewBooks search misses

## Goal

Recover a name or passage hidden by Hebrew OCR, catalogue spelling or a query that
never reached the search service. The useful question is **which layer failed**, before
another spelling is tried or a miss is recorded.

## Mental model

Keep these observations separate; each changes the next useful action.

| Surface | What the observation represents | Next action |
| --- | --- | --- |
| Mobile app history/empty state after a short query | A local query gate in the pinned source | Expand the intended title or name |
| Catalogue title/author result | A candidate work | Identify the edition, then investigate its contents |
| OCR text miss | A spelling or recognition probe that missed | Test the documented one-letter confusions |
| Printed name index | Entries organized by the index's own key | Establish given-name versus surname ordering |
| Viewer page pointer | A location in a particular scan | Read the printed locator and edition |
| HTTP 403 | An inaccessible route | Switch discovery route and retain the intended query |

## Decision procedure

1. **Establish that a search actually ran.** An access error, an unsubmitted query and
   a completed search with zero hits are different observations. Record the surface and
   the observation before interpreting it.
   - In the published HebrewBooks mobile app source at commit `7b2443c`, the search
     screen shows history or an empty state for a raw query shorter than **three UTF-16
     code units**. The results widget also returns before its catalogue request for
     that length. A two-letter query such as `אב` therefore does not produce a catalogue
     miss through that screen. Expand it to the intended full name or title.
   - The app stores the query without trimming it. Spaces and Hebrew combining marks
     contribute to its length; padding is not a meaningful expansion. This finding belongs to the pinned
     app implementation; do not transfer its threshold to the website or API.

2. **Choose the surface that can answer the question.** Use the catalogue to locate a
   work by title or author; use full text to seek a person or passage inside it. A surname
   missing from title/author metadata has not been searched inside the book. For a
   catalogue miss, issue separately recorded plene/defective spellings and attested name
   variants. The catalogue described by Zitter in 2010–2011 lacked authority control:
   search those spellings yourself rather than expecting automatic unification. Preserve
   the spelling that identifies the edition you find.

3. **After the correct Hebrew spelling misses in OCR, try a documented confusion.**
   The 2011 Hebrew-search workaround gives these concrete probes:

   | Intended text | Retrieval probe | Changed letter |
   | --- | --- | --- |
   | `יעקב` | `ימקב` | ע to מ |
   | `תלמיד חכם` | `תלמיד מכם` | ח to מ |
   | A token containing ד or ר | Swap that letter | ד and ר |

   Test one changed letter per probe. The malformed query is a retrieval key:
   **never record `ימקב` as a historical variant of `יעקב` on this basis**.

4. **Change discovery route when the surface has failed.** Run
   `site:hebrewbooks.org <Hebrew phrase>` in an external search engine; include the
   OCR-confused spelling when that is the probe. MacDowell demonstrates exactly this
   combination with `site:hebrewbooks.org ימקב`. Also try `https://beta.hebrewbooks.org/`,
   the enhanced search entry point identified by Brand's 2022 guide.
   **For an inaccessible catalogue, also use the [Shafeh search form](https://shafeh.org/hb/search).**
   It exposes separate title, author and OCR fields. A live title-field query for
   `מסילת ישרים` on 2026-10-03 returned matching record **41768**, alongside partial
   titles such as `מסילת הברזל` and `דובר ישרים`.
   **If a route returns 403, switch to Shafeh or external site-search to collect book
   links or IDs.** Save the intended
   within-book query for when the viewer is accessible.

5. **For a located work, use its printed index when OCR does not find the passage.**
   Read the heading and several entries before choosing the lookup key. A J-Roots
   participant explicitly corrected a supposed surname index to one alphabetized by
   **given name**. Search the given-name section when that is the demonstrated order;
   a surname-only lookup can miss an indexed person.

6. **Keep the hit's coordinates separate.** Record the book ID (`req`), viewer page
   (`pgnum`), printed page or folio visible on the image, and edition from the title page.
   The viewer number is not necessarily the printed number. A link has this shape:
   `https://hebrewbooks.org/pdfpager.aspx?req=<id>&pgnum=<n>`.

## Prompt patterns

- **Recover a miss:** “I searched [surface] for [literal query] and observed [completed
  zero-hit search / no request / access error]. Propose the next surface or one-letter
  OCR probe. Label intended spelling separately from retrieval spelling.”
- **Inspect an index:** “Read this heading and these entries. Identify the demonstrated
  ordering key, then show where [given name and surname] should be sought.”
- **Save a hit:** “Return book ID, viewer page, printed locator and edition separately.
  Transcribe the relevant image text. Leave an unread coordinate unresolved.”

## Failure modes

- Turning an OCR-confused query into a name variant in a genealogy record.
- Reporting a mobile-app short query or an HTTP 403 as a completed zero-hit search.
- Searching a catalogue surname field and claiming that the book's text was searched.
- Assuming that every scanned name index is arranged by surname.
- Inferring current Boolean, fuzzy, wildcard or proximity syntax from historical guides.
- Treating a forum's book ID and ambiguous “page” pointer as an image-verified citation.
