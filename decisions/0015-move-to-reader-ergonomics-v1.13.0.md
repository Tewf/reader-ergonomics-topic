# 0015: Move to reader-ergonomics v1.13.0

**Decision:** this repository checks against reader-ergonomics v1.13.0, whose standard-links check holds every text
link into the standard to the commit the workflows pin.

**Status:** accepted, 2026-10-29. **Shape:** [decision record](https://github.com/Tewf/reader-ergonomics/blob/bfbe9f7ed27bfdca0c6a4922d0b3e302f9e55d3f/shapes/decision-record.md).

## Context

- The rule since [0009](0009-follow-the-standards-decision-record.md) is that every link into the standard names the
  pinned commit. The bumps to v1.11.0 and v1.12.0 each left the record they superseded at its old commit, and only a
  sibling's check found the two links.
- Release v1.13.0 adds standard-links, so that rule is now a program's check here too.

## Decision

- CI, the site build and every text link name commit 7a76cc6, superseded records included. All linked files resolve
  there, anchors included.

## Consequences

- At v1.13.0 before the move: no finding on master, every judgment answered, the topic check's tests green.
- A pin raise that misses a link now fails CI, as standard-pin already makes it fail for a missed workflow.
- **Bad:** the fifth pin move in a day, after [0014](0014-move-to-reader-ergonomics-v1.12.0.md); each reopens the
  answers of the files it touches.

## See also

[Decisions](README.md); [0014](0014-move-to-reader-ergonomics-v1.12.0.md), the move before.
