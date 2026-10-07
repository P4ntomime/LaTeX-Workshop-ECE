<script setup lang="ts">
/**
 * The practice slide that closes every block. Keeps the three things a
 * student needs on screen while they work: what to do, how long they
 * have, and which file to copy if it has all gone wrong.
 *
 *   <HandsOn block="1" todos="1.1 - 1.5" minutes="7" checkpoint="checkpoint-01.tex" />
 */
defineProps<{
  block: string
  todos: string
  minutes: string
  checkpoint: string
}>()
</script>

<template>
  <div class="mt-4">
    <div class="flex items-baseline gap-6">
      <div class="text-6xl font-bold">{{ minutes }} min</div>
      <div class="text-3xl opacity-70">
        Block {{ block }} &mdash; <code>TODO {{ todos }}</code>
      </div>
    </div>

    <div class="mt-8 text-xl">
      <slot />
    </div>

    <div class="mt-10 px-5 py-4 rounded-lg bg-amber-400 bg-opacity-15
                border-l-4 border-amber-500">
      <div class="font-semibold">Stuck? Do not debug alone.</div>
      <div class="mt-1">
        Copy <code>checkpoints/{{ checkpoint }}</code> over
        <code>latex-workshop.tex</code> and carry on with everyone else.
        You will not have missed anything.
      </div>
    </div>
  </div>
</template>
