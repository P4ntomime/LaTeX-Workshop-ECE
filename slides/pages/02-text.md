---
layout: section
---

# Block 2
## Text that behaves

<div class="mt-6 opacity-70">Paragraphs, line breaks and lists</div>

---
layout: center
---

# Where we are going

<GoalTracker :done="['structure']" now="text" />

<!--
First item is green. It took 26 minutes. Say that out loud -- it
makes the remaining three blocks feel cheap.
-->

---

# Warm-up: three things are wrong here

```latex {all}
\documentclass{article}
\begin{document}

\section{Results}

The \emph{most important finding is this.

\begin{itemize}
  \item 100% of the samples
\end{itemized}

\end{document}
```

<v-click>

<div class="grid grid-cols-3 gap-4 mt-5 text-base">
<div class="nope">Line 6: <code>\emph{</code> never closes</div>
<div class="nope">Line 9: a bare <code>%</code> eats the rest of the line</div>
<div class="nope">Line 10: <code>itemized</code> &ne; <code>itemize</code></div>
</div>

</v-click>

<!--
TWO MINUTES, laptops shut. In pairs, out loud.

This is retrieval practice: they are pulling block 1 back out of their
heads after a break, which is worth far more than you re-explaining it.
It also wakes the room up, which at 4:45pm is not a small thing.

Do not reveal until at least two pairs have found all three. If the
room is quiet, give them the first one.
-->

---

# Where do line breaks come from?

You type this:

```latex
A freshly poured coffee is
too hot to drink, and a
forgotten one is too cold.
```

<v-click>

You get this:

<div class="px-5 py-3 mt-2 rounded bg-gray-500 bg-opacity-10 font-serif text-lg">
A freshly poured coffee is too hot to drink, and a forgotten one is too cold.
</div>

</v-click>

<v-click>

<div class="nope mt-6">
One line. Your three lines of source became one line of output.
</div>

</v-click>

<!--
PREDICT FIRST. Ask the room what will come out before you click. Get a
show of hands between "three lines" and "one line".

The wrong prediction is the point: being surprised here is what makes
the rule stick. If you just state the rule they will nod and then write
\\ everywhere anyway.
-->

---

# The rules, all of them

<div class="text-lg">

<v-clicks>

- A **single newline** in the source is just a space.
- An **empty line** starts a new paragraph. This is how you break text.
- `%` at the end of a line swallows even that space. Useful in tables and macros.
- `~` is a space that LaTeX may **not** break across lines &mdash; `Fig.~\ref{...}`.

</v-clicks>

</div>

<div v-click class="aha mt-7">

Because a newline is only a space, you may put **one sentence per
line** in the source. The PDF is identical &mdash; but `git diff` then
shows you the sentence that changed instead of the whole paragraph.
The template is written this way.

</div>

<div v-click class="nope mt-5">

`\\` is **not** a paragraph break and **not** a blank line.

It means "end this line *here*", and it belongs in exactly two places:
inside a table, and inside maths. Anywhere else it gives you underfull
boxes and a document that quietly falls apart.

</div>

<!--
The \\ warning is the single most valuable thing in block 2. Every
beginner reaches for \\ because it is what Word's Enter key feels like,
and it is wrong in a way that does not show up until the document is
long enough to reflow.

Concrete symptom to name out loud, so they recognise it later:
"Underfull \hbox (badness 10000)" in the log, and a paragraph whose
last line is stretched across the full width.
-->

---

# Paragraph spacing: do it once

<div class="grid grid-cols-2 gap-8 mt-4">

<div>

### What beginners do

```latex
\noindent
First paragraph.

\noindent
Second paragraph.

\noindent
Third paragraph.
```

<div class="nope mt-3 text-base">
Every paragraph, forever. Miss one and it looks broken.
</div>

</div>

<div>

### What you do

```latex
\usepackage{parskip}
```

<div class="aha mt-3 text-base">
Once, in the preamble. Every paragraph in the document, consistent,
and reversible by deleting one line.
</div>

</div>

</div>

<div v-click class="mt-8 text-center text-xl">
Whenever you catch yourself repeating a command, the answer is almost
always a package or a macro.
</div>

<!--
This is structure-before-appearance for the third time, and by now they
should feel the pattern rather than need it explained.

Worth mentioning: blank-line-between-paragraphs is the normal
convention in German-language typesetting anyway, so for a lot of their
coursework parskip is simply correct rather than a preference.
-->

---

# Three kinds of list

<div class="grid grid-cols-3 gap-4 text-sm">

<div>

```latex
\begin{itemize}
  \item bread
  \item milk
\end{itemize}
```

<div class="mt-2 text-base opacity-80">
<strong>itemize</strong><br/>
order does not matter
</div>

</div>

<div>

```latex
\begin{enumerate}
  \item heat water
  \item pour
\end{enumerate}
```

<div class="mt-2 text-base opacity-80">
<strong>enumerate</strong><br/>
order <em>does</em> matter
</div>

</div>

<div>

```latex
\begin{description}
  \item[tau] time constant
  \item[T] temperature
\end{description}
```

<div class="mt-2 text-base opacity-80">
<strong>description</strong><br/>
naming things
</div>

</div>

</div>

<v-click>

<div class="aha mt-8">
Same shape every time: <code>\begin</code>, a pile of <code>\item</code>,
<code>\end</code>. Nest them by putting one inside another &mdash; the
labels and the indentation sort themselves out.
</div>

</v-click>

<!--
Fast. Three minutes. They already know what a list is; all they need is
the three names and the shared shape.

The one thing worth demoing live is nesting, because the automatic
change of label (bullet -> dash, 1 -> a) is another small "it did that
for me" moment, and those are what carry a tired room.

description is the one they have never seen. Point out that the
bracket argument is the term being defined -- they will use it in
block 3 for the symbol list.
-->

---

# The preamble: where the settings live

```latex {1|3-6|8}
\documentclass[a4paper,11pt]{article}

\usepackage[T1]{fontenc}        % output encoding
\usepackage[english]{babel}     % hyphenation, language conventions
\usepackage{parskip}            % paragraph spacing
\usepackage{amsmath}            % everything maths

\begin{document}
```

<v-clicks at="4">

- Everything between `\documentclass` and `\begin{document}`
- `\usepackage` loads an extension. There are about 6,000 of them on CTAN
- Order rarely matters &mdash; until it does. `hyperref` goes last

</v-clicks>

<div v-click class="aha mt-5">
This is the answer to "can LaTeX do...?". Almost always: yes, there is
a package, and it is one line.
</div>

<!--
Deliberately held back until now. In block 1 the preamble was "the
settings area, we'll come back to it" -- and that was enough, because
they had nothing to put in it yet. Now they do, and amsmath is sitting
there waiting for the next block.

6,000 is roughly right for CTAN and it always gets a reaction. The
useful follow-up is: you will personally use about eight of them.
-->

---
layout: center
class: text-left
---

# Your turn

<HandsOn block="2" todos="2.1 - 2.6" minutes="7" checkpoint="checkpoint-02.tex">

Working down the file:

<div class="mt-3 opacity-80">
add <code>parskip</code> &rarr; write a second paragraph &rarr; fix the
three line-break crimes in Measurement Setup &rarr; an
<code>itemize</code>, an <code>enumerate</code> and a
<code>description</code>
</div>

</HandsOn>

<!--
7 MINUTES.

TODO 2.3 is the interesting one: the paragraph they are fixing has the
\\ habits from the rules slide baked in, and it compiles perfectly
happily. The lesson is that LaTeX will not tell you -- you have to look
at the page. Say that when you reveal it.

Watch for: people putting a blank line INSIDE a list and wondering why
the spacing went strange. Common, harmless, worth a word from the front
if you see it twice.

BREAK after this. 5 minutes. Again: name the restart time.
-->
