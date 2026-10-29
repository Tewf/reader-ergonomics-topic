# Review

This file reads the literature on storing, reusing and checking a tree of units of writing. Strands run from existing reviews to the seminal models, their critique, reuse, cycles, checking and practice.

Each grey score is in [sources](sources.md), marked as the [evidence README](../README.md#method) says.

## 0. Existing reviews

- Andersen 2015 reviews **component content management** (CCM), writing in small reusable components: how content is defined, which processes and tools are adopted (abstract, through a library page). It treats each component as a genre of granularity, reusability and potentiality.
- Batova 2014 (abstract and method read) reviews CCM and multilingual quality, 60 articles of which 10 peer-reviewed. Sources disagree: consistency gains against loss of context, text segmentation and the load on translators.
- Batova 2017 (roles and skills in CCM) and Clark 2016 (content strategy) are reviews read by title and venue only.
- DeRose 2004 (read) reviews the options for markup **overlap** (CONCUR, segmentation, MECS, milestones) against stated criteria. In Bible texts the book, chapter and verse hierarchy and the story and paragraph hierarchy diverge throughout; a milestone variant became the OSIS norm.
- Marinelli 2008 compares formats for overlapping markup toward a unified one (title and venue only).
- Murata 2005 (abstract) classes schema languages as tree grammars: DTD local, XML Schema single-type, RELAX NG regular, with a validation algorithm for each.
- Zhang 2012 (abstract, secondary) reviews the 23 GoF patterns to 2009: 611 candidates, 10 papers with 11 experiments, no firm support for the claims made for patterns in general, some for maintenance. Ampatzoglou 2013 and Bafandeh Mayvan 2017 map the same field (title and venue). None studies documents.
- Fleckenstein 2023 (abstract) pools automated writing evaluation: 20 studies, k = 84, N = 2,828, g = 0.55 on students' writing, heterogeneity high (secondary).
- How this review differs: none of these joins the stored tree, its reuse and its checking. This one asks it for a recursive topic, compares how standards treat cycles, and scores standards and tools as grey sources.

## 1. Document models that treat text as a tree

- Goldfarb 1981 is cited by Renear 1996 as an early source of the hierarchy view, in generalized markup (title and venue only).
- Coombs 1987 (read, archived copy) sorts markup into six kinds and argues for **descriptive markup**: maintainability, portability, lower cognitive demands, and views such as an outline of section titles. Its claim that documents are naturally hierarchical is argued, not measured.
- DeRose 1990 stated the **OHCO thesis**: text is an ordered hierarchy of content objects (read through Renear 1996).
- Renear 1996 sorts the arguments for it. Pragmatic: such texts are easier to create, modify, print and transfer. Empirical: talk about texts names chapters, stanzas, lines. Theoretical: a text survives a change of layout, not of its objects.
- XML 1.0 (Bray 2008): elements nest properly, every element but the root has one parent, and a content model is a grammar over child types (sections 2.1, 3.2.1). A well-formed instance is a finite tree.
- The recursion sits in the content model, often beside a capped form:
  - DocBook's `section` is recursive with unbounded depth; `sect1` to `sect5` can only be five levels deep (Walsh 2019);
  - TEI's `div` nests recursively; `div1` to `div7` stop at seven, and the two styles must not be mixed (TEI 2026, section 4.1).
- DITA makes the titled topic its recursive unit: topics can be defined inside topics, but nesting needs special care, since it can make documents less usable and less reusable (OASIS 2015, 2.2.1.6). Maps are advised for the links between topics, to keep each topic reusable. Sections cannot nest, and every topic has a title (B.11). Maps and topics are separate document types (SO 2016b, by handoff). How topics are typed belongs to [information-typing](../information-typing/review.md).
- Outline formats store the same recursion. An OPML `outline` may contain zero or more `outline` elements, each with a required text attribute (Winer 2007, by handoff). An Org heading's level is its number of asterisks (Orgmode 2026, by handoff).
- Markdown stores no section node. CommonMark divides blocks into containers and leaves, and a heading is a leaf of level 1 to 6 (CommonMark 2024, sections 3.2, 4.2). The mdast format gives a heading a depth of 1 to 6 (mdast 2026); Pandoc's `Header` holds inlines, `Div` and `BlockQuote` hold blocks (Pandoc 2026).
- HTML specified an outline from nested sectioning elements; WHATWG replaced it in 2022 with one based on heading levels, as user agents had not implemented it for over a decade (WHATWG 2022).
- ProseMirror constrains a node type's children by a content expression such as `block+` (ProseMirror 2026); a Notion block holds an ordered array of child IDs and one parent ID (Notion 2021, the owner's account).
- The **Composite pattern** composes objects into trees of part-whole hierarchies, so a part and a whole are treated alike (Gamma 1995, intent as quoted by Wikipedia 2026d). The book's case study is a document editor (publisher's table of contents); its text was not read.
- Composite trades type safety for uniformity when child operations sit on the shared interface (Wikipedia 2026d); an answer calls it a recursive data type (SESE 2014f). Hoare 1975 was located by title and venue only.

