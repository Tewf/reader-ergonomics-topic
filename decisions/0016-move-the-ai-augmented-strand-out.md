# 0016: Move the AI-augmented strand out of this repository

**Decision:** the AI-augmented strand leaves, with its git history, for a repository of its own that will pin a
release of the topic. The topic keeps one template, its check and its three reviews.

**Status:** accepted, 2026-10-29. Supersedes [0012](0012-ai-augmented-topic-as-an-extension.md). **Shape:** [decision record](https://github.com/Tewf/reader-ergonomics/blob/7a76cc6a86b7a5c1e451e4416534d113abd0f594/shapes/decision-record.md).

## Context

- Record 0012 kept the strand here, since the topic alone seemed thin. It joined master the same day, as v0.5.0.
- Its subject is checking reasoning, where this repository's scope has said from the start that how a claim is proved
  or verified is out. The two now contradicted each other on the front page.
- The strand is about to grow code and a proof assistant in CI, while the topic is stable; and the topic no longer
  needs a guest to show its use: reader-ergonomics-learning pins it.

## Decision

- The folders ai-augmented/ and evidence/autoformalization/ leave, with their history, filtered out of this one.
- The 282 bibliography rows only they cited leave with them; a work both cite stays in both bibliographies.
- Their state at departure stays readable at v0.5.0, and record 0012 links it there.

## Consequences

- The scope and the contents agree again: one template, its check, three reviews of 218 sources.
- The strand becomes a sibling, a second adopter of the topic beside learning, and the family's key check gains a
  repository once it is published.
- **Bad:** until the new repository is published, the strand's latest work is reachable only in this repository's
  history and at v0.5.0, and links to its pages on this site stop resolving.

## See also

[Decisions](README.md); [0012](0012-ai-augmented-topic-as-an-extension.md), the record it supersedes.
