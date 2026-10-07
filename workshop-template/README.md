# LaTeX Workshop — student template

Everything you need for the workshop. By the end of the afternoon you
will have written a short report on how quickly a hot drink goes cold,
containing a title page, a table of contents, sections, lists,
equations, a table, a figure and a bibliography — which is every
ingredient of a term paper or a thesis.

## What is in here

```
.
├── latex-workshop.tex      <- the file you work in, all afternoon
├── references.bib          <- the bibliography database (block 4)
├── figures/
│   └── cooling-curves.pdf  <- the plot you will place in block 4
└── checkpoints/
    ├── checkpoint-00.tex   <- a pristine copy of the starting file
    ├── checkpoint-01.tex   <- state after block 1 (skeleton)
    ├── checkpoint-02.tex   <- state after block 2 (text and lists)
    ├── checkpoint-03.tex   <- state after block 3 (maths)
    └── checkpoint-04.tex   <- the finished document
```

## What this document is

A **worked example**, not a real experiment. Nobody measured any coffee:
the numbers and the plot were invented for this workshop. Your job today
is to *typeset* the report, not to run it — so if a sentence says the
temperature was recorded every 30 seconds, read that as part of the
example, not as homework.

## House style in these files

The `.tex` files follow three conventions. None of them changes the
output by a single pixel; they change how readable the *source* is.

- **One sentence per line.** A long sentence may break at a comma.
  Because a single newline in LaTeX is just a space, this costs nothing
  — and it makes `git diff` show you the sentence that changed instead
  of the whole paragraph.
- **`\label` on the same line as its `\section`.** A paragraph break
  between them can leave `\pageref` pointing at the wrong page.
- **Four spaces per indent level.**

## How to use the checkpoints

**If you get stuck, do not spend the rest of the workshop debugging.**
Open the checkpoint for the block that just ended, copy its whole
contents over `latex-workshop.tex`, and carry on with everybody else.

Each checkpoint already contains the TODO comments for the block that
*follows* it, so you can rejoin at the start of any block without having
lost anything.

The TODOs are numbered by block: `TODO 2.4` is the fourth task of
block 2. They sit in the file at the place where the work belongs, in
the order you meet them reading from top to bottom.

> The checkpoint files are meant to be **copied into**
> `latex-workshop.tex`, not compiled where they sit — their paths to
> `figures/` and `references.bib` assume they are run from the project
> root. On Overleaf that happens to work anyway; locally it does not.

## Getting set up

### Overleaf (recommended for the workshop)

1. Make a free account at <https://overleaf.com> **before** the session.
2. New Project → Upload Project → pick the zip of this folder.
3. Open `latex-workshop.tex` and press *Recompile*.

### Locally (if you would rather)

Install a TeX distribution and an editor:

| Platform | Distribution | Editors that work well              |
|----------|--------------|-------------------------------------|
| Windows  | MiKTeX       | VS Code + LaTeX Workshop, TeXstudio |
| Linux    | TeX Live     | VS Code + LaTeX Workshop, TeXstudio |
| macOS    | MacTeX       | TeXShop, VS Code + LaTeX Workshop   |

Then, from this directory:

```sh
latexmk -pdf latex-workshop.tex
```

`latexmk` runs LaTeX as many times as the document needs, and runs
`biber` for the bibliography, so you never have to count compilation
passes yourself. Overleaf and the VS Code extension do the same thing
for you. To clean up the auxiliary files afterwards:

```sh
latexmk -c
```

## When something goes wrong

1. **Read the first error, not the last one.** One missing brace
   produces a cascade; only the first message points at the real cause.
2. The error names a line number. It is usually right, or a line or two
   late.
3. A `?` prompt means LaTeX has stopped and is waiting for you. Type
   `x` and Enter to quit, fix the source, and compile again.
4. A reference that comes out as `??`, or a citation that comes out as
   a bold `[key?]`, almost always means the **name is wrong** — a typo
   in the key, or a `\label` you never actually wrote. Search your
   source for the name in the warning. (It can also mean the document
   has not been compiled often enough, but any modern setup handles
   that for you, so suspect the name first.)
