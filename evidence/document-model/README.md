# Document model: how a unit that holds units of its own type is stored, reused and checked

Question: how is a unit that can hold units of its own type stored, so that it is a tree a reader can follow, reusable in several places and checkable by a program? And what do document models and their critics say?

- It covers published research, standards and tools: 46 formal sources and 36 grey ones (25 from the web, 11 threads from Q/A sites).
- It scores every grey source out of 20; 1 falls below the threshold of 10, and 1 more (SO 2015b) fell below it for the second rater; both are used as examples only.

## Files

| File | Role |
|---|---|
| [protocol](protocol.md) | how the pool on document models, reuse and checking was searched and scored |
| [sources](sources.md) | the pool, counted stage by stage, and each source with its quality |
| [frame](frame.md) | step 1: the problem, and what markup research and practice call it |
| [review](review.md) | step 2: OHCO and its critics, content models, reuse, cycles, checking |
| [state of the art](state-of-the-art.md) | step 3: how fourteen systems treat recursion, reuse and cycles |
| [position](position.md) | step 4: the answers on self-reference and graphs, and candidate rules |
| [against](against.md) | the cost of strict models, and fragments reused without their context |
| [baseline](baseline.md) | step 5: DITA maps and conref, DocBook with RELAX NG, and OHCO |
| [bibliography](../bibliography.md) | every cited work, shared by the three reviews |
| `flow.json` | the flow as data, drawn in the figure of [sources](sources.md) |

## Claims

| Claim | Grade | Where |
|---|---|---|
| Document standards put recursion in the type and keep each instance a finite tree | convention (standards), descriptive | review.md 1, 4 |
| DocBook and TEI offer a capped numbered form (5 and 7 levels) beside the recursive one | convention (standards) | review.md 1 |
| Recursion is common in schemas and shallow in instances: 58% of DTDs hold recursive elements; 99% of web XML documents have fewer than 8 levels | measured, descriptive (secondary) | review.md 5 |
| No version of the OHCO thesis is free of counterexample | supported with caveat (argument from cases) | review.md 2 |
| Where reuse is not enforced, copies are common: mean clone coverage 13.6% over 28 specifications, up to 71.6% | measured, descriptive, one study | review.md 3 |
| Clone detection finds duplicated prose at precision above 85% after tailoring; recall was not measured | measured, descriptive, one study | review.md 5 |
| In 2008, half of 276 respondents used single sourcing or content management; half of its users reported significant downsides; about 1 in 10 had seen a failure | measured, descriptive (survey, secondary) | review.md 3 |
| Reused components lose context for translators, and the sources disagree on quality | supported with caveat (integrative review of 60 articles) | review.md 0; against.md |
| 85.4% of 180,000 web XML files are well-formed; about a third of those that name a schema validate | measured, descriptive (secondary) | review.md 5 |
| Every system read on cycles that allows references forbids, reports or caps a cycle, or leaves it undefined; none keeps a self-containing unit | convention, descriptive count of 14 systems | state-of-the-art.md |
| A unit with two parents is allowed only by reference, with a rule per use for links, navigation or permissions | convention, descriptive | position.md |
| Automated writing feedback improves students' writing, g = 0.55 | measured (meta-analysis, secondary; students, not documentation) | review.md 0 |
| The evidence for design patterns in general is weak; none of it concerns documents | measured, systematic review (secondary) | review.md 0 |
| Reuse by reference helps readers or keeps documentation consistent | not found: no study in this search | position.md |
| One containing parent, acyclic references, each reuse valid in each place | convention, untested (candidate rules) | position.md |

## The two questions this review answers

- **Self-reference.** The template needs the recursive type, a topic whose children are topics. No model read needs a topic that contains itself, and standards forbid it by syntax, by a rule on references, or in the processor ([position](position.md)).
- **Graphs.** In the standards read, the stored form is a graph of trees (files that reference files), each reading is a tree, and what crosses the hierarchy is held beside it as pointers. No study shows which view helps readers ([position](position.md)).

## Named baseline

- To beat: DITA 1.3 topics and maps, reuse by `conref` and keys, validated, with a processor that reports cycles (OASIS 2015; DITA-OT 2026b).
- Single-document twin: DocBook 5.2 recursive `section` with RELAX NG and XInclude (Walsh 2019; Clark 2001; Marsh 2006).
- Model to beat as a claim about text: OHCO (DeRose 1990), with its critique (Renear 1996).
- Comparison: seeded structural defects, consistency after a change, reading a reused unit in a new place, cost to the writer ([baseline](baseline.md)).

## General findings linked, not reviewed again

- [One place per fact](https://github.com/Tewf/reader-ergonomics/blob/6980fa64583912922d6f5b5c01316749d654345f/principles/collection/one-place-per-fact.md), with its evidence on duplication and clones in [file-structure](https://github.com/Tewf/reader-ergonomics/blob/6980fa64583912922d6f5b5c01316749d654345f/evidence/file-structure/review.md).
- [Shallow outline](https://github.com/Tewf/reader-ergonomics/blob/6980fa64583912922d6f5b5c01316749d654345f/principles/document/shallow-outline.md), and the levels effect in [psycholinguistics](https://github.com/Tewf/reader-ergonomics/blob/6980fa64583912922d6f5b5c01316749d654345f/evidence/psycholinguistics/review.md).
- Docs as code in [architecture-descriptions](https://github.com/Tewf/reader-ergonomics-software-design/blob/master/evidence/architecture-descriptions/review.md); tools that check documentation in the reader-ergonomics [checks README](https://github.com/Tewf/reader-ergonomics/blob/6980fa64583912922d6f5b5c01316749d654345f/checks/README.md).
- Typed units and derived types: [information-typing](../information-typing/README.md). Showing nested trees to readers: [progressive-disclosure](../progressive-disclosure/README.md).
