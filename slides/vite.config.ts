import { defineConfig } from 'vite'

export default defineConfig({
  build: {
    // WHY THIS IS HERE
    // With `lineNumbers: true` in the headmatter, Slidev emits a rule
    //   .slidev-code-line-numbers .slidev-code code .line::before { --uno: ... }
    // whose UnoCSS expansion the lightningcss minifier refuses to parse,
    // so `npm run build` dies with "Invalid token in pseudo element".
    //
    // Turning CSS minification off sidesteps it. The deck is served
    // locally or as a static export, so a few unminified kilobytes of
    // CSS cost nothing. `slidev dev` was never affected.
    //
    // Try removing this after a Slidev upgrade; if the build still
    // works, delete the file.
    cssMinify: false,
  },
})
