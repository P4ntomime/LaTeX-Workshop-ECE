---
layout: section
---

# Block 3
## Maths

<div class="mt-6 opacity-70">The reason most people are here</div>

---
layout: center
---

# Where we are going

<GoalTracker :done="['structure', 'text']" now="math" />

---

# Warm-up: what comes out?

```latex
\begin{itemize}
  \item bread
  \item milk
\end{itemize}

And now a new paragraph.
```

<v-click>

<div class="nope mt-6">
A trick question. There is no blank line before
<code>And now</code>, so it is <strong>not</strong> a new paragraph
&mdash; it carries straight on from the list.
</div>

</v-click>

<!--
TWO MINUTES, in pairs, laptops shut.

Nasty on purpose, and the people who get it right will be pleased with
themselves for the rest of the hour. The ones who get it wrong have now
made the mistake in a room where it costs nothing, which is the whole
idea.

Tie it back: "the empty line is the paragraph break" -- same rule as
before the break, now in a place where it is easy to forget.
-->

---

# Two ways in

<div class="grid grid-cols-2 gap-8 mt-4">

<div>

### Inline &mdash; inside a sentence

```latex
The constant $\tau$ sets the pace,
and $T_0$ is where we start.
```

<div class="px-4 py-3 mt-2 rounded bg-gray-500 bg-opacity-10 font-serif">

The constant $\tau$ sets the pace, and $T_0$ is where we start.

</div>

</div>

<div>

### Display &mdash; on its own line

```latex
\[
  T(t) = T_\mathrm{env} + \Delta T
\]
```

<div class="px-4 py-3 mt-2 rounded bg-gray-500 bg-opacity-10 font-serif text-center">

$$ T(t) = T_\mathrm{env} + \Delta T $$

</div>

</div>

</div>

<div v-click class="nope mt-6">
You will see <code>$$...$$</code> for display maths all over the
internet. It is a leftover from plain TeX, it breaks spacing above and
below, and <code>amsmath</code> asks you not to. Use <code>\[...\]</code>.
</div>

<!--
The $$ warning matters more than it sounds, because they WILL have met
$$ in Markdown, in Jupyter and in every StackExchange answer. Say it
once, clearly, and the cheat sheet repeats it.

Note the asymmetry worth pointing out: inline maths shrinks to fit the
line (fractions get small, sums get compact limits), display maths does
not. That is not a bug, it is what keeps line spacing even.
-->

---

# Numbered, and worth pointing at

````md magic-move
```latex
\[
  T(t) = T_\mathrm{env} + (T_0 - T_\mathrm{env})
         \mathrm{e}^{-t/\tau}
\]
```

```latex
\begin{equation}
  T(t) = T_\mathrm{env} + (T_0 - T_\mathrm{env})
         \mathrm{e}^{-t/\tau}
\end{equation}
```

```latex
\begin{equation}
  T(t) = T_\mathrm{env} + (T_0 - T_\mathrm{env})
         \mathrm{e}^{-t/\tau}
  \label{eq:cooling}
\end{equation}

As Equation~\eqref{eq:cooling} shows, ...
```
````

<div v-click class="aha mt-4">
Same move as <code>\tableofcontents</code>: you never type the number.
Insert an equation above it and everything renumbers, including the
sentence that refers to it.
</div>

<!--
Three clicks. Unnumbered -> numbered -> labelled and referenced.

This is the first callback to the block 1 promise, and it is worth
naming as one: "remember the contents list? Same deal."

\eqref gives you "(1)" with the brackets; \ref gives you bare "1".
For equations you almost always want \eqref.
-->

---

# Several lines, one alignment

```latex {all|3,5|4}
\begin{align}
  \frac{T - T_\mathrm{env}}{T_0 - T_\mathrm{env}}
    &= \mathrm{e}^{-t/\tau} \notag \\
  t &= -\tau \ln \left(
       \frac{T - T_\mathrm{env}}{T_0 - T_\mathrm{env}} \right)
\end{align}
```

<div class="grid grid-cols-2 gap-6 mt-5">
<div v-click>

`&` marks the alignment point &mdash; put it just before the `=` on
every line, and the equals signs line up.

</div>
<div v-click>

`\\` ends a line. **This** is the second of its two legitimate homes.

`\notag` drops the number on a line nobody will cite.

</div>
</div>

<!--
Callback: back in block 2 you told them \\ belongs in exactly two
places, tables and maths. This is one of them. Say "told you" -- the
payoff for the earlier promise is what makes the next promise credible.

Do not teach align*, gather, split, multline or aligned. align plus
\notag covers everything they will need this year, and the cheat sheet
lists the rest.
-->

