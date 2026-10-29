# Protocol: how the pool of sources was built

This file records every search, count and rule of the document-model review. Shared rules: [evidence README](../README.md#method). Searches ran on 2026-10-29. Terms are defined in [frame](frame.md).

## 1. Why grey literature

Garousi 2019, Table 4, answered for document-model: all seven questions get a yes.

| # | Question | Answer for this review |
|---|---|---|
| 1 | Complex, not solvable from formal literature alone? | yes: the rules for nesting, reuse and cycles live in standards and tools (XML, XInclude, DITA, TEI) |
| 2 | Lack of volume or quality of evidence? | yes: no reader study of reuse was found; the corpus studies are from 2002 to 2011 |
| 3 | Context important? | yes: literary encoding, technical documentation and wikis meet different structures |
| 4 | Corroborate research with practice? | yes: the OHCO critique against the standards that kept the tree |
| 5 | Challenge practice with research, or the reverse? | yes: reuse was standardised without a measured effect (position.md) |
| 6 | Would a synthesis serve both communities? | yes |
| 7 | Large practitioner volume? | yes: prose linters and document tools with thousands of stars each (state-of-the-art.md) |

## 2. Questions

The six sub-questions Q1 to Q6 are stated in [frame](frame.md). In short: document models and their recursive rule; text that is not a tree; a unit with two parents; self-reference and cycles; checking by program; the cost of strict models.

## 3. Existing reviews (Garousi Guideline 2)

- Searched first, as strings F7, F13, F25 and the review terms of F26, and by the leads the commissioner named.
- Terms: integrative literature review, systematic literature review, mapping study, meta-analysis, review, with component content management, content strategy, design patterns, overlap, schema languages, automated writing evaluation.
- Found: 11 reviews and taxonomies; 2 read in full (DeRose 2004; Batova 2014 in its abstract and method), 4 by abstract, 5 by title and venue. They are placed in review.md strand 0.

## 4. Formal search

Count sources: the Semantic Scholar bulk search (title and abstract, sorted by citations, no key) and the arXiv API (all fields or abstract). The OpenAlex column was counted afterwards, at 10:11 UTC. Semantic Scholar does not match phrases exactly, so its counts are noisy upper bounds; four strings returned mostly unrelated work and carry no weight (marked noise).

| Id | String as run | Semantic Scholar | arXiv | OpenAlex |
|---|---|---|---|---|
| F1 | `"ordered hierarchy of content objects" \| OHCO` | 41 | not run | 45 |
| F2 | `"overlapping hierarchies" + markup` | 16 | 0 (with F3, as one OR string) | 16 |
| F3 | `"concurrent markup" \| "multihierarchical markup" \| GODDAG \| "overlapping markup"` | 54 | 0 (`ti:"overlapping markup"`) | 82 |
| F4 | `transclusion` | 95 | 1 | 100 |
| F5 | `"content reuse" + documentation` | 16 | 5 | 24 |
| F6 | `"single sourcing" + documentation` | 265 | refused by the service | 393 |
| F7 | `"component content management"` | 39 | not run | 48 |
| F8 | `(DITA + "Darwin Information Typing Architecture") \| (DITA + conref) \| (DITA + map + reuse)` | 61 | not run | 82 |
| F9 | `(DTD \| "XML Schema") + (recursion \| recursive)` | 152 | refused | 133 |
| F10 | `"JSON Schema" + (empirical \| "real-world" \| recursion \| recursive)` | 80 | 16 | 189 |
| F11 | `"composite pattern" \| "composite design pattern"` | 851 (noise) | 96 (noise) | 926 |
| F12 | `"composite pattern" + (software \| "object-oriented" \| design)` | 169 | not run | 178 |
| F13 | `"design patterns" + ("systematic literature review" \| "mapping study")` | 117 | not run | 152 |
| F14 | `(documentation \| specification) + (clones \| duplicates \| duplication) + (reuse \| "clone detection")` | 243 | refused | 452 |
| F15 | `"prose linting" \| "prose linter" \| "documentation linting" \| "documentation linter" \| "style checker" + documentation` | 2 | 0 | 2 |
| F16 | `(linter \| linting) + (documentation \| prose \| writing \| markdown)` | 150 | not run | 316 |
| F17 | `"documentation smells" \| ("documentation" + "style guide" + automated + checking)` | 2 | not run | 6 |
| F18 | `Schematron \| "RELAX NG"` | 210 | not run | 264 |
| F19 | `("XML documents" \| "XML data" \| DTDs) + ("empirical study" \| "statistical analysis" \| "real-world" \| "the XML web")` | 706 | not run | 552 |
| F20 | `"descriptive markup"` | 57 | not run | 63 |
| F21 | `"structured documents" + ("document model" \| "logical structure" \| editing)` | 275 | not run | 251 |
| F22 | `"quality of the XML web" \| ("XML" + "well-formed" + valid + web + study)` | 12 | not run | 14 |
| F23 | `"Writer's Workbench"` | 58 | not run | 58 |
| F24 | `"controlled language" + checker` | 40 | not run | 32 |
| F25 | `"automated writing evaluation" + meta-analysis` | 14 | not run | 25 |
| F26 | `("markup" + overlap + review) \| "Text as Graph" \| TAGML \| LMNL` | 1,531 (noise) | not run | 73 |
| F27 | `(Xanadu \| "Ted Nelson") + hypertext` | 115 | not run | 114 |
| F28 | `"Text Encoding Initiative" + (model \| critique \| hierarchy)` | 140 | not run | 167 |
| F29 | `"documentation reuse"` | 26 | not run | 37 |
| F30 | `(documentation + "near duplicates") \| ("software documentation" + duplicates)` | 33 | not run | 61 |
| F31 | `"technical documentation" + (clones \| "copy and paste" \| duplication)` | 25 | not run | 61 |
| F32 | `("single sourcing" \| "content reuse" \| "modular documentation" \| "structured authoring") + (experiment \| usability \| comprehension \| "user study")` | 19,449 (noise) | not run | 22,870 (noise) |
| F33 | `("XML" \| "markup") + validation + (errors \| "error detection") + (documents \| documentation) + empirical` | 6 | not run | 13 |
| F34 | `"single sourcing" + usability` | 17,791 (noise) | not run | 20,992 (noise) |
| F35 | `"content reuse" + experiment` | 16 | not run | 22 |
| F36 | `"structured authoring" + study` | 321 | not run | 323 |
| A1 | arXiv only: `abs:"recursive schema" OR abs:"recursive schemas"` | | 7 (noise) | 47 |
| A2 | arXiv only: `abs:"docs as code" OR abs:"documentation as code"` | | 161 (noise) | 32 |

- Screened by title: the 15 most cited of F1 to F9, the 12 most cited of F10 to F21, and the 10 most cited of F22 to F33. Then the 8 most cited of F34 to F36, and the first 5 to 8 arXiv hits per string.
- F15, F17 and the arXiv overlap strings returned 0 to 2 results; they were read as wrong queries and followed by rephrased strings (F16; F2, F3 on Semantic Scholar).
- Snowballing, backward: the reference lists of Renear 1996 (giving Barnard 1988, Goldfarb 1981, DeRose 1990), Mlýnková 2006 (Choi 2002, Mignet 2003, Bex 2004) and TEI 2026 chapter 21 (GODDAG, LMNL).
- Forward: Semantic Scholar citations of Coombs 1987 (293) and Sperberg-McQueen 2004 (92); the 12 most cited since 2010 of each were screened. They confirmed Schmidt 2010, Di Iorio 2011 and Haentjens Dekker 2017, and added none.
- Web searches used only to find a readable copy of a formal work are not counted as strings.
- Added by handoff from the two sibling reviews, which ran at the same time: Priestley 2001 and OASIS 2015 sections 2.2.1.6 and B.11 (information-typing), Edge 2024 and Nelson's transclusion (progressive-disclosure). Each was read here before use; Rockley's book on enterprise content was located (an Open Library record) but not opened, so it supports no claim.

## 5. Grey search

- Types and producers, chosen because the rules for nesting, reuse and cycles are set by standards and implemented by tools:
  - standards bodies and their specifications (W3C, OASIS, TEI, WHATWG, the JSON Schema project);
  - reference processors and document tools (DITA-OT, Sphinx, Asciidoctor, MediaWiki, ProseMirror, Pandoc, mdast, CommonMark);
  - company engineering posts (Notion);
  - Q/A sites (below).
- Engine: a general web search engine, all results of the first page or pages shown. Results personalise and change.

| Id | String as run (abridged) | Screened | Included |
|---|---|---|---|
| G1 | DITA 1.3 specification conref circular reference processing rules | 19 | 1 (OASIS 2015; vendor and forum pages not used) |
| G2 | DITA-OT error message conref circular OR references itself | 9 | 1 (DITA-OT 2026b, read directly) |
| G3 | WHATWG HTML outline algorithm removed 2022 pull request, headings, never implemented | 40 | 1 (WHATWG 2022, read on GitHub) |
| G4 | DITA 1.3 copy-to attribute, topic referenced multiple times in a map | 20 | 0 new (OASIS 2015) |
| P | direct visits to named producers: W3C, OASIS, TEI, DocBook, JSON Schema, CommonMark, mdast, Pandoc, Sphinx, Asciidoctor, MediaWiki, ProseMirror, Notion, RELAX NG, Schematron, the publisher of Gamma 1995, Wikipedia, ISO, the GitHub API | 33 | 19 (ISO pages refused automated access) |
| H | by handoff: the OPML 2.0 specification (archived), the Org syntax, the Logseq documentation | 3 | 3 |

### Q/A sites

Strings NM1 to NM13 ran on 2026-10-29, one reviewer, grey tier 2. Other rules: [evidence README](../README.md#method)., reused as is. One change: the search call used the default filter, and the answers of the opened threads were then read with `filter=withbody`.

| Id | String as run | Site | Returned = screened | Included | New |
|---|---|---|---|---|---|
| NM1 | `title=transclusion`; `q=transclusion` | Stack Overflow; Software Engineering, Writing, User Experience | 30; 0, 0, 0 | 0 | 0 |
| NM2 | `q=DITA conref` | Stack Overflow | 12 | 0 | 0 |
| NM3 | `q=single source` | Writing | 30 | 2 | 2 |
| NM4 | `q=documentation reuse` | Software Engineering | 30 | 0 | 0 |
| NM5 | `title=recursive json schema` | Stack Overflow | 4 | 0 | 0 |
| NM6 | `q=overlapping hierarchies xml` | Stack Overflow | 10 | 0 | 0 |
| NM7 | `q=composite pattern tree` | Software Engineering | 20 | 2 | 2 |
| NM8 | `q=DITA` | Writing | 5 | 2 | 2 |
| NM9 | `q=linter` | Writing | 0 | 0 | 0 |
| NM10 | `q=docs as code` | Software Engineering | 30 | 0 | 0 |
| NM11 | `title=xinclude` | Stack Overflow | 30 | 2 | 2 |
| NM12 | `q=reuse content` | Writing | 6 | 1 | 0 |
| NM13 | `title=DRY` | Writing | 7 | 1 | 1 |
| Total | 13 strings, 16 calls | | 214 | 9 (distinct) | 9 |

- Included: 9, scored on the 20 criteria of section 8 with the shared Q/A rules; none below 10.
- Added by handoff from information-typing: SO 2016b and SO 2015b (question 31749306), read with the same API on 2026-10-29 and scored the same way; 11 threads in all.
- Opened and excluded: two Composite threads with low-voted answers, a how-to on recursive JSON Schema, and a Writing thread on topic-based against modular authoring, handed to information-typing.
- NM1 shows a homonym: 28 of the 30 Stack Overflow titles use "transclusion" for content projection in Angular, Vue or Aurelia, 1 for org-mode and 1 for MediaWiki.
- Stopping point: the run ended after NM13, when each field term had been run in one form; NM13 added the last new thread. The API quota is shared by address, so the run was kept short.

## 6. Stopping rule

- Stated before searching: effort bounded, top N per string as in section 4 (15, 12, 10 or 8), with saturation, k = 5 consecutive results that add no new concept.
- Formal: evidence exhaustion for the small sets (F1 to F3, F5, F15, F17, F22, F33); effort bounded for the rest.
- Grey web: all results shown per string; producer visits stopped when every system named in the frame had been read once.
- Q/A: as in the shared protocol, k = 10 within a string; the run stopped after NM13.

## 7. Selection

- Include: a source on how documents are modelled as trees or graphs, how units are reused, how cycles are handled, or how structure is checked by program. English, and readable on the search date.
- Exclude:
  - uses of the words in other fields (geology, chemistry, medicine, user-interface frameworks);
  - query languages, storage and database mapping of XML with no bearing on the document model;
  - vendor pages selling a content management product;
  - sources whose text and abstract could not be reached and whose title does not settle relevance (located only).

## 8. Quality of grey sources (Garousi Guideline 11, Table 7)

- The 20 criteria and the threshold: [evidence README](../README.md#method).
- Outlet tier: books and standards = tier 1 (1); project documentation, specifications of community projects, pull requests, wiki and Q/A pages = tier 2 (0.5); company blogs = tier 3 (0).
- Impact is judged from stars, the size of the user base, or votes and views.
- Threshold: 10 of 20. Below it a source stays only as an **example of practice**; the text that cites it says so.
- A part of a source that was not seen scores 0 on its criteria (Gamma 1995, read only through its table of contents and a secondary page).

## 9. Extraction and synthesis

- Extracted per source: kind, year, the claim, the evidence offered, any number with its location, and whether it was read in full, by abstract or by title.
- Synthesis is narrative, by question Q1 to Q6, and every claim traces to a row of [sources](sources.md).

## 10. Limits

- One first rater for document-model; the second rater's blind sample is reported in the [evidence README](../README.md#method).
- Shared limits: [evidence README](../README.md#method). Here: arXiv refused some calls on the day.
- Several works were reachable only by title and venue: publisher sites refused automated access, and no identity was sent to any service to reach them. Those works carry no number in the text.
- Forward snowballing covered two works; backward snowballing three.
