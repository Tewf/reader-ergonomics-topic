# 0013: Move to reader-ergonomics v1.11.0

**Decision:** this repository checks against reader-ergonomics v1.11.0, whose figure checks now hold the drawn figures
the extension brought to master.

**Status:** accepted, 2026-10-29. **Shape:** [decision record](https://github.com/Tewf/reader-ergonomics/blob/adb53c52fa8eefe0e621e520365157bbbcad1a1a/shapes/decision-record.md).

## Context

- The extension joined master with eight drawn figures, beside the five drawn earlier, each a Graphviz source with its
  SVG and the source folded under the image.
- Release v1.10.0 adds the family's four figure checks. A drawn figure is due where a typed one stood; its alt text
  says what it shows; its SVG is stamped from its source; its lines reach a contrast of at least 3:1.
- Release v1.11.0 lets an organisation's citation key carry a title word, and fixes llms.txt for a card without
  principles; neither changes a finding here.

## Decision

- CI, the site build and every text link name commit 6980fa6. All 31 linked files resolve there, anchors included.

## Consequences

- Run at v1.11.0 before the move, master gave no error and no warning, every judgment answered, and the topic check's
  tests passed; its thirteen drawn figures pass the four figure checks.
- **Bad:** this is the third pin move in a day, after [0010](0010-move-to-reader-ergonomics-v1.4.1.md) and
  [0011](0011-move-to-reader-ergonomics-v1.9.0.md); each rewrote the links of most files and reopened their answers.

## See also

[Decisions](README.md); [0011](0011-move-to-reader-ergonomics-v1.9.0.md), the move before.
