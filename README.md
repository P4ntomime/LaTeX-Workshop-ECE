# LaTeX Workshop

An introductory LaTeX workshop for bachelor students of any discipline,
held at OST (Ostschweizer Fachhochschule). In about two hours,
participants go from an empty file to a short lab report with a title,
a table of contents, sections, lists, equations, a table, a figure and a
bibliography: every ingredient of a term paper or a thesis.

No previous LaTeX knowledge is needed, and nobody has to keep up: every
block ends with a checkpoint file that puts everyone back on track.

<div align="center">
  <a href="https://p4ntomime.github.io/LaTeX-Workshop-ECE/">
    <img src="site/readme-button.svg" alt="LaTeX Workshop" width="540">
  </a>
</div>

## For participants

The [workshop page](https://p4ntomime.github.io/LaTeX-Workshop-ECE/) has
everything you need, in the latest version: the slides, the handout and
`workshop-template.zip`, the template you work in during the workshop.
Older versions are on the [releases page](https://github.com/P4ntomime/LaTeX-Workshop-ECE/releases).

The [template's README](template/README.md) explains how to open it in
Overleaf (recommended for the workshop) or on your own computer.

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
├── site/        The workshop page (GitHub Pages) and the README button
├── .github/     Workflows: build and release, publish the page
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
- `site/`: `index.html` is the workshop page; `build.py` fills in the
  version, date and file sizes of the latest release. `icons.py` draws
  `readme-button.svg` and the favicon from the Latin Modern fonts.

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
make -C slides handout    # slides-handout.pdf: one page per slide, no notes
make -C handout           # handout.pdf (reads ../slides and ../template/build)
```

`make -C template zip` writes `template/build/workshop-template.zip`, the
file that goes into a release. `make test` fails on any LaTeX error or
warning, so a template that passes compiles cleanly for the students.

To change the template, edit `template/master.tex` and run
`make -C template test`; the checkpoints are regenerated from it and
cannot drift apart.

## Releases

Every push to `main` builds everything on GitHub Actions; the files are
attached to the run. To publish a new version, push a tag starting
with `v`:

```sh
git tag -a v2026.2 -m "Workshop 2026"
git push origin v2026.2
```

The workflow then creates a release with `workshop-template.zip`,
`slides.pdf` (the handout version of the slides), `handout.pdf` and
`latex-workshop.zip` (all three), and updates the workshop page.

## Licence and attribution

This work is licensed under
[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/): you may
share and adapt it, also commercially, as long as you give credit and
share your version under the same licence.

- Based on the LaTeX-Workshop slides by Naoki Pross,
  <https://github.com/OST-Stud/LaTeX-Workshop>, CC BY-SA 4.0.
- This revision: Laurin Heitzer, MSE EE, 2026.
- Example document and figure: written for this workshop, synthetic data.