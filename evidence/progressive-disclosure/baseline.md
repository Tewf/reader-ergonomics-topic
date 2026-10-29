# Baseline: what the node template is compared against

This file names the baseline a nested, foldable node must beat, for a human reader and for a model reader, and how the comparison would be measured. Terms are defined in [frame](frame.md).

## The named baselines

| Reader | Baseline | Why this one |
|---|---|---|
| Human | **B1, shallow outline with overview plus detail**: the same content as one linear document, at most three heading levels, with its contents list always visible beside the text | overview plus detail gave the best comprehension and was preferred in the one document-reading comparison (Hornbæk 2003, secondary); it is the standard practice (Cockburn 2009); the three-level cap is the [shallow outline](https://github.com/Tewf/reader-ergonomics/blob/6d4e324157b17862aa5c5158fde0ba02db992729/principles/document/shallow-outline.md) the node must obey anyway |
| Human, control | **B0, fully expanded tree**: every level open, no contents pane | the "stable" interface of Chimera 1994, which isolates the effect of folding |
| Model | **DOS RAG**: passages retrieved and kept in the document's original order, at a matched token budget (Laitenberger 2025) | it matched or beat summary trees and an agent on three benchmarks |
| Model, agent | **one level of disclosure**: a short description, then an index of chunks, read on demand (He 2026) | no cell rewarded a second level: it tied one level within noise or trailed it (He 2026, tables 1 and 2) |

- The node must beat B1, not B0: beating a fully expanded tree is already shown (Chimera 1994), and B1 is what a careful writer would do without the node.
- For models, beating RAPTOR (Sarthi 2024) is not enough, since simpler baselines already do (Laitenberger 2025).

## Candidate variant to test

- Each node opens with a summary that stands for it when folded.
- A view shows at most three levels: the focus, its children and its siblings, with the path to the root always visible.
- The reader can zoom into any node, which then becomes the root of the view.
- What most readers need sits above the first fold.
- These are hypotheses, graded convention, untested.

## How a comparison would be measured

| Reader task | Outcome | Instrument | Prior study to borrow from |
|---|---|---|---|
| Find a fact | time to correct answer; accuracy | timed questions whose answers sit at known depths: top, middle, leaf | Chimera 1994 (nine timed tasks) |
| Understand the whole | blind-graded summary or essay; recall of high-level against low-level idea units | essay after reading; free recall scored by level | Hornbæk 2003; the levels effect ([psycholinguistics](https://github.com/Tewf/reader-ergonomics/blob/6d4e324157b17862aa5c5158fde0ba02db992729/evidence/psycholinguistics/review.md)) |
| Reach below the fold | share of readers opening folded nodes; accuracy on questions answered only below the fold | logged opens; questions placed by depth | McDonald 2009; Wikimedia 2016 |
| Keep bearings | correct naming of the path from the focus to the root; a lostness measure | prompt at random moments; navigation logs | the disorientation literature (Otter 2000, title only) |
| Depth in storage, with view capped | all outcomes above | the same content stored at depth 3, 5 and 7, each shown capped at three levels, against B1 | none found: this is the gap (position.md) |

- Design: within subjects, crossover, order counterbalanced, a delayed test one week later.
- Report effect sizes with confidence intervals; record preference, but never as the outcome, since preference and performance part ways (Hornbæk 2002).
- Subjects: novices and readers who know the domain, analysed apart, since structure and knowledge interact (McDonald 1998, secondary).

For a model reader:

- Benchmarks: QASPER, NarrativeQA and QuALITY, as in Sarthi 2024; ∞Bench, as in Laitenberger 2025 and He 2026.
- Conditions: node-tree navigation, DOS RAG, and one-level disclosure, at matched token budgets.
- Readers of at least two sizes, since gains from compression shrink with stronger readers (Laitenberger 2025).
- Outcomes: accuracy, tokens read, and whether the answer cites the right leaf.

## A checklist for a document in the baseline's own terms

Per document, B1:

1. At most three heading levels.
2. Every heading names its content and stands alone when read out of context (WSE 2013, an opinion).
3. The main claims sit at the top level, as headings or the first sentence of each part.
4. A contents list is visible beside the text and links every section.
5. Nothing is folded; whatever is optional is marked, not hidden.