---

# Words inside formulas

<div class="grid grid-cols-2 gap-8">

<div>

### Wrong

```latex
$V_{out}$        $T_{env}$
```

<div class="nope mt-2 text-base">
Reads as <em>V</em> times <em>o</em> times <em>u</em> times <em>t</em>.
Italic, wrongly spaced, and it looks it.
</div>

</div>

<div>

### Right

```latex
$V_\mathrm{out}$   $T_\mathrm{env}$
```

<div class="aha mt-2 text-base">
Upright, because it is a <em>label</em>, not a product of variables.
</div>

</div>

</div>

<v-click>

Same for whole words in a formula &mdash; use `\text{}`:

```latex
\begin{cases}
    \text{too hot}   & \text{if} \quad T > 65\,^{\circ}\mathrm{C} \\
    \text{drinkable} & \text{otherwise}
\end{cases}
```

<div class="text-sm opacity-60 mt-1">

The template's version has a third branch &mdash; same shape, one more
line.

</div>

</v-click>

<div v-click class="mt-4 text-lg">
Rule of thumb: <strong>a quantity goes in maths mode, a word goes in
<code>\text</code> or <code>\mathrm</code></strong> &mdash; even when
that means switching in the middle of a sentence.
</div>

<!--
The V_{out} example is the single most common thing beginners get
wrong in a report, and it is visible from the back of the room, which
is why it earns a whole slide.

cases also shows & and \\ doing the same job as in align -- point that
out, it makes cases feel familiar rather than new.

They will meet \,^{\circ}\mathrm{C} here and find it ugly. Good. Tell
them there is a better way and that it is coming at the end of block 4.
That IS the hook for siunitx.
-->

---

# Dos and don'ts

<div class="text-lg">

| Don't | Do | Why |
|---|---|---|
| `a * b` | `a \cdot b` | `*` means convolution in maths |
| `$$...$$` | `\[...\]` | plain-TeX leftover, breaks spacing |
| `V_{out}` | `V_\mathrm{out}` | "out" is a label, not three variables |
| `sin(x)` | `\sin(x)` | upright, with correct spacing |
| `d/dx` | `\frac{\mathrm{d}f}{\mathrm{d}x}` | the d is an operator, so upright |

</div>

<div v-click class="aha mt-6">
Use <code>\cdot</code> for multiplying numbers, and
<code>\times</code> for cross products, dimensions
(<code>3\times3</code>) and scientific notation
(<code>3\times10^{8}</code>). Both are correct; they mean different
things.
</div>

<!--
Keep this to two minutes. It is a reference table and it is on the
cheat sheet; reading it aloud line by line will lose the room.

Pick the two that matter most for THIS group and say only those. For a
mixed audience that is usually \mathrm for labels and \sin for
function names.

The \cdot / \times note is there because the old deck said "never use
\times", which is too strong -- it is right for cross products and
dimensions, and someone in the room will know that.
-->

---
layout: center
---

# Don't know the symbol?

<div class="text-center mt-6">

### detexify.kirelabs.org

<div class="mt-4 text-xl opacity-80">
Draw it with the mouse. It tells you the command.
</div>

</div>

<div class="mt-10 text-center text-lg opacity-70">
This is how everyone does it. Nobody memorises the symbol tables.
</div>

<!--
Ten seconds, and it is worth every one of them. The fear that they will
have to memorise hundreds of commands is the main reason people bounce
off LaTeX, and this kills it outright.

Mention that the same is true of everything else today: you look it up
until you stop needing to.
-->

---
layout: center
class: text-left
---

# Your turn

<HandsOn block="3" todos="3.1 - 3.6" minutes="7" checkpoint="checkpoint-03.tex">

The Theory section is waiting for you:

<div class="mt-3 opacity-80">
load <code>amsmath</code> &rarr; set the symbol list in maths &rarr; a
numbered equation with a label &rarr; an <code>align</code> derivation
&rarr; refer back to both &rarr; a <code>cases</code> block
</div>

</HandsOn>

<!--
7 MINUTES. The fullest block of the four, so expect fewer people to
finish -- that is fine and planned for, which is exactly what
checkpoint-03 is for.

Anyone who does finish: the three drills at the bottom of the
checkpoint file (logistic map, Shannon entropy, inverse Laplace
transform). The Laplace one is genuinely hard and will keep the
strongest person in the room busy for the whole seven minutes.

Walk the room looking for ONE thing: missing $ around symbols in prose.
It is the error with the worst habit-forming potential.

BREAK after this. 5 minutes. Last one.
-->
