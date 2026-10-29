# Against: controversies, limits and failed assumptions

This file gathers the evidence against the tree model and its reuse: the critique of OHCO, the costs of strict models, fragments read out of context, and the limits of the evidence used here.

## Text is not one tree

- Renear 1996 concludes that "no version appears to be free from counterexample" of the OHCO thesis.
- Its counterexamples come from literary and textual scholarship: verse against sentence, enjambment, strike-outs, variants, link anchors.
- Schmidt 2010 (abstract) goes further: embedded markup hides the text and carries obsolescent, subjective data, beyond overlap.
- Haentjens Dekker 2017 makes hierarchy optional and orders only the text.
- Against the critique: Renear 1996 itself keeps that perspectives often determine hierarchies, and TEI 2026 still builds on XML trees, with workarounds for what does not nest.
- Whether ordinary documentation overlaps as literary texts do is not known (position.md).

## Strict models cost

- Dayton 2010 (abstract): half of the users of single sourcing or content management reported significant downsides, and about 1 in 10 respondents had seen an implementation fail.
- Batova 2018 (abstract): at one company, writers' motivation fell when component content management was framed only as efficiency.
- Martens 2006 (abstract) relates the little use of XML Schema's extra power to the complexity of its specification.
- HTML's outline from nested sections stayed unimplemented for over a decade and was replaced by heading levels (WHATWG 2022).
- XInclude was never shipped by browsers; an answer cites the cost of loop detection among the reasons (SO 2011d).
- S1000D's schemas are more rigid than DITA's (WSE 2018b), and a do-it-yourself DITA setup gives little support for reuse (WSE 2014a): opinions.
- The Composite pattern's uniform interface loses type safety (Wikipedia 2026d), and the evidence for design patterns in general is weak (Zhang 2012).

## Fragments reused without their context

- Batova 2014: segmentation strips content of its larger context, so translators cannot judge it and make context errors; best practices do not resolve the conflict between consistency and adaptation.
- WSE 2018g: readers who dip into documentation need repetition at read time; reuse tools serve this only if each use reads on its own.
- DITA needs `@copy-to` so that a topic used twice gets its own links and navigation (OASIS 2015): without it, position-bound links are shared.
- Notion gave up several parents per block because permissions became ambiguous (Notion 2021, the owner's account).
- Copies are not always wrong: some code clones help maintenance, as [file-structure](https://github.com/Tewf/reader-ergonomics/blob/257958ed3bcb26d2c213bb1b0a66ac19e9645157/evidence/file-structure/against.md) reviews (Kapser 2008), linked, not repeated.

## Limits of the measured evidence

- The corpus studies of XML are old: Choi 2002, Mignet 2003, Mlýnková 2006, Grijzenhout 2011. Choi and Mignet were read through Mlýnková 2006, Grijzenhout through its abstract.
- Their documents are web XML of every kind (feeds, data, configuration), not documentation.
- Juergens 2010 measures copies in requirements specifications; its reading and inspection costs are computed from published rates, not observed.
- Dayton 2010 surveyed 1,000 STC members in 2008-05 and 276 answered (27.6%), so the respondents selected themselves; read by abstract.
- Fleckenstein 2023 pools studies of students' essays, not documentation or linters; its heterogeneity is high.
- Johnson 2020 is a preprint, read by abstract, on one wiki.

## Limits of the practice evidence

- Standards state rules, not outcomes; tool documentation states behaviour, not effect.
- Notion 2021 is a company describing its own design.
- Stars measure interest, not use; standards older than GitHub are understated (state-of-the-art.md).
- Schematron 2026 scores under 10 of 20 and is used only for its own edition claim (sources.md).
- The Q/A threads are opinion; the GoF reading in SESE 2022c is secondary.

## What was not found

- No reader study comparing reuse by reference with copies.
- No replication of Juergens 2010 on user documentation; Luciv 2018 and Nosál 2016 count duplicates without consequences.
- No study of overlap frequency in technical documentation.
- No evaluation of the DITA conref or key mechanisms on consistency, in this search.
