---
layout: center
---

# You wrote all of this

<GoalTracker :done="['structure', 'text', 'math', 'floats', 'cite']" />

<div class="mt-10 text-lg opacity-70">
Two hours ago none of you had compiled a document.
</div>

<!--
All five green. Let it sit there for a few seconds.

This is the slide the advance organiser was built for: the session that
felt like four small things is now visibly one finished thing. Do not
undercut it by talking over it.
-->

---

# Three packages to add next

<div class="text-lg mt-4">

<v-clicks>

<div>

**`siunitx`** for numbers with units, as promised

```latex
\qty{65}{\degreeCelsius}    \qty{300}{\milli\litre}    \qty{24}{\minute}
```

Right spacing, right font, every time. One line changes the whole
document.

</div>

<div>

**`microtype`** for quietly better justification. Load it and look at the margin.

</div>

<div>

**`hyperref`** makes every `\ref`, `\eqref` and `\cite` clickable.

<span class="opacity-70">Load it **last** of all your packages.</span>

</div>

</v-clicks>

</div>

<div v-click class="aha mt-6">
Three lines in the preamble. No change to anything you have written.
</div>

<!--
siunitx is first because you owed them this from block 3, where they
typed \,^{\circ}\mathrm{C} by hand and found it ugly. Close the loop
out loud: "remember that mess? This."

Deliberately only three. A list of twenty useful packages is a list
nobody acts on.
-->

---

# When your document gets bigger

<div class="grid grid-cols-2 gap-8 mt-4">

<div>

```txt
thesis/
├── main.tex
├── references.bib
├── figures/
│   └── ...
└── sections/
    ├── introduction.tex
    ├── theory.tex
    └── results.tex
```

</div>

<div>

```latex
\begin{document}

\input{sections/introduction}
\input{sections/theory}
\input{sections/results}

\end{document}
```

<div class="mt-4 text-base opacity-80">
One file per chapter. Your editor stays usable and two people can work
without fighting.
</div>

</div>

</div>

<div v-click class="mt-6 text-lg">
Not worth it for three pages. Essential at thirty.
</div>

<!--
Thirty seconds. They do not need this today and they will need it for
their thesis; the point is that they have seen it once and will
recognise it when a supervisor's template does it.

Same for a separate preamble.tex -- mention it exists, do not demo it.
-->

---
layout: two-cols
---

# Where to look things up

**Detexify**, draw a symbol and get the command
<span class="opacity-60">detexify.kirelabs.org</span>

**Overleaf docs**, the best beginner reference there is
<span class="opacity-60">overleaf.com/learn</span>

**TeX StackExchange**, your exact error already answered
<span class="opacity-60">tex.stackexchange.com</span>

**CTAN**, every package with its manual
<span class="opacity-60">ctan.org</span>

::right::

# And the cheat sheet

<div class="mt-7"></div>

Everything this deck left out:

- all the sectioning levels
- the rest of the text styling commands
- matrix environments
- column types and float specifiers
- the reserved characters, in full

<div class="aha mt-5 text-base">
Two pages, written in LaTeX. The source is in the repo.
</div>

<!--
Hand the cheat sheet out on paper at the START of the session, not here
-- it is a reference they should have had in front of them all
afternoon.

This slide is just the reminder that it exists and why the deck left
things out.
-->

---
layout: center
class: text-center
---

# One last thing

<div class="text-2xl mt-8 leading-relaxed opacity-90">
Nobody writes LaTeX from memory.
</div>

<v-click>

<div class="text-xl mt-6 opacity-70">
Everyone looks things up and copies their last preamble.<br/>
That is the normal way to work.
</div>

</v-click>

<!--
The honest closing note, and worth the ten seconds.

The beginner's failure mode is believing that fluent users have
memorised it all and that they are uniquely slow. They have not, and
the student is not.
-->

---
layout: center
class: text-center
---

# Thank you

<div class="mt-6 text-xl opacity-80">
The template, these slides and the cheat sheet are all in the repo.
</div>

<div class="mt-10 text-base opacity-60">
Questions. And if something breaks in your next report, ask.
</div>

<!--
Stay at the front for a few minutes if you can. The best questions
always come one-to-one after the room empties.
-->

---
layout: center
class: text-sm
---

# Attribution and licence

<div class="mt-4 text-left max-w-2xl mx-auto leading-relaxed">

<div class="mb-4">

**TODO before you publish this repo.** The workshop these slides descend
from is licensed **CC BY-SA 4.0**, which means this deck must:

1. credit the original author by name, with a link to the original, and
2. be released under CC BY-SA 4.0 as well.

</div>

<div class="opacity-70">

Fill in below, and put the same text in the repository's top-level
`LICENSE`:

- Original workshop: *&lt;author&gt;*, *&lt;link&gt;*, CC BY-SA 4.0
- This revision: Laurin Heitzer, ECE, CC BY-SA 4.0
- Example document and figures: written for this workshop; the cooling
  data is synthetic

</div>

</div>

<!--
This slide is for YOU, not the students -- either fill it in properly
and keep it as a visible credit slide, or move the text to the README
and delete the slide.

Share-alike is not optional: a CC BY-SA original makes this deck
CC BY-SA too. Given the history with the other group's variant, having
the attribution clean and public is worth the ten minutes it takes.
-->
