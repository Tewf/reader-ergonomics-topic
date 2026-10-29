# Protocol: how the pool of sources was built

This file records every search, count and rule of the information-typing review. Shared rules: [evidence README](../README.md#method). Searches ran on 2026-10-29.

## 1. Why grey literature

Garousi 2019, Table 4, answered for information-typing: all seven questions get a yes.

| # | Question | Answer for this review |
|---|---|---|
| 1 | Complex, not solvable from formal literature alone? | yes: the main typed systems (DITA, Information Mapping) come from practice |
| 2 | Lack of volume or quality of evidence? | yes: one controlled test of a typed format against untyped text was found, in a 1969 government report |
| 3 | Context important? | yes: the domain (software, aerospace, schools) decides which types exist |
| 4 | Corroborate research with practice? | yes |
| 5 | Challenge practice with research, or the reverse? | yes: the DITA specification cites research this search could not find (position.md) |
| 6 | Would a synthesis serve both communities? | yes |
| 7 | Large practitioner volume? | yes: 802 firms are listed as using DITA (DITAWriter 2026) |

## 2. Questions

| Id | Question |
|---|---|
| Q1 | Which systems define a base unit and derive types from it, and what does the base hold? |
| Q2 | Does a typed, predictable structure help readers find, understand or recall, measured? |
| Q3 | Does knowing one type transfer to another type, or to a derived type? |
| Q4 | What does practice adopt, with counts? |
| Q5 | What does typing cost: rigidity, authoring burden, failed fit? |
| Q6 | Do typed units help a language model as reader, kept apart from vendor claims? |

## 3. Existing reviews (Garousi Guideline 2)

- Searched first, by strings F10 (meta-analyses of text structure instruction), F29 (reviews of DITA and structured authoring) and F18 (component content management).
- Found: 8 reviews. 3 meta-analyses read by abstract (one also through its thesis chapter), 1 review read by abstract, 3 reviews of component content management by title and venue only. 1 review of content strategy located only (Clark 2016, not used).
- No systematic review of DITA, Information Mapping or topic types measured on readers was found. They are placed in review.md strand 0.

## 4. Formal search

Count source: the Semantic Scholar bulk title-and-abstract search, sorted by citation count, and the arXiv search API (all fields). The OpenAlex column was counted afterwards, at 10:09 UTC. Semantic Scholar matches stemmed words, not phrases, so its counts are noisy upper bounds.

| Id | String as run | Semantic Scholar | arXiv | OpenAlex |
|---|---|---|---|---|
| F1 | "information typing" | 3,828 | 110 | 4,314 |
| F2 | "DITA" +(topic \| specialization \| authoring) | 243 | 1 (DITA AND topic AND documentation); 0 for "Darwin Information Typing Architecture" | 327 |
| F2b | Darwin Information Typing Architecture (relevance ranking, 20 read) | total not a count | not run | 88 |
| F3 | "information mapping" +Horn | 7 | 0 | 5 |
| F4 | "information mapping" +(writing \| documentation \| instruction) | 52 | not run | 60 |
| F5 | "topic-based" +(authoring \| writing \| documentation) | 977 | 1 ("topic-based authoring") | 1,236 |
| F6 | "structured authoring" | 993 | refused (HTTP 429) | 1,198 |
| F7 | "structured writing" +(documentation \| Horn \| technical) | 51 | not run | 68 |
| F8 | "story grammar" (the plural returned the same 787) | 787 | 4 | 895 |
| F9 | superstructure +(text \| discourse) +(comprehension \| schema) | 68 | not run | 82 |
| F10 | "text structure" +instruction +comprehension +meta-analysis | 9 | not run | 8 |
| F11 | "text structure" +strategy +(recall \| comprehension) | 369 | refused (HTTP 429) | 445 |
| F12 | "genre knowledge" +(reading \| comprehension \| readers) | 102 | not run | 138 |
| F13 | "genre as social action" | 71 | not run | 80 |
| F14 | "rhetorical genre studies" | 136 | not run | 191 |
| F15 | "genre awareness" +transfer | 40 | not run | 72 |
| F16 | "minimal manual" | 1,115 | not run | 1,490 |
| F17 | "minimalism" +(documentation \| manual \| instruction) +Carroll | 44 | not run | 58 |
| F18 | "component content management" | 39 | not run | 48 |
| F19 | "content reuse" +(documentation \| topic) | 34 | not run | 39 |
| F20 | "single sourcing" +documentation | 265 | not run | 393 |
| F21 | "text types" +(typology \| genre) +comprehension | 85 | not run | 100 |
| F22 | "information mapped" \| "information-mapped" | 1,385 | not run | 1,451 |
| F23 | Horn +"structured writing" | 3 | not run | 1 |
| F24 | "information types" +(documentation \| technical communication \| DITA) | 94 | not run | 162 |
| F25 | "topic types" +(documentation \| writing) | 39 | not run | 41 |
| F26 | "genre expectations" +(reading \| comprehension) | 48 | not run | 83 |
| F27 | "procedural instructions" +(principles \| examples) +transfer | 7 | not run | 9 |
| F28 | "rhetorical structure" +"text comprehension" | 9 | not run | 8 |
| F29 | (DITA \| "structured authoring" \| "topic-based authoring") +("systematic review" \| "literature review") | 37 | not run | 50 |
| F30 | "Every Page is Page One" \| "topic-based writing" | 19 | not run | 21 |
| F31 | "story schema" +recall | 23 | not run | 26 |
| X1 | arXiv only: "element type" AND chunking AND retrieval | not run | 1 | 1 |
| X2 | arXiv only: "document structure" AND chunking AND "retrieval augmented" | not run | 26 | 64 |
| X3 | arXiv only: "technical documentation" AND "retrieval augmented generation" | not run | 37 | 140 |

- Totals: Semantic Scholar 10,979 records over 31 strings; arXiv 180 over 9 strings.
- Screened by title: the 20 most cited of each Semantic Scholar string (fewer where fewer were returned), 554 in all; the 20 of F2b; 16 arXiv titles listed by the script. 590 in all, with repeats across strings.
- F1, F5, F6, F16 and F22 were too noisy to screen past the first page (genetics, physics, image annotation).
- Abstracts were then read through the public ERIC, PubMed and Crossref services, without any identity; these lookups add no records to the counts.
- Leads named in the brief and verified: Kintsch 1978, Mandler 1977, Thorndyke 1977, Stein and Glenn (found as the 1975 report), Black 1979, Meyer 2001, Miller 1984, Horn 1969, Baker 2013, Baker 2018b.
- Leads not used: Horn's book (1989; not located in a readable form), Rockley's and Hackos's books (not opened; reuse belongs to the document-model review), van Dijk and Kintsch's book (1983; not opened). Also not used: Stein and Glenn's chapter (1979; not opened; the 1975 report used instead), Carroll's book (1990; not opened; Carroll 1987 located instead). Also not used: an IBM article of 2001 by Day, Priestley and Schell (listed by Semantic Scholar without a stable link, not read; Priestley 2001 and Priestley 2002 used).
- Snowballing, backward: the section "Role of the schema" of Kintsch 1978 was read for further type systems; it names Mandler 1977, Rumelhart 1975 and Stein and Glenn, all reached. Forward: none beyond the strings.

## 5. Grey search

- Types and producers, chosen because the formal search pointed to them. Standards bodies (OASIS), the method's company (Information Mapping), practitioner books (XML Press), open-source documentation projects (Kubernetes), web vocabularies (Schema.org), practitioner blogs, and Q/A sites.
- Engine: a general web search engine, first result page per string. Results personalise and change.

| Id | String as run (abridged) | Screened | Included |
|---|---|---|---|
| G1 | Horn "Information Mapping for Learning and Reference" 1969 ERIC OR pdf | 10 | 1 (Horn 1969, archived scan) |
| G2 | OASIS DITA 2.0 specification approved OASIS Standard date | 9 | 0 (status not confirmed) |
| G3 | DITA structured content topic types improve RAG chatbot accuracy, vendor blog | 28 | 1 (Johnson 2013); one vendor page timed out |
| P | direct visits: OASIS committee page and DITA 1.3 specification, dita-lang.org, DITAWriter, Kubernetes, Information Mapping, XML Press (two books), Schema.org (three types), GitHub repository counts | 12 | 7 |

- Searches made only to reach a formal text (the Utrecht thesis, the ERIC record of Hebert 2016, Zwaan 1994, two Kintsch texts) are not grey strings and are not counted.

### Q/A sites

Strings TU1 to TU14 ran on 2026-10-29, one reviewer, grey tier 2. Other rules: [evidence README](../README.md#method).: top 30 by votes per string and site, `order=desc&sort=votes&pagesize=30&filter=withbody`, endpoint `search/advanced`, version 2.3, no key.

| Id | String as run | Site | Returned = screened | Included | New |
|---|---|---|---|---|---|
| TU1 | `q=DITA` | Writing | 5 | 3 | 3 |
| TU2 | `tagged=dita` | Stack Overflow | 30 | 1 | 1 |
| TU3 | `q=topic-based` | Writing | 30 | 2 | 0 |
| TU4 | `q=structured authoring` | Writing | 30 | 1 | 0 |
| TU5 | `q=information mapping` | Writing | 11 | 0 | 0 |
| TU6 | `q=DITA` | User Experience | 0 | 0 | 0 |
| TU7 | `q=DITA` | Software Engineering | 2 | 0 | 0 |
| TU8 | `title=genre conventions` | Writing | 2 | 2 | 2 |
| TU9 | `title=story structure` | Writing | 9 | 0 | 0 |
| TU10 | `q=concept task reference` | Writing | 2 | 0 | 0 |
| TU11 | `q=DITA specialization` | Stack Overflow | 15 | 2 | 2 |
| TU12 | `title=hero's journey` | Writing | 8 | 2 | 2 |
| TU13 | `title=documentation` | User Experience | 30 | 1 | 1 |
| TU14 | `tagged=technical-writing&title=structure` | Writing | 5 | 1 | 1 |
| Total | 14 strings | | 179 | 12 (distinct) | 12 |

- Opened: threads whose title bore on a question of the review; the question and its two top answers were read.
- Excluded after reading: how-to and tool questions (learning DITA, XSLT), writers' craft with no reader claim, and threads of another topic (reuse, page length).
- Included: 12, scored on the 20 criteria (section 8) with the shared rules for Q/A threads; 2 fall below 10 of 20 and are examples only.
- The run ended after TU14; the last string that added a thread was TU14 (1 new).
- The daily quota of the service is shared by address; it fell from 161 to 142 calls during this run, so strings were kept few.
- Display names are not recorded; threads are cited by site, year and number.

## 6. Stopping rule

- Stated at the start of the formal search: effort bounded, N = 20 most cited per Semantic Scholar string, with saturation, k = 5 strings in a row that add no new included source.
- Formal: evidence exhaustion for F3, F10, F23, F27, F28 (fewer than 10 records); effort bounded for the rest. The genre strings F12 to F15 and F21 reached saturation for reader-side evidence: they added writing-studies theory, not reader measures.
- Grey web: first result page per string; saturation for G2.
- Q/A: as above, ended after TU14.

## 7. Selection

- Include: a source on how a unit of writing is given a type, how types derive from a base, or how readers or models use typed units. Also in English, and readable on the day at least by abstract or, for a book, by its publisher's page.
- Exclude:
  - automatic genre classification and topic modelling (the words "topic" and "type" in another sense);
  - school writing interventions with no reading or typing claim;
  - reuse, maps, schemas and validation (document-model review) and nested display (progressive-disclosure review), passed to those reviews when met;
  - sources whose abstract could not be read and whose title does not settle relevance (kept as located only).

## 8. Quality of grey sources (Garousi Guideline 11, Table 7)

- The 20 criteria and the threshold: [evidence README](../README.md#method).
- Outlet tier: books, theses, government reports and standards = tier 1 (1); company and project pages, Q/A threads = tier 2 (0.5); blogs and informal lists = tier 3 (0).
- A part not seen scores 0; a book known only from its publisher's page scores low for that reason, and says so.
- Threshold: 10 of 20. Below it a source is an **example of practice** only, never support for a claim.
- Scores, with subtotals, are in sources.md.

## 9. Extraction and synthesis

- Extracted per source: kind, year, the claim, the evidence offered, any number (marked "(secondary)" if not read in the primary), and which question it answers.
- Synthesis is narrative, by question Q1 to Q6; every claim traces to a row of sources.md.

## 10. Limits

- One first rater for information-typing; the second rater's blind sample is reported in the [evidence README](../README.md#method).
- Shared limits: [evidence README](../README.md#method). Here: two arXiv strings were refused.
- Most formal sources were read by abstract only, several by title only; sources.md says which. Publisher pages of Elsevier, Wiley, IEEE and APA were not readable without access.
- No archived copy was made of the practice pages; three of them (DITAWriter, Information Mapping, a blog) may move.
- This search did not find a reader study of a DITA topic type; that is not proof none exists.
