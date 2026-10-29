# Shape: topic

The base every shape derives from: a unit of writing with a title, a summary that stands for it, a body, and the topics
it contains or points to. A genre shape adds blocks to it and removes none.

A **topic** is one unit of writing that a reader can take alone. Its parts may be topics of the same shape, to any depth.

## Skeleton

```markdown
# <Title: what the topic holds, in the field's words>

<Summary: one to three sentences that stand for the topic wherever it is folded or listed.>

<Body: the parts, in the order the reader needs them.>

## Contents          the topics this one holds, each by its title and its summary;
                     omit the section while there are none

| Topic | Summary |
|---|---|
| [title of the child](child.md) | the child's summary |

## See also          topics this one points to without holding them: its parent, and related topics
```

## The blocks

| Block | Rule | Principle | Evidence |
|---|---|---|---|
| Title | one per topic; it names what the topic holds | [names predict content](https://github.com/Tewf/reader-ergonomics/blob/d408349e4bc0f8e9ac7672645bd2aa393e5e6704/principles/collection/names-predict-content.md) | DITA requires a title on every topic ([information typing](../evidence/information-typing/review.md)) |
| Summary | right after the title, or after its metadata (a byline, a status); at most 60 words; it may be labelled Abstract or Summary; it stands for the topic when folded or listed | [overview first](https://github.com/Tewf/reader-ergonomics/blob/d408349e4bc0f8e9ac7672645bd2aa393e5e6704/principles/document/overview-first.md) | a folded node must carry a summary ([progressive disclosure](../evidence/progressive-disclosure/position.md)) |
| Body | the parts in the reader's order; at most three heading levels | [shallow outline](https://github.com/Tewf/reader-ergonomics/blob/d408349e4bc0f8e9ac7672645bd2aa393e5e6704/principles/document/shallow-outline.md) | readers keep the top levels best (levels effect, reader-ergonomics [psycholinguistics](https://github.com/Tewf/reader-ergonomics/tree/d408349e4bc0f8e9ac7672645bd2aa393e5e6704/evidence/psycholinguistics)) |
| Contents | each child by its title and its summary, or by its type alone when the type's role is stated once | [signal the structure](https://github.com/Tewf/reader-ergonomics/blob/d408349e4bc0f8e9ac7672645bd2aa393e5e6704/principles/page/signal-the-structure.md) | readers rarely open a layer they cannot judge from outside ([progressive disclosure](../evidence/progressive-disclosure/review.md)) |
| See also | links, never copies | [one place per fact](https://github.com/Tewf/reader-ergonomics/blob/d408349e4bc0f8e9ac7672645bd2aa393e5e6704/principles/collection/one-place-per-fact.md) | the standards reuse by reference ([document model](../evidence/document-model/position.md)) |

The 60 words are a tunable: `summary_words` in `checks/config.toml`, PROVISIONAL until a reader study sets it.

## How a shape derives from it

```text
                              topic
            title · summary · body · contents · see also
                                ▲
         ┌───────────────┬──────┴─────────┬──────────────────┐
       note            report           folder             commit
   + terms           + what it tests   + example          title and summary
   + check yourself  + plan and steps  + rules for          share one line
   + open            + checks            the folder
   see also: Links
```

- **Keep every block.** A derived shape keeps all five. It may call a block by another of its accepted names, from
  the table below, and by no other. It may leave Contents or See also empty while there is nothing to hold.
- **Title and summary come first**, in that order: they are what a folded view shows. Only metadata may stand between
  them. The other blocks may be ordered by the shape.
- **Add, never remove.** A shape adds its own blocks, such as a note's Check yourself.
- **Announce the type.** A document links the shape it follows, so a reader knows which blocks to expect, and the
  check knows which to look for.
- Grade: convention, untested. Whether a reader who knows the topic reads a derived shape better is the open question
  of [information typing](../evidence/information-typing/position.md).

The accepted names, in one place. A shape that needs a new name adds it here first, with the shape that uses it:

| Block | Accepted names | Used by |
|---|---|---|
| Title | the one `# ` heading; a subject line | every shape; a commit |
| Summary | summary, abstract, short description, decision | the topic; papers; DITA; the [decision record](https://github.com/Tewf/reader-ergonomics/blob/d408349e4bc0f8e9ac7672645bd2aa393e5e6704/shapes/decision-record.md) |
| Contents | contents, files, steps | the topic and a folder; a review's README; a report |
| See also | see also, links, references, uses | the topic and a folder; a note; papers; a proof |

The [decision record](https://github.com/Tewf/reader-ergonomics/blob/d408349e4bc0f8e9ac7672645bd2aa393e5e6704/shapes/decision-record.md) was first written here, then moved down to reader-ergonomics (v1.3.0), where three
levels can link it; it fits the topic like the four general shapes. The topic's own derived shapes will come from
its extension.

The four general shapes of reader-ergonomics, and six forms of the genre extensions it was not built from, are
checked against these rules in [the conformance table](README.md). Five of the six fit; a decision record without a
summary does not.

## Depth

- **In storage, any depth.** A topic may hold topics that hold topics.
- **In view, at most three levels.** A view shows the topic, its children by their summaries, and one level more.
- **The path to the root is always there.** A topic read alone names its parent in See also; the site shows the full
  path.
- What most readers need sits in the summary and the first part of the body, above the first fold.
- Grade: supported with caveat, never tested as such ([progressive disclosure](../evidence/progressive-disclosure/position.md)).

## Graph

- **One containing parent.** A topic lives in one place: in a repository, one folder or one file.
- **Any other parent points to it.** It links the topic and never copies it.
- **No topic contains itself**, directly or through an inclusion, at any depth.
- Grade: convention, the rule of every document model read ([document model](../evidence/document-model/position.md)).

## The check

[`checks/local/topic.py`](../checks/local/topic.py) runs on every topic declared in `checks/config.toml`, at any
depth:

| Rule | Kind |
|---|---|
| one title, and it opens the topic | error |
| a summary right after the title, or labelled within its first blocks | error |
| the summary within `summary_words` | warning |
| listed by its containing topic, so it can be reached from the root | error |
| listed with its summary, or by its declared type, not as a bare link | warning |
| no inclusion cycle | error |

Heading depth, links that resolve and the headings a shape requires are checked by reader-ergonomics itself.

## See also

[Shapes](README.md), the folder this shape heads; the [evidence](../evidence/README.md) behind each rule.
