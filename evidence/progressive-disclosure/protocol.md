# Protocol: how the pool of sources was built

This file records every search, count and rule of the progressive-disclosure review. Shared rules: [evidence README](../README.md#method). Searches ran on 2026-10-29. Its terms are defined in [frame](frame.md).

## 1. Why grey literature

Garousi 2019, Table 4, answered for progressive-disclosure: six of seven questions get a yes.

| # | Question | Answer for this review |
|---|---|---|
| 1 | Complex, not solvable from formal literature alone? | yes: accordions, `details`, outliners and folding come from practice |
| 2 | Lack of volume or quality of evidence? | yes: one review (Cockburn 2009) finds no clear guidelines; few studies use documents |
| 3 | Context important? | yes: mobile against desktop, reference against learning, human against model reader |
| 4 | Corroborate research with practice? | yes |
| 5 | Challenge practice with research, or the reverse? | yes: practice nests accordions and trees of summaries; studies question both (position.md) |
| 6 | Would a synthesis serve both communities? | yes |
| 7 | Large practitioner volume? | no for documents as such; yes for outliners (state-of-the-art.md counts) |

## 2. Questions

The sub-questions Q1 to Q7 of [frame](frame.md).

## 3. Existing reviews (Garousi Guideline 2)

- Searched first, by strings R1 to R4 (section 4) and by the lead named in the brief (Cockburn 2009).
- Found: 7. Read in full or in the relevant sections: Cockburn 2009, Brusilovsky 2001. By abstract: Chen 1996, Dillon 1998. By title only: Knutov 2009, Lam 2011. Held by a linked review: DeStefano 2007.
- No systematic review or MLR of folded, expandable or nested text in documents was found; that is a statement about this search.

## 4. Formal search

Count sources: the Semantic Scholar bulk search (title and abstract, no key) and the arXiv search API. OpenAlex was not called: its anonymous daily budget was spent until 00:00 UTC on 2026-10-30; the strings are kept in OpenAlex syntax for a later count. Semantic Scholar matches words and uses its own operators (`+` for AND, `|` for OR), so its counts are not phrase-exact and are noisy upper bounds.

| Id | String as run (Semantic Scholar syntax) | Semantic Scholar | arXiv |
|---|---|---|---|
| R1 | (hypertext \| hypermedia) +("meta-analysis" \| "systematic review" \| "review of") | 2,068 | not run |
| R2 | (stretchtext \| "adaptive presentation" \| "adaptive hypermedia") +(survey \| review) | 139 | not run |
| R3 | ("tree visualization" \| "hierarchy visualization" \| "multi-level interface") +(survey \| review \| "empirical study") | 78 | not run |
| R4 | ("retrieval-augmented generation" \| RAG) +(hierarchical \| tree) +survey | 49 | not run |
| F1 | "stretchtext" | 13 | 0 |
| F2 | "expandable text" | 212 | refused (timeout) |
| F3 | "collapsible" +outline | 77 | not run |
| F4 | "progressive disclosure" | 241 | 40 |
| F5 | "progressive disclosure" +(text \| document \| reading) | 41 | not run |
| F6 | "focus+context" \| "focus plus context" | 1,111 | 17 |
| F7 | "fisheye view" \| "fisheye views" | 278 | 6 |
| F8 | "overview+detail" \| "overview plus detail" | 294 | 8 |
| F9 | "zoomable user interface" \| "zoomable user interfaces" | 221 | 0 |
| F10 | (fisheye \| "overview+detail" \| "focus+context") +(document \| documents \| reading) +(text \| electronic) | 56 | not run |
| F11 | hypertext +structure +hierarchical +(network \| linear) +(comprehension \| navigation) | 50 | 0 (hierarchical AND comprehension) |
| F12 | hypertext +disorientation | 144 | 0 |
| F13 | "outliner" | 1,256,416 (not parsed; unusable) | 23,865 (unusable) |
| F14 | "outline processor" | 415 (noise) | not run |
| F15 | "collapsible outline" \| "outline view" | 121 (noise) | not run |
| F16 | "table of contents" +browsing +hierarchical | 36 | 0 |
| F17 | "recursive summarization" \| "recursively summarizing" | 27 | 12 (A1) |
| F18 | "tree-structured retrieval" \| "tree-organized retrieval" \| "hierarchical retrieval" +(summaries \| summary) +(language model \| LLM) | 9 | 14 (A2) |
| F19 | "hierarchical summarization" +(long documents \| books) +(LLM \| "language models") | 7 | not run |
| F20 | stretchtext \| "expandable text" \| "telescopic text" | 227 | not run |
| F21 | "layered" +("privacy notice" \| "privacy policy" \| "privacy policies") +(comprehension \| format) | 10 | not run |
| F22 | ("layered consent" \| "tiered consent" \| "layered information") +(consent \| comprehension) +(randomized \| trial) | 13 | not run |
| F23 | breadcrumb +navigation +(study \| usability \| experiment) | 88 | not run |
| F24 | "code folding" \| "fisheye" +"source code" +(navigation \| comprehension) | 10 | not run |
| F25 | ("outlining software" \| "outline editor" \| "hierarchical note-taking" \| "networked notes") | 339 (noise) | not run |
| A3 | arXiv only: abs:RAPTOR AND abs:retrieval | not run | 13 |
| A4 | arXiv only: abs:"hierarchical" AND abs:"long document" AND abs:"tree" AND abs:"question answering" | not run | 1 |

- A1 and A2 are the arXiv forms of F17 and F18: A1 `abs:"recursive summarization" OR abs:"recursively summarizing"`; A2 `abs:"tree-structured" AND abs:retrieval AND abs:summar*`.
- Screened by title: the 15 most cited results of each Semantic Scholar string (all results where fewer), and every arXiv result of A1 to A4.
- F13 and F25 were rephrased three ways (outliner, outline processor, outline editor and note-taking); none returned a relevant title. Outliners are covered by practice (section 5).
- Backward snowballing read four reference lists: Furnas 1986 (gave Engelbart 1968 and Nelson's book), Cockburn 2009 (gave Nekrasovski 2006, Plaisant 2002 and the code-folding studies).
- Also Chimera 1994 (gave SuperBook) and He 2026 (gave Edge 2024).
- Forward snowballing: the arXiv strings A3 and F18 return works that cite RAPTOR (Laitenberger 2025, Jayraj 2026); no citation index was paged.
- By handoff from the information-typing review, 2026-10-29: Heinonen 2022, Swarts 2022, Mortezaagha 2026, Johnson 2013, WSE 2018c and the User Experience thread 119762 (UXSE 2018b). Each was verified here against Crossref, arXiv, the page or the Stack Exchange API; none was dropped. Johnson 2013 and WSE 2018c keep the scores information-typing gave them.

## 5. Grey search

- Types and producers were chosen because the components come from practice.
- They are standards bodies (WHATWG, W3C), a government design system (GOV.UK), a usability firm (Nielsen Norman Group), an encyclopedia project's research wiki (Wikimedia), and tool repositories with public counts.
- Engine: a general web search engine, first result page per string. Results personalise and change.

| Id | String as run (abridged) | Screened | Included |
|---|---|---|---|
| G1 | Wikimedia mobile web sections collapsed by default experiment expand all sections research results | 27 | 1 (Wikimedia 2016); Baymard paywalled, excluded |
| G2 | stretchtext Ted Nelson coined Computer Lib Dream Machines (1974) | 18 | 1 (Wikipedia 2026c); one archive page returned 404 |
| P | direct visits to named producers: NN/g progressive disclosure and accordions; GOV.UK accordion and details; W3C tree view pattern; WHATWG `details`; HTTP Archive Web Almanac (2021) and 2024 (markup); five tool repositories; one plugin statistics file | 14 | 6 scored; 2 counts; Web Almanac held no `details` figure; one NN/g page returned 404 |

- Further web searches looked for open copies of formal works: Cockburn 2009, Chen 1996, Chimera 1994, Furnas 1986, Höök 1997, and the conference version of Hornbæk 2003.
- They added no source, and the conference version could not be reached.
- One web result page carried embedded instructions addressed to automated readers; it was ignored and is not a source.

### Q/A sites

Strings RD1 to RD16 ran on 2026-10-29, one reviewer, grey tier 2. Other rules: [evidence README](../README.md#method).: top N = 30 by votes, k = 10, `order=desc&sort=votes&pagesize=30&filter=withbody` on `search/advanced`, API version 2.3, no key and no login.

| Id | String as run | Site | Returned = screened | Included | New |
|---|---|---|---|---|---|
| RD1 | `title=accordion` | User Experience | 30 | 1 | 1 |
| RD2 | `q=progressive disclosure` | User Experience | 30 | 2 | 1 |
| RD3 | `title=nested accordion` | User Experience | 1 | 0 | 0 |
| RD4 | `title=collapse expand` | User Experience | 0 | 0 | 0 |
| RD5 | `title=tree view` | User Experience | 17 | 1 | 1 |
| RD6 | `title=nested` | User Experience | 30 | 2 | 1 |
| RD7 | `title=hierarchy levels` | User Experience | 0 | 0 | 0 |
| RD8 | `title=show more` | User Experience | 21 | 0 | 0 |
| RD9 | `q=heading levels` | Writing | 30 | 2 | 2 |
| RD10 | `title=nested` | Writing | 2 | 0 | 0 |
| RD11 | `title=regions` | Software Engineering | 11 | 1 | 1 |
| RD12 | `q=code folding` | Software Engineering | 30 | 2 | 2 |
| RD13 | `title=outline` | Writing | 28 | 0 | 0 |
| RD14 | `title=breadcrumb` | User Experience | 30 | 1 | 1 |
| RD15 | `title=collapsible` | User Experience | 28 | 1 | 1 |
| RD16 | `title=expand` | User Experience | 30 | 1 | 1 |
| Total | 16 strings | | 318 | 12 (distinct) | 12 |

- Stack Overflow was not searched: its titles on these words are how-to questions about widgets.
- Included: 12, scored on the 20 criteria (section 8) with the shared Q/A rules. Below 10: 2, kept as examples only.
- Stopping point: the run ended after RD16, when each practitioner term of the frame had been run in one form. The last string that added a new thread was RD16 (1 new). RD4, RD7 and RD10 returned 0 to 2 results and were read as weak queries, followed by a title form (RD15, RD6).
- Display names are not recorded; threads are cited by title and number.

## 6. Stopping rule

- Stated before searching: effort bounded, N = 15 per formal string and 10 per web string, with saturation, k = 5 consecutive results that add no new concept.
- Formal: evidence exhaustion for F1, F18, F19, F21, F22, F24 and A1 to A4 (small sets); effort bounded for the rest.
- Grey web: G1 and G2 stopped by saturation after the first page.
- Q/A sites: as in section 5.

## 7. Selection

- Include: a source on showing nested text to a reader (folded, expandable, zoomable, fisheye, layered, outlined).
- Include also: hierarchical against networked structure for reading, or trees of summaries read by a model; English; readable on the search date.
- Exclude: graphics and maps with no text or hierarchy; distortion techniques for images; tree visualisation for phylogeny or data; adaptive systems that adapt only links; vendor pages selling a product; duplicates.
- A source whose text and abstract could not be read is kept only as "located", never as support.

## 8. Quality of grey sources (Garousi Guideline 11, Table 7)

- The 20 criteria and the threshold: [evidence README](../README.md#method).
- Outlet tier: standards, government guidance = tier 1 (1); company pages, project documentation, wiki and Q/A pages = tier 2 (0.5); blogs = tier 3 (0).
- Threshold: 10 of 20. Below it a source is an **example of practice** only.
- A count read from a public listing (stars, downloads) is the reviewer's measurement, not a source, and is not scored.
- Scores, with subtotals, are in [sources](sources.md).

## 9. Extraction and synthesis

- Extracted per source: kind, year, the claim, the evidence, any number with where it was read, marked "(secondary)" when read in an abstract or another work's summary.
- Synthesis is narrative, by question Q1 to Q7, and every claim traces to a row of [sources](sources.md).

## 10. Limits

- One first rater for progressive-disclosure; the second rater's blind sample is reported in the [evidence README](../README.md#method).
- The ACM Digital Library and ScienceDirect refused automated reads on the day. ACM papers were read in author or course copies where found, otherwise through their abstract or through Cockburn 2009, and marked so.
- Shared limits: [evidence README](../README.md#method). Here: one arXiv call timed out (F2).
- Forward snowballing was not paged in a citation index.