## 2. The critique: text that is not one tree

- Barnard 1988 named overlapping hierarchies in SGML markup of literary texts (title and venue; content through Renear 1996).
- Renear 1996 (read, archived final version of 1993) tests three versions of the thesis:
  - OHCO-1 fails on multiple logical hierarchies, verse lines against sentences;
  - OHCO-2 (each analytical perspective determines a hierarchy) fails on terms such as enjambment that relate objects across perspectives;
  - OHCO-3 (perspectives decompose into hierarchical sub-perspectives) fails on objects that overlap themselves: strike-outs and variants, link anchors and targets, topics, lists broken across paragraphs.
- Its conclusion keeps a weaker claim: perspectives often, not always, determine hierarchies. The practice it reports: flatten all hierarchies but one into milestones, or use SGML's CONCUR, rarely implemented and verbose.
- Huitfeldt 1994 and Buzzetti 2002 extend the critique (title and venue only).
- TEI 2026 chapter 21 gives five methods: redundant encodings, boundary milestones, fragments joined by pointers, stand-off markup, and non-XML models (CONCUR, GODDAG, LMNL); it calls XML's document model strongly hierarchical.
- Data models proposed: GODDAG for overlapping hierarchies (Sperberg-McQueen 2004, title and venue); EARMARK for overlapping and out-of-order markup (Peroni 2009; Di Iorio 2011, title and venue).
- TAG is a directed property hypergraph whose markup nodes point to sets of text nodes; only text is ordered and hierarchy is optional (Haentjens Dekker 2017, abstract read). It claims overlap and discontinuity, not yet simultaneity and transposition.
- Schmidt 2010 (abstract): beyond overlap, embedded markup carries obsolescent and subjective data and hides the text; he separates versions from content, with a data structure in Schmidt 2009 (title and venue).

## 3. One unit, several parents: transclusion and reuse

