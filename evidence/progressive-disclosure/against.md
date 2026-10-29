# Against: controversies, limits and failed assumptions

This file gathers the evidence against showing text folded or nested: null results, disputed studies, and practice that a study contradicts. Terms are defined in [frame](frame.md).

## Whether folding helps the reader

- On the easiest retrieval task, the fully expanded list and the multi-pane view beat expand/contract (Chimera 1994, p < .01).
- On the task of finding the item that covers three topics, the fully expanded list was fastest, not significantly: 46.1 s against 85.9 s for expand/contract and 55.0 s for multi-pane (Chimera 1994).
- The authors explain it: the target sat near the start, and its chapter title did not predict its contents, so readers of the folded views opened the wrong chapters.
- Chimera 1994 credits part of the expand/contract gain to animation, so folding and animation are confounded.
- Shrinking text around the focus made reading faster and comprehension worse (Hornbæk 2003, through Cockburn 2009, secondary).
- A short first layer made readers faster and less accurate on what it left out; few went further (McDonald 2009, section 4).
- Sections open on load drew more reading time than folded ones: 190 s against 146 s at the 90th percentile (Wikimedia 2016).

## Whether an overview or a fisheye helps

- Readers preferred an overview and were not more accurate with it; on a map built in levels they were faster without it (Hornbæk 2002).
- Switching between overview and detail cost time and effort (Hornbæk 2002; Cockburn 2009, section 8).
- On large trees, pan and zoom beat a distorting fisheye, and an overview did not change task time (Nekrasovski 2006, through Cockburn 2009).
- Distortion-based techniques have largely failed to show performance gains (Cockburn 2009, section 8).
- Preference and performance part ways in several of these studies, so a preferred design is not shown to be a better one.

## Whether hypertext structure is the lever

- Effects vary strongly between studies, and cognitive traits gave effects not clearly different from zero (Chen 1996, secondary).
- Method flaws limit every conclusion about hypermedia and learning (Dillon 1998).
- Several studies adapting presentation to readers' traits found no significant differences (Brusilovsky 2001).
- Pure hierarchy is not always best: hierarchy with cross-links did better in McDonald 1998, while added network links gave nothing in Mohageg 1992.

## Whether trees of summaries help a model

- Passages kept in their original order matched or beat RAPTOR at matched token budgets; RAPTOR without its summaries beat RAPTOR with them (Laitenberger 2025, sections 3 and 4).
- RAPTOR's own ablation used a 3B reader limited to 400 tokens, a setting that favours compression (Laitenberger 2025, section 4).
- Within RAPTOR, searching all layers flattened beat descending the tree layer by layer (Sarthi 2024, section 3); the layer ablation in the main text is one story (Table 8).
- About 4% of RAPTOR's summaries held minor hallucinations (Sarthi 2024, section 3).
- The gain of a summary tree may come from navigation, not from the summaries (Jayraj 2026, secondary).
- A second level of disclosure for agents never helped and sometimes broke accuracy (He 2026, Table 1).
- Merging summaries up a hierarchy is more coherent and loses detail against a running summary (Chang 2024, secondary).

## Weaknesses of the strongest studies

- Furnas 1986: 20 subjects, one task of order judgments, one taxonomy.
- Chimera 1994: 41 novices, one contents of three levels, one workstation of its time; the title calls it exploratory.
- McDonald 2009: an online sample entered for a lottery, one domain (privacy policies), six companies; 7 of 756 were removed for clicking through.
- Wikimedia 2016: not a strict A/B test; about 0.05% of users per group, in 2015-12 and 2016-01; it measured time, not understanding.
- He 2026 and Jayraj 2026 are preprints; He 2026 uses one benchmark, ∞Bench. Laitenberger 2025 appeared at EMNLP (2025).
- Hornbæk 2003 and the code and tree studies were read only through Cockburn 2009.

## Limits of the practice evidence

- Nielsen 2006b gives the two-level limit with no data; its owner sells consulting.
- GOV.UK 2026a and 2026b report research findings without numbers or samples.
- Wang 2023 (example only, 9 of 20) says folded content is missed; it is one company article.
- PageIndex reports 98.7% on FinanceBench itself, with no independent evaluation linked (VectifyAI 2026, example only).
- Stars and downloads measure interest, not reading.
- Baymard's guideline on collapsed sections is paywalled and was not read.

## What the Q/A threads add against

- Folding a long block hides it instead of fixing it; regions are called an antipattern (SESE 2011o, accepted answer of 351 votes).
- A folded block has no name, scope or interface, so it is not a summary of what it hides (SESE 2014e).
- Do not hide answers to save scrolling; readers scroll when they expect something worth finding (UXSE 2012b).
- These are opinions; they agree with McDonald 2009 and Wikimedia 2016 on the cost of hiding.

## Failed or missing replications

- This search found no replication of Furnas 1986's experiment or of Chimera 1994.
- RAPTOR's gains did not hold under matched budgets and stronger readers in two later comparisons (Laitenberger 2025; Jayraj 2026, secondary).
- No replication of He 2026 was found; it appeared in 2026-07.
