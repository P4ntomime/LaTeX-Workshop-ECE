---
layout: section
---

# Block 1
## The skeleton

<div class="mt-6 opacity-70">From an empty file to a structured PDF</div>

---
layout: center
---

# Where we are going

<GoalTracker now="structure" />

<!--
Second showing. Point at the arrow: "this one, in the next 20 minutes."
-->

---

# Everything is a command

A LaTeX file is plain text. Anything that is not text is a command,
and they all have the same shape:

<CommandAnatomy
  class="mt-8"
  code="\documentclass[a4paper]{article}"
  :parts="[
    { from: 0,  to: 1,  label: 'Command delimiter', labelAt: 3 },
    { from: 1,  to: 14, label: 'Command name', labelAt: 11, drop: 0.5 },
    { from: 23, to: 32, label: 'Mandatory argument', labelAt: 28, drop: 0.5 },
    { from: 14, to: 23, label: 'Optional argument', labelAt: 19, inserted: true },
  ]"
  :reveal="$clicks"
/>

<div v-click="5" class="aha mt-4">
Backslash, letters, arguments. Every command today looks like this.
</div>

<!--
Go slowly here and do not apologise for it. Three minutes spent on this
slide saves twenty minutes of confusion later, because from here on
they can *parse* what they are looking at even when they do not know
what it does.

The detail worth saying out loud: a non-letter ends a command name.
That is why `\LaTeX2e` does not work and why they will one day need
`\LaTeX{} is nice`. Do not dwell, just plant it.
-->

---

# ...and some commands wrap things

When something applies to a *region* rather than a point, it is an
**environment**.

<EnvironmentAnatomy
  class="mt-10"
  :lines="['\\begin{center}', '    Content', '\\end{center}']"
  :placeholder-lines="[1]"
  :join="{
    targets: [
      { line: 0, from: 7, to: 13 },
      { line: 2, from: 5, to: 11 },
    ],
    label: 'Same name twice',
  }"
  :body="{ from: 1, to: 2, label: 'Everything in here is inside' }"
  :reveal="$clicks"
/>

<div v-click="3" class="aha mt-8">
A command acts <em>here</em>. An environment acts on <em>all of this</em>.
</div>

<!--
Use the line highlighting: first the whole thing, then the fence, then
the contents. It makes the "wrapping" idea visual.

Promise them now that a mismatched \begin/\end is the error they will
hit most often today. When it happens in block 2 and you can say "told
you", they trust the next prediction too.
-->

---

# The characters LaTeX keeps for itself

<div class="chartable mt-4">

| **Symbol** | **Description** | **Substitute** |
|---|---|---|
| `%` | starts a comment, killing the rest of the line | `\%` |
| `{ }` | group things together | `\{ \}` |
| `$` | switches maths on and off | `\$` |
| `&` | separates table columns | `\&` |
| `#` | stands in for an argument | `\#` |
| `_ ^` | subscript and superscript, in maths | `\_` `\^{}` |
| `~` | a space that will not break | `\textasciitilde` |
| `\` | starts every command | `\textbackslash` |

</div>

<style>
.chartable table {
    width: 100%;
    font-size: 0.9rem;
}
/* Eight rows do not fit at the theme's default row padding. */
.chartable th,
.chartable td {
    padding-top: 0.3rem;
    padding-bottom: 0.3rem;
}
.chartable th:first-child,
.chartable td:first-child {
    text-align: right;
    white-space: nowrap;
}
.chartable td:last-child,
.chartable th:last-child {
    white-space: nowrap;
}
</style>

<!--
Same job as variant A, but the third column answers the question people
actually ask -- "how do I type a percent sign?" -- in the same row.

Two rows here are not in the list variant:
  \  because they have just met it, and \\ is NOT how you escape it
  (that is a line break; \textbackslash is the character).
  ~   is left out on purpose; it arrives in block 2 as a non-breaking
  space, where it has a reason to exist.

Do not read the table out. Point at %, say the warning, move on.
-->

---

# The smallest document that compiles

````md magic-move {lines: true}
```latex
\documentclass[a4paper,11pt]{article}

\begin{document}

Hello OST!

\end{document}
```

```latex
\documentclass[a4paper,11pt]{article}

\title{How Fast Does Your Coffee Go Cold?}
\author{Your Name}
\date{\today}

\begin{document}

\maketitle

Hello OST!

\end{document}
```

```latex
\documentclass[a4paper,11pt]{article}

\title{How Fast Does Your Coffee Go Cold?}
\author{Your Name}
\date{\today}

\begin{document}

\maketitle

\section{Introduction}

A freshly poured coffee is too hot to drink.

\section{Theory}

\section{Conclusion}

\end{document}
```
````

<!--
MAGIC MOVE. Three clicks, and the code morphs rather than being
replaced, so they can see exactly what got added each time. This is the
slide that justifies Slidev over Beamer.

Narrate the three steps as: it compiles -> it has a title -> it has a
shape. Nothing else.

Note \documentclass is OUTSIDE \begin{document}. Someone always asks.
The answer: that region is the preamble, we come back to it in block 2.
-->

---
layout: two-cols
---

# What you typed

```latex {all|5,9,13}
\documentclass[a4paper,11pt]{article}

