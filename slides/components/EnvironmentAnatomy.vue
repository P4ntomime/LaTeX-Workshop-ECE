<script setup lang="ts">
import { computed } from 'vue'

/**
 * Dissection of an environment: the two halves of the begin/end pair are
 * joined by a rail on the right, and the body is bracketed on the left.
 *
 * Companion to CommandAnatomy, and deliberately the same visual
 * language: same stroke weight, same easing, same Shiki token colours,
 * same fade-and-rise on the labels.
 *
 * Layout is a three-column flex row -- left gutter, code, right gutter --
 * so the two annotations never compete for the same space. Horizontal
 * offsets inside the code block are in `ch` (monospace grid); vertical
 * offsets are in line-heights, so nothing depends on measurement.
 */
interface Target { line: number, from: number, to: number }

const props = withDefaults(defineProps<{
    /** Each line of the environment. */
    lines: string[]
    /** Lines rendered as italic prose rather than code, e.g. "Content". */
    placeholderLines?: number[]
    /** The two token ranges joined by the right-hand rail. */
    join: { targets: [Target, Target], label: string }
    /** The lines bracketed on the left. */
    body: { from: number, to: number, label: string }
    reveal?: number
    fontSize?: string
}>(), {
    placeholderLines: () => [],
    reveal: undefined,
    fontSize: '1.9rem',
})

const shown = (i: number) => props.reveal === undefined || i < props.reveal

type Tok = 'punct' | 'name' | 'opt' | 'mand' | 'plain'

const tokenize = (code: string): { text: string, tok: Tok }[] => {
    const chars = [...code]
    const t: Tok[] = new Array(chars.length).fill('plain')
    let i = 0
    while (i < chars.length) {
        const c = chars[i]
        if (c === '\\') {
            t[i++] = 'punct'
            while (i < chars.length && /[a-zA-Z]/.test(chars[i])) t[i++] = 'name'
        }
        else if (c === '[') {
            t[i++] = 'punct'
            while (i < chars.length && chars[i] !== ']') t[i++] = 'opt'
            if (i < chars.length) t[i++] = 'punct'
        }
        else if (c === '{') {
            t[i++] = 'punct'
            while (i < chars.length && chars[i] !== '}') t[i++] = 'mand'
            if (i < chars.length) t[i++] = 'punct'
        }
        else { t[i++] = 'plain' }
    }
    const runs: { text: string, tok: Tok }[] = []
    for (let k = 0; k < chars.length; k++) {
        const last = runs[runs.length - 1]
        if (last && last.tok === t[k]) last.text += chars[k]
        else runs.push({ text: chars[k], tok: t[k] })
    }
    return runs
}

const rows = computed(() => props.lines.map((text, i) => ({
    text,
    placeholder: props.placeholderLines.includes(i),
    runs: tokenize(text),
})))

const widthCh = computed(() => Math.max(...props.lines.map(l => [...l].length)))

/** Vertical centre of a line, in line-heights from the top of the block. */
const centreOf = (line: number) => `calc(${line + 0.5} * var(--lh))`
const topOf = (line: number) => `calc(${line} * var(--lh))`

const boxes = computed(() => props.join.targets.map(t => ({
    left: `${t.from}ch`,
    width: `${t.to - t.from}ch`,
    top: topOf(t.line),
})))

const rail = computed(() => {
    const [a, b] = props.join.targets
    const hi = Math.min(a.line, b.line)
    const lo = Math.max(a.line, b.line)
    return {
        topY: centreOf(hi),
        height: `calc(${lo - hi} * var(--lh))`,
        midY: centreOf((hi + lo) / 2),
        aY: centreOf(a.line),
        bY: centreOf(b.line),
        aIn: `${widthCh.value - a.to}ch`,   // gap from the token to the block edge
        bIn: `${widthCh.value - b.to}ch`,
    }
})

const bodyBox = computed(() => ({
    top: topOf(props.body.from),
    height: `calc(${props.body.to - props.body.from} * var(--lh))`,
    midY: centreOf((props.body.from + props.body.to - 1) / 2),
}))
</script>

