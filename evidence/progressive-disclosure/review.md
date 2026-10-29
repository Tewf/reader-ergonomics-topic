# Review

This file reads the literature on showing a nested tree of text to a reader. Strands run from existing reviews to the seminal work, then one strand per sub-question, then practice.

Terms are in [frame](frame.md); markings and scores, in the [evidence README](../README.md#method).

## 0. Existing reviews

- Cockburn 2009 (read in full): reviews overview plus detail, zooming, focus plus context and cue-based interfaces.
  - Its summary (section 8): none of the four is ideal, and research "fails to provide clear guidelines" on which fits which task.
  - It found one document-reading comparison and a few on program text and trees; strands 2 and 4 cite them through it.
- Chen 1996 (abstract, secondary): a meta-analysis of 23 hypertext experiments, 56 effect sizes. Hypertext users were more effective and less efficient; maps of the organisation raised usefulness; results varied strongly.
- Dillon 1998 (abstract): hypermedia helps learning only for tasks of repeated searching and manipulation; method flaws limit every conclusion.
- Brusilovsky 2001 (read in the relevant sections): a survey of adaptive hypermedia. It lists **stretchtext**, text that expands in place, among the canned-text adaptation technologies, beside inserting, altering and dimming fragments.
- DeStefano 2007 is held by [learning-science](https://github.com/Tewf/reader-ergonomics/blob/master/evidence/learning-science/review.md) (strand 6) and not read again.
- Located by title only: Knutov 2009 (adaptive hypermedia survey), Lam 2011 (multi-level interfaces from study evidence).
- How this review differs: text nested to any depth, not maps or images; it adds layered documents, outliners and model readers (position.md).

## 1. Seminal work

- Stretchtext is Nelson's term, coined in 1970 (Wikipedia 2026c; Nelson's own text not read).
- Furnas 1986 (read): the **fisheye view** shows a point when its a priori importance minus its distance from the focus passes a threshold.
  - On a tree, importance is minus the depth and distance is the path length; the view keeps the ancestral line, then siblings, then cousins (Figure 2).
  - In a regular tree the view is a logarithmically compressed display, computed in time proportional to the view, not the tree (section 3).
  - In its experiment, 20 subjects judged the order of two parts of an unfamiliar botanical hierarchy, 16 pairs each (page 21).
  - Correct answers: 52% with two flat views, 64% with one fisheye and one flat, 75% with two fisheyes.
  - A footnote links fisheye views of outlines to the outline processors then reaching the market.
- Early systems for a global and a detailed view: Engelbart 1968 (cited so by Furnas 1986), Pad++ for zooming (Bederson 1994), the document lens for continuous distortion (Robertson 1993).
- None of these three was read beyond its title and those citations.
- Carroll 1984 (abstract): blocking error-prone function for new users gave faster learning; the control group spent almost a quarter of its time recovering from errors.
- Nielsen 2006b names deferring advanced or rare features to a second level **progressive disclosure**, and dates the idea to over 30 years before 2006.

## 2. Q1: folded and expandable text

| Source | What was compared | Result | Read |
|---|---|---|---|
| Furnas 1986 | flat window against fisheye of a hierarchy | 52% correct with two flat views, 64% with one of each, 75% with two fisheyes, on order judgments; 20 subjects, 16 pairs each | full text |
| Egan 1989 | SuperBook, a hypertext book whose contents expands chapters and sections (Chimera 1994), against print | better search and open-book essays; MiteyBook, its PC version, searched about 25% faster and 25% more accurately than print | abstract (secondary) |
| Chimera 1994 | contents of 1,296 items, three levels deep, 48 screens when fully expanded: stable list, expand/contract, multi-pane | both dynamic interfaces significantly faster for many of nine tasks (41 novices); on the easiest task, the stable list and multi-pane beat expand/contract (p < .01) | technical report version |
| Hornbæk 2003 | linear text, overview plus detail, fisheye text keeping headings and first and last paragraphs | fisheye read faster at a cost in comprehension; overview plus detail understood best and preferred | through Cockburn 2009 section 7.2.4 (secondary) |
| Höök 1997 | adaptive stretchtext that hides what the inferred task does not need, against the same system fixed | fewer actions, clear preference, and answers shaped by what the system chose to show | abstract (secondary) |
| McDonald 2009 | layered privacy policy (short layer, full text behind) against full text and a standard format, 749 participants | layered was faster but less accurate on topics not in the short layer; cookie question 78% correct layered | authors' version, section 4 |
| Heinonen 2022 | maintenance instructions in DITA layered by skill level, the reader choosing the depth; user studies in three countries | well received across skill levels; observation, interviews and questionnaires, no comparison condition | abstract (secondary) |

- McDonald 2009 concludes that few participants went beyond the first page of a layered policy (section 4.1).
- Springer 2020 (abstract): in four studies of an explained system, users gained from simple feedback first and the detail on demand; it is about explanations, not documents.
- Located, not read: Zellweger 2000 (fluid documents, an observational study), Boyle 1994 (MetaDoc, adaptive stretchtext).
- Johnson 2013 (a blog, 13 of 20, scored in information-typing): one DITA topic per contents entry scatters brief tasks; he would nest them under a parent and favours collapsible sections; no data.

## 3. Q2: hierarchical against networked hypertext

The linked reviews hold the overview and map effects: [reading-order](https://github.com/Tewf/reader-ergonomics/blob/master/evidence/reading-order/review.md) (strand 1) and [learning-science](https://github.com/Tewf/reader-ergonomics/blob/master/evidence/learning-science/review.md) (strand 6), with DeStefano 2007 and Amadieu 2009.

- Mohageg 1992 (abstract): hierarchical links beat network links by 49 s per task on average; adding network links to the hierarchy gave no consistent gain for novices.
- McDonald 1998 (abstract): hierarchy plus cross-references beat pure hierarchy and pure network for finding answers; prior knowledge helped in every structure.
- Located, abstract not readable on the day: McDonald 1996, Calisir 2003, Potelle 2003.

## 4. Q3: focus plus context and zooming for documents and trees

- Hornbæk 2002 (abstract): 32 subjects, zoomable maps with and without an overview. Accuracy did not differ and 80% preferred the overview; on the map built in levels with semantic zoom, subjects were faster without it.
- Through Cockburn 2009 (section 7.2, secondary):
  - Jakobsen 2006: a fisheye of source code that folds by degree of interest was significantly faster than a flat listing, and preferred.
  - Nekrasovski 2006: on large trees, pan and zoom beat a rubber-sheet fisheye; an overview did not change task time.
  - Plaisant 2002 and the hyperbolic-tree studies: results depend on the task and on how well labels predict what lies below.
  - Baudisch 2002: a focus plus context screen was up to 56% faster than overview plus detail and zooming on static graphs.
- Cockburn 2009 (section 5.2.2): folding of program blocks is standard in editors and of sections in word processors, while automatic folding by degree of interest stays in research labs.

## 5. Q4: levels in one view

- No study found varies the depth of a stored tree while holding the depth in view fixed.
- Measured levels: Chimera 1994 tested three levels in view at most; Furnas 1986 shows the ancestral line plus one or two rings around the focus.
- For menus, two levels beat three: [file-structure](https://github.com/Tewf/reader-ergonomics/blob/master/evidence/file-structure/against.md) (Kiger 1984; Larson 1998).
- For proofs, about 4 to 10 steps per level, a convention: [mathematical-writing](https://github.com/Tewf/reader-ergonomics-academic/blob/master/evidence/mathematical-writing/review.md).
- Nielsen 2006b: designs beyond two disclosure levels typically have low usability; no data given.
- For model readers, He 2026 (strand 6) found one level of disclosure enough and a second harmful.
- A node read alone loses its place in the tree; in a corpus of topic-based documentation, relative clauses carry the context of related topics (Swarts 2022, abstract).

## 6. Q6: trees of summaries for models as readers

- Wu 2021 (abstract, secondary): a book summarized section by section, then the summaries recursively; matched human quality on about 5% of books.
- Sarthi 2024 (RAPTOR, read): leaves are chunks, parents are summaries of clusters of children, about 72% shorter (Appendix C).
  - With GPT-4 it reached 82.6% on QuALITY against a previous best of 62.3% (Table 7); 18.5% to 57% of retrieved nodes were non-leaves (Appendix I.2).
  - Searching all layers at once, the tree flattened, beat descending it layer by layer on 20 QASPER stories (section 3, Figure 3).
- Laitenberger 2025 (read): passages retrieved and kept in the document's original order matched or beat RAPTOR and an agent at matched token budgets.
  - On ∞Bench at 30K tokens: 93.1% against 87.8% for the same passages ordered by similarity, and 2 to 8 points above the multi-stage methods (section 3).
  - RAPTOR without its summaries beat RAPTOR with them; its original ablation used a 3B reader limited to 400 tokens (section 4).
- He 2026 (read): agents reading books on ∞Bench, three harnesses, three model families.
  - A second level of disclosure never beat one level and sometimes collapsed accuracy: 0.9126 to 0.6398 on one cell (Table 1).
  - With 20 books staged, raw navigation fell to 0.26 on English open questions where one level held 0.46.
- Jayraj 2026 (abstract, secondary): a tree used only to navigate, emitting leaves, matched the strongest flat retriever; the gain came from navigation, not summaries.
- Chen 2023 (abstract): a model walks a tree of summary nodes to answer; better than long-context and retrieval baselines. Edge 2024 (abstract) summarizes graph communities to answer questions about a whole corpus; it is a graph, not a tree.
- Mortezaagha 2026 (abstract, secondary): on 2,359 PubMed Central articles, content-similarity retrieval had the best MRR (0.517) but drew from one section; structure-aware retrieval drew from up to 15.6 times more sections.
- Chang 2024 (abstract, secondary): over 100 books, merging summaries up a hierarchy was more coherent than updating one running summary, which kept more detail.

## 7. Practice

| Who | Form | Evidence of use |
|---|---|---|
| WHATWG 2026 | `details` and `summary`: one disclosure; a shared `name` makes an exclusive accordion; not for footnotes or tabs | the HTML standard, updated 2026-10-26 |
| W3C 2026b | tree view pattern: nested groups, expand with Right, collapse with Left; level and position given only when nodes load lazily | no depth limit stated |
| GOV.UK 2026a | accordion: not for content all users need; never inside another accordion; not all users notice it | government design system; research reported without numbers |
| GOV.UK 2026b | details: never hide what most users need; some users avoid it, fearing it leaves the page | same |
| Nielsen 2006b | progressive disclosure: few options first, at most two levels | company article, no data |
| Wikimedia 2016 | mobile Wikipedia folds every section below the lead; a test opened them | expanded: reading time 190 s against 146 s at the 90th percentile, 53 s against 38 s at the 75th |
| Outliners (Logseq, SiYuan, Obsidian plugins) | nested bullets, fold, zoom into one bullet as the root | counts in state-of-the-art.md |
| Code editors | folding of blocks and `#region` | standard feature (Cockburn 2009) |
| Tree retrieval (RAPTOR, GraphRAG, PageIndex) | trees or graphs of summaries for model readers | counts in state-of-the-art.md; PageIndex reports 98.7% on FinanceBench itself (VectifyAI 2026, example only) |

- Wikimedia 2016 is not a strict A/B test: about 0.05% of mobile users per group, one week of 2016-01.
- Wang 2023 (example only, held by [typography-and-layout](https://github.com/Tewf/reader-ergonomics/blob/master/evidence/typography-and-layout/review.md)) says folded content may be missed.

Q/A sites (searched 2026-10-29; 12 threads, 2 under 10 of 20; strings in [protocol](protocol.md)). Practitioner opinion, no data.

- Unbounded depth is a known problem: indenting fails after a few levels of nested comments; one site moves a thread to a new page after about ten levels (UXSE 2010).
- A path of a hundred decisions needs checkpoints, not a longer breadcrumb (UXSE 2015).
- Nesting folds is advised against: an accordion inside an accordion confuses (UXSE 2012a; UXSE 2014b), as GOV.UK 2026a says.
- Do not hide answers to save scrolling; list the questions with anchor links instead (UXSE 2012b).
- A deep heading should name itself in full, since a reader may meet it without its ancestors (WSE 2013); whether every level carries text of its own divides practitioners (WSE 2018e).
- One long page or many granular ones: cohesion matters more than length, and a tree keeps overview pages near the root (WSE 2018c, scored in information-typing).
- UXSE 2018b (example only) asks the same of a three-level nest.
- Folding code hides a long block but gives it no name, scope or dependencies, which a function does (SESE 2014e; SESE 2011o).
- Depth can be shown by colour or a gutter per level instead of indentation (SESE 2011r).
- Examples only: a five-level tree on one mobile screen (UXSE 2018a); "expand all" for searching folded sections (UXSE 2016).
