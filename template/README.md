# LaTeX Workshop: student template

Everything you need for the workshop. By the end of the afternoon you
will have written a short report on how quickly a hot drink goes cold,
with a title, a table of contents, sections, lists, equations, a table,
a figure and a bibliography: every ingredient of a term paper or a
thesis.

## What is in here

```
.
├── workshop.tex            <- the file you work in, all afternoon
├── references.bib          <- the bibliography database (block 4)
├── figures/
│   └── cooling-curves.pdf  <- the plot you will place in block 4
└── checkpoints/
    ├── checkpoint-00.tex   <- an untouched copy of workshop.tex
    ├── checkpoint-01.tex   <- state after block 1 (skeleton)
    ├── checkpoint-02.tex   <- state after block 2 (text)
    ├── checkpoint-03.tex   <- state after block 3 (math)
    └── checkpoint-04.tex   <- the finished document
```

## What this document is

A **worked example**, not a real experiment. Nobody measured any coffee:
the numbers and the plot were invented for this workshop. Your job today
is to *typeset* the report, not to run it. If a sentence says the
temperature was recorded every 30 seconds, read that as part of the
example, not as homework.

## How the TODOs work

All TODOs of the workshop are in `workshop.tex` from the start. They are
numbered by block: `TODO 2.4` is the fourth task of block 2. Search for
`TODO 2.` to find every TODO of block 2; some of them have a part in the
preamble as well.

The text of the report is already in the file, as comments. Write your
own, or uncomment it (on Overleaf and in VS Code: select the lines and
press `Ctrl+/`, or `Cmd+/` on a Mac). The TODOs are about the commands
around the text.

## House style in these files

The `.tex` files follow three conventions. None of them changes the
output; they make the *source* easier to read.

- **One sentence per line.** A long sentence may break at a comma.
  A single newline in LaTeX is just a space, so this costs nothing, and
  `git diff` then shows the sentence that changed instead of the whole
  paragraph.
- **`\label` on the same line as its `\section`.** A paragraph break
  between them can leave `\pageref` pointing at the wrong page.
- **Four spaces per indent level.**

## How to use the checkpoints

**If you get stuck, do not spend the rest of the workshop debugging.**
Open the checkpoint for the block that just ended, copy its whole
contents over `workshop.tex`, and carry on with everybody else.

A checkpoint is `workshop.tex` with every TODO up to that block done.
The later TODOs are still in it, so you continue exactly where everybody
else is. Optional TODOs are never done in a checkpoint.

> The checkpoint files are meant to be **copied into** `workshop.tex`,
> not compiled where they sit: their paths to `figures/` and
> `references.bib` assume they are run from the project root.

## Getting set up

### Overleaf (recommended for the workshop)

1. Make a free account at <https://overleaf.com> **before** the session.
2. Download `workshop-template.zip` from the latest release of the
   repository (not the "Source code" zip).
3. New Project → Upload Project → pick `workshop-template.zip`.
4. Open `workshop.tex` and press *Recompile*.
   If Overleaf compiles a checkpoint instead, open the menu and set
   *Main document* to `workshop.tex`.

### Locally (if you would rather)

Install a TeX distribution and an editor:

| Platform | Distribution | Editors that work well              |
|----------|--------------|-------------------------------------|
| Windows  | MiKTeX       | VS Code + LaTeX Workshop, TeXstudio |
| Linux    | TeX Live     | VS Code + LaTeX Workshop, TeXstudio |
| macOS    | MacTeX       | TeXShop, VS Code + LaTeX Workshop   |

Unpack `workshop-template.zip` into a folder of its own. Then, from that
folder:

```sh
latexmk -pdf workshop.tex
```

`latexmk` runs LaTeX as many times as the document needs, and runs
`biber` for the bibliography, so you never have to count compilation
passes yourself. Overleaf and the VS Code extension do the same thing
for you.

`latexmk` is a Perl script. Linux and macOS come with Perl, and TeX Live
for Windows brings its own. MiKTeX does not: on Windows with MiKTeX, install
[Strawberry Perl](https://strawberryperl.com) first, otherwise `latexmk`
stops with a message that it cannot find `perl`.

To clean up the auxiliary files afterwards:

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
   its key in bold, almost always means the **name is wrong**: a typo
   in the key, or a `\label` you never actually wrote. Search your
   source for the name in the warning. (It can also mean the document
   has not been compiled often enough, but any modern setup handles
   that for you, so suspect the name first.)
