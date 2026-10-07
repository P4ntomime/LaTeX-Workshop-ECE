<script setup lang="ts">
/**
 * A marked gap for an asset you still have to produce -- almost always a
 * screenshot of a real compiled PDF. Deliberately loud, so that none of
 * them survive to the day of the workshop.
 *
 *   <Placeholder what="checkpoint-01.pdf, page 1" h="260px" />
 *
 * Once the file exists, replace the whole tag with:
 *   <img src="/renders/checkpoint-01-p1.png" class="rounded shadow" />
 */
defineProps<{ what: string; h?: string }>()
</script>

<template>
  <div
    class="w-full flex flex-col items-center justify-center gap-2
           border-2 border-dashed border-pink-400 rounded-lg
           bg-pink-400 bg-opacity-5 text-pink-500"
    :style="{ height: h ?? '220px' }"
  >
    <div class="text-sm uppercase tracking-widest opacity-70">screenshot needed</div>
    <div class="text-base font-mono px-6 text-center">{{ what }}</div>
  </div>
</template>
