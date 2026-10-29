# Frame: the problem and its names

This file states the problem of typed units in one sentence, then the names research and practice give it, then the questions the review answers.

## The problem in one sentence

Give each unit of writing a declared type, derived from one base, so that a reader who knows the base form can read every form derived from it.

## Terms used in every file

| Term | Definition here |
|---|---|
| **unit** | a piece of writing read as one thing: a topic, a map, a section, a story episode |
| **type** | a named kind of unit with a fixed set of parts in an expected order |
| **base type** | the type every other type derives from; it holds the parts all units share |
| **derived type** | a type that keeps the base's parts and adds or narrows some of its own |
| **derivation** | the rule that makes one type from another; DITA calls it **specialization** |
| **generalization** | reading or processing a derived unit as if it were its base type |
| **schema** (reader side) | the reader's knowledge of a type's categories and their order |

## What research calls it

| Name | Field | What it covers | Entry point |
|---|---|---|---|
| **schematic structure**, later **superstructure** | discourse psychology | the conventional categories of a text type and their order, used by the reader to build the gist | Kintsch 1978 |
| **story grammar**, **story schema** | cognitive psychology | rules that rewrite a story into setting and episodes, and episodes into smaller parts | Rumelhart 1975; Mandler 1977; Thorndyke 1977; Stein 1975 |
| **causal network** | cognitive psychology | the successor to story grammars: events linked by causes | Trabasso 1985 |
| **text structure**, **top-level structure** | reading research | expository patterns (comparison, cause, problem and solution) taught to readers | Meyer 1975 (linked); Meyer 2001; Hebert 2016 |
| rhetorical structure (in the 1982 sense, not rhetorical structure theory) | discourse psychology | the conventional form of an essay, with or without cues | Kintsch 1982 |
| **genre expectation** | discourse psychology | the reader's belief about a text's genre, which changes how it is processed | Zwaan 1994 |
| **genre**, **genre knowledge**, **uptake** | rhetorical genre studies | genre as a recurring social action; how writers carry genre knowledge to new settings | Miller 1984; Artemeva 2008 |
| **genre awareness**, **transfer** | applied linguistics, writing studies | whether knowing one genre helps with another | Cheng 2007; Brent 2011 |
| **information types** (procedure, principle, example) | human factors | which kind of instruction helps performance, learning or transfer | Eiriksdottir 2011 |
| **minimalism**, **minimal manual** | human-computer interaction | task-oriented documentation, the lineage of the task type | Carroll 1987 |
| **component content management** (CCM) | technical communication research | writing and managing small typed components instead of whole documents | Andersen 2015 |

## What practitioners call it

| Practitioners say | Where | The field says |
|---|---|---|
| **information typing**, **topic type** | DITA (OASIS 2015) | type of unit |
| **specialization** and **generalization** | DITA (OASIS 2015) | derivation, and reading a derived unit as its base |
| **concept**, **task**, **reference** | DITA technical content; Kubernetes 2026b adds **tutorial** | derived types |
| **Information Mapping**, **information block**, **information map** | Horn 1969; Information Mapping 2026 (example only) | typed blocks inside typed maps |
| **structured writing** | Horn 1981; Baker 2018b (example only) | writing to a declared structure |
| **topic-based authoring**, **modular authoring** | Baker 2013; WSE 2018a | units read on their own |
| **Every Page is Page One** (EPPO) | Baker 2013 | a topic that conforms to a type and stands alone |
| **modules**: concept, procedure, reference | Red Hat 2026b, reviewed in [documentation](https://github.com/Tewf/reader-ergonomics/blob/bfbe9f7ed27bfdca0c6a4922d0b3e302f9e55d3f/evidence/documentation/frame.md) | derived types |
| **data module** | S1000D, named in WSE 2018b | typed unit in aerospace documentation |
| **type hierarchy**: CreativeWork, HowTo, Recipe | SchemaOrg 2026 | derivation for machine readers |
| **story structure**, **hero's journey**, **three-act structure** | fiction writers (WSE 2022a; WSE 2020a, example only) | story grammar, in practice |

- The words differ more than the idea.
- Research says **schema**: the type lives in the reader's head.
- Practice says **type**: the type lives in the markup.
- This review keeps the two apart: a declared type helps only if the reader holds a matching schema.

## The questions

| Id | Question |
|---|---|
| Q1 | Which systems define a base unit and derive types from it, and what does the base hold? |
| Q2 | Does a typed, predictable structure help readers find, understand or recall, measured? |
| Q3 | Does knowing one type transfer to another type, or to a derived type? |
| Q4 | What does practice adopt, with counts? |
| Q5 | What does typing cost: rigidity, authoring burden, failed fit? |
| Q6 | Do typed units help a language model as reader, kept apart from vendor claims? |

## Search terms tried, three ways

- Academic: information typing, structured authoring, topic-based authoring, story grammar, story schema, superstructure, text structure instruction, genre expectations, genre knowledge, genre awareness and transfer, rhetorical genre studies, component content management, minimal manual, procedural instructions.
- Acronym: DITA, CCM, EPPO, STOP, RAG.
- Author: Horn, Priestley, Day, Baker, Mandler, Thorndyke, Stein, Rumelhart, Black, Kintsch, van Dijk, Meyer, Hebert, Zwaan, Miller, Andersen, Batova, Carroll.
- Zero or near-zero results: "Darwin Information Typing Architecture" on arXiv (0) and "information mapping" with Horn on arXiv (0). The research sits in journals of technical communication and education, not on arXiv; the formal strings were moved there.

## Not reviewed here

- The levels effect and rhetorical structure theory: [psycholinguistics](https://github.com/Tewf/reader-ergonomics/blob/bfbe9f7ed27bfdca0c6a4922d0b3e302f9e55d3f/evidence/psycholinguistics/frame.md).
- The four documentation modes of Diataxis: [documentation](https://github.com/Tewf/reader-ergonomics/blob/bfbe9f7ed27bfdca0c6a4922d0b3e302f9e55d3f/evidence/documentation/frame.md).
- Moves, steps and CARS in research articles: [academic-papers](https://github.com/Tewf/reader-ergonomics-academic/blob/master/evidence/academic-papers/frame.md).
- Storing, nesting and reusing typed units (DITA maps, conref, schemas): the document-model review.
- Showing a nested tree to a reader: the progressive-disclosure review.
