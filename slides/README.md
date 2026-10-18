# LaTeX from Scratch: workshop slides

A two-hour hands-on introduction to LaTeX, built with Beamer and the
`own` theme from the 2025 deck. The deck follows the four-block
structure (Skeleton, Text, Maths, Illustrations & References); each block ends with a
hands-on slide pointing at the matching TODOs and checkpoint in the
student template.

## Building

```sh
latexmk slides.tex      # or: make
```

The code on the slides is highlighted by `minted`, which calls Pygments
(Python), so pdflatex needs `-shell-escape`. `latexmkrc` passes it for
you. Overleaf enables it by default.

Built and checked with TeX Live 2023 (minted 2.9, beamer tcolorbox theme
0.6) and with the 2026 tcolorbox theme (1.6). Your 2026 build uses minted 3
and also compiled correctly.

`slides.pdf` has the presenter notes on a second screen (every page is
twice as wide). For a plain PDF, comment out the two lines under
"Presenter notes" in `slides.tex`.

## Layout

```
slides.tex                 title data and the list of sections
preamble.tex               packages and helpers, each with a usage comment
beamerthemeown.sty         2025 theme; only the headline is new
beamercolorthemeown.sty    2025 colours, plus the progress bar colour
sections/                  one file per block, plus intro and closing
listings/                  every piece of code shown on a slide
renders/                   compiled PDFs the slides include
Makefile                   `make renders` rebuilds renders/
```

## How the slides are put together

- **Code lives in `listings/`.** Slides show it with `\tcbinputlst{file}`
  (or `\tcbexinputlst{file}[title]` for a titled box). Where the slide
  also shows the result, the same file is `\input` inside an
  `outputbox`, so code and output cannot drift apart.
- **Build-ups cut between states.** Highlighted lines change with
  `\only<n>{\tcbinputlst[highlightlines={...}]{file}}`.
- **Annotated code** (the two anatomy slides): `\tikzmark`s sit between
  the tokens via `escapeinside=||`, and `\annotatebelow` /
  `\annotateabove` draw a bracket and label between two marks.
  Explained at the top of section 3 of `preamble.tex`.
- **Recurring slides** have one helper each: `\blockframe`,
  `\begin{roadmap}{state}` (the timeline), `\handson{...}`.
- **Colours of code** come from the Pygments style in `\setminted`
  (`xcode`). `pygmentize -L styles` lists the alternatives.

## Changes from the 2025 deck

- The headline shows the section names and a thin progress bar instead
  of one dot per frame.
- `listings` is replaced by `minted`: every LaTeX command is
  highlighted without a hand-kept keyword list.
- Long-unused code (C++ and VHDL listing styles, commented-out
  experiments) is gone from the preamble.

## Before publishing

- `\repourl` in `slides.tex` (link and QR code on the last slide)
- Original author and link on the attribution slide in
  `sections/99-closing.tex`, and in the repository's top-level `LICENSE`