- Nelson 1965 (read, in a reprint): the Evolutionary List File holds entries, lists and links, and "a given entry may be in any number of lists". Variants are patches pointing to the original; the paper also introduces the word hypertext.
- Nelson 1995 makes transclusion the unifying idea of hypermedia (title and venue). Nelson 1999 (read, author's copy) pairs content links with **transclusion**, visible reuse, over content lists that point into stabilised media, and aims to replace hierarchical directories.
- XML parsed entities reuse by reference inside one document (Bray 2008, section 4), which Coombs 1987 calls referential markup; XInclude merges a resource or fragment at processing time (Marsh 2006).
- DITA is reuse by reference (Priestley 2001, title and venue):
  - `conref` pulls an element in place, `conaction` pushes one, `conkeyref` and keys add indirection (OASIS 2015, section 2.4.2.1);
  - a processor must not resolve a reuse that would be invalid under the rules of either the reused or the reusing content (OASIS 2015);
  - chains of conrefs resolve recursively, pair by pair (OASIS 2010);
  - a map may reference one topic several times; `@copy-to` names one instance so its links and navigation point to a copy (OASIS 2015).
- MediaWiki transcludes templates; Wikidata transclusion that changes article content on English Wikipedia runs at about 5%, against 61% suggested earlier (Johnson 2020, preprint, abstract).
- Sphinx accepts a document under several tables of contents, reports it, and names the one parent it selects, the greatest name (Sphinx 2026).
- Notion once let a block sit in several content arrays; permission inheritance became ambiguous, so a block now has one parent pointer (Notion 2021, the owner's account).
- ProseMirror nodes are immutable values: one node may sit in several structures, or several times in one (ProseMirror 2026).
- Logseq offers both forms of a second parent: a block reference shows one block elsewhere; an embed shows the block with all its descendants, editable in place (Logseq 2023, by handoff). OPML's `include` type points an outline at another OPML file (Winer 2007).
- GoF leaves a Composite child's number of parents open and mentions shared components (SESE 2022c, an answer reading the book; secondary); Calder 1990 shares glyphs as flyweights (title and venue).
- Copies are common where reuse is not enforced (measured, descriptive):
  - Juergens 2010 (read): 28 requirements specifications, 8,667 pages; mean clone coverage 13.6%, from 0% to 71.6%, 6 of 28 above 20%. The mean blow-up of 3,578 words is converted into about 16 minutes of reading and 6 hours of inspection per document, from published rates: an estimate.
  - Luciv 2018 (abstract, secondary): documentation of 19 projects, of every kind, holds exact and near duplicates. Nosál 2016 (read): 6,102 documentation fragments repeated at least four times in the Java 8 sources, one of them 344 times.
  - Inconsistent code clones are reviewed in [file-structure](https://github.com/Tewf/reader-ergonomics/blob/e8864477a53d713251ba42a4cf7b7a0d761243a2/evidence/file-structure/against.md) (Juergens 2009), linked, not repeated.
- Dayton 2010 (abstract, secondary): 1,000 STC members surveyed in 2008-05, 276 answers. Half used single sourcing or content management; about 1 in 10 had seen an implementation fail; half the users reported significant downsides; about 1 in 9 used DITA.
- Batova 2018 (abstract, secondary): over 12 months at one company moving to CCM, writers' motivation fell when CCM meant only efficiency and rose with job crafting.
- Rockley 2002 (information models for single sourcing) and Sapienza 2007 (single sourcing through intertextuality) were read by title and venue only.
- This search found no study that measures readers of reused fragments.

## 4. Self-reference: a recursive type against a cycle

- In every model read, the type may be recursive and the instance is a finite tree: XML (Bray 2008), DocBook (Walsh 2019), TEI (TEI 2026), JSON Schema instances (Wright 2022), ProseMirror (ProseMirror 2026).
- A cycle enters only through a reference, and the systems read meet it in five ways (table in [state of the art](state-of-the-art.md)):
  - forbidden by the grammar: a parsed entity must not refer to itself, directly or indirectly (Bray 2008, section 4.1);
  - fatal when met: an include repeated within its own inclusion chain; two non-nested includes of one resource are not forbidden (Marsh 2006, section 4.2.7);
  - detected and reported: DITA-OT 2026b errors DOTX013E (a conref includes itself), DOTX053E (a map references itself), DOTJ069E (a circular key definition); MediaWiki's template loop warning (MediaWiki 2026b); Sphinx's circular toctree warning (Sphinx 2026);
  - capped: Asciidoctor's `max-include-depth` of 64, to curtail infinite include loops (Asciidoctor 2026); MediaWiki's template depth of 100 since version 1.38, 40 before (MediaWiki 2026a);
  - undefined: a JSON schema must not run into an infinite loop against an instance, and mutually recursive `allOf` references are undefined (Wright 2022, section 9.4.1). The DITA conref pages read do not address cycles (OASIS 2010; OASIS 2015).
- Browsers never shipped XInclude, in part because loops must be detected and that is hard (SO 2011d, citing a Mozilla bug).

## 5. Checking the tree by program

- RELAX NG is an OASIS specification (Clark 2001), and its site gives it as ISO/IEC 19757-2. Schematron checks for the presence or absence of patterns with XPath; its fourth ISO edition appeared in 2025 (Schematron 2026, example only).
- Martens 2006 (abstract): XML Schemas in practice use their extra power over DTDs only to a very limited extent.
- Corpus studies (measured, descriptive):
  - Choi 2002: non-linear recursive elements in 58% of DTDs; Mignet 2003: about 200,000 web documents, 99% under 8 levels, mean depth 4, 15% with recursive elements (both secondary, through Mlýnková 2006).
  - Mlýnková 2006 (read): over 20 GB of real XML. Depths stay under 13 once the 5% extremes are set aside; recursion is mostly linear, with up to 3 recursive element names. Schemas reach depths near 80 when recursion is set aside.
  - Grijzenhout 2011 (abstract): 180,000 web XML files; 85.4% well-formed; 25% refer to a DTD or XSD, and about a third of those validate (secondary). Bex 2004 compared real DTDs and XSDs (title and venue only).
- Reuse and validation interact: XInclude defines no relation to schema validation, so validation may come before or after inclusion (SO 2009g, quoting the recommendation).
- ProseMirror's low-level constructors do not check content; a checked constructor and an after-the-fact check do (ProseMirror 2026).
- Prose checks:
  - Macdonald 1982 describes the Writer's Workbench, computer aids for text analysis (title and venue only).
  - Juergens 2010: clone detection on specifications reached precision above 85% for each document after 1 to 33 minutes of tailoring (mean 99%), from as low as 2% before; recall was not measured.
  - Fleckenstein 2023 (strand 0) is the only effect size found for automated feedback on writing, and it concerns students.
- Checking tools for documentation are compared with the reader-ergonomics checks in its [checks README](https://github.com/Tewf/reader-ergonomics/blob/e8864477a53d713251ba42a4cf7b7a0d761243a2/checks/README.md); docs as code is reviewed in [architecture-descriptions](https://github.com/Tewf/reader-ergonomics-software-design/blob/master/evidence/architecture-descriptions/review.md).

## 6. Practice

| Who | Version or date | Form | Evidence of use |
|---|---|---|---|
| W3C XML 1.0, XInclude | 2008; 2006 | tree, content models, entities; inclusion with loops fatal | the base of DocBook, TEI and DITA; XInclude not in browsers (SO 2011d) |
| OASIS DITA | 1.2 (2010), 1.3 (2015) | nested topics, maps, conref, keys, `@copy-to` | about 1 in 9 of 276 STC respondents in 2008 (Dayton 2010) |
| DocBook, TEI | 2019; 2026 | recursive sections beside capped numbered ones | project documentation |
| CommonMark, mdast, Pandoc | 2024; read 2026 | containers; headings as leaves of level 1 to 6 | stars (state-of-the-art.md) |
| Sphinx, Asciidoctor, MediaWiki | read 2026 | tables of contents, includes, templates, each with a cycle rule | stars; Wikipedia |
| Notion, ProseMirror | 2021; read 2026 | one parent per block; schema content expressions | the owners' accounts |

Q/A sites (Stack Overflow, Software Engineering, Writing; 11 threads, 9 from the strings and 2 by handoff, all at or above 10 of 20 for the first rater; strings in [protocol](protocol.md)). Practitioner opinion, no data.

- Q3, repeat or refer: the more a set is read like a book, the less it should repeat; read one page at a time, as aviation checklists are, it should repeat (WSE 2018g).
- The accepted answer there: reuse tools let text stored once appear many times at read time, because readers dip into a set rather than read it whole. Repeating serves the reader now, referring keeps content correct over time (WSE 2018f); single sourcing separates content from design (WSE 2011a).
- By handoff: single-sourcing tools let a topic written once be embedded in many documents. An open standard such as DITA avoids a proprietary format that is hard to leave (SO 2015b, an example of practice only).
- Q4 and Q5: XInclude needs XPointer and loop detection, which held browsers back (SO 2011d). Validate after inclusion, though a second answer allows either order (SO 2009g). GoF left room for a child with several parents (SESE 2022c).
- Q6: S1000D's schemas are more rigid than DITA's and are extended only by business rules a tool checks (WSE 2018b). A do-it-yourself DITA setup gives little support for reuse; an integrated one costs a few thousand (WSE 2014a).
