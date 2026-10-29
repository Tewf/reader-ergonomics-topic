# Frame: the problem and its names

This file states the problem of showing a deep tree of text to a reader, then the names research and practice give it, and the sub-questions the review answers.

## The problem in one sentence

A body of writing is stored as a tree of units nested to any depth. Decide how it is shown, so the reader keeps the top levels in view and can still reach any leaf.

## Terms used in every file of this folder

| Term | Definition |
|---|---|
| **node** | one unit of the tree: a heading or summary that stands for it, and a body that may hold child nodes |
| **depth in storage** | the number of levels the stored tree has |
| **depth in view** | the number of levels a reader sees open at one time |
| **folded** | a node shown by its heading or summary only, its children hidden until the reader opens it |
| **focus** | the node the reader is reading now |
| **context** | what is shown around the focus: its ancestors, siblings, or an overview of the whole |

## What the field calls it

| Field name | What it names | Entry point |
|---|---|---|
| **stretchtext** | text that expands and contracts in place, so the surrounding text stays as context | Wikipedia 2026c: defined in print in 1970, described in an unpublished note by Nelson in 1967 |
| **adaptive presentation**, canned-text adaptation | a system chooses which fragments of a page to show or stretch for this reader | Brusilovsky 2001 |
| **focus plus context** (focus+context, F+C) | focus and context fused in one view, often by eliding or shrinking the far parts | Cockburn 2009 |
| **fisheye view**, **degree of interest** (DOI) | show a node when its importance minus its distance from the focus passes a threshold | Furnas 1986 |
| **overview plus detail** (O+D) | a separate overview pane beside the detail view | Cockburn 2009 |
| **zooming**, **zoomable user interface** (ZUI), **semantic zoom** | one view at a time, moved in scale; semantic zoom changes content, not only size | Bederson 1994; Hornbæk 2002 |
| **expand/contract** table of contents | a contents tree opened one level at a time | Chimera 1994 |
| **hypertext structure**: hierarchical, network, mixed | how the links between nodes are arranged | Mohageg 1992; McDonald 1998 |
| **disorientation**, "lost in hyperspace", cognitive overhead | the reader not knowing where they are or how to go on | Conklin 1987 |
| **layered notice** | a short first layer with the full text one step away | McDonald 2009 |
| **recursive summarization**, **tree-organized retrieval** | a model summarizes chunks, then summaries, into a tree it reads or searches | Wu 2021; Sarthi 2024 |
| **progressive disclosure** for agents | an agent loads a short description first and the body on demand | He 2026 |

## What practitioners call it

| Practitioners say | The field says |
|---|---|
| accordion, collapsible section, expander, "show more" | stretchtext; folded node |
| `details` and `summary` (HTML), disclosure widget | stretchtext with one level (WHATWG 2026) |
| tree view, outline view, sidebar navigation | expand/contract contents; fisheye of a tree |
| progressive disclosure, staged disclosure | disclosure of function, later of content (Nielsen 2006b; Carroll 1984) |
| code folding, `#region` | manual fisheye of program text (Cockburn 2009) |
| outliner, block editor, zoom into a bullet ("hoist") | outline processor; zooming on a subtree |
| breadcrumbs | the ancestral line of the focus, the zero-order fisheye of Furnas 1986 |
| table of contents beside the text, minimap | overview plus detail |
| skills, llms.txt, "load on demand" | progressive disclosure of context (He 2026; linked review below) |

## Sub-questions

| Id | Question |
|---|---|
| Q1 | Does showing a unit with its children folded change comprehension, search time or recall? |
| Q2 | Hierarchical against networked hypertext, beyond what the linked reviews hold |
| Q3 | Focus plus context, fisheye and zoomable views of documents and outlines |
| Q4 | How many levels a reader handles in one view, and whether depth in storage matters once depth in view is capped |
| Q5 | Outliners and block editors in practice, with adoption numbers |
| Q6 | Trees of summaries for models as readers, measured on benchmarks |
| Q7 | Hidden content left unread, disorientation, deep nesting |

## Search terms tried, three ways

- Academic: stretchtext, expandable text, collapsible outline, progressive disclosure, focus plus context, fisheye view, overview plus detail, zoomable user interface, hypertext structure, disorientation, layered notice, recursive summarization, tree-organized retrieval.
- Acronym: F+C, O+D, ZUI, DOI, RAG, RAPTOR.
- Author: Nelson, Furnas, Bederson, Cockburn, Hornbæk, Shneiderman, Chimera, Egan, McDonald, Rada, Brusilovsky, Höök, Sarthi, Wu.
- The word "outliner" could not be searched: both engines returned unrelated millions or tens of thousands, so outliners are covered through practice (protocol section 4).

## Not reviewed here, linked instead

- Recall of the top levels of a text, the **levels effect**: [psycholinguistics](https://github.com/Tewf/reader-ergonomics/blob/e8864477a53d713251ba42a4cf7b7a0d761243a2/evidence/psycholinguistics/review.md).
- Depth against breadth of menus and folders: [file-structure](https://github.com/Tewf/reader-ergonomics/blob/e8864477a53d713251ba42a4cf7b7a0d761243a2/evidence/file-structure/against.md).
- General before detail, advance organizers, zoom-lens sequencing: [reading-order](https://github.com/Tewf/reader-ergonomics/blob/e8864477a53d713251ba42a4cf7b7a0d761243a2/evidence/reading-order/review.md).
- Hypertext cognitive load, signaling, segmenting: [learning-science](https://github.com/Tewf/reader-ergonomics/blob/e8864477a53d713251ba42a4cf7b7a0d761243a2/evidence/learning-science/review.md).
- Collapsed content missed, as one company article: [typography-and-layout](https://github.com/Tewf/reader-ergonomics/blob/e8864477a53d713251ba42a4cf7b7a0d761243a2/evidence/typography-and-layout/review.md).
- Progressive disclosure of context to agents, instruction files: [llm-readers](https://github.com/Tewf/reader-ergonomics/blob/e8864477a53d713251ba42a4cf7b7a0d761243a2/evidence/llm-readers/review.md).
- Hierarchical proofs, Lamport's steps and levels: [mathematical-writing](https://github.com/Tewf/reader-ergonomics-academic/blob/master/evidence/mathematical-writing/review.md).
- Slide builds as progressive disclosure: [presentations](https://github.com/Tewf/reader-ergonomics-presentations/blob/master/evidence/presentations/review.md).
- Storing the tree, reuse and validation: topic document-model of this repository; unit types: topic information-typing.
