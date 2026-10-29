# 0009: Follow the standard's decision record

**Decision:** this repository's records follow the decision-record shape of reader-ergonomics v1.3.0, and its own copy
of the shape is removed.

**Status:** accepted, 2026-10-29. **Shape:** [decision record](https://github.com/Tewf/reader-ergonomics/blob/03cfbc9dd1d243aa86f8ba3168abc61be2bab19f/shapes/decision-record.md).

## Context

- The shape was first written here (0007), and software-design wrote one too. Each was one level above a repository
  that needed it, and neither could be linked from below.
- Three levels of the family write decision records. The sessions agreed to move the general form down to the
  standard, which carries its own evidence for it. v1.3.0, at commit d408349, ships it in this form.

## Decision

- `shapes/decision-record.md` is removed; every record links the standard's shape, at the pinned commit, and takes
  its form: `# NNNN:` before the choice, **Status** and **Shape** in bold.
- The topic check accepts a shape linked in another repository, so the records still announce theirs.
- CI, the site build and every text link name commit d408349.

## Consequences

- The decision record fits the topic as the four general shapes do; the conformance table now has five columns.
- The topic has no derived shape of its own again. Its first ones will come from its extension.

## See also

[Decisions](README.md); [0007](0007-derive-the-decision-records-from-the-topic.md), which wrote the shape here.
