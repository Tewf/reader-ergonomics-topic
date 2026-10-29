# Progressive disclosure: showing a tree of text nested to any depth

Question: how is a tree of units nested to any depth shown to a reader, so the top levels are kept and any leaf is reached? And what does the evidence say about depth, expansion and navigation in nested text?

- It covers published research and public practice, for human readers and for models as readers.
- It holds 47 formal sources, 41 of them new, 3 of those by handoff from the information-typing review.
- It adds 23 new grey sources, scored out of 20 (8 from the web, 15 threads or posts); 4 fall below the threshold of 10 and are used as examples only.

## Files

| File | Role |
|---|---|
| [protocol](protocol.md) | how the pool on folding, zooming and hypertext was searched and scored |
| [sources](sources.md) | the flow from hits to sources, then each source with its quality |
| [frame](frame.md) | step 1: the problem, and what interface, hypertext and model research call it |
| [review](review.md) | step 2: fisheye views, folded text, hypertext structure, outliners, summary trees |
| [state of the art](state-of-the-art.md) | step 3: most adopted against best evidence; what a capped view can show |
| [position](position.md) | step 4: depth in storage against depth in view, and its three conditions |
| [against](against.md) | readers who leave folds closed, null results, the limits of the studies |
| [baseline](baseline.md) | step 5: three heading levels with contents beside, and document-order retrieval |
| [bibliography](../bibliography.md) | every cited work, shared by the three reviews |
| `flow.json` | the flow as data, drawn in the figure of [sources](sources.md) |

## The repository's question

- Can depth be unbounded in storage and capped in what a reader sees? The evidence allows it as a design, supported with caveat, never measured as such.
- Three conditions come with it: show the path to the root, keep what most readers need above the first fold, and give every folded node a summary that stands for it ([position](position.md)).

## Claims

| Claim | Grade | Where |
|---|---|---|
| A fisheye of a tree keeps the focus, its neighbours and its ancestral line; in a regular tree its size grows with the logarithm of the tree | supported with caveat (a property of the definition, Furnas 1986) | review.md 1 |
| Fisheye views beat flat windows for judging order in an unfamiliar hierarchy: 52% correct with two flat views, 64% with one fisheye, 75% with two | measured, one study, 20 subjects | review.md 1 |
| Expand/contract contents beat a fully expanded list for retrieval in a three-level tree of 1,296 items on five of nine tasks, lost on the easiest, and did not differ on three | measured, one study, 41 novices | review.md 2 |
| Overview plus detail gives the best comprehension of a document; shrinking text by importance is faster and understood less | measured, one study (secondary) | review.md 2 |
| Readers of a layered document answer less accurately on topics left out of its first layer (measured); the authors infer that few went past it | measured, one study, 749 Internet users; the inference not measured | review.md 2 |
| Sections open on load drew more reading time than folded ones on mobile Wikipedia | convention, with data: one uncontrolled test, on a grey source | review.md 7 |
| Hierarchical links beat network links for novices finding facts; hierarchy with cross-links can beat both | measured (secondary) | review.md 3 |
| No interface for focus and context wins on every task; distortion rarely improves performance | measured (one review) | review.md 0; against.md |
| On maps and trees, readers preferred an overview without performing better with it | measured, two studies (both secondary) | against.md |
| For strong long-context models, passages in document order match or beat trees of summaries | measured (benchmarks, matched budgets) | review.md 6 |
| For agents, one level of disclosure is enough, and a second can collapse accuracy | measured, one preprint | review.md 6 |
| A capped view must elide the ancestors of nodes deeper than the cap | inference from the definitions | state-of-the-art.md |
| Outliners store and show unbounded depth and are widely used: 1,471,149 downloads of one plugin, 45,407 stars for one tool | measured, descriptive | state-of-the-art.md |
| At most two disclosure levels; never an accordion inside another | convention, untested | review.md 5, 7 |
| Depth unbounded in storage, capped at three levels in view, with the path to the root shown | supported with caveat (no direct test) | position.md |

## Named baseline

- Human reader: **B1**, the same content as one linear document with at most three heading levels and its contents always visible beside it (overview plus detail); **B0**, the fully expanded tree, as the control.
- Model reader: **DOS RAG**, passages retrieved in the document's original order at a matched token budget (Laitenberger 2025); one level of disclosure for agents (He 2026).
- Comparison: timed retrieval at known depths, blind-graded summaries, recall by level, opens below the fold, path naming; crossover with a one-week delay.
- The open question gets its own test: storage depth 3, 5 and 7 under a view capped at three ([baseline](baseline.md)).

## General principles linked, not reviewed again

- [Overview first](https://github.com/Tewf/reader-ergonomics/blob/03cfbc9dd1d243aa86f8ba3168abc61be2bab19f/principles/document/overview-first.md)
- [Shallow outline](https://github.com/Tewf/reader-ergonomics/blob/03cfbc9dd1d243aa86f8ba3168abc61be2bab19f/principles/document/shallow-outline.md)
- [Signal the structure](https://github.com/Tewf/reader-ergonomics/blob/03cfbc9dd1d243aa86f8ba3168abc61be2bab19f/principles/page/signal-the-structure.md)
