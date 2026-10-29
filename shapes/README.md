# Shapes

The topic, the base every shape derives from, and how the four general shapes of reader-ergonomics fit it. The four
are not copied here: each is linked at the release this repository checks against, reader-ergonomics v1.12.0.
Their blocks are unchanged since v1.0.0.

## Contents

| Topic | Summary |
|---|---|
| [topic](topic.md) | the base: a title, a summary that stands for it, a body, the topics it holds and the topics it points to |

## The general shapes, against the topic

Each cell says which part of the shape fills the topic's block.

| Topic block | [note](https://github.com/Tewf/reader-ergonomics/blob/adb53c52fa8eefe0e621e520365157bbbcad1a1a/shapes/note.md) | [report](https://github.com/Tewf/reader-ergonomics/blob/adb53c52fa8eefe0e621e520365157bbbcad1a1a/shapes/report.md) | [folder](https://github.com/Tewf/reader-ergonomics/blob/adb53c52fa8eefe0e621e520365157bbbcad1a1a/shapes/readme-and-folder.md) | [commit](https://github.com/Tewf/reader-ergonomics/blob/adb53c52fa8eefe0e621e520365157bbbcad1a1a/shapes/commit.md) | [decision record](https://github.com/Tewf/reader-ergonomics/blob/adb53c52fa8eefe0e621e520365157bbbcad1a1a/shapes/decision-record.md) |
|---|---|---|---|---|---|
| Title | the topic, named as the field names it | the problem, named by what solving it achieves | what the folder is for | the subject line | NNNN and the choice |
| Summary | one quoted line: what this is and why it matters | one quoted line: what is asked | one or two sentences: the folder's role | the subject line again | the line labelled Decision |
| Body | In three points, Terms, The idea, Check yourself, Open | The plan, the steps, Checks | Example | why it changed, and what it buys | Context, Decision, Consequences |
| Contents | none: one topic per note | the steps, held as sections | Contents, the folder's files | none | none: a record holds no topics |
| See also | Links, renamed | What this tests, a link to the note | See also | none | See also |
| Adds | Terms, Check yourself, Open | What this tests, Checks, If you meet this again | Rules for the folder | the 72-character subject | Status and Shape, between summary and body |

## What the table shows

- **All five fit.** Each keeps every block of the topic, in the topic's order for title and summary. The decision
  record joined the four in reader-ergonomics v1.3.0.
- **Two renames:** the note calls See also "Links"; the report places its one pointer, What this tests, before the plan.
- **One merge:** a commit fills title and summary with the same line, because git shows one line before the body. No
  block is lost, and no other shape needs it.
- **No shape fails**, but these four are the material the topic was drawn from: the held-out test below is the
  fairer one. Neither is a reader study.

## The held-out test, on shapes the topic was not built from

The four shapes above were the material the topic was drawn from, so their fit proves little. On 2026-10-29, after
tagging v0.1.0, six forms of the genre extensions were checked against it. The decision rule was written before
reading them:

- a form fits if title, summary and body are present, renamed or merged;
- a missing block revises the base, or puts the form outside it with a reason;
- a block renamed by half the forms or more gets its names listed.

| Form | Source, at the commit tested | Title | Summary | Result |
|---|---|---|---|---|
| structured proof | reader-ergonomics-academic, `shapes/proof.md`, 1d9760c | the statement | the statement, then a one-line sketch | fits, merged; nested to any depth by construction |
| mathematical article | reader-ergonomics-academic, `shapes/mathematical-article.md`, 1d9760c | the title | a paragraph labelled Abstract, after a byline | fits, with metadata before the summary |
| research paper | reader-ergonomics-academic, `shapes/research-paper.md`, 1d9760c | the title | an Abstract section, after a byline | fits, renamed, with metadata before it |
| proposal, Rust RFC template | named by reader-ergonomics-software-design, `evidence/design-decisions/baseline.md`, 9ffefd3 | a Feature Name field | a Summary section | fits, renamed |
| assertion-evidence slide | reader-ergonomics-presentations, `evidence/presentations/baseline.md`, 710fdb2 | the sentence headline | the same headline | fits, merged |
| decision record, Nygard | named by reader-ergonomics-software-design, `evidence/design-decisions/baseline.md`, 9ffefd3 | the title | none | does not fit |

What the test changed in the topic, by the rule fixed before:

- **Metadata may stand between title and summary**: both papers put a byline there, and the summary is otherwise
  present. Without this, two of the six forms would fail on position alone.
- **The summary may carry a label**, Abstract or Summary. Only two forms rename it, both "Abstract", below the
  half the rule asked for; the label is listed anyway, because the check must find the summary past a byline. Before,
  it took the byline for the summary and passed a paper it should have measured.
- **The Nygard record stays outside the topic as written.** It has no summary: the decision comes after the context.
  It fits with one line added after the title, the decision in a sentence, which the software-design review already
  asks of a proposal. The default slide, a topic-phrase headline over bullets, misses the summary the same way; the
  presentations review's evidence favours the sentence headline that supplies it.

The check of v0.1.0, run unchanged on the three extension repositories (113 documents), found no topic without a
title or summary, none unreachable from the root and no inclusion cycle. It flagged 91 children listed as bare links,
nearly all review steps (frame, protocol, review and the rest) whose roles each review family states once. The rule
was at fault, not the repositories: a child of a declared type may now be listed by its type name. With the eight
steps declared, 3 bare listings remain, the bibliography of each repository, and 4 summaries past 60 words.

## See also

The [repository's front page](../README.md), the parent of this folder.
