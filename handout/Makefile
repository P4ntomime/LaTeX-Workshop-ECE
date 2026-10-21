# Build the handout:                      make
# Rebuild the handout's own example renders: make renders
# Remove build files:                     make clean
#
# The handout reuses the slides' listings and renders from ../slides.
# Its own examples (the ones the slides do not have) live in listings/
# and are compiled into renders/ with the slides' snippet driver, so
# they look exactly like the slides' renders.

# Snippets without parskip (examples that belong before block 2's
# Paragraph Spacing slide) and with parskip (everything later).
SNIPPETS = ch03-latex-space ch03-styling-all ch03-ulem ch03-sizes \
           ch04-quotes ch04-csquotes ch04-dashes ch04-nested ch04-item-label
SNIPPETS_PARSKIP = ch05-bigops ch05-brackets ch05-operators ch05-text-mathrm \
                   ch05-gather ch05-multline ch05-split ch05-aligned ch05-matrix \
                   ch06-pcolumn ch06-multicolumn ch06-subfigures \
                   ch07-nameref ch07-cleveref-render ch07-citemore \
                   ch07-styles-alphabetic ch07-styles-ieee \
                   ch09-siunitx-more ch09-scolumn ch09-babel-render ch09-enumitem \
                   ch09-amssymb ch09-tabularx ch09-xcolor \
                   ch10-newcommand

# Complete documents from the slides' listings that the slides show
# without a render; compiled as they are and cropped in the handout.
DOCUMENTS = 01-minimal-3

# Complete documents of the handout's own (listings/), compiled the same way.
OWN_DOCUMENTS = ch06-lof

# Citation examples find their .bib files here. The handout's own
# bibliography is handout.bib, so it is never mistaken for the slides'
# references.bib (biber looks in the current folder first).
SNIPPET_ENV = BIBINPUTS=listings:../slides/listings:

handout.pdf: handout.tex preamble.tex $(wildcard chapters/*.tex) handout.bib
	latexmk -pdf handout.tex

renders:
	mkdir -p renders/figures
	for d in $(DOCUMENTS); do \
	    latexmk -pdf -outdir=renders/build ../slides/listings/$$d.tex || exit 1; \
	    cp renders/build/$$d.pdf renders/; \
	done
	for d in $(OWN_DOCUMENTS); do \
	    latexmk -pdf -outdir=renders/build listings/$$d.tex || exit 1; \
	    cp renders/build/$$d.pdf renders/; \
	done
	cp ../slides/renders/figures/cooling-curves.pdf renders/figures/
	for s in $(SNIPPETS); do \
	    $(SNIPPET_ENV) latexmk -pdf -outdir=renders/build -jobname=$$s renders/snippet.tex || exit 1; \
	    cp renders/build/$$s.pdf renders/; \
	done
	for s in $(SNIPPETS_PARSKIP); do \
	    $(SNIPPET_ENV) latexmk -pdf -outdir=renders/build-parskip -jobname=$$s renders/snippet-parskip.tex || exit 1; \
	    cp renders/build-parskip/$$s.pdf renders/; \
	done

clean:
	latexmk -C handout.tex
	rm -rf renders/build renders/build-parskip

.PHONY: renders clean
