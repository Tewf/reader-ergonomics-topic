# Shapes

The topic, the base every shape derives from, and how the four general shapes of reader-ergonomics fit it. The four
are not copied here: each is linked at the release this repository checks against, reader-ergonomics v1.0.0.

## Contents

| Topic | Summary |
|---|---|
| [topic](topic.md) | the base: a title, a summary that stands for it, a body, the topics it holds and the topics it points to |

## The four general shapes, against the topic

Each cell says which part of the shape fills the topic's block.

| Topic block | [note](https://github.com/Tewf/reader-ergonomics/blob/40cd9fb3ed21a01a8913788edc46ade9562a797d/shapes/note.md) | [report](https://github.com/Tewf/reader-ergonomics/blob/40cd9fb3ed21a01a8913788edc46ade9562a797d/shapes/report.md) | [folder](https://github.com/Tewf/reader-ergonomics/blob/40cd9fb3ed21a01a8913788edc46ade9562a797d/shapes/readme-and-folder.md) | [commit](https://github.com/Tewf/reader-ergonomics/blob/40cd9fb3ed21a01a8913788edc46ade9562a797d/shapes/commit.md) |
|---|---|---|---|---|
| Title | the topic, named as the field names it | the problem, named by what solving it achieves | what the folder is for | the subject line |
| Summary | one quoted line: what this is and why it matters | one quoted line: what is asked | one or two sentences: the folder's role | the subject line again |
| Body | In three points, Terms, The idea, Check yourself, Open | The plan, the steps, Checks | Example | why it changed, and what it buys |
| Contents | none: one topic per note | the steps, held as sections | Contents, the folder's files | none |
| See also | Links, renamed | What this tests, a link to the note | See also | none |
| Adds | Terms, Check yourself, Open | What this tests, Checks, If you meet this again | Rules for the folder | the 72-character subject |

## What the table shows

- **All four fit.** Each keeps every block of the topic, in the topic's order for title and summary.
- **Two renames:** the note calls See also "Links"; the report places its one pointer, What this tests, before the plan.
- **One merge:** a commit fills title and summary with the same line, because git shows one line before the body. No
  block is lost, and no other shape needs it.
- **No shape fails**, so nothing here argues against the base. The table was built by reading the four skeletons; it
  is not a reader study.

## See also

The [repository's front page](../README.md), the parent of this folder.
