# Review

This file reads the literature on typed units of writing. Existing reviews come first, then the seminal theory, Information Mapping read first-hand. DITA, reader studies, transfer, cost, models as readers, and practice follow.

How numbers and scores are marked: the [evidence README](../README.md#method).

## 0. Existing reviews

| Review | Scope | Finding for this review | Read |
|---|---|---|---|
| Hebert 2016 | meta-analysis, 45 studies, grades 2 to 12, expository text structure instruction | effective on proximal measures, and across three levels of transfer: maintenance, untaught text structures, general comprehension; far transfer small and inconsistent | abstract (secondary) |
| Pyle 2017 | meta-analysis, 19 of 21 studies, kindergarten to grade 12, 1970-2013 | mean effect 0.95; larger with one or two structures taught, 11 to 20 hours, researcher implementers | abstract (secondary) |
| Bogaerds-Hazenberg 2020 | meta-analysis, 44 studies, grades 4 to 6, informational and narrative | immediate g = 0.25 (questions), 0.57 (summary), 0.37 (recall), 0.38 (structure knowledge); no advantage at delayed posttest | abstract (secondary); the thesis chapter read for transfer (Bogaerds-Hazenberg 2023) |
| Eiriksdottir 2011 | review of instructions: procedures, principles, examples | specific instructions help first performance; general ones help learning and transfer | abstract |
| Andersen 2015; Batova 2014; Batova 2017 | integrative and systematic reviews of component content management | none extracted here | title and venue only here; read in [document-model](../document-model/review.md) |

- No review was found of DITA, Information Mapping or topic types measured on readers. That is a statement about this search.
- The three meta-analyses test **teaching readers the types**, not **writing to a type**. Their effect is a lower bound on what a schema in the reader can do, not a test of a template.

## 1. Seminal theory: schematic structures and story grammars

- Kintsch 1978 (read first-hand, section "Schematic structures of discourse"): a conventional text type is a set of categories with rules for their order.
  - Its examples are a story, an argument and a psychological research report.
  - The rules of formation are "(sometimes recursive)", in the paper's words.
  - The schema controls which propositions reach the gist; it is shared by a cultural group (section "Role of the schema").
- Rumelhart 1975: the first schema for stories (title and venue only).
- Mandler 1977: an analysis of simple stories; children and adults recall them differently, so schemata develop (ERIC abstract).
- Thorndyke 1977: two experiments vary the amount of structure in passages and separate structure from content (ERIC abstract, secondary).
- Stein 1975: a story schema tested on 48 first and fifth graders; recall differed by age and delay, but which categories were recalled was stable across stories (ERIC abstract, secondary).
- Mandler 1978: the story schema used in retrieval (title and venue only).
- Black 1979 evaluated the grammars: one formally adequate, many stories not generated, one class of non-story generated, nothing added over content models (abstract, secondary).
- Trabasso 1985: causal networks of events, the content-based account that followed (title and venue only).

## 2. Information Mapping, read first-hand

Horn 1969 (the 1969 Air Force report, read in full scan) replaces the encyclopedia page that reader-ergonomics cited under the same key.

- Units: separable **information blocks**, each with a marginal label, grouped into **information maps**; each map type has its own format (chapter 1).
- Eight map types in the appendix chart: concept, structure, process, procedure, classification, decision, fact, proof (pp. 122-123).
- Derivation from a base already appears: a structure map takes every block of the concept map; a process map takes every concept and structure block; a procedure map takes every concept block.
- The concept map is the most frequent type (chapter 2).
- The one controlled comparison (chapter 5, Harvard series):
  - same content, same questions, either as information maps (IM) or with the labels, boxes and unit pages removed (prose, P); random assignment;
  - adjusted posttest means 19.56 (IM, n = 20) against 17.65 (P, n = 21), t = 1.17, 38 df, not significant;
  - the authors offer two readings and favour the second: the one-session class test was not sensitive enough to show a difference.
- Chapter 7 warns that such evaluations test one book, not the method, and have no external reference point.
- Jonassen 1980 (journal abstract, secondary): information mapping against programmed instruction; no difference in recall, but retrieving information from the text benefited significantly from mapping.
- Later formal work, mostly not opened: Horn 1981 (structured writing for software documentation), Horn 1999 (STOP against structured writing), Fields 1981 (a survey, ERIC abstract). Also later formal work, mostly not opened: Fields 1982 (an evaluation, title only), Hartley 1981 (a critique).
- Kools 2008 varied one health text by the method: headings sped search, the number of headings did not change speed, and the method's information order had no effect (abstract).

## 3. DITA and topic-based authoring

- OASIS 2015 (DITA 1.3, read first-hand):
  - every topic has the same base: title, short description or abstract, prolog, body, related links, nested topics (2.2.1.6);
  - concept, task and reference derive from topic by **specialization**, a subtype hierarchy in which a derived type inherits meaning and default processing (2.5.3.1);
  - the `@class` attribute lists each element's ancestry, so any processor can treat a derived element as its ancestor (2.5.3.6); content can be **generalized** back to any ancestor (2.5.4.1);
  - information typing is said to rest on Horn's Information Mapping and Hughes Aircraft's STOP; no study is cited (2.2.1.4);
  - limits: sections cannot nest, every topic needs a title, and a type that breaks these is no longer DITA (B.11).
- Priestley 2001 and Priestley 2002: the IBM architecture papers on reuse and on specialization (title and venue only).
- Evia 2015: teaching DITA through rhetorical and computational thinking (title and venue only).
- Swarts 2022: a corpus of topic-based documentation; relative clauses signal context to readers who arrive at one topic alone (abstract).
- Heinonen 2022: DITA layered by skill level, tested with maintenance staff in three countries by observation, interview and questionnaire; well received (abstract, secondary; no control).

## 4. Does a typed structure help the reader (Q2)

| Study | Manipulation | Result | Grade |
|---|---|---|---|
| Kintsch 1982 | essays in good rhetorical form with cues, against bad form, no cues, deviant order | better comprehension with good form and cues on questions about the topic and main points (global); the cloze test (local) did not differ; 2 experiments, 72 students; no numbers in the abstracts | measured (ERIC and APA abstracts) |
| Horn 1969 | typed maps against the same text as prose | no significant difference in learning | measured, one study, 41 students |
| Kools 2008 | headings and order of an information-mapped text | headings help search; amount of headings and order do not | measured (abstract) |
| Zwaan 1994 | one text framed as literature or as news | literary framing: longer reading, better surface memory, weaker situation memory | measured (secondary) |
| Triantafyllopoulos 2021 | the same framing, three online experiments | no difference in comprehension by genre expectation | measured (abstract, secondary) |
| Markevich 2025 | narrative, expository and poetic texts, 44 adolescents, eye tracking | forward reading for narrative, more lookbacks for expository and poetry | measured, descriptive (abstract) |
| Carroll 1987; Lazonder 1993 | task-oriented minimal manual against a standard manual | not extracted | title and venue only |

## 5. Does knowing one type transfer (Q3)

- Hebert 2016: instruction transferred to untaught text structures (near transfer); far transfer was small and inconsistent (abstract).
- Bogaerds-Hazenberg 2023: some delayed posttests in the pooled studies used untaught structures; too few to test transfer (thesis, chapter on the meta-analysis).
- Meyer 2001: nine hours of structure strategy training raised adults' total recall from a variety of texts and from an informative video; interest training did not (ERIC abstract, secondary).
- Eiriksdottir 2011: abstract instructions favour transfer, specific ones favour first performance.
- Writing studies treat transfer of genre knowledge as recontextualisation (Cheng 2007; Artemeva 2008; Brent 2011; titles and venues only).
- No study was found that teaches readers a base type and tests them on a type derived from it.

## 6. What typing costs (Q5)

- Batova 2018, on writers' motivation in a move to component content management, is reviewed in [document-model](../document-model/review.md).
- Bailie 2015 and Coggio 2015: case studies of content management changing how writers write (titles and venues only).
- Black 1979: a type grammar can accept non-stories and reject stories, so form alone does not define the kind.

## 7. Models as readers (Q6)

- Jimeno Yepes 2024: chunking financial reports by element type improved retrieval-augmented question answering over paragraph chunks (preprint, abstract).
- Mortezaagha 2026: structure-aware retrieval for models reading a tree, reviewed in [progressive-disclosure](../progressive-disclosure/review.md); its trade-off is in [against](against.md).
- No study was found that gives a model DITA topic types or Information Mapping blocks and measures the answer. General findings on layout and models: [llm-readers](https://github.com/Tewf/reader-ergonomics/blob/6980fa64583912922d6f5b5c01316749d654345f/evidence/llm-readers/frame.md).

## 8. Practice

| Who | Since | Base and derived types | Evidence of use |
|---|---|---|---|
| Information Mapping (Horn 1969; Information Mapping 2026) | 1969 | blocks in maps; eight map types in 1969 | company page: nine gains, such as +83% initial learning and -51% reading time, credited to Horn's studies without a reference (example only) |
| DITA (OASIS 2015) | OASIS Standard 1.0 in 2005; 1.3 on 2015-12-17 | topic, then concept, task, reference | 802 firms listed by DITAWriter 2026; DITA-OT 2026 repository, 458 stars |
| Kubernetes 2026b | page dated 2026-05-03 | concept, task, tutorial, reference | the project's contributor style guide; no use count |
| Red Hat 2026b; GitLab 2026 | undated | concept, procedure, reference modules; topic types | reviewed in [documentation](https://github.com/Tewf/reader-ergonomics/blob/6980fa64583912922d6f5b5c01316749d654345f/evidence/documentation/review.md) |
| SchemaOrg 2026 | 2026-08 counts | CreativeWork, then HowTo, then Recipe; Article, then TechArticle | HowTo on 100K to 1M domains; TechArticle and Recipe on 10K to 100K |
| Baker 2013 | 2013 | eight traits of a topic, one of them that it conforms to a type | publisher page |

Q/A sites (Writing, Stack Overflow, User Experience; searched 2026-10-29; 12 threads, 2 under 10 of 20; strings in [protocol](protocol.md)). Practitioner opinion, no data.

- Q1: DITA topics and S1000D data modules are both modular units; DITA lets a team derive types, S1000D only constrains a fixed schema (WSE 2018b).
- Q1: code must act on `@class` values, not tag names, because DITA has no single grammar (SO 2016b).
- Q1: the base topic is the most forgiving type; deriving a type needs a developer, says the asker, and is trivially easy, says the accepted answer (SO 2013a).
- Q2: readers expect a genre's general rules, and familiar elements make the new ones stand out (WSE 2018d; WSE 2014b).
- Q2: a topic should solve one user problem, so length is the wrong measure (WSE 2018c, an answer by the author of Baker 2013 by its own account).
- Q3: moving a story from the hero's journey to the four parts of kishotenketsu means retelling it, not relabelling it (WSE 2022a).
- Q5: DITA tooling ranges from free editors to integrated systems; the hidden cost is set-up time (WSE 2014a); drop a story template when it forces content (WSE 2020a, example only).
- Q4: DITA is little used by software library developers, says one asker (SO 2019a, example only); name document types from user research (UXSE 2014a).
