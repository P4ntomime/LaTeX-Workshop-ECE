# Build the slides:               make
# Rebuild the compiled examples:  make renders
# Remove build files:             make clean
#
# minted needs -shell-escape; latexmkrc passes it to pdflatex for you.

# Where the student template lives, relative to this directory.
TEMPLATE ?= ../workshop-template

# Listings that are only a piece of a document. Each one is wrapped in an
# article by renders/snippet.tex and compiled to renders/<name>.pdf.
# Add a new snippet's file name (without .tex) here.
SNIPPETS = 01-styling 01-emph

slides.pdf: slides.tex preamble.tex beamerthemeown.sty beamercolorthemeown.sty \
            $(wildcard sections/*.tex) $(wildcard listings/*)
	latexmk slides.tex

# renders/ holds the PDFs the slides include:
#   01-sections.pdf, 01-toc.pdf   compiled from listings/, shown next to their code
#   01-styling.pdf, 01-emph.pdf   snippets from listings/, see SNIPPETS above
#   checkpoint-04.pdf             the finished template document (intro slide)
#   cooling-curves.pdf            the template's figure (figure slide)
# They are committed, so this is only needed after changing their sources.
renders: snippets
	latexmk -pdf -outdir=renders/build listings/01-sections.tex listings/01-toc.tex
	cp renders/build/01-sections.pdf renders/build/01-toc.pdf renders/
	# The checkpoints expect figures/ and references.bib next to them.
	rm -rf renders/build/template
	mkdir -p renders/build/template
	cp -r $(TEMPLATE)/figures $(TEMPLATE)/references.bib renders/build/template/
	cp $(TEMPLATE)/checkpoints/checkpoint-04.tex renders/build/template/
	cd renders/build/template && latexmk -pdf -interaction=nonstopmode -halt-on-error checkpoint-04.tex
	cp renders/build/template/checkpoint-04.pdf $(TEMPLATE)/figures/cooling-curves.pdf renders/

# Only the snippets, without the template: make snippets
# The job name tells renders/snippet.tex which listing to wrap.
snippets:
	for s in $(SNIPPETS); do \
	    latexmk -pdf -outdir=renders/build -jobname=$$s renders/snippet.tex || exit 1; \
	    cp renders/build/$$s.pdf renders/; \
	done

clean:
	latexmk -C slides.tex
	rm -rf _minted-slides renders/build

.PHONY: renders snippets clean
