# Topic

[![Checks against reader-ergonomics](https://github.com/Tewf/reader-ergonomics-topic/actions/workflows/checks.yml/badge.svg)](https://github.com/Tewf/reader-ergonomics-topic/actions/workflows/checks.yml)
[![Site](https://github.com/Tewf/reader-ergonomics-topic/actions/workflows/pages.yml/badge.svg)](https://tewf.github.io/reader-ergonomics-topic/)

One template for a unit of writing, called a **topic**, whose parts can be topics of the same template. Any body of
information is then written as a tree that reads the same way at every depth.

The name is the field's own. A **topic** is the unit of DITA and of topic-based authoring
([information typing](evidence/information-typing/frame.md)). Document models call the same unit a content object
([document model](evidence/document-model/frame.md)), and studies of trees on screen call it a node
([progressive disclosure](evidence/progressive-disclosure/frame.md)).

This page in French: [README.fr.md](README.fr.md).

> **Status:** the literature review is done (2026-10-29): three multivocal reviews, 218 sources, in
> [evidence](evidence/). The topic template and its check are written; no reader study has tested them. It is not
> an official standard, not a peer-reviewed study and not a new result.
>
> **How it is made:** with Claude, an AI assistant by Anthropic, under the maintainer's direction, the way
> reader-ergonomics was made. Corrections are welcome as issues.

## Where it sits

```text
        uses ──▶ (points to what it depends on)

 level 2   the genre extensions: reader-ergonomics-academic,          other projects
           reader-ergonomics-presentations, reader-ergonomics-software-design
                                 │                                        │
                                 ├────────────────────────────────────────┘
                                 ▼  may use the topic as their skeleton (a hypothesis)
 level 1   reader-ergonomics-topic    one topic shape, nested to any depth, its review and its check
                                 │
                                 ▼  obeys the principles; CI runs their checks here
 level 0   reader-ergonomics          how any text serves its reader
```

- **It obeys [reader-ergonomics](https://github.com/Tewf/reader-ergonomics)**, so it sits one level above it, and a
  project that uses it sits above it in turn. No level depends on a level above it.
- **reader-ergonomics never links to it:** the standard links to no extension ([extending.md](https://github.com/Tewf/reader-ergonomics/blob/257958ed3bcb26d2c213bb1b0a66ac19e9645157/extending.md)).
  This repository links down to the standard, never up to the extensions.
- **That the projects above will use it is a hypothesis.** If none does, this repository still answers one question.

## Scope

| | What | Why |
|---|---|---|
| in | the evidence on recursive templates, from the reader's side | the reader is the object, as in reader-ergonomics |
| in | the topic shape: the blocks every topic has, and how a topic holds or points to other topics | one template, kept in one place |
| in | one check a program runs on a topic at any depth | what a program can check, a program checks |
| out | the genres: papers, proofs, talks, design documents | they stay in their own repositories |
| out | what a research claim is, how it is proved or verified | another problem, with its own evidence |

## What the review found

Each answer links the review that holds its evidence; a grade says how strong that evidence is.

| Question | Answer | Grade | Review |
|---|---|---|---|
| **Depth.** Readers recall the top levels best, and reader-ergonomics caps an outline at three levels. Can the recursion be unbounded in storage and capped in what a reader sees? | Yes, as a design, under three conditions: the path to the root is shown, what most readers need sits above the first fold, and each folded topic shows a summary. Readers rarely open a second layer, and for agents a second level of folding never helped. | supported with caveat; never tested directly | [progressive-disclosure](evidence/progressive-disclosure/) |
| **Self-reference.** A topic type whose children are topics gives a tree; a topic that contains itself is a cycle. Which does the template need? | The recursive type only. Every document model read keeps each instance a finite tree, and forbids, reports or caps a cycle. | convention, across 14 systems | [document-model](evidence/document-model/) |
| **Graphs.** A topic used by two parents no longer forms a tree. Is the tree only the storage, and the graph the meaning? | The standards store a graph of trees and give each reading one tree: one containing parent, any other parent by reference. No study of how readers meet a reused unit was found. | convention; the reader side is a gap | [document-model](evidence/document-model/) |
| **Genres.** Is the topic what the genre shapes share, or a rival to them? | What they share, as practice already does: DITA derives concept, task and reference from one base topic. Typing alone showed no learning gain in Horn's own 1969 test (19.56 against 17.65, 41 students). Whether a reader who knows the base reads a derived type better is untested. | convention; the transfer is this repository's open question | [information-typing](evidence/information-typing/) |

## The baseline the topic must beat

| Reader | Baseline | Control |
|---|---|---|
| a person, the unit and its types | the DITA 1.3 base topic with its concept, task and reference types, its maps and its reuse by reference, validated, cycles reported | the same content as untyped prose |
| a person, the tree on a page | the same content as one document of at most three heading levels, its contents always visible beside it | the fully expanded tree |
| a model | passages retrieved in the document's own order, at a matched token budget | a tree of summaries |

The comparison measures finding, gist against detail, recall after a delay, transfer to a derived type never seen,
and what a program check catches. Each review's `baseline.md` gives the design.

## The topic template

| Part | Summary |
|---|---|
| [shapes](shapes/) | the topic, the base every shape derives from, and how the four general shapes of reader-ergonomics fit it |
| [the check](checks/local/topic.py) | runs on every topic of this repository, at any depth: title, summary, listed by its parent with that summary, no inclusion cycle |
| [decisions](decisions/) | one record per architectural choice, each opening with the decision in one sentence |

- The topic has five blocks: title, summary, body, contents and see also. Each is traced to a principle of
  reader-ergonomics and to the evidence here ([topic](shapes/topic.md)).
- The four general shapes all fit, with two renames and one merge: a commit's subject line is both its title and its
  summary. They are the material the topic was drawn from, so the fairer test is the next line
  ([the table](shapes/README.md)).
- On six forms of the genre extensions it was not built from, five fit; a decision record with no summary does not.
  Run on those three repositories, 113 documents, the check finds 7 faults once their review steps are declared
  as types.
- The first shape derived from the topic is the [decision record](shapes/decision-record.md). This repository's own
  decision records follow it, and the check verifies that each one says so.
- This repository is its own first tree of topics: the check runs on it in CI, and the tests of the check are in
  [checks/test_topic.py](checks/test_topic.py).

## Next

1. Compare the topic with the baseline above, on readers: the design is in each review's `baseline.md`.
2. The genre extensions may derive their shapes from the topic; each would say so in its own repository.

## Check it

```sh
git clone https://github.com/Tewf/reader-ergonomics
python3 reader-ergonomics/checks/run.py path/to/this/repository
```

CI runs the same checks on every push, and a run fails on any error ([checks.yml](https://github.com/Tewf/reader-ergonomics-topic/blob/master/.github/workflows/checks.yml)). Every
push to master also renders the site, [tewf.github.io/reader-ergonomics-topic](https://tewf.github.io/reader-ergonomics-topic/)
([pages.yml](https://github.com/Tewf/reader-ergonomics-topic/blob/master/.github/workflows/pages.yml)).

## Licence

Code under the [Apache License 2.0](LICENSE); prose under [CC BY 4.0](LICENSES/CC-BY-4.0.txt). Reuse it as you wish, with
credit to this repository; [CITATION.cff](CITATION.cff) gives a citation if you need one.