\begin{document}
\maketitle

\section{Introduction}

A freshly poured coffee is too
hot to drink.

\section{Theory}

\section{Conclusion}
\end{document}
```

::right::

# What came out

<Placeholder what="checkpoint-01.pdf page 1, cropped to the headings" h="280px" />

<div v-click class="mt-4 text-lg">

You never typed **1**, **2** or **3**.

</div>

<!--
Hold on that last line. The numbering is the first thing all afternoon
that LaTeX did FOR them rather than TO them, and it sets up the table
of contents on the next slide.

Ask the room: "what happens to those numbers if I move Theory above
Introduction?" Let someone say it.
-->

---

# One line, and the document indexes itself

```latex {4}
\begin{document}

\maketitle
\tableofcontents

\section{Introduction}
```

<div class="grid grid-cols-2 gap-6 mt-4">
<div>
<Placeholder what="checkpoint-01.pdf page 1, the Contents block" h="200px" />
</div>
<div v-click>

Nobody typed that list.

It comes from your `\section` commands, and it stays right when you
rename or reorder them.

</div>
</div>

<div v-click class="aha mt-5">
Describe the structure once, and the document maintains itself.
</div>

<!--
THE KEY SLIDE OF BLOCK 1. If they remember one thing from the first
half hour, make it this one.

Don't rush to the next slide. Ask what else could be generated from
structure they have already written -- someone will guess page numbers,
cross-references, the bibliography. Say "yes, all of that, before
half past five."

(Deliberately NOT teaching the two-compilation-passes thing here.
Overleaf and every modern editor handle it. They will meet the one
case that still bites -- a misspelled citation key -- in block 4.)
-->

---

# Marking up text

```latex
The underlying physics is \emph{Newton's law of cooling}.
Three \textbf{vessels} are compared: \texttt{mug}, \texttt{glass}, \texttt{flask}.
```

<div class="grid grid-cols-3 gap-5 mt-8 text-lg">

<div v-click class="px-4 py-3 rounded border border-gray-400 border-opacity-40">
<code>\emph{...}</code>
<div class="mt-2 opacity-80">"this matters"</div>
<div class="mt-1 text-sm opacity-60">usually italic</div>
</div>

<div v-click class="px-4 py-3 rounded border border-gray-400 border-opacity-40">
<code>\textbf{...}</code>
<div class="mt-2 opacity-80">"make this bold"</div>
<div class="mt-1 text-sm opacity-60">always bold</div>
</div>

<div v-click class="px-4 py-3 rounded border border-gray-400 border-opacity-40">
<code>\texttt{...}</code>
<div class="mt-2 opacity-80">"this is code"</div>
<div class="mt-1 text-sm opacity-60">monospace</div>
</div>

</div>

<div v-click class="aha mt-8">
<code>\emph</code> says what you <em>mean</em>, <code>\textbf</code> what
you <em>want</em>. Prefer the first: italics inside italics then comes
out upright.
</div>

<!--
The emph-vs-textbf distinction is the same structure-vs-appearance idea
from the opening slide, now in miniature and concrete. That is why it
is here and not in a table of nine font commands.

Demo if you have 20 seconds spare: \emph inside \emph flips back to
upright, \textit inside \textit does not. It is a cheap, memorable
party trick that makes the semantic point better than any explanation.

The other six styling commands are on the cheat sheet. Do not read them out.
-->

---
layout: center
---

# Block 1, in one screen

```latex
\documentclass[a4paper,11pt]{article}   % what kind of document

\title{...}  \author{...}  \date{\today}

\begin{document}                         % the document starts

\maketitle                                % print the title block
\tableofcontents                          % print the contents

\section{...}       \subsection{...}      % structure

\emph{...}   \textbf{...}   \texttt{...}  % emphasis

\end{document}                            % the document ends
```

<div class="mt-6 text-center text-lg opacity-70">
All of it is in <code>checkpoints/checkpoint-01.tex</code>.
</div>

<!--
Leave this up while they work if you like -- it is deliberately a
reference slide, not a teaching one.
-->

---
layout: center
class: text-left
---

# Your turn

<HandsOn block="1" todos="1.1 - 1.5" minutes="7" checkpoint="checkpoint-01.tex">

Open <code>latex-workshop.tex</code> and work down the TODOs.

<div class="mt-3 opacity-80">
a document that compiles &rarr; a title block &rarr; five sections
&rarr; a table of contents &rarr; three styled words
</div>

</HandsOn>

<!--
7 MINUTES. Set a timer and show it.

Walk the room. Do not answer from the front unless three people have
the same problem -- then stop everyone, fix it once, out loud.

The two failures you will actually see:
  - \begin{document} without \end{document}
  - a smart-quote or an em-dash pasted in from somewhere

At 5 minutes, say "two minutes left, if you are behind, grab
checkpoint-01." Say it loudly and without judgement; it is permission,
and the people who need it will not ask.

BREAK after this slide. 5 minutes. Say the actual wall-clock time you
will start again, and start then.
-->
