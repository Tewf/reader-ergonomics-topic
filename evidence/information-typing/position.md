# Position

Each "not known" below is a statement about this search, not about the world.

## Against the existing reviews

- The three meta-analyses (Hebert 2016; Pyle 2017; Bogaerds-Hazenberg 2020) measure readers taught text types, in schools.
- The reviews of component content management (Andersen 2015; Batova 2014; Batova 2017) were located by title only; their titles name management, roles and quality, not readers.
- This search found no review that joins the two: a typed template on one side, the reader's schema on the other.
- This review adds that join, Information Mapping read first-hand, the DITA base read in the specification, adoption counts, and Q/A threads scored on 20 criteria.

## Known

- Typed units are old: Information Mapping had eight typed maps in 1969, and some took every block of the concept map (Horn 1969).
- DITA declares one base topic and derives every type from it; a program can process any derived unit as its base (OASIS 2015).
- Readers hold schemata of conventional text types, and the schema decides what reaches the gist (Kintsch 1978).
- Conventional form with cues helps global comprehension (Kintsch 1982).
- Teaching readers text types helps comprehension at once, with effects that fade by the delayed test (Bogaerds-Hazenberg 2020), and transfers to untaught types (Hebert 2016).
- Headings help search in an information-mapped text, but more headings and the method's order do not (Kools 2008).
- Removing the visible typed format from the same content did not significantly lower learning, in one study (Horn 1969).
- A genre label changed processing in 1994 (Zwaan 1994) and did not in three online experiments in 2021 (Triantafyllopoulos 2021).

## Not known

- Whether a declared type helps a reader who was never taught it: every positive reader result above taught the types, or used conventions the reader already held.
- Whether a reader who knows a base type reads a derived type better: the hypothesis of this repository has no test in this search.
  - DITA guarantees it for programs (generalization), not for people.
  - Hebert 2016 tests transfer between sibling types taught together, not from a base to a child.
- Whether a declared base type is what readers learn at all, or whether they learn each derived type separately.
- How many types a reader can hold: DITA's best-known set is three (concept, task, reference), Information Mapping had eight in 1969, Kubernetes 2026b has four; no study compares the counts.
- Whether typed units help a language model when the type is given as a label; the closest result types the chunk boundary, not the label (Jimeno Yepes 2024).
- Whether the effects of Kintsch 1982 and Kools 2008 hold for adults reading documentation online.

## Where practice runs ahead of the evidence

- DITA's specification says information typing rests on extensive research and names Horn and STOP, but cites no reader study (OASIS 2015, 2.2.1.4).
- The one controlled study in Horn's own report found no significant learning gain (Horn 1969); the company page claims benefits without numbers (Information Mapping 2026, example only).
- 802 firms list DITA (DITAWriter 2026); no reader study of a DITA topic type was found.
- Topic types spread to open-source documentation (Kubernetes 2026b; Red Hat 2026b) with no comparison against untyped pages.
- Schema.org types reach 100K to 1M domains for HowTo (SchemaOrg 2026); this is adoption by machine readers, not evidence of reader benefit.

## Where evidence is ignored by practice

- The meta-analyses find that readers gain when taught the types; templates ship the types to writers and assume readers will infer them.
- Effects fade without practice (Bogaerds-Hazenberg 2020); documentation sets assume a reader keeps the type in mind between visits.
- Story grammars were judged inadequate as models of what a story is (Black 1979). Story templates for writers (the hero's journey) are still taught, and practitioners warn against forcing content into them (WSE 2020a, example only).
- Abstract instructions favour transfer and specific ones favour first performance (Eiriksdottir 2011); task types are written for first performance only.

## What this repository adds

- It treats the topic as a **base type**, and genre forms as **derived types**, in the sense of OASIS 2015 and Horn 1969.
- It names the gap the topic would fill: a reader-side test of derivation, which neither DITA nor Information Mapping has.
- It offers candidate rules, each convention, untested:
  - the base holds what every derived type keeps (a title, a one-line statement, typed parts, links, child topics), as the DITA base does;
  - a derived type adds or narrows parts and never removes a base part, so a reader of the base always finds them;
  - the type is announced to the reader, not only declared in markup, since the positive results all rest on readers who knew the type.
- It does not claim a new result or the state of the art.
