# Recursive atom

[![Checks against reader-ergonomics](https://github.com/Tewf/recursive-atom/actions/workflows/checks.yml/badge.svg)](https://github.com/Tewf/recursive-atom/actions/workflows/checks.yml)
[![Site](https://github.com/Tewf/recursive-atom/actions/workflows/pages.yml/badge.svg)](https://tewf.github.io/recursive-atom/)

One template for a unit of writing, called a **node**, whose parts can be nodes of the same template. Any body of
information is then written as a tree that reads the same way at every depth.

> **Status:** the literature review is done (2026-10-29): three multivocal reviews, 218 sources, in
> [evidence](evidence/). The node itself is not written yet. It is not an official standard, not a peer-reviewed study
> and not a new result.
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
                                 ▼  may use the node as their skeleton (a hypothesis)
 level 1   recursive-atom             one node shape, nested to any depth, its review and its check
                                 │
                                 ▼  obeys the principles; CI runs their checks here
 level 0   reader-ergonomics          how any text serves its reader
```

- **It obeys [reader-ergonomics](https://github.com/Tewf/reader-ergonomics)**, so it sits one level above it, and a
  project that uses it sits above it in turn. No level depends on a level above it.
- **reader-ergonomics may link to it, never copy it:** a link is a reference, not a dependency.
- **That the projects above will use it is a hypothesis.** If none does, this repository still answers one question.

## Scope

| | What | Why |
|---|---|---|
| in | the evidence on recursive templates, from the reader's side | the reader is the object, as in reader-ergonomics |
| in | the node shape: the blocks every node has, and how a node holds or points to other nodes | one template, kept in one place |
| in | one check a program runs on a node at any depth | what a program can check, a program checks |
| out | the genres: papers, proofs, talks, design documents | they stay in their own repositories |
| out | what a research claim is, how it is proved or verified | another problem, with its own evidence |

## What the review found

Each answer links the review that holds its evidence; a grade says how strong that evidence is.

| Question | Answer | Grade | Review |
|---|---|---|---|
| **Depth.** Readers recall the top levels best, and reader-ergonomics caps an outline at three levels. Can the recursion be unbounded in storage and capped in what a reader sees? | Yes, as a design, under three conditions: the path to the root is shown, what most readers need sits above the first fold, and each folded node shows a summary. Readers rarely open a second layer, and for agents a second level of folding never helped. | supported with caveat; never tested directly | [recursive-depth](evidence/recursive-depth/) |
| **Self-reference.** A node type whose children are nodes gives a tree; a node that contains itself is a cycle. Which does the template need? | The recursive type only. Every document model read keeps each instance a finite tree, and forbids, reports or caps a cycle. | convention, across 14 systems | [node-model](evidence/node-model/) |
| **Graphs.** A node used by two parents no longer forms a tree. Is the tree only the storage, and the graph the meaning? | The standards store a graph of trees and give each reading one tree: one containing parent, any other parent by reference. No study of how readers meet a reused unit was found. | convention; the reader side is a gap | [node-model](evidence/node-model/) |
| **Genres.** Is the node what the genre shapes share, or a rival to them? | What they share, as practice already does: DITA derives concept, task and reference from one base topic. Typing alone showed no learning gain in Horn's own 1969 test (19.56 against 17.65, 41 students). Whether a reader who knows the base reads a derived type better is untested. | convention; the transfer is this repository's open question | [typed-units](evidence/typed-units/) |

## The baseline the node must beat

| Reader | Baseline | Control |
|---|---|---|
| a person, the unit and its types | the DITA 1.3 base topic with its concept, task and reference types, its maps and its reuse by reference, validated, cycles reported | the same content as untyped prose |
| a person, the tree on a page | the same content as one document of at most three heading levels, its contents always visible beside it | the fully expanded tree |
| a model | passages retrieved in the document's own order, at a matched token budget | a tree of summaries |

The comparison measures finding, gist against detail, recall after a delay, transfer to a derived type never seen,
and what a program check catches. Each review's `baseline.md` gives the design.

## Next: the node

1. Write the node: a base of a few blocks, each traced to a principle of reader-ergonomics and to the evidence here.
2. Derive the existing genre shapes from it, as the node plus what each shape changes. A shape that cannot be derived
   without loss shows the base is wrong.
3. Write the one check a program runs on a node at any depth.
4. Compare with the baseline above.

## Check it

```sh
git clone https://github.com/Tewf/reader-ergonomics
python3 reader-ergonomics/checks/run.py path/to/this/repository
```

CI runs the same checks on every push, and a run fails on any error ([checks.yml](https://github.com/Tewf/recursive-atom/blob/master/.github/workflows/checks.yml)). Every
push to master also renders the site, [tewf.github.io/recursive-atom](https://tewf.github.io/recursive-atom/)
([pages.yml](https://github.com/Tewf/recursive-atom/blob/master/.github/workflows/pages.yml)).

## Licence

Code under the [Apache License 2.0](LICENSE); prose under [CC BY 4.0](LICENSES/CC-BY-4.0.txt). Reuse it as you wish, with
credit to this repository; [CITATION.cff](CITATION.cff) gives a citation if you need one.
