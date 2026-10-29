# Baseline: what the node model is compared against

This file names the baseline a proposed node model must beat on storing, reusing and checking, and how the two would be compared.

## The named baselines

| Role | Baseline | Why this one |
|---|---|---|
| Storage, reuse and checking (the one to beat) | **DITA 1.3**: nested topics and maps, reuse by `conref` and keys, `@copy-to` per use, validated by its grammar and processed by DITA-OT | the only standard read that joins a recursive unit, reuse by reference, a validity rule for reuse and a reference processor that reports cycles (OASIS 2015; DITA-OT 2026b); adoption measured, about 1 in 9 of 276 in 2008 (Dayton 2010) |
| Single document, no reuse layer | **DocBook 5.2** recursive `section` (or `sect1` to `sect5`), validated against its RELAX NG schema, with XInclude for inclusion | the recursive section with an explicit depth-capped twin (Walsh 2019); RELAX NG is a standard grammar (Clark 2001); inclusion loops are fatal (Marsh 2006) |
| The model to beat, as a claim about text | **OHCO** (Coombs 1987; DeRose 1990) | the thesis behind descriptive markup; its critique (Renear 1996) is the known failure case |

- The grey scores: OASIS 2015 17, DITA-OT 2026b 12.5, Walsh 2019 14.5, Clark 2001 17 and Marsh 2006 16.5 of 20 (sources.md).
- Markdown with flat headings (CommonMark 2024) is the most adopted form and the practical floor: no section node, no reuse, no grammar beyond the syntax.
- The maintainer's draft node template is the candidate; the comparison below is what it must win.

## Candidate variant to test

- One node type whose children are nodes, nested in one containment tree per document.
- Reuse only by reference, resolved into a tree when read, with an identity per use.
- An acyclic reference graph, checked by program, with a depth cap as a backstop.
- Cross-tree relations (overlap, links) as stand-off pointers.
- These are hypotheses, graded convention, untested (position.md).

## How a comparison would be measured

| Task | Outcome | Instrument | Prior study to borrow from |
|---|---|---|---|
| Catch structural defects | recall and precision of the check | a corpus seeded with known defects: a reference cycle, a dangling reference, a reused unit invalid in its new place, a node nested past the cap | Juergens 2010 (precision of clone detection, with tailoring time); the DITA-OT 2026b error list as the defect taxonomy |
| Keep reused content consistent | inconsistent copies after a change; clone coverage | the same change made to the same content kept under each model, then a clone detector run | Juergens 2010 (clone coverage, blow-up); Luciv 2018 (near duplicates) |
| Read a reused unit in a new place | accuracy and time on fixed questions about that unit | one fragment shown in two contexts, reused against written for its place, crossover order | no prior study found; the gap this baseline exposes |
| Cost to the writer | time to make a change across N uses; errors introduced | timed task under each model | Dayton 2010 (perceived downsides) as the questionnaire's starting items |
| Validity at scale | share of documents valid against their own schema | a crawl or a repository sample | Grijzenhout 2011 |

- Design: crossover with counterbalanced order for the reader and writer tasks; a fixed seeded corpus for the program tasks.
- Effect sizes for the reader and writer tasks; recall with a confidence interval for the checks.
- Subjects: technical writers and readers of documentation, not students only (Fleckenstein 2023 pools students).

## A checklist in the baseline's own terms

Per DITA 1.3 map and topic set (OASIS 2015; DITA-OT 2026b):

1. Every conref and key resolves, and a resolved reuse is valid in both its source and its target context.
2. No conref chain, map reference or key definition returns to its start (DOTX013E, DOTX053E, DOTJ069E).
3. A topic referenced more than once carries `@copy-to` where its links or navigation must differ per use.
4. Topics nest only where the grammar allows.

Per DocBook 5.2 document (Walsh 2019; Marsh 2006):

1. Sections are recursive `section` elements, or numbered `sect1` to `sect5` properly nested, at most five levels.
2. The document is valid against the RELAX NG schema after XInclude processing.
3. No include repeats within its own inclusion chain.

A rule may be rejected deliberately; the rejection is written where a reviewer looks for the missing check.
