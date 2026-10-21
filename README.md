# LaTeX Workshop

An introductory LaTeX workshop for bachelor students of any discipline,
held at OST (Ostschweizer Fachhochschule). In about two hours,
participants go from an empty file to a short lab report with a title,
a table of contents, sections, lists, equations, a table, a figure and a
bibliography: every ingredient of a term paper or a thesis.

No previous LaTeX knowledge is needed, and nobody has to keep up: every
block ends with a checkpoint file that puts everyone back on track.

## For participants

Everything you need is attached to the
[latest release](https://github.com/P4ntomime/LaTeX-Workshop-ECE/releases/latest):

| File                     | What it is                                              |
|--------------------------|---------------------------------------------------------|
| `workshop-template.zip`  | The template you work in during the workshop            |
| `slides.pdf`             | The slides                                              |
| `handout.pdf`            | The handout: everything on the slides, plus the details |

Download `workshop-template.zip` from the release, not the "Source code"
zip. The [template's README](template/README.md) explains how to open it
in Overleaf (recommended for the workshop) or on your own computer.

Before the session, make a free account at <https://overleaf.com>.

## The workshop

The running example is a short lab report on Newton's law of cooling,
*How Fast Does Your Coffee Go Cold?* The numbers and the plot are
invented for the workshop; the point is to typeset the report, not to
run the experiment. The report text is already in the template as
comments, so the TODOs are about the LaTeX around it.

| Block | Topic                        | Covers                                                  | TODOs   |
|-------|------------------------------|---------------------------------------------------------|---------|
| 1     | Skeleton                     | Commands, environments, title, sections, table of contents, text styling | 1.1–1.5 |
| 2     | Text                         | Paragraphs, line breaks, lists, preamble and packages   | 2.1–2.7 |
| 3     | Math                         | Math mode, sub- and superscripts, equations, alignment  | 3.1–3.4 |
| 4     | Illustrations & References   | Tables, figures, cross-references, citations            | 4.1–4.6 |

Each block is a short input followed by 5 to 10 minutes of hands-on work
on its TODOs, with a short break between blocks. A closing part points to
useful packages, larger documents and where to look things up.

## Repository layout

```
.
├── slides/      Beamer slides with presenter notes
├── template/    Source of the student template (workshop.tex and checkpoints)
├── handout/     The handout, a LaTeX report
└── LICENSE.txt  CC BY-SA 4.0
```

- [`slides/`](slides/README.md): the deck, one file per block in
  `sections/`. Every piece of code shown on a slide lives in `listings/`,
  and every example output is a pre-compiled PDF in `renders/`, so it
  looks exactly like the students' own document.
- [`template/`](template/README.md): `master.tex` is the single source of
  `workshop.tex` and all checkpoints; `gen.py` generates them. Never edit
  the generated files in `template/build/`.
- `handout/`: the handout, one file per chapter in `chapters/`. It reuses
  the slides' listings and renders, and shows the finished template in
  its appendix.

## Building

You need a current TeX Live (the 2026 materials were built with TeX Live
2026), `latexmk`, `biber`, Python 3 with Pygments (for `minted` in the
slides) and `make`. The slides use the Noto and Inconsolata fonts, the
handout newtx (Times).

The three parts depend on each other, so build them in this order:

```sh
make -C template test     # generate the template and compile every state
make -C slides renders    # re-compile the example outputs (only after changing them)
make -C slides            # slides.pdf (minted needs -shell-escape; latexmkrc sets it)
make -C handout           # handout.pdf (reads ../slides and ../template/build)
```

`make -C template zip` writes `template/build/workshop-template.zip`, the
file that goes into a release. `make test` fails on any LaTeX error or
warning, so a template that passes compiles cleanly for the students.

To change the template, edit `template/master.tex` and run
`make -C template test`; the checkpoints are regenerated from it and
cannot drift apart.

## Licence and attribution

This work is licensed under
[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/): you may
share and adapt it, also commercially, as long as you give credit and
share your version under the same licence.

- Based on the LaTeX-Workshop slides by Naoki Pross,
  <https://github.com/OST-Stud/LaTeX-Workshop>, CC BY-SA 4.0.
- This revision: Laurin Heitzer, MSE EE, 2026.
- Example document and figure: written for this workshop, synthetic data.