# State of the art, per sub-question

Two records are kept apart: most adopted (what people use) and best evidence (what a study measured).

| Sub-question | Most adopted | Best evidence | Measured how |
|---|---|---|---|
| Q1 Which models store text as a tree, with what recursive rule | Markdown's flat headings over container blocks (CommonMark 2024); XML content models with a recursive section (DocBook, TEI, DITA) | Mignet 2003 and Mlýnková 2006: recursion is common in schemas and shallow in instances | corpus statistics of web XML |
| Q2 Text that is not a tree | milestones and stand-off markup (TEI 2026, chapter 21; the OSIS norm in DeRose 2004) | Renear 1996: every version of OHCO met a counterexample | argument from cases, no frequency count |
| Q3 A unit with two parents | reuse by reference: conref and keys (OASIS 2015), XInclude, MediaWiki templates | Juergens 2010 for copies; Dayton 2010 for adoption; Johnson 2020 for the rate of transclusion | clone detection on 28 specifications; a survey of 276; a classification of transclusions |
| Q3 Effect of reuse on readers | none | none found | none |
| Q4 Cycles through references | detection and report, or a depth cap (table below) | none; standards and tool documentation only | descriptive comparison of 14 systems, this review |
| Q5 Checking by program | grammar validation in XML; prose linters in docs as code | Grijzenhout 2011 (validity on the web); Juergens 2010 (precision of clone detection); Fleckenstein 2023 (students) | crawl of 180,000 files; precision on 28 documents; meta-analysis, g = 0.55 |
| Q6 What strict models cost | lighter forms: Markdown; HTML heading levels (WHATWG 2022); one parent per block (Notion 2021) | Dayton 2010 (downsides, failures); Batova 2014 (context loss, contradictory); Martens 2006 (unused power) | survey; integrative review of 60 articles; analysis of real schemas |

## How each system meets a cycle through a reference

| System | Recursive type | Reuse by reference | A cycle through a reference | Source |
|---|---|---|---|---|
| XML 1.0 | content models; the instance nests properly | parsed entities | forbidden: well-formedness constraint No Recursion | Bray 2008, 4.1 |
| XInclude 1.0 | none of its own | include of a resource or fragment | fatal within the inclusion chain; two non-nested includes allowed by implication | Marsh 2006, 4.2.7 |
| DITA 1.2 and 1.3 | nested topics and topic references | conref, conkeyref, keys, map references | not addressed in the conref pages read | OASIS 2010; OASIS 2015 |
| DITA-OT | as DITA | as DITA | reported: DOTX013E, DOTX053E, DOTJ069E | DITA-OT 2026b |
| DocBook 5.2 | `section`, unbounded; `sect1` to `sect5` | not read here | not read here | Walsh 2019 |
| TEI P5 | `div`; `div1` to `div7` | pointers, stand-off | not read here | TEI 2026 |
| JSON Schema, version 2020-12 | `$ref`, `$dynamicRef` | `$ref` | must not loop against an instance; mutual `allOf` loops undefined | Wright 2022, 9.4.1 |
| MediaWiki | templates in templates | template transclusion | reported as a template loop; depth capped at 100 | MediaWiki 2026a; 2026b |
| Asciidoctor | nested includes | include directive | capped: `max-include-depth` 64 | Asciidoctor 2026 |
| Sphinx | tree of tables of contents | a document under several parents | self-reference and circular references reported and ignored; for several parents, one is named as selected | Sphinx 2026 |
| CommonMark | containers hold blocks; headings flat | none in the specification | none possible | CommonMark 2024 |
| OPML 2.0 | `outline` in `outline` | `include` of another OPML file | not addressed in the specification read | Winer 2007 |
| Logseq | nested blocks | block reference; embed of a block with its descendants | not read here | Logseq 2023 |
| ProseMirror | content expressions | one node value in several places | none possible among values (an inference from immutability) | ProseMirror 2026 |

- Of the 10 systems whose reuse is by reference (TEI pointers and ProseMirror shared values set aside), 5 forbid or report a cycle (XML, XInclude, DITA-OT, MediaWiki, Sphinx), and 2 cap depth (Asciidoctor, MediaWiki). In 3 texts it is undefined or unaddressed (JSON Schema, DITA, OPML), and 1 was not read on cycles (Logseq). MediaWiki does both.
- No system read stores a unit that contains itself on purpose.

## Adoption counts, descriptive, taken 2026-10-29

| Repository | Stars | What it is |
|---|---|---|
| jgm/pandoc | 46,736 | document converter over one tree model |
| sphinx-doc/sphinx | 8,084 | documentation builder with a tree of tables of contents |
| DavidAnson/markdownlint | 6,401 | Markdown structure linter |
| vale-cli/vale | 6,300 | prose linter |
| asciidoctor/asciidoctor | 5,227 | AsciiDoc processor with includes |
| json-schema-org/json-schema-spec | 5,199 | the JSON Schema specification |
| btford/write-good; get-alex/alex | 5,107; 5,105 | prose linters |
| amperser/proselint; textlint/textlint | 4,587; 3,203 | prose linters |
| syntax-tree/mdast | 1,484 | Markdown syntax tree specification |
| dita-ot/dita-ot | 458 | DITA reference processor |
| TEIC/TEI; ProseMirror/prosemirror-model | 358; 338 | TEI source; ProseMirror document model |
| relaxng/jing-trang; Schematron/schematron; docbook/docbook | 260; 97; 89 | validators and schema sources |

- Counts come from the public GitHub API, unauthenticated, on 2026-10-29 (GitHub 2026d). Stars measure interest, not use.
- Standards that predate GitHub (XML, DocBook, TEI, DITA) are understated by their repositories.
- Dayton 2010 is the only measured adoption share found: about 1 in 9 of 276 technical communicators used DITA in 2008, and half used single sourcing or content management.

## Upper bounds (achieved)

- A reference processor detects three kinds of cycle: conref, map and key (DITA-OT 2026b).
- Clone detection finds duplicated prose in specifications at precision above 85% per document after tailoring (Juergens 2010).
- Data models for overlap exist and are implemented: GODDAG, EARMARK, TAG (strand 2 of the review).
- Automated feedback improves students' writing, g = 0.55 (Fleckenstein 2023, secondary).
- A web-scale measure of validity exists: 85.4% of 180,000 files well-formed (Grijzenhout 2011, secondary).

## Lower bounds (impossible, or not shown)

- A well-formed XML element cannot contain itself: proper nesting gives a finite tree (Bray 2008, 2.1), and a parsed entity may not recurse (4.1). This follows from the syntax.
- No single hierarchy holds every perspective on a text: each version of OHCO met a counterexample (Renear 1996). This is an argument from cases, not a proof.
- Not shown in this search: any effect on readers of reuse by reference against copies, of a tree model against a graph model, or of a depth-capped against an unbounded section.
- Not shown: the recall of any prose or structure checker on documentation; Juergens 2010 measured precision only.
