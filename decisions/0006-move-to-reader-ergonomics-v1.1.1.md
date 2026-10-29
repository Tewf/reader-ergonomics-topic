# 0006 Move to reader-ergonomics v1.1.1

**Decision:** this repository checks against reader-ergonomics v1.1.1, at commit 257958e, instead of v1.0.0.

Status: accepted, 2026-10-29; its pin superseded by [0008](0008-move-to-v1.2.0-and-drop-the-local-quote-check.md). Shape: [decision record](../shapes/decision-record.md).

## Context

- The standard released v1.1.0 and v1.1.1 the same day: decision records, a guarantee per check, property tests,
  and a timeout made a warning. An extension moves to a release deliberately, by changing its pin.
- Run against v1.1.1 before moving, this repository gave 0 errors and two warnings, both about a stylesheet it does
  not have; its tests passed.

## Decision

- CI, the site build and every text link name commit 257958e.
- `checks/config.toml` lists no stylesheet to measure, as the standard's extension contract asks of a repository
  whose site loads the standard's own.

## Consequences

- The four general shapes are unchanged between the two releases, so the conformance table still holds.
- The judgment-quotes check is promised for the standard's v1.2.0; when it ships, this repository drops its copy and
  moves again.

## See also

[Decisions](README.md); [0003](0003-link-the-shapes-never-move-them.md), on why the links name a commit.
