---
layout: section
---

# Block 4
## Connections

<div class="mt-6 opacity-70">Tables, figures and citations &mdash; and the one idea behind all three</div>

---
layout: center
---

# Where we are going

<GoalTracker :done="['structure', 'text', 'math']" :now="['floats', 'cite']" />

---
layout: center
class: text-center
---

# The whole of block 4, in one sentence

<div class="text-4xl mt-10 leading-relaxed">
You never type a number that LaTeX<br/>can work out for you.
</div>

<v-click>

<div class="mt-12 text-xl opacity-80">
Not a section number. Not an equation number. Not a figure number.
Not a reference number.
</div>

</v-click>

<div v-click class="mt-6 text-lg">
You give the thing a <code>\label</code>, and you ask for it by name.
</div>

<!--
Say this, then stop talking for a beat.

Everything in the next twenty minutes is one idea wearing four hats.
If they leave with only this, block 4 worked.

They have already seen it twice -- the table of contents in block 1 and
\eqref in block 3 -- so this is naming a pattern they have felt, not
introducing a new one. Point that out; it is why it will stick.
-->

---

# A table, the hard way first

```latex {all|1|2|3,4}
\begin{tabular}{lllr}
  Vessel & Material & Lid & Time constant \\
  Mug    & glazed ceramic & no  & 24 min  \\
  Glass  & borosilicate   & no  & 18 min  \\
\end{tabular}
```

<v-clicks at="4">

- `{lllr}` &mdash; one letter per column: **l**eft, **c**entre, **r**ight
- `&` separates columns
- `\\` ends a row &mdash; the *first* of its two legitimate homes

</v-clicks>

<div v-click class="nope mt-5">
Paste this straight into your text and it lands wherever it happens to
fall &mdash; mid-sentence, split across a page break. A bare
<code>tabular</code> is not a table yet.
</div>

<!--
Let them see the bare tabular misbehave. The TODO has them type it
unwrapped on purpose, so the float on the next slide solves a problem
they have actually just had, rather than one you asserted.

p{3cm} for wrapping columns is on the cheat sheet. Mention it exists
when someone's text runs off the page, not before.
-->

---

# Make it float

```latex {all|1,7|2|3|4}
\begin{table}[htbp]
  \centering
  \caption{Time constants of the three vessels.}
  \label{tab:vessels}
  \begin{tabular}{lllr}
    ...
  \end{tabular}
\end{table}
```

<v-clicks at="5">

- `[htbp]` &mdash; **h**ere, **t**op, **b**ottom, **p**age of its own.
  A wish list, tried in order
- `\caption` numbers it for you
- `\label` **must come after** `\caption`, or it labels the wrong thing
- `\usepackage{caption}` &mdash; without it the gap above the table is far too tight

</v-clicks>

<div v-click class="aha mt-4">
LaTeX moves floats to where they look good. That is a feature. Fighting
it is the single biggest time sink for new users.
</div>

<!--
The \label-after-\caption rule is the one that will actually bite them,
because it fails silently -- they get a reference to the wrong number
rather than an error. Say it twice.

On [H] from the float package: mention it exists, say it is a last
resort, and move on. If you teach it as the normal solution they will
use it everywhere and their documents will have half-empty pages.

