# Screenshots of compiled output

Put the PNGs the deck references here. They are deliberately real
compiled PDF output, not a web approximation, so that students see
exactly what their own compiler produces.

Suggested names, matching the `<Placeholder>` boxes in the slides:

    checkpoint-04-all.png        all four pages of the finished report
    checkpoint-01-p1.png         page 1, cropped to the numbered headings
    checkpoint-01-toc.png        just the Contents block
    table-hline.png              the vessel table with \hline rules
    table-booktabs.png           the same table with booktabs rules

To make them, compile the checkpoint and rasterise the page:

    latexmk -pdf checkpoints/checkpoint-01.tex
    pdftoppm -png -r 200 -f 1 -l 1 checkpoint-01.pdf checkpoint-01-p1

Then crop. Keep them above about 150 dpi so they stay sharp on a
projector.
