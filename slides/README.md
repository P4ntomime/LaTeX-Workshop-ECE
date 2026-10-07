# LaTeX from Scratch — workshop slides

A two-hour hands-on introduction to LaTeX for students of any
discipline, built with [Slidev](https://sli.dev).

The slides are one half of the workshop; the other half is the student
template (`latex-workshop-template`), which the deck refers to
throughout by TODO number.

## Running it

```sh
npm install
npm run dev        # http://localhost:3030, hot-reloads as you edit
npm run build      # static site in dist/
npm run export     # slides.pdf
```

Press `p` in the browser for presenter mode — notes, timer, next-slide
preview. Every slide in this deck has notes.

## Shape of the session

| | Block | Ends with |
|---|---|---|
| 26 min | 1 — Skeleton | `TODO 1.1–1.5`, checkpoint-01 |
| 5 | break | |
| 26 min | 2 — Text | `TODO 2.1–2.6`, checkpoint-02 |
| 5 | break | |
| 26 min | 3 — Maths | `TODO 3.1–3.6`, checkpoint-03 |
| 5 | break | |
| 26 min | 4 — Connections | `TODO 4.1–4.6`, checkpoint-04 |

119 minutes. Each block is roughly 2 min recall, 17 min teaching,
7 min hands-on.

## Layout

```
slides.md              headmatter + imports; edit content in pages/
tools/                 figure generator; NOT shipped to students
pages/
  00-intro.md          hook, poll, why, setup, goal slide
  01-skeleton.md       syntax, minimal doc, sections, TOC, styling
  02-text.md           line breaks, parskip, lists, preamble
  03-math.md           inline/display, equation, align, cases
  04-connections.md    tables, floats, figures, citations
  99-closing.md        wrap-up, packages, resources, licence
components/
  GoalTracker.vue      the advance organiser; returns each block
  HandsOn.vue          the practice slide at the end of each block
  Placeholder.vue      a marked gap where a screenshot still has to go
public/renders/        put the compiled-PDF screenshots here
```

## Before you present: the screenshots

The deck deliberately shows **real compiled output** next to the source
rather than a web-rendered approximation, so students see exactly what
their own compiler will produce. Those images do not exist yet — every
one is marked with a pink `<Placeholder>` box.

Compile the checkpoints, screenshot the relevant part, drop the files
in `public/renders/`, and swap each placeholder for:

```html
<img src="/renders/checkpoint-01-p1.png" class="rounded shadow" />
```

Search for `<Placeholder` to find them all. There are six.

## Two toolchain notes

**`vite.config.ts` disables CSS minification.** With `lineNumbers: true`
in the headmatter, Slidev emits a rule that the lightningcss minifier
refuses to parse and `npm run build` dies. Unminified CSS costs nothing
here. Try deleting the file after a Slidev upgrade.

**Keep comments out of the headmatter.** A `#` comment as the first line
inside the opening `---` makes Slidev parse the block as content rather
than YAML, and every key — theme, `lineNumbers`, `title` — is silently
ignored. Symptom: the deck's browser-tab title is your comment text.

**Want the in-deck PDF download button?** Add `download: true` to the
headmatter and `npm i -D playwright-chromium`. Without the browser
installed the build still succeeds but logs an export error.

## House style in the LaTeX examples

The code on the slides matches the template: one sentence per line,
`\label` on the same line as its `\section`, four-space indents. Block 2
explains the first of these as a consequence of "a newline is just a
space"; block 4 explains the second when it introduces `\label`.

## Licence

**TODO before publishing.** This deck descends from a workshop licensed
CC BY-SA 4.0, so share-alike applies: the repository must credit the
original author with a link, and must itself be released under
CC BY-SA 4.0.

There is deliberately no `LICENSE` file in this directory — the
repository's top-level one covers it. Two things still need filling in:

- the original author and link, in the top-level `LICENSE`
- the same, on the attribution slide at the end of `99-closing.md`

The example document, its figure and the synthetic data in `tools/`
were written for this workshop and fall under the same licence.
