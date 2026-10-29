# Information typing: how a unit of writing is given a type derived from a base

Question: how is a unit of writing given a type, so that a reader who knows the base form can read every form derived from it? And what does the evidence say about typed units and how types derive from a base?

- It covers published research and public practice: discourse psychology, reading research, technical communication, rhetorical genre studies, standards and documentation projects.
- It scores 22 grey sources out of 20 (10 from the web, 12 threads from Q/A sites); 4 fall below the threshold of 10 and are used as examples only.

## Files

| File | Role |
|---|---|
| [protocol](protocol.md) | how the pool was built: questions, strings, counts, stopping rule, scoring |
| [sources](sources.md) | the flow of the pool, and one row per source with its quality |
| [frame](frame.md) | step 1: the problem in one sentence, and what research and practice call it |
| [review](review.md) | step 2: existing reviews, seminal theory, Information Mapping first-hand, DITA, reader studies, transfer, cost, models, practice |
| [state of the art](state-of-the-art.md) | step 3: most adopted against best evidence, per question; upper and lower bounds |
| [position](position.md) | step 4: known, not known, where practice runs ahead of the evidence |
| [against](against.md) | null results, a failed replication, critiques, costs |
| [baseline](baseline.md) | step 5: the baseline the topic template must beat, and how to measure it |
| [bibliography](../bibliography.md) | every cited work: key, citation, link |
| `flow.json` | the flow as data, drawn in the figure of [sources](sources.md) |

## Claims

| Claim | Grade | Where |
|---|---|---|
| Readers hold schemata of conventional text types: categories plus rules of order, sometimes recursive, that decide what reaches the gist | supported with caveat (theory, read first-hand) | review.md 1 |
| Typed units with a base were already in use in 1969: eight map types, some taking every block of the concept map | convention, described in one report (read first-hand) | review.md 2 |
| The same content with or without the typed format gave no significant difference in learning (19.56 against 17.65, 41 students) | supported with caveat: one controlled test, in a report not peer-reviewed | review.md 2; against.md |
| Headings help search in an information-mapped text; more headings and the method's order do not | measured, one study (abstract) | review.md 4 |
| Information-mapped text matched programmed instruction on recall and beat it on retrieving information | measured, one study (abstract, secondary) | review.md 2 |
| Conventional form with cues helps comprehension; the effect depended on whether the test was global or local, in a direction the abstract does not give | measured, one study (abstract, secondary) | review.md 4 |
| Teaching readers text types helps comprehension at once (g = 0.25 to 0.57); at a delay the advantage is gone, except with individual practice | measured, meta-analysis of 44 studies (secondary) | review.md 0 |
| Text structure instruction transfers to untaught structures; far transfer is small and inconsistent | measured, meta-analysis of 45 studies (secondary) | review.md 0, 5 |
| A genre label changed processing in 1994 and not in three online experiments in 2021 | measured, contested (the 2021 study read by abstract, secondary) | review.md 4; against.md |
| DITA declares one base topic, derives concept, task and reference from it, and lets a program read any derived unit as its base | convention, standardised (read first-hand) | review.md 3 |
| 802 firms are listed as using DITA (2026-04-24) | measured, descriptive (informal list) | state-of-the-art.md |
| Schema.org HowTo is used on 100K to 1M domains | measured, descriptive (the vocabulary's own band, 2026-08) | state-of-the-art.md |
| Story grammars were judged formally inadequate and no better than content models | supported with caveat (critique, abstract) | review.md 1; against.md |
| Typed chunk boundaries help a model retrieve, in one domain | measured, preprint (abstract) | review.md 7 |
| A reader who knows a base type reads a derived type better | convention, untested (no study found) | position.md; baseline.md |
| A derived type keeps every part of its base and the type is announced to the reader | convention, untested (a hypothesis to test) | position.md |

## Named baseline

- To beat: the DITA 1.3 base topic (OASIS 2015) with the concept, task and reference specializations of its technical content edition (OASIS 2015b).
- Historical anchor and control: Information Mapping's typed maps and the same content as untyped prose, as in Horn 1969.
- Comparison: find, understand (global against local), recall at delay, transfer to an unseen derived type, and a program check at every depth; crossover with a delayed session, Hedges' g per outcome (baseline.md).

## General principles linked, not reviewed again

- [Names predict content](https://github.com/Tewf/reader-ergonomics/blob/7a76cc6a86b7a5c1e451e4416534d113abd0f594/principles/collection/names-predict-content.md)
- [One mode per document](https://github.com/Tewf/reader-ergonomics/blob/7a76cc6a86b7a5c1e451e4416534d113abd0f594/principles/document/one-mode-per-document.md)
- [Overview first](https://github.com/Tewf/reader-ergonomics/blob/7a76cc6a86b7a5c1e451e4416534d113abd0f594/principles/document/overview-first.md)
- [Signal the structure](https://github.com/Tewf/reader-ergonomics/blob/7a76cc6a86b7a5c1e451e4416534d113abd0f594/principles/page/signal-the-structure.md)
