# Baseline: what the node template must beat

This file names the baseline a typed node template is compared against, and how the comparison would be measured.

## The named baseline

| Role | Baseline | Why this one |
|---|---|---|
| Typed units with derivation (the one to beat) | the DITA 1.3 base topic with its concept, task and reference specializations (OASIS 2015) | the only system found that declares a base, derives types from it, and lets a program read any derived unit as its base; an OASIS Standard since 2005, listed by 802 firms (DITAWriter 2026) |
| Historical anchor | Information Mapping's typed maps, as in Horn 1969 | the first typed system found with derivation (a map type taking every block of another), and the only one with a controlled test against untyped text |
| Control | the same content as untyped prose, Horn's "P version" | removes the visible typing and keeps the words, so a gain belongs to the type |

- The DITA base is the right rival because it already holds what the node claims. It has one base shape (title, short description, prolog, body, related links, nested topics; OASIS 2015, 2.2.1.6) and derived types that keep it.
- The node must therefore beat DITA on readers, not on structure: DITA has no reader study in this search, so the node's claim is testable where DITA's is not yet tested.
- Kubernetes 2026b (concept, task, tutorial, reference) is a second, lighter baseline in Markdown, without declared derivation.

## What "beat" means

The node beats the baseline if, on the same content, it does at least one of these without losing on the others:

1. readers find a fact faster;
2. readers recall the gist better, at once and after a delay;
3. readers who learned the base read an unseen derived type better than readers who learned only sibling types;
4. a program checks more of the reader-ergonomics rules on it, at any depth.

## How a comparison would be measured

| Reader task | Outcome | Instrument | Prior study to borrow from |
|---|---|---|---|
| Find | time to locate a stated fact; share found | fixed search questions on one document set in three forms | Kools 2008 (search speed with and without headings) |
| Understand | gist questions against local questions, separately | main-idea and summary items; cloze or verbatim items | Kintsch 1982 (global against local comprehension) |
| Recall, delayed | recall at once and after one week or more | free recall scored by idea units | Bogaerds-Hazenberg 2020 (effects gone at delay) |
| Transfer to a derived type | performance on a type never studied, derived from the base | train on the base and two derived types, test on a third derived type | Hebert 2016 (near transfer to untaught structures) |
| Cost to the writer | time to write; errors against the type | the same content written in each template | none found for typed templates |
| Program check | share of units that validate as their base type at every depth | a checker that reads each node as its base, as DITA's `@class` fallback does | OASIS 2015 (2.5.3.6, 2.5.4) |

- Forms compared: untyped prose (the control), DITA concept, task and reference, and the node template; the words held constant, as in Horn 1969.
- Design: within-subject crossover, counterbalanced order, a delayed session after one week.
- Effect sizes: Hedges' g with confidence intervals, as in the meta-analyses; report each outcome apart, since effects differ by outcome (Bogaerds-Hazenberg 2020).
- Readers: adults reading documentation, not school students; most evidence above comes from students, a threat to generalisation.
- Readers are not taught the types beforehand in one arm, and are taught them in another: the positive results so far all rest on taught or known types.
- For a model as reader: the same three forms, with and without the type label, scored on retrieval and answer accuracy, as in Jimeno Yepes 2024.

## A checklist in the baseline's own terms

Per unit, from the DITA base (OASIS 2015):

1. The unit has an identifier and a title.
2. A short description says what the unit is about; the specification treats it as optional and strongly advised.
3. The body holds only what the unit's type permits.
4. Related units are linked from a related-links part.
5. Child units are nested whole, each with its own title.
6. A derived type declares its ancestry, so it can be read as its base.

Per map, from Information Mapping (Horn 1969):

1. Each block carries a label naming its kind.
2. Each kind of block keeps one format across the document.
3. A map begins on a new page and fits one page where possible.
4. Feedback questions sit next to the block they test.

