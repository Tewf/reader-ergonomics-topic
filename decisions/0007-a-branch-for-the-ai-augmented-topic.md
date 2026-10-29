# 0007 A branch for the AI-augmented topic

**Decision:** the AI-augmented topic starts on its own branch of this repository. It has one problem, the topic as
the interface between a person, a model and a proof assistant, and one first instance: proofs in Lean.

Status: accepted, 2026-10-29.

## Context

- The maintainer proposed a loop. A person writes reasoning as topics, and checks judge the form. A model helps and
  translates formal topics into Lean, Lean judges the logic, and the model turns its verdict into guidance.
- A project that attacks many problems at once stalls; the idea touches writing, models and formal proof together.

## Decision

- A branch, not master: it may be abandoned, and master stays the released topic.
- One problem, the interface; one instance, proofs in Lean. Other targets are named in the scope and left out.
- The work starts with a grey literature review, since the tools move faster than the papers.

## Consequences

- If the work grows into its own problem, it moves to its own repository, in the family's naming scheme.
- Nothing is built before the review names the baseline to beat.

## See also

[Decisions](README.md); the [scope](../ai-augmented/README.md).
