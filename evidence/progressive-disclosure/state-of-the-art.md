# State of the art, per sub-question

Two records are kept apart: most adopted (what people use) and best evidence (what a study measured). Terms are defined in [frame](frame.md); sources are in [review](review.md).

| Sub-question | Most adopted | Best evidence | Measured how |
|---|---|---|---|
| Q1 folded and expandable text | accordion and `details` (WHATWG 2026; GOV.UK 2026a, 2026b) | Chimera 1994; McDonald 2009; Hornbæk 2003 (secondary) | timed retrieval on a 1,296-item contents, 41 novices; accuracy and time on privacy policies, 749 adults; essays and questions on scientific papers |
| Q2 hierarchy against network | hierarchy with cross-links | Mohageg 1992; McDonald 1998; Chen 1996 (all by abstract) | time per retrieval task; answers found; meta-analysis of 23 experiments |
| Q3 focus plus context, zooming | a contents pane beside the text (overview plus detail); folding in editors | Cockburn 2009 (review); Hornbæk 2002 (secondary); Jakobsen 2006 (secondary) | task time, accuracy, preference; no technique wins across tasks |
| Q4 levels in one view | three heading levels (reader-ergonomics shallow outline); at most two disclosure levels (Nielsen 2006b, example of practice); no accordion inside another (GOV.UK 2026a) | for menus, two levels beat three (file-structure, linked); for agents, one level of disclosure beat two (He 2026) | menu search time; question answering on ∞Bench |
| Q5 outliners and block editors | Logseq, SiYuan, Obsidian outliner plugins (counts below) | none found | no study of reading an outline in an outliner was found |
| Q6 trees of summaries for models | GraphRAG and PageIndex repositories (counts below) | Laitenberger 2025; He 2026; Sarthi 2024 | matched-token comparisons on QuALITY, NarrativeQA, ∞Bench |
| Q7 hidden content left unread | sections folded by default on mobile Wikipedia (Wikimedia 2016) | McDonald 2009; Wikimedia 2016 | accuracy on topics outside the first layer; reading time with sections open or folded |

## Adoption counts, descriptive, taken 2026-10-29

| Count | Value | Caveat |
|---|---|---|
| stars, Logseq (outliner, created 2020) | 45,407 | interest, not use (GitHub 2026c) |
| stars, SiYuan (block editor, created 2020) | 46,984 | same |
| repositories tagged `outliner` | 137 | self-tagged |
| repositories tagged `org-mode` | 1,271 | self-tagged |
| downloads, Obsidian Outliner plugin | 1,471,149 | of 9,606 community plugins; the largest has 8,763,578 (Obsidian 2026) |
| downloads, Obsidian Zoom plugin (a bullet as the root) | 113,488 | same |
| stars, RAPTOR reference code (created 2024) | 1,775 | interest, not use |
| stars, GraphRAG (created 2024) | 36,477 | a graph of summaries, not a tree |
| stars, PageIndex (created 2025) | 39,880 | its benchmark figure is the vendor's own (VectifyAI 2026, example only) |

- Counts come from the public GitHub API and Obsidian's published plugin statistics, read without a key.
- No count of web pages using `details` was found: the Web Almanac markup chapters of 2021 and 2024 do not report it.

## Upper bounds (achieved)

- A fisheye of a regular tree is a logarithmically compressed view of it, computable in time proportional to the view (Furnas 1986, section 3).
- On order judgments in an unfamiliar hierarchy, correct answers rose from 52% with two flat windows to 64% with one fisheye and 75% with two (Furnas 1986, 20 subjects, pages 20 to 21).
- On a three-level contents of 1,296 items, expand/contract and multi-pane views were both significantly faster than the fully expanded list on four of nine tasks, and expand/contract on a fifth (Chimera 1994).
- A hypertext book with an expandable contents beat print on search and essays (Egan 1989, secondary).
- A tree of summaries raised QuALITY accuracy to 82.6% with GPT-4, against a previous best of 62.3% (Sarthi 2024, Table 7).
- Retrieval in document order reached 93.1% on ∞Bench at 30K tokens (Laitenberger 2025).
- One level of disclosure kept agents at 0.46 on English open questions over 20 books, where raw reading fell to 0.26 (He 2026).

## Lower bounds and limits (not shown, or shown not to hold)

- No study found varies depth in storage while holding depth in view fixed; whether storage depth matters to a reader is not measured.
- No study found shows a document more than three levels deep in one view to readers.
- A second level of disclosure never helped agents and cut accuracy in some cells, from 0.9126 to 0.6398 (He 2026, Table 1).
- With strong long-context readers, the summaries in a tree did not help: the same pipeline without them did better (Laitenberger 2025, section 4).
- Distortion-based fisheyes have rarely shown performance gains over the usual alternatives (Cockburn 2009, section 8).
- A view of at most k lines cannot hold the whole ancestral line of a node deeper than k, so a capped view of an unbounded tree must elide ancestors. This follows from the definitions; it is not a study.
- Folded or layered text was read less. Readers answered worse on what the first layer left out, and the authors infer few went past it (McDonald 2009). Folded sections drew less reading time (Wikimedia 2016).
