# Evidence

One literature review per part of the template, in the steps reader-ergonomics uses for its own
[evidence](https://github.com/Tewf/reader-ergonomics/tree/257958ed3bcb26d2c213bb1b0a66ac19e9645157/evidence): frame, review, state of the art, position, the
case against, baseline. Every work cited is listed once in the [bibliography](bibliography.md), with its citation and a stable link.

| Review | Question | The repository's question it answers |
|---|---|---|
| [information-typing](information-typing/) | how a unit of writing is given a type derived from a base, so a reader who knows the base reads every derivative | genres |
| [progressive-disclosure](progressive-disclosure/) | how a tree of units nested to any depth is shown, so the top levels are kept and any leaf is reached | depth |
| [document-model](document-model/) | how a unit that holds units of its own type is stored, reused and checked by a program | self-reference, graphs |

## Method

Each review is a **multivocal literature review**: research and **grey literature** (standards, company practice,
practitioner books, tools, Q/A sites) in one review, built to a written protocol after Garousi 2019. Two files in each
topic make the review checkable and rerunnable:

| File | What it holds |
|---|---|
| `protocol.md` | why grey literature is included, the questions, every search string with its date and count, the stopping rule, the selection criteria |
| `sources.md` | every included source, how it was found, and its quality: the evidence grade for research, a score out of 20 for grey literature |

A grey source is scored on Garousi's 20 criteria, in eight groups. The `sources.md` tables abbreviate them: A authority
(of 4), M methodology (6), O objectivity (4), D date (1), P position among related sources (1), N novelty (2), I impact
(1), T outlet tier (1). Below 10 of 20 it may illustrate what practice does, but it never supports a claim.

Each review keeps the form most used in practice apart from the best tested one; practice counts as evidence only
where a study measured its effect.

The three reviews share these rules, which their protocols do not repeat:

- **Why grey literature:** each protocol answers the seven questions of Garousi 2019, Table 4; one yes suggests
  including grey literature.
- **Q/A sites:** threads are read through the Stack Exchange API, by the method of the reader-ergonomics-software-design
  [architecture-descriptions protocol](https://github.com/Tewf/reader-ergonomics-software-design/blob/master/evidence/architecture-descriptions/protocol.md#qa-sites):
  its stopping parameters, its API call, how a thread is read and scored, and its limits.
- **Limits:** search engines personalise and change, so counts differ on a repeat. OpenAlex counted every string after the searches,
  on the same day. Semantic Scholar and arXiv counts are not phrase-exact.
- **Counts:** each formal string was counted in three databases, without a key: the Semantic Scholar bulk search
  (title and abstract), the arXiv search API, and OpenAlex (title and abstract, phrase search). Semantic Scholar
  matches stemmed words, not phrases, so its counts are noisy upper bounds.
- A number read only in an abstract or a summary is marked "(secondary)".
- None of these reviews is a standard, a new result, or a claim to the state of the art.

**Second rater.** A second rater re-scored, blind, every fifth scored grey source of the three reviews (15 of 82):

- inclusion: the raters agreed on 14 of 15, Cohen's kappa 0.76, unstable at this size (bootstrap 0.00 to 1.00);
- totals: mean absolute difference 1.20 of 20, the second rater 0.27 points lower;
- the raters differed most on objectivity (0.63) and methodology (0.57), least on outlet tier (0.03);
- one source fell below 10 for the second rater (SO 2015b, 11.5 against 9.5), and it is now an example of practice only;
- seven of the fifteen are Q/A threads, which both raters read through the Stack Exchange API.

## What these reviews do not repeat

Works already reviewed in a sibling repository are linked there, with one line of context, and not reviewed again:

| Repository and topic | Holds |
|---|---|
| reader-ergonomics [psycholinguistics](https://github.com/Tewf/reader-ergonomics/tree/257958ed3bcb26d2c213bb1b0a66ac19e9645157/evidence/psycholinguistics) | the levels effect, rhetorical structure theory |
| reader-ergonomics [file-structure](https://github.com/Tewf/reader-ergonomics/tree/257958ed3bcb26d2c213bb1b0a66ac19e9645157/evidence/file-structure) | depth against breadth of menus and folders |
| reader-ergonomics [reading-order](https://github.com/Tewf/reader-ergonomics/tree/257958ed3bcb26d2c213bb1b0a66ac19e9645157/evidence/reading-order) | advance organizers, elaboration theory and zoom-lens sequencing |
| reader-ergonomics [learning-science](https://github.com/Tewf/reader-ergonomics/tree/257958ed3bcb26d2c213bb1b0a66ac19e9645157/evidence/learning-science) | atomic notes, hypertext load, signaling |
| reader-ergonomics [documentation](https://github.com/Tewf/reader-ergonomics/tree/257958ed3bcb26d2c213bb1b0a66ac19e9645157/evidence/documentation) | Diataxis and documentation types |
| reader-ergonomics-academic [academic-papers](https://github.com/Tewf/reader-ergonomics-academic/tree/master/evidence/academic-papers) | IMRaD, moves and steps (Swales) |
| reader-ergonomics-academic [mathematical-writing](https://github.com/Tewf/reader-ergonomics-academic/tree/master/evidence/mathematical-writing) | structured proofs |
| reader-ergonomics-presentations [presentations](https://github.com/Tewf/reader-ergonomics-presentations/tree/master/evidence/presentations) | Minto, assertion-evidence, slide builds |
| reader-ergonomics-software-design [pseudocode](https://github.com/Tewf/reader-ergonomics-software-design/tree/master/evidence/pseudocode), [architecture-descriptions](https://github.com/Tewf/reader-ergonomics-software-design/tree/master/evidence/architecture-descriptions) | stepwise refinement; C4, arc42 and ISO 42010 |

A key names one work across all five repositories: the keys here were checked by script against the four other
bibliographies. One key differs on purpose. Horn 1969 here is the 1969 report itself; reader-ergonomics still cites an
encyclopedia page under it, and will change at its next release.

## Audit

- Every DOI was resolved against Crossref when the reviews were written.
- On 2026-10-29, the numbers behind four conclusions were checked against the primary text by the maintainer's
  session: Furnas 1986, Horn 1969, He 2026 and Juergens 2010. All were correct; one line had left out Furnas's mixed
  view (64%).
- Then every line carrying a number, or graded measured, was audited against its primary source, one auditor per
  review, none of whom had written it: 159 rows.

| Review | Rows | Correct | Imprecise | Wrong | Unverifiable | Checked before, or repeats |
|---|---|---|---|---|---|---|
| information-typing | 51 | 41 | 3 | 2 | 1 | 4 |
| progressive-disclosure | 66 | 48 | 11 | 0 | 1 | 6 |
| document-model | 42 | 29 | 5 | 0 | 0 | 8 |
| all | 159 | 118 | 19 | 2 | 2 | 18 |

- Every wrong and imprecise row is corrected. Each correction to a number was checked in its source before it was
  written, since a correction is a claim too.
- The two wrong rows: a review called "the largest" that is not, and a company page said to show no numbers that
  shows nine.
- The two unverifiable rows: the direction of an effect in Kintsch 1982 is softened to what the abstract read
  supports; Höök 1997 stays marked "(secondary)", since its abstract could not be reached again.
- The audit also found missing "(secondary)" marks, grades above their evidence, and findings stated in two reviews;
  all are fixed.
