# 0011: Move to reader-ergonomics v1.9.0

**Decision:** this repository checks against reader-ergonomics v1.9.0. Its checks now hold what the family's audits
asked of this repository by hand: one key per work, a record's rules, a shape's example, drawn figures.

**Status:** accepted, 2026-10-29. **Shape:** [decision record](https://github.com/Tewf/reader-ergonomics/blob/adb53c52fa8eefe0e621e520365157bbbcad1a1a/shapes/decision-record.md).

## Context

- The standard released v1.5.0 to v1.9.0 in one day, most of it from the family's audits of one another.
- Release v1.5.0 checks that a key names one work across the family; v1.6.0 checks the rules of a decision record;
  v1.7.0 checks that a shape links a filled example.
- Releases v1.8.0 and v1.9.0 draw figures as SVG from Graphviz sources, each source folded under its figure and kept
  equal to its file.
- This repository met each rule by hand first. Its keys were reconciled and its records name their costs; the topic
  shape links a filled topic, and its five figures are drawn, with their sources folded under them.

## Decision

- CI, the site build and every text link name commit e886447. All 31 linked files resolve there, anchors included.

## Consequences

- Each general shape gained a worked example; their blocks did not change, so the
  [conformance table](../shapes/README.md) holds.
- **Bad:** five releases in a day mean the pin lags again as soon as it moves, and each move rewrites the links of most
  files and reopens their judgment answers.
- **Bad:** records run without a gap, so the extension's record, numbered 0011 on its branch, becomes 0012 there, its
  fifth renumbering since the branch opened.

## See also

[Decisions](README.md); [0010](0010-move-to-reader-ergonomics-v1.4.1.md), the move before.
