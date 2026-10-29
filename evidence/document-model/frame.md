# Frame: the problem and its names

This file states, in one sentence, the problem of storing a recursive unit of writing, then the names research and practice give it, and the terms used in every file of this folder.

## The problem in one sentence

Decide how to store a unit that holds units of its own type, so it forms a tree a reader can follow, serves in several places and can be checked by a program.

## Terms used in this folder

| Term | Definition |
|---|---|
| **tree** | each unit has at most one parent, and no unit is its own ancestor |
| **DAG** (directed acyclic graph) | a unit may have several parents, and still no chain returns to its start |
| **cycle** | a chain of containment or reference that returns to the unit it started from |
| **recursive type** | a type whose definition names itself, directly or through others; it describes trees of any finite depth |
| **self-containment** | an instance that contains itself; in the models read it can arise only through a reference |
| **content model** | the rule that says which children an element type may have, and in what order; XML 1.0 calls it a simple grammar (Bray 2008, section 3.2.1) |
| **well-formed**, **valid** | well-formed meets the syntax rules; valid also matches the schema the document declares |
| **reuse by reference** | a unit is stored once and pulled into other places by a pointer, instead of being copied |

## What the field calls it

| Our phrase | Field names | Entry points |
|---|---|---|
| a unit whose parts are units of its type | **recursive content model**, **recursive data type**, **Composite pattern** | Walsh 2019; Hoare 1975; Gamma 1995 |
| text as a tree of typed parts | **OHCO** (ordered hierarchy of content objects), **descriptive markup**, **document type**, **logical structure** | Coombs 1987; DeRose 1990; Renear 1996 |
| the rule for what a node may contain | **content model**, **DTD** (document type definition), **schema**, **tree grammar** (local, single-type, regular) | Bray 2008; Murata 2005 |
| text that is not one tree | **overlapping hierarchies**, **overlap**, **self-overlap**, **concurrent markup**, **multihierarchical markup**, **non-hierarchical structures**, **discontinuity** | Barnard 1988; Renear 1996; DeRose 2004; TEI 2026 |
| models proposed for it | **GODDAG**, **LMNL**, **EARMARK**, **TAG** (text as graph), **stand-off markup**, **milestones**, **CONCUR**, **multi-version document** | Sperberg-McQueen 2004; Peroni 2009; Haentjens Dekker 2017; Schmidt 2009 |
| one unit shown in several places | **transclusion**, **content reuse**, **reuse by reference**, **single sourcing**, **component content management** (CCM) | Nelson 1965; Nelson 1999; Priestley 2001; Andersen 2015 |
| copies instead of references | **clones**, **near duplicates**, **redundancy**, **blow-up** | Juergens 2010; Luciv 2018 |
| a unit that contains itself through references | **recursive entity reference**, **inclusion loop**, **circular reference**, **template loop** | Bray 2008; Marsh 2006; DITA-OT 2026b; MediaWiki 2026b |
| checking structure by program | **validation**, **schema languages** (DTD, XSD, RELAX NG, Schematron), **controlled language checker**, **automated writing evaluation** (AWE) | Murata 2005; Grijzenhout 2011; Fleckenstein 2023 |

## What practitioners call it

| Practitioners say | The field says |
|---|---|
| includes, partials, snippets, embeds, shortcodes | transclusion |
| conref, conkeyref, keyref, XInclude, the include directive, MediaWiki templates | reuse by reference |
| single source of truth, DRY in documentation | single sourcing; [one place per fact](https://github.com/Tewf/reader-ergonomics/blob/03cfbc9dd1d243aa86f8ba3168abc61be2bab19f/principles/collection/one-place-per-fact.md) |
| CCMS, structured authoring | component content management |
| blocks, nested blocks, block references | recursive content model; transclusion |
| AST, mdast, the Pandoc AST | the document tree |
| prose linter, style linter, markdownlint | style checker, controlled language checker |
| schema, RNG, Schematron rules, BREX (S1000D) | validation |
| docs as code, docs like code | no research term found; reviewed in [architecture-descriptions](https://github.com/Tewf/reader-ergonomics-software-design/blob/master/evidence/architecture-descriptions/frame.md) |

- On Stack Overflow "transclusion" is mostly a homonym: 28 of the 30 most-voted titles with the word concern content projection in Angular, Vue or Aurelia (string NM1, protocol.md).

## The method named

- This review is a **multivocal literature review (MLR)**: formal literature pooled with **grey literature**, material not controlled by commercial publishers (Garousi 2019).
- Grey sources fall in three tiers by outlet control: tier 1 (books, standards, theses), tier 2 (project documentation, Q/A and wiki pages, talks), tier 3 (blogs).
- [protocol](protocol.md) states the searches; [sources](sources.md) lists the pool and the scores.

## Six sub-questions

| Id | Question |
|---|---|
| Q1 | Which document models treat text as a tree of typed objects, and what is their recursive rule? |
| Q2 | The critique: text that is not a tree, and the models proposed for it |
| Q3 | A unit used by two parents: transclusion, reuse, single sourcing; any measured effect on consistency, cost or readers |
| Q4 | Self-reference: a recursive type against a cycle in an instance, and how tools forbid cycles |
| Q5 | Checking structure by program: validation and prose linting, with adoption, and any evidence that it catches errors |
| Q6 | What strict models cost, and fragments reused without their context |

## Search terms tried, three ways

- Academic: ordered hierarchy of content objects, descriptive markup, overlapping hierarchies, concurrent markup, transclusion, content reuse, single sourcing, component content management, recursive XML schema, real-world schemas, documentation clones, controlled language checker, automated writing evaluation.
- Acronyms: OHCO, SGML, XML, DTD, XSD, TEI, DITA, CCM, GODDAG, LMNL, TAG, EARMARK, AWE.
- Authors: Renear, DeRose, Coombs, Sperberg-McQueen, Huitfeldt, Nelson, Priestley, Rockley, Andersen, Batova, Murata, Mlýnková, Juergens, Vitali.
- Zero or two results were read as wrong queries, not absence. On arXiv every overlap string returned 0, since the field publishes in digital humanities venues. "Prose linting" returned 2 (F15), so it was rephrased twice (F16, F17).

## Not reviewed here

- How a unit is given a type, and how types derive from a base (DITA specialization, information typing): [information-typing](../information-typing/frame.md).
- How a nested tree is shown to a reader (expandable text, outliners, depth per view): [progressive-disclosure](../progressive-disclosure/frame.md).
- Duplication in code, minimal DAGs and the rule of one place per fact: [file-structure](https://github.com/Tewf/reader-ergonomics/blob/03cfbc9dd1d243aa86f8ba3168abc61be2bab19f/evidence/file-structure/review.md), linked, not repeated.
- The levels effect, readers recalling the top of a hierarchy best: [psycholinguistics](https://github.com/Tewf/reader-ergonomics/blob/03cfbc9dd1d243aa86f8ba3168abc61be2bab19f/evidence/psycholinguistics/review.md).
- Docs as code as a practice: [architecture-descriptions](https://github.com/Tewf/reader-ergonomics-software-design/blob/master/evidence/architecture-descriptions/review.md).
