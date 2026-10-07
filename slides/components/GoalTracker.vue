<script setup lang="ts">
/**
 * The advance organiser. It appears once at the start (nothing ticked)
 * and again at the top of every block, with the previous blocks' items
 * ticked off.
 *
 *   <GoalTracker :done="['structure', 'text']" now="math" />
 *
 * `now` highlights what the block about to start will deliver. Block 4
 * delivers two of these, so it also accepts an array:
 *
 *   <GoalTracker :done="[...]" :now="['floats', 'cite']" />
 */
const props = defineProps<{
    done?: string[]
    now?: string | string[]
}>()

const goals = [
    { key: 'structure', label: 'A title, sections and a table of contents' },
    { key: 'text',      label: 'Text and lists that break where you want' },
    { key: 'math',      label: 'Equations you can point back at' },
    { key: 'floats',    label: 'A table and a figure, captioned and numbered' },
    { key: 'cite',      label: 'A citation out of a .bib file' },
]

const isDone = (key: string) => props.done?.includes(key) ?? false
const isNow = (key: string) =>
    Array.isArray(props.now) ? props.now.includes(key) : props.now === key
</script>

<template>
    <div class="flex flex-col gap-3 mt-6">
        <div
            v-for="g in goals"
            :key="g.key"
            class="flex items-center gap-4 transition-all duration-500"
            :class="{
                'opacity-30': !isDone(g.key) && !isNow(g.key),
                'font-semibold': isNow(g.key),
            }"
        >
            <!-- Marker. Drawn with CSS rather than a glyph: the old
                 play-triangle character picked up emoji presentation
                 in some fonts and rendered as a boxed arrow. -->
            <div
                class="w-7 h-7 rounded-full border-2 shrink-0
                       flex items-center justify-center"
                :class="isDone(g.key)
                    ? 'bg-green-500 border-green-500'
                    : isNow(g.key) ? 'border-blue-600' : 'border-gray-400'"
            >
                <svg v-if="isDone(g.key)" viewBox="0 0 24 24" class="w-4 h-4"
                     fill="none" stroke="white" stroke-width="3.5"
                     stroke-linecap="round" stroke-linejoin="round">
                    <path d="M4 12.5 L9.5 18 L20 6.5" />
                </svg>
                <div v-else-if="isNow(g.key)"
                     class="w-2.5 h-2.5 rounded-full bg-blue-600" />
            </div>
            <span class="text-xl">{{ g.label }}</span>
        </div>
    </div>
</template>
