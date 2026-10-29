# Shape: decision record

A topic that records one choice and why it was made: Nygard's decision record, with the summary the held-out test
found it lacks. It is the first shape derived from the topic in this repository, and its own records use it.

## Skeleton

```markdown
# <NNNN The choice, as an action>

**Decision:** <the choice in one sentence; a reader who stops here knows what was decided>

Status: <accepted, superseded by NNNN, or withdrawn>, <date>. Shape: [decision record](<path to this file>).

## Context              the situation that made a choice necessary, and the facts it rests on

## Decision             what was chosen, in full sentences

## Consequences         what follows, good and bad, and what it leaves open

## See also             the folder that lists the records, and the work the choice concerns
```

## How it derives from the topic

| Topic block | Here | Change |
|---|---|---|
| Title | `# NNNN` and the choice as an action | numbered, so records keep their order |
| Summary | the line labelled **Decision** | a named label, listed among the topic's accepted names |
| Body | Context, Decision, Consequences | added, in Nygard's order |
| Contents | none | a record holds no topics |
| See also | See also | kept |
| (metadata) | Status and Shape | the line between summary and body, which the topic allows |

It keeps every block of the topic, and adds Status, Context, Decision and Consequences.

## Checked by

- the [topic check](../checks/local/topic.py): title, summary, listed by the decisions README, and the Shape link that
  announces the type;
- the standard's shape check, declared in `checks/config.toml`: the headings Context, Decision, Consequences and See
  also.

## See also

[Shapes](README.md), and the base it derives from: the [topic](topic.md).