(The old deck said ! "forces" placement. It does not -- it only relaxes
LaTeX's internal limits. [H] is the one that forces.)
-->

---

# Rules that look like a real table

<div class="grid grid-cols-2 gap-8">

<div>

```latex
\hline
Vessel & Lid \\
\hline
Mug & no \\
\hline
```

<Placeholder what="the same table with \hline, compiled" h="120px" />

<div class="nope mt-2 text-base">Looks like a spreadsheet.</div>

</div>

<div>

```latex
\usepackage{booktabs}

\toprule
Vessel & Lid \\
\midrule
Mug & no \\
\bottomrule
```

<Placeholder what="the same table with booktabs, compiled" h="120px" />

<div class="aha mt-2 text-base">Looks like a journal.</div>

</div>

</div>

<div v-click class="mt-5 text-center text-lg">
No vertical rules. No double lines. This is not a style opinion &mdash;
it is what typographers have done for a century.
</div>

<!--
Put the two PDFs side by side and say nothing for three seconds. The
difference does the teaching.

If anyone asks why no vertical lines: white space separates columns
perfectly well, and rules add ink without adding information. The
booktabs manual says it better and is worth linking on the resources
slide.
-->

---

# A figure is the same shape

```latex {all|3}
\begin{figure}[htbp]
  \centering
  \includegraphics[width=0.8\textwidth]{figures/cooling-curves}
  \caption{Measured and modelled cooling curves.}
  \label{fig:cooling}
\end{figure}
```

<v-clicks at="2">

- Identical structure to `table` &mdash; float, centre, caption, label
- `0.8\textwidth` scales to the page, so it survives a margin change
- **No file extension.** LaTeX picks the best format it can find

</v-clicks>

<div v-click class="nope mt-5">
PDF or PNG, not SVG &mdash; <code>pdflatex</code> cannot read SVG.
Export vector graphics as PDF and they stay sharp at any zoom.
</div>

<!--
"Same shape as a table" is the point. They learned floats once and get
figures nearly free, which is why tables come before figures here
rather than next to lists.

The no-extension habit is worth insisting on: it is what lets the same
source build with pdflatex and lualatex, and it is one less thing to
get wrong.
-->

---

# Pointing at things

```latex
Figure~\ref{fig:cooling} shows the measured temperatures,
and Table~\ref{tab:vessels} lists the time constants.
```

<div class="grid grid-cols-2 gap-6 mt-6">

<div v-click>

### The tilde

`Figure~\ref{...}` &mdash; a space LaTeX may **not** break.

Without it, "Figure" can end one line and "3" start the next.

</div>

<div v-click>

### Naming things

`fig:`, `tab:`, `eq:`, `sec:` &mdash; a useful convention.

Your sections have had `\label`s since block 1:

```latex
\section{Results}\label{sec:results}
```

Same line as the `\section`, or `\pageref` may point at the wrong page.

</div>

</div>

<div v-click class="aha mt-4">
Move the figure to another section: everything renumbers, and every
sentence referring to it stays correct.
</div>

<!--
That last line is the payoff of the whole block and it is worth a pause.

The tilde is a small thing that marks out people who know what they are
doing. Cheap to teach, permanent once learned.
-->

---

# Citations: write the source down once

<div class="grid grid-cols-2 gap-6">

<div>

### `references.bib`

```bibtex
@book{halliday2018,
  author    = {Halliday, David and
               Resnick, Robert and
               Walker, Jearl},
  title     = {Fundamentals of Physics},
  edition   = {11},
  publisher = {Wiley},
  year      = {2018},
}
```

</div>

<div>

### In the document

```latex
\usepackage[backend=biber,
            style=numeric]{biblatex}
\addbibresource{references.bib}
...
...as shown by \cite{halliday2018}.
...
\printbibliography
```

</div>

</div>

<div v-click class="aha mt-5">
Change <code>style=numeric</code> to <code>style=authoryear</code> and
every citation and the whole bibliography reformat. You never touch the
sources.
</div>

<!--
The style-switch line is the moment this lands for anyone who has ever
reformatted a reference list by hand for a different submission.

Where the .bib entries come from matters more than the syntax: DOI,
Google Scholar, the library's export button, Zotero. Nobody types these.
Say that, because half the room will assume they have to.

biblatex + biber, not legacy BibTeX. If they find a 2008 tutorial
online it will tell them otherwise; this is the current answer.
-->

---

# The one error that still bites

```latex
...as shown by \cite{halliday2019}.
```

<div class="grid grid-cols-2 gap-6 mt-4">

<div v-click>

In the PDF:

<div class="px-4 py-3 rounded bg-gray-500 bg-opacity-10 font-serif text-lg">
...as shown by <strong>[halliday2019?]</strong>.
</div>

</div>

<div v-click>

In the log:

```text
Package biblatex Warning:
  The entry 'halliday2019' could
  not be found in the bibliography.
```

</div>

</div>

<div v-click class="aha mt-6">
A <code>??</code> or a <code>[key?]</code> almost always means the
<strong>name is wrong</strong> &mdash; a typo in the key, or a
<code>\label</code> you never actually wrote. Search your source for
the name in the warning.
</div>

<!--
TODO 4.5 has them misspell the key deliberately, so they meet this in a
controlled setting with the log message next to it.

The reflex you are building: read the warning, take the name out of it,
search for that name. Not "compile again and hope".

(The other classic cause, too few compilation passes, is handled for
them by Overleaf and latexmk, which is why it is not the headline here.
Mention it in one clause if someone asks.)
-->

---
layout: center
class: text-left
---

# Your turn

<HandsOn block="4" todos="4.1 - 4.6" minutes="7" checkpoint="checkpoint-04.tex">

The last stretch:

<div class="mt-3 opacity-80">
a bare <code>tabular</code> &rarr; wrap it in a float with
<code>booktabs</code> &rarr; place the figure &rarr; refer to both
&rarr; break a citation on purpose, then fix it
</div>

</HandsOn>

<!--
7 MINUTES, and this one genuinely has more in it than seven minutes
allows. That is deliberate: 4.1 to 4.4 is the core, 4.5 and 4.6 are for
whoever gets there.

Tell them that explicitly. "If you only do the table and the figure,
you have got what you came for" removes the end-of-day panic and
nobody leaves feeling behind.

checkpoint-04 is the finished document, so anyone who wants the whole
thing can just take it.
-->
