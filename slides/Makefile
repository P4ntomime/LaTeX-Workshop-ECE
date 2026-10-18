# Build the slides:               make
# Rebuild the compiled examples:  make renders
# Remove build files:             make clean
#
# minted needs -shell-escape; latexmkrc passes it to pdflatex for you.

# Where the student template lives, relative to this directory.
TEMPLATE ?= ../workshop-template

slides.pdf: slides.tex preamble.tex beamerthemeown.sty beamercolorthemeown.sty \
            $(wildcard sections/*.tex) $(wildcard listings/*)
	latexmk slides.tex

# renders/ holds the PDFs the slides include:
#   01-sections.pdf, 01-toc.pdf   compiled from listings/, shown next to their code
#   checkpoint-04.pdf             the finished template document (intro slide)
#   cooling-curves.pdf            the template's figure (figure slide)
# They are committed, so this is only needed after changing their sources.
renders:
	latexmk -pdf -outdir=renders/build listings/01-sections.tex listings/01-toc.tex
	cp renders/build/01-sections.pdf renders/build/01-toc.pdf renders/
	# The checkpoints expect figures/ and references.bib next to them.
	rm -rf renders/build/template
	mkdir -p renders/build/template
	cp -r $(TEMPLATE)/figures $(TEMPLATE)/references.bib renders/build/template/
	cp $(TEMPLATE)/checkpoints/checkpoint-04.tex renders/build/template/
	cd renders/build/template && latexmk -pdf -interaction=nonstopmode -halt-on-error checkpoint-04.tex
	cp renders/build/template/checkpoint-04.pdf $(TEMPLATE)/figures/cooling-curves.pdf renders/

clean:
	latexmk -C slides.tex
	rm -rf _minted-slides renders/build

.PHONY: renders clean
