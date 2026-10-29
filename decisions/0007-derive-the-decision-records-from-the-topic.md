# 0007 Derive the decision records from the topic

**Decision:** the decision record is the first shape derived from the topic, this repository's records follow it,
and the check verifies that each one says so.

Status: accepted, 2026-10-29. Shape: [decision record](../shapes/decision-record.md).

## Context

- The topic was meant as a base that shapes derive from, yet nothing declared it: the four general shapes fit it
  only structurally.
- The topic's rule that a document announces its type had no check, and a shape could rename any block freely.

## Decision

- [shapes/decision-record.md](../shapes/decision-record.md) derives from the topic, block by block.
- Every record links that shape in its Status line; the topic check fails a declared file that does not.
- The topic lists the accepted names of each block in one table; a shape uses those names, and a new one is added
  there first.

## Consequences

- The derivation rule is now exercised on real documents and checked, not only described.
- Path answers in `checks/judgments.toml` must quote a name from their path, closing the gap template answers could
  still pass through.

## See also

[Decisions](README.md); the [topic](../shapes/topic.md).
