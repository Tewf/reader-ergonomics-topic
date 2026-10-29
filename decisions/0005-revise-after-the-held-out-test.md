# 0005: Revise the topic after the held-out test

**Decision:** the topic allows metadata before the summary, names the summary's labels, and lets a typed child be
listed by its type; the Nygard decision record stays outside it as written.

**Status:** accepted, 2026-10-29, released as v0.2.0. **Shape:** [decision record](https://github.com/Tewf/reader-ergonomics/blob/d408349e4bc0f8e9ac7672645bd2aa393e5e6704/shapes/decision-record.md).

## Context

- v0.1.0 was checked only against the four shapes it was drawn from.
- Six forms of the genre extensions were checked against it, with the decision rule written before they were read;
  its check was run unchanged on 113 documents of those repositories.

## Decision

- A byline or a status may stand between title and summary: both papers put one there.
- A summary may be labelled Abstract or Summary, so the check finds it past a byline instead of taking the byline for
  it.
- A child of a declared type may be listed by its type name: 91 of 113 documents were flagged otherwise, nearly all
  review steps whose role each family states once.

## Consequences

- Five of six held-out forms fit. The decision record fits with one sentence added under its title; the records in
  this folder are written that way.
- Two forms renamed the summary, below the half the rule asked for: the labels were listed for the check's sake, and
  the record says so.

## See also

[Decisions](README.md); the [held-out test](../shapes/README.md).
