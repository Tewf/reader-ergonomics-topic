# Recursive atom

[![Checks against reader-ergonomics](https://github.com/Tewf/recursive-atom/actions/workflows/checks.yml/badge.svg)](https://github.com/Tewf/recursive-atom/actions/workflows/checks.yml)
[![Site](https://github.com/Tewf/recursive-atom/actions/workflows/pages.yml/badge.svg)](https://tewf.github.io/recursive-atom/)

One template for a unit of writing, called a **node**, whose parts can be nodes of the same template. Any body of
information is then written as a tree that reads the same way at every depth.

> **Status:** set up on 2026-10-29; nothing is written yet beyond the scope. The first job is a literature review, not
> started. It is not an official standard, not a peer-reviewed study and not a new result.
>
> **How it is made:** with Claude, an AI assistant by Anthropic, under the maintainer's direction, the way
> reader-ergonomics was made. Corrections are welcome as issues.

## Where it sits

```text
        uses ──▶ (points to what it depends on)

 level 2   reader-ergonomics-academic   reader-ergonomics-presentations   software-design-writing   other projects
                        │                              │                             │                     │
                        └────────┬─────────────────────┴─────────────────────────────┴─────────────────────┘
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

## The first job: a literature review

Not started. It follows the order of a thesis review:

1. **Frame:** the problem in one sentence, and what each field calls it. The repository may be renamed then; GitHub
   redirects the old address.
2. **Review:** each name below, searched by its academic name, its acronym and its author.
   - the Composite pattern: a part made of parts of the same type;
   - recursive schemas: a schema whose fields can hold the schema itself;
   - DITA: nested topics and maps;
   - transclusion: one block shown inside another without being copied;
   - stretchtext: text that expands in place, level by level;
   - the Pyramid Principle and Information Mapping, read first-hand;
   - structured proofs, and what reader-ergonomics already holds: the levels effect, rhetorical structure theory and
     the shallow outline.
3. **State of the art, and the case against.**
4. **Baseline:** a node template the maintainer has already drafted, compared with a structured proof and a pyramid.

## Questions the review must answer

- **Depth.** Readers recall the higher levels of a text best, and reader-ergonomics caps an outline at three levels.
  Can the recursion be unbounded where it is stored and capped in what a reader sees?
- **Self-reference.** A node type whose children are nodes gives a tree; a node that contains itself is a cycle. Which
  of the two does the template need?
- **Graphs.** A node used by two parents no longer forms a tree. Is the tree only the storage, and the graph the
  meaning?
- **Genres.** reader-ergonomics gives each kind of document its own shape. Is the node what those shapes share, or a
  rival to them?

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
