# 0014: Move to reader-ergonomics v1.12.0

**Decision:** this repository checks against reader-ergonomics v1.12.0, whose standard-pin check holds every workflow
step that checks out the standard to one commit.

**Status:** accepted, 2026-10-29. **Shape:** [decision record](https://github.com/Tewf/reader-ergonomics/blob/7a76cc6a86b7a5c1e451e4416534d113abd0f594/shapes/decision-record.md).

## Context

- A pin raise edits every workflow that checks out the standard. In another extension, one raise left the site build
  fetching its stylesheet from an older release while CI moved on.
- This repository has three such steps: two jobs in checks.yml and the stylesheet in pages.yml. They were checked by
  hand before this move and all named the same commit.
- Release v1.12.0 adds standard-pin, which makes that a program's check.

## Decision

- CI, the site build and every text link name commit adb53c5. All 31 linked files resolve there, anchors included.

## Consequences

- Checked first at the new release: no finding on master, all of its judgments answered, the topic check's tests
  green.
- A pin raise that misses a workflow now fails CI instead of drifting unseen.
- **Bad:** the fourth pin move in a day, after [0013](0013-move-to-reader-ergonomics-v1.11.0.md); each rewrites the
  links of most files and reopens their answers.

## See also

[Decisions](README.md); [0013](0013-move-to-reader-ergonomics-v1.11.0.md), the move before.
