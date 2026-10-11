<script setup lang="ts">
import { computed } from 'vue'

/**
 * TikZ-style dissection of a command: brackets under spans of the code,
 * elbow connectors dropping to labels underneath.
 *
 * WHY IT IS BUILT THIS WAY
 * The code is monospace, so character N sits at exactly N `ch` from the
 * start. Brackets, elbows and labels are all positioned on that one
 * grid, so nothing is measured at runtime and nothing drifts when the
 * font size changes.
 *
 * Everything is HTML rather than SVG on purpose: an SVG path's `d`
 * cannot be CSS-transitioned, and a part marked `inserted` morphs the
 * line by expanding its characters from zero width, which shifts every
 * bracket to its right. Divs can animate that; paths cannot.
 *
 * `from`/`to` are character indices into `code`, half-open.
 */
interface Part {
    from: number
    to: number
    label: string
    /** Label centre in characters; defaults to the span's centre. */
    labelAt?: number
    /** 0..1, deepens the elbow so crossing connectors do not overlap. */
    drop?: number
    /** These characters are absent until this part is revealed, so the
     *  line morphs instead of the whole command being there up front. */
    inserted?: boolean
}

const props = withDefaults(defineProps<{
    code: string
    parts: Part[]
    /** Show parts with index < reveal. Omit to show everything. */
    reveal?: number
    fontSize?: string
}>(), {
    reveal: undefined,
    fontSize: '1.9rem',
})

const chars = [...props.code]
const shown = (i: number) => props.reveal === undefined || i < props.reveal

/* ---- syntax colouring ------------------------------------------------
   These are the deck's own Shiki colours for latex (vitesse light/dark),
   read off a rendered code block so the dissection matches every other
   code sample in the deck rather than approximating it. */
type Tok = 'punct' | 'name' | 'opt' | 'mand' | 'plain'

const tokens = computed<Tok[]>(() => {
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
    return t
})

/* ---- the character grid ---------------------------------------------- */

/** A character is absent while the `inserted` part it belongs to is hidden. */
const present = computed(() =>
    chars.map((_, i) => !props.parts.some(
        (p, pi) => p.inserted && i >= p.from && i < p.to && !shown(pi),
    )),
)

/** x of character i, in characters: how many present characters precede it. */
const pos = computed(() => {
    const out: number[] = new Array(chars.length + 1)
    let n = 0
    for (let i = 0; i < chars.length; i++) { out[i] = n; if (present.value[i]) n++ }
    out[chars.length] = n
    return out
})

const totalCh = computed(() => pos.value[chars.length])

/* The line is rendered as segments, not as individual characters.
   An inserted part is ONE clipping span whose width animates from 0,
   so the text after it glides on a single easing curve. Animating each
   character separately made the trailing text lurch, because nine
   overlapping transitions do not sum to a smooth motion. */
interface Run { text: string, tok: Tok }
interface Segment { runs: Run[], inserted: number | null, len: number }

const segments = computed<Segment[]>(() => {
    const insOf = (i: number) => {
        const k = props.parts.findIndex(p => p.inserted && i >= p.from && i < p.to)
        return k < 0 ? null : k
    }
    const segs: Segment[] = []
    let cur: Segment | null = null
    let curIns: number | null | undefined
    for (let i = 0; i < chars.length; i++) {
        const ins = insOf(i)
        if (cur === null || ins !== curIns) {
            cur = { runs: [], inserted: ins, len: 0 }
            segs.push(cur)
            curIns = ins
        }
        const tok = tokens.value[i]
        const last = cur.runs[cur.runs.length - 1]
        if (last && last.tok === tok) last.text += chars[i]
        else cur.runs.push({ text: chars[i], tok })
        cur.len++
    }
    return segs
})

/** Same, for a fractional character index. */
const posAt = (x: number) => {
    const i = Math.max(0, Math.min(Math.floor(x), chars.length))
    const j = Math.min(i + 1, chars.length)
    return pos.value[i] + (pos.value[j] - pos.value[i]) * (x - i)
}

/* Everything is expressed in `ch` and transitioned with ONE shared
   duration and easing. That is what keeps the morph coherent: the
   container grows 23ch -> 32ch, the inserted span grows 0 -> 9ch, and
   every bracket shifts by 9ch, all on the same curve, so they move as
   one object instead of three things that happen to start together.

   Percentages cannot do this. A percentage of a width that is itself
   animating resolves against the CURRENT width, and the percentage
   value also jumps at t=0, so the annotations lurch while the text
   glides. */
const geom = computed(() => props.parts.map((p) => {
    const l = pos.value[p.from]
    const r = pos.value[p.to]
    const centre = (l + r) / 2
    const labelX = posAt(p.labelAt ?? (p.from + p.to) / 2)
    const dropY = 22 + (p.drop ?? 0) * 16
    return {
        braceLeft: `${l}ch`,
        braceWidth: `${Math.max(r - l, 0)}ch`,
        centre: `${centre}ch`,
        labelLeft: `${labelX}ch`,
        runLeft: `${Math.min(centre, labelX)}ch`,
        runWidth: `${Math.abs(labelX - centre)}ch`,
        v1Height: `${dropY - 10}px`,
        dropY: `${dropY}px`,
    }
}))
</script>