<template>
    <div class="env-anatomy" :style="{ '--fs': fontSize }">
        <!-- LEFT GUTTER: bracket around the body -->
        <div class="gutter left">
            <div class="ann" :class="{ 'is-off': !shown(1) }">
                <div
                    class="body-brace"
                    :style="{ top: bodyBox.top, height: bodyBox.height }"
                />
                <div
                    class="body-stub"
                    :style="{ top: bodyBox.midY }"
                />
            </div>
            <div
                class="lbl right-align font-sans"
                :class="{ 'is-off': !shown(1) }"
                :style="{ top: bodyBox.midY, transitionDelay: shown(1) ? '0.12s' : '0s' }"
            >{{ body.label }}</div>
        </div>

        <!-- THE CODE -->
        <div class="env-code" :style="{ width: `${widthCh}ch` }">
            <div
                v-for="(r, i) in rows"
                :key="i"
                class="env-line"
                :class="r.placeholder ? 'placeholder font-sans' : ''"
            ><template v-if="r.placeholder">{{ r.text }}</template><span
                v-else
                v-for="(run, ri) in r.runs"
                :key="ri"
                :class="`tok-${run.tok}`"
            >{{ run.text }}</span></div>

            <!-- dashed outline on each half of the pair -->
            <div
                v-for="(bx, i) in boxes"
                :key="'b' + i"
                class="name-box"
                :class="{ 'is-off': !shown(0) }"
                :style="{ left: bx.left, width: bx.width, top: bx.top,
                          transitionDelay: shown(0) ? `${i * 0.08}s` : '0s' }"
            />
        </div>

        <!-- RIGHT GUTTER: rail joining the two names -->
        <div class="gutter right">
            <div class="ann" :class="{ 'is-off': !shown(0) }">
                <div
                    class="lead"
                    :style="{ top: rail.aY, left: `calc(-1 * ${rail.aIn})`,
                              width: `calc(var(--rail) + ${rail.aIn})` }"
                />
                <div
                    class="lead"
                    :style="{ top: rail.bY, left: `calc(-1 * ${rail.bIn})`,
                              width: `calc(var(--rail) + ${rail.bIn})` }"
                />
                <div
                    class="spine"
                    :style="{ left: `var(--rail)`, top: rail.topY, height: rail.height }"
                />
            </div>
            <div
                class="lbl left-align font-sans"
                :class="{ 'is-off': !shown(0) }"
                :style="{ top: rail.midY, left: `calc(var(--rail) + 0.6rem)`,
                          transitionDelay: shown(0) ? '0.12s' : '0s' }"
            >{{ join.label }}</div>
        </div>
    </div>
</template>

<style scoped>
.env-anatomy {
    font-family: var(--slidev-code-font-family, monospace);
    font-size: var(--fs);
    letter-spacing: 0;

    --lh: 1.55em;
    --rail: 2.2rem;
    --gap: 0.6rem;
    --ws-dur: 0.45s;
    --ws-ease: cubic-bezier(0.4, 0, 0.2, 1);

    display: flex;
    align-items: flex-start;
    justify-content: center;
}

.gutter {
    position: relative;
    flex: none;
}

.gutter.left  { width: 11rem; }
.gutter.right { width: 10.5rem; }

.env-code {
    position: relative;
    flex: none;
}

.env-line {
    height: var(--lh);
    line-height: var(--lh);
    white-space: pre;
}

.env-line.placeholder {
    /* No font-family here: the element carries the `font-sans` utility,
       which is the deck's own face. A var() fallback to `serif` quietly
       gives you the browser default instead. */
    font-style: italic;
    letter-spacing: normal;
    opacity: 0.7;
}

/* The deck's Shiki latex palette. */
.tok-punct { color: #999999; }
.tok-name  { color: #1E754F; }
.tok-opt   { color: #393A34; }
.tok-mand  { color: #998418; }
.tok-plain { color: #393A34; }

:global(html.dark) .tok-punct { color: #666666; }
:global(html.dark) .tok-name  { color: #4D9375; }
:global(html.dark) .tok-opt   { color: #DBD7CAEE; }
:global(html.dark) .tok-mand  { color: #B8A965; }
:global(html.dark) .tok-plain { color: #DBD7CAEE; }

.ann {
    opacity: 0.75;
    transition: opacity var(--ws-dur) ease;
}

.ann.is-off { opacity: 0; }

/* right-hand rail */
.lead, .spine {
    position: absolute;
}

.lead {
    height: 0;
    border-top: 1.5px solid currentColor;
}

.spine {
    width: 0;
    border-left: 1.5px solid currentColor;
}

/* left-hand body bracket: "[" facing the code, plus a stub to the label */
.body-brace {
    position: absolute;
    right: var(--gap);
    width: 0.5rem;
    border: 1.5px solid currentColor;
    border-right: none;
}

.body-stub {
    position: absolute;
    right: calc(var(--gap) + 0.5rem);
    width: 0.8rem;
    height: 0;
    border-top: 1.5px solid currentColor;
}

/* dashed outline on the environment names */
.name-box {
    position: absolute;
    height: calc(var(--lh) * 0.82);
    margin-top: calc(var(--lh) * 0.09);
    border: 1.5px dashed currentColor;
    border-radius: 3px;
    opacity: 0.55;
    transition: opacity var(--ws-dur) ease;
    pointer-events: none;
}

.name-box.is-off { opacity: 0; }

/* labels */
.lbl {
    position: absolute;
    font-size: 0.95rem;
    line-height: 1.2;
    letter-spacing: normal;
    transform: translateY(-50%);
    transition: opacity 0.4s ease, transform 0.4s ease;
}

.lbl.right-align {
    right: 2.3rem;
    text-align: right;
    width: 8rem;
}

.lbl.left-align {
    text-align: left;
    width: 8rem;
}

.lbl.is-off {
    opacity: 0;
    transform: translateY(calc(-50% + 6px));
}
</style>
