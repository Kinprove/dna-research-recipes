## Sources

- Nahum Zitter, *HebrewBooks: first among equals*,
  [Safranim](https://safranim.com/גיליון-ח/ג-נחום-זיטר-מאגר-היברובוקס-ראשון-בין-ש/).
  Circa 2010–2011, incorporating a November 2010 announcement.
  Supports catalogue/full-text separation,
  spelling variation and the historical absence of authority control.
- Mississippi Fred MacDowell, *Searching online in Hebrew with imperfect OCR*,
  [On the Main Line, 2011-09-02](https://onthemainline.blogspot.com/2011/09/searching-online-in-hebrew-with.html).
  Supports the three OCR-confusion examples and external site-search route.
- Ezra Brand, *Guide and Review of Online Resources 2022, Part I*,
  [Seforim Blog, 2022-03-30](https://seforimblog.com/2022/03/guide-and-review-of-online-resources-2022-part-i/).
  Recommends the beta search entry point.
- [Shafeh catalogue form](https://shafeh.org/hb/search) and
  [submitted title query](https://shafeh.org/hb/search?title=%D7%9E%D7%A1%D7%99%D7%9C%D7%AA+%D7%99%D7%A9%D7%A8%D7%99%D7%9D&author=&ocr=&commit=%D7%97%D7%99%D7%A4%D7%95%D7%A9),
  inspected independently twice on 2026-10-03. Both requests returned HTTP 200; the query
  rendered catalogue records. The form submits separate `title`, `author` and `ocr`
  parameters. The footer attributes data to beta.hebrewbooks.org.
- [J-Roots topic 64, “Случайные находки”](https://forum.j-roots.info/viewtopic.php?f=15&t=64).
  A participant corrected surname index order to given-name order.
- [Hebrew Wikisource template documentation](https://he.wikisource.org/wiki/תבנית:היברובוקס-דף),
  last edited 2016-03-08. Distinguishes viewer and printed page numbers.
- HebrewBooks public mobile app, commit `7b2443c23854ef8fa68b3d3d0104bf1ec2dcb428`:
  [search screen](https://github.com/hebrewbooks/mobile_app_public/blob/7b2443c23854ef8fa68b3d3d0104bf1ec2dcb428/lib/screens/search.dart#L205),
  [results widget](https://github.com/hebrewbooks/mobile_app_public/blob/7b2443c23854ef8fa68b3d3d0104bf1ec2dcb428/lib/shared/widgets/book_list.dart#L342),
  [query provider](https://github.com/hebrewbooks/mobile_app_public/blob/7b2443c23854ef8fa68b3d3d0104bf1ec2dcb428/lib/providers/search_query_provider.dart#L28).
  The screen's length guard selects history/empty state; the widget's guard precedes
  `fetchSearchBooks` at line 359; the provider stores the supplied value without trimming.
  [Dart String.length documentation](https://api.dart.dev/dart-core/String/length.html)
  confirms that the measurement is UTF-16 code units.

## Credits

- Kinprove — original distillation and synthesis — FSL-1.1-MIT (kinprove-original)