<template>
    <div
        class="cmd-anatomy"
        :style="{ '--fs': fontSize, width: `${totalCh}ch` }"
    >
        <!-- The command. One inline-block per character, so an inserted
             span can expand from zero width and push the rest along. -->
        <div class="cmd-line"><template
            v-for="(seg, si) in segments"
            :key="si"
        ><span
            v-if="seg.inserted === null"
            class="seg"
        ><span
            v-for="(r, ri) in seg.runs"
            :key="ri"
            :class="`tok-${r.tok}`"
        >{{ r.text }}</span></span><span
            v-else
            class="seg ins"
            :style="{ width: shown(seg.inserted) ? `${seg.len}ch` : '0ch' }"
        ><span
            v-for="(r, ri) in seg.runs"
            :key="ri"
            :class="`tok-${r.tok}`"
        >{{ r.text }}</span></span></template></div>

        <!-- Brackets and elbows. -->
        <div class="cmd-annot">
            <template v-for="(p, i) in parts" :key="i">
                <div
                    class="part"
                    :class="{ 'is-off': !shown(i) }"
                    :style="{ transitionDelay: shown(i) ? '0.05s' : '0s' }"
                >
                    <div
                        class="brace"
                        :style="{ left: geom[i].braceLeft, width: geom[i].braceWidth }"
                    />
                    <div
                        class="v1"
                        :style="{ left: geom[i].centre, height: geom[i].v1Height }"
                    />
                    <div
                        class="run"
                        :style="{ left: geom[i].runLeft, width: geom[i].runWidth,
                                  top: geom[i].dropY }"
                    />
                    <div
                        class="v2"
                        :style="{ left: geom[i].labelLeft, top: geom[i].dropY }"
                    />
                </div>
            </template>
        </div>

        <!-- Labels. -->
        <div class="cmd-labels">
            <!-- Zero-width anchor on the grid font, so `left` is in real
                 characters; the label inside carries its own type. -->
            <div
                v-for="(p, i) in parts"
                :key="i"
                class="anchor"
                :style="{ left: geom[i].labelLeft }"
            ><div
                class="cmd-label font-sans"
                :class="{ 'is-off': !shown(i) }"
                :style="{ transitionDelay: shown(i) ? '0.12s' : '0s' }"
            >{{ p.label }}</div></div>
        </div>
    </div>
</template>

<style scoped>
.cmd-anatomy {
    /* The grid font: `ch` on this element and its layout children must
       resolve against the same monospace face as the code line. */
    font-family: var(--slidev-code-font-family, monospace);
    font-size: var(--fs);
    letter-spacing: 0;
    margin: 0 auto;

    --ws-dur: 0.45s;
    --ws-ease: cubic-bezier(0.4, 0, 0.2, 1);

    /* The box is centred, so its width IS the position of everything to
       the left of the insertion. Snap it and `\documentclass` jumps
       while only the inserted span glides. */
    transition: width var(--ws-dur) var(--ws-ease);
}

.cmd-line {
    line-height: 1.25;
    white-space: pre;
}

.seg {
    display: inline-block;
    vertical-align: top;
    white-space: pre;
}

/* The inserted group: one width animation, content clipped while it
   opens, so the rest of the line moves on a single easing curve. */
.ins {
    overflow: hidden;
    transition: width var(--ws-dur) var(--ws-ease);
}

.ins > span {
    display: inline-block;
}

/* The deck's Shiki latex palette, light and dark. */
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

.cmd-annot {
    position: relative;
    height: 48px;
}

.part {
    opacity: 0.75;
    transition: opacity 0.4s ease;
}

.part.is-off {
    opacity: 0;
}

.brace,
.v1,
.run,
.v2 {
    position: absolute;
    /* Every offset is a percentage of the grid box, so all of them
       animate when an inserted span widens the line. */
    transition: left var(--ws-dur) var(--ws-ease),
                width var(--ws-dur) var(--ws-ease),
                top var(--ws-dur) var(--ws-ease);
}

.brace {
    top: 0;
    height: 10px;
    border: 1.5px solid currentColor;
    border-top: none;
}

.v1, .v2 {
    width: 0;
    border-left: 1.5px solid currentColor;
}

.v1 { top: 10px; }
.v2 { bottom: 0; }

.run {
    height: 0;
    border-top: 1.5px solid currentColor;
}

.cmd-labels {
    position: relative;
    height: 3.2rem;
}

/* Zero-width, inherits the grid font, so its `left` is in characters. */
.anchor {
    position: absolute;
    top: 0;
    width: 0;
    transition: left var(--ws-dur) var(--ws-ease);
}

.cmd-label {
    position: absolute;
    top: 0;
    width: 7.5rem;
    margin-left: -3.75rem;
    text-align: center;
    line-height: 1.2;
    font-size: 0.95rem;
    letter-spacing: normal;
    opacity: 1;
    transform: translateY(0);
    transition: opacity 0.4s ease, transform 0.4s ease;
}

.cmd-label.is-off {
    opacity: 0;
    transform: translateY(6px);
}
</style>
