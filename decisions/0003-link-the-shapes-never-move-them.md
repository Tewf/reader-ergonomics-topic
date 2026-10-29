# 0003: Link the four general shapes, never move them

**Decision:** the four general shapes stay in reader-ergonomics; this repository links down to them and shows from its
own side that each fits the topic.

**Status:** accepted, 2026-10-29. It replaces a plan withdrawn the same day. **Shape:** [decision record](https://github.com/Tewf/reader-ergonomics/blob/adb53c52fa8eefe0e621e520365157bbbcad1a1a/shapes/decision-record.md).

## Context

- The topic is meant as the base the shapes derive from, and the four general shapes (note, report, folder, commit)
  live in reader-ergonomics, one level below.
- The first plan moved them here and had reader-ergonomics link to this repository. The standard's extension
  contract forbids it: the standard never links to, or depends on, an extension.

## Decision

- reader-ergonomics is not edited for the topic.
- The fit is a **structural fit**: a shape fits the topic because it has the topic's blocks, not because it declares it, as
  a type satisfies an interface in Go or TypeScript.
- The links name the release's commit, so they stay true while the standard changes.

## Consequences

- The arrows all point down, and each shape's skeleton stays in one place.
- No shape of reader-ergonomics declares the topic; only a genre extension could, in its own repository.
- **Bad:** a reader checking a shape's fit follows a link into another repository, one hop more. A change to a general
  shape reaches this repository only when its pin moves, so the conformance table can lag the standard until then.

## See also

[Decisions](README.md); the [conformance table](../shapes/README.md).
