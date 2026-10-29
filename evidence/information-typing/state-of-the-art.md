# State of the art, per question

Two records are kept apart: most adopted (what practice uses) and best evidence (what a study measured).
An **upper bound** is what has been achieved; a **lower bound** is what has not been shown, or cannot be.

## The two records

| Question | Most adopted | Best evidence | Measured how |
|---|---|---|---|
| Q1 What a base unit holds, and how types derive | DITA topic: title, short description, prolog, body, related links, nested topics; concept, task, reference by specialization (OASIS 2015) | none measured; Kintsch 1978 gives the theory: a type is categories plus rules of order | specification read first-hand; theory |
| Q2 Does a typed structure help readers | topic types in DITA, Kubernetes 2026b, Red Hat 2026b | Kintsch 1982 (form plus cues helps global comprehension); Kools 2008 (headings help search); Horn 1969 (typed format against prose: no significant gain) | controlled comparisons, small; abstracts except Horn 1969 |
| Q2, readers taught the types | text structure instruction in schools | Bogaerds-Hazenberg 2020, 44 studies, g = 0.25 to 0.57 at once, none at delay; Pyle 2017, 19 studies, 0.95 | meta-analyses (secondary) |
| Q3 Does knowing one type transfer | DITA generalization: a program reads any derived unit as its base (OASIS 2015, 2.5.4) | Hebert 2016: near transfer to untaught structures, weak far transfer; Meyer 2001: training transferred across texts and a video | meta-analysis (secondary); one experiment (abstract) |
| Q4 What practice adopts | DITA: 802 firms (DITAWriter 2026, informal list, 2026-04-24) | Andersen 2015 and Batova 2017 review component content management (not extracted) | owner-compiled list; reviews by title only |
| Q4, machine-read types | Schema.org HowTo on 100K to 1M domains (SchemaOrg 2026, 2026-08) | none | the vocabulary's own usage band |
| Q5 What typing costs | tool and set-up cost, rigidity of fixed schemas (WSE 2014a; WSE 2018b) | Batova 2018: motivation falls when typing is framed as efficiency only | one 12-month qualitative study (abstract) |
| Q6 Typed units for models | vendor claims, none read | Jimeno Yepes 2024: element-type chunks beat paragraph chunks on financial reports | preprint, abstract |

## Adoption counts, descriptive, taken 2026-10-29

| Count | Value | Caveat |
|---|---|---|
| firms listed as using DITA | 802, of which 126 new in the update | informal, compiled by one practitioner; firms may have left DITA (DITAWriter 2026) |
| stars on the DITA Open Toolkit repository | 458 | interest, not use (DITA-OT 2026) |
| stars on the DITA technical committee repository | 48 | read from the public repository listing |
| domains using Schema.org HowTo | 100K to 1M | a band from Google's index, 2026-08 (SchemaOrg 2026) |
| domains using TechArticle, and Recipe | 10K to 100K each | same source |
| DITA versions approved as OASIS Standards | 1.0 (2005), 1.1 (2007), 1.2 (2010), 1.3 (2015-12-17) | the committee's page; the status of DITA 2.0 was not confirmed |
| map types in Information Mapping, Horn 1969 | 8 | Horn 1969 appendix; later lists differ (against.md) |

## What the base holds, compared

| Base part | DITA topic (OASIS 2015) | Information map, 1969 (Horn 1969) | Text schema (Kintsch 1978) | Kubernetes page (Kubernetes 2026b) |
|---|---|---|---|---|
| a name or title | required | a title per map | not part of the schema | page title |
| a short statement of purpose | short description, optional | an introduction block on most concept maps | not part of the schema | overview paragraph |
| typed parts | body, with sections typed by the derived type | labelled blocks, typed by the map type | the categories of the text type | sections per content type |
| links to other units | related links | a connections block | not part of the schema | a list of next pages, up to five |
| units inside units | nested topics | not stated in the report | rules of order, sometimes recursive | none |
| derivation | specialization, declared in `@class` | a map type takes every block of another | none declared | none declared |

- Only DITA declares derivation so that a program can check it.
- Information Mapping derives by content, in a chart written for writers.
- The text schema is recursive in the reader's knowledge, not in markup.

## Upper bounds (achieved)

- A typed base with declared derivation and fallback processing is standardised and in industrial use (OASIS 2015; DITAWriter 2026).
- Teaching readers several text types raises comprehension at once (Pyle 2017; Bogaerds-Hazenberg 2020) and transfers to untaught types (Hebert 2016).
- Conventional form with cues helps the reader's gist more than local detail (Kintsch 1982).
- Typed boundaries help a model retrieve, in one domain (Jimeno Yepes 2024).

## Lower bounds (not shown)

- No study found compares the same content as untyped text, as DITA topics and as another typed template, on readers.
- The one controlled test of a typed format against prose found no significant gain in learning (Horn 1969), and it has not been repeated in this search.
- No study found tests the hypothesis that a reader who knows a base type reads a derived type faster or better.
- No effect of a type survives a delayed posttest in the largest review (Bogaerds-Hazenberg 2020).
- A grammar of types cannot by itself tell a story from a non-story (Black 1979): form is not sufficient to define a kind.
