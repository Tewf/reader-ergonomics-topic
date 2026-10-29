# 0010: Move to reader-ergonomics v1.4.1

**Decision:** this repository checks against reader-ergonomics v1.4.1, whose figure-width check and phone stylesheet
take over what its text figures were measured against by hand.

**Status:** accepted, 2026-10-29. **Shape:** [decision record](https://github.com/Tewf/reader-ergonomics/blob/03cfbc9dd1d243aa86f8ba3168abc61be2bab19f/shapes/decision-record.md).

## Context

- A peer's screenshot showed the front page's figure cut mid-word on the site. Nine text figures here ran past 60
  columns; they were redrawn under 56, measured by hand.
- At 375 px the site's column held about 29 monospace characters, so no figure width fitted a phone: that fix
  belonged to the standard's stylesheet.
- Release v1.4.0, at commit ff809a3, adds `figure-width`, a warning past 60 columns.
- Release v1.4.1, at commit 03cfbc9, shrinks a text figure on screens under 600 px so that its 60 columns show, down
  to 9 px.
- Releases v1.3.1 and v1.3.2 between them changed two references and the line ceiling's exemptions.

## Decision

- CI, the site build and every text link name commit 03cfbc9. All 25 linked files resolve there, anchors included.
- The figure width is not set here: the standard's 60 columns, marked provisional there, apply.

## Consequences

- Run at v1.4.1 before the move, master and the extension's branch gave no error and no warning, every judgment
  answered, and the topic check's tests passed. The new check finds no figure past 60 columns.
- The phone rule of v1.4.1 was applied to the published front page at 375 px. Its figure dropped from 16.7 px to
  9 px type and fitted whole: 324 px wide in a 324 px column, against 516 px before.
- **Bad:** 9 px is far below the 16 px the standard sets for body text. On a phone a figure is seen whole but read
  with effort; the standard chose that over a figure cut at its right side, and this repository takes its choice.
- **Bad:** the move touched 32 files and reopened 11 judgment answers on master, each checked before it was carried over.
- The commit shape's text changed in v1.4.0: its figure was rewrapped and one rule moved to a list. Its blocks did not
  change, so the [conformance table](../shapes/README.md) holds.

## See also

[Decisions](README.md); [0009](0009-follow-the-standards-decision-record.md), the move before.
