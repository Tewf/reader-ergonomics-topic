# 0012: The AI-augmented topic, as this repository's extension

**Decision:** the AI-augmented topic is this repository's extension, started on its own branch. It has one problem,
the topic as the interface between a person, a model and a proof assistant, and one first instance: proofs in Lean.

**Status:** accepted, 2026-10-29; its review named the baseline, B1, with both passes in, and it joined master the
same day. Superseded the same day by [0016](0016-move-the-ai-augmented-strand-out.md): the strand moved to a
repository of its own. **Shape:** [decision record](https://github.com/Tewf/reader-ergonomics/blob/bfbe9f7ed27bfdca0c6a4922d0b3e302f9e55d3f/shapes/decision-record.md).

## Context

- The maintainer proposed a loop. A person writes reasoning as topics, and checks judge the form. A model helps and
  translates formal topics into Lean, Lean judges the logic, and the model turns its verdict into guidance.
- A project that attacks many problems at once stalls; the idea touches writing, models and formal proof together.
- The maintainer judged the topic alone too thin to stand as a repository, and chose to keep the extension here.

## Decision

- A branch, not master: it may be abandoned, and master stays the released topic.
- One problem, the interface; one instance, proofs in Lean. Other targets are named in the scope and left out.
- The work starts with a [grey literature](../evidence/README.md) review, since the tools move faster than the papers.

## Consequences

- It stays in this repository, as the topic's extension: the topic gives it its format, and it gives the topic a use.
- Nothing is built before the review names the baseline to beat.
- **Bad:** the repository takes a second subject beside the topic, with a review that, once its formal pass is in,
  is larger than any of the other three, and the audits grow with it. While the extension lives on its branch, every
  change to master is merged in, and this record was renumbered five times, from 0007 to 0012.

## See also

[Decisions](README.md); the [scope](https://github.com/Tewf/reader-ergonomics-topic/blob/3ce8ec139fc08c2852f77e893b8bc38f073f668e/ai-augmented/README.md), as it stood at v0.5.0; [0016](0016-move-the-ai-augmented-strand-out.md), the move out.
