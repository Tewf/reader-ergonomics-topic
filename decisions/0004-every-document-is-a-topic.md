# 0004: Every document here is a topic, checked in CI

**Decision:** every document of this repository is declared a topic, and the topic check runs on all of them in CI.

**Status:** accepted, 2026-10-29. **Shape:** [decision record](https://github.com/Tewf/reader-ergonomics/blob/03cfbc9dd1d243aa86f8ba3168abc61be2bab19f/shapes/decision-record.md).

## Context

- A template no document follows cannot show its cost or its faults.
- reader-ergonomics is its own first example of the standard; this repository can be the same for the topic.

## Decision

- `checks/config.toml` declares README.md, evidence/, shapes/ and decisions/ as the tree.
- The check runs with the standard's checks on every push, and its tests run beside it.

## Consequences

- The first run found 21 faults in this repository: shapes/ unreachable from the front page, two reviews listing
  their files as bare links, three summaries too long. All are fixed.
- Every new file must be listed by its folder's README with its summary, or CI fails.

## See also

[Decisions](README.md); the [check](../checks/local/topic.py).
