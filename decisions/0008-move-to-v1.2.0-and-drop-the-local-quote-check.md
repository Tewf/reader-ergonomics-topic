# 0008: Move to reader-ergonomics v1.2.0, and drop the local quote check

**Decision:** this repository checks against reader-ergonomics v1.2.0, whose judgment-quotes check replaces the local
copy, and it keeps that check strict on path questions.

**Status:** accepted, 2026-10-29. **Shape:** [decision record](https://github.com/Tewf/reader-ergonomics/blob/03cfbc9dd1d243aa86f8ba3168abc61be2bab19f/shapes/decision-record.md).

## Context

- The local check that an answer quotes its own file was built here and in software-design the same day. Two copies
  of one check drift, so it was offered to the standard.
- v1.2.0, at commit 6d4e324, carries it, built from both copies. By default it makes path questions optional, so
  that no extension fails on its next pin.

## Decision

- The local check and its tests are removed; CI, the site build and the text links name commit 6d4e324.
- `checks/config.toml` sets `[judgment_quotes] optional = []`: this repository's path answers already quote their
  paths, so they stay required.

## Consequences

- The check lives in one place. Its first run here caught an answer quoting a file the removal had just deleted.
- The decision-record shape is promised for the standard's v1.3.0; when it ships, this repository's shape moves down
  to it.

## See also

[Decisions](README.md); [0006](0006-move-to-reader-ergonomics-v1.1.1.md), the move before.
