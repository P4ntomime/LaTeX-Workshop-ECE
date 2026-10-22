# Build the slides:               make
# Build the handout version:      make handout
# Rebuild the compiled examples:  make renders
# Remove build files:             make clean
#
# minted needs -shell-escape; latexmkrc passes it to pdflatex for you.

# The student template's source (master.tex), relative to this directory,
# and the template generated from it. `make renders' regenerates it first.
TEMPLATE_SRC ?= ../template
TEMPLATE ?= $(TEMPLATE_SRC)/build/workshop-template

# Listings that are only a piece of a document. Each one is wrapped in an
# article by renders/snippet.tex and compiled to renders/<name>.pdf.
# Add a new snippet's file name (without .tex) here.
# SNIPPETS:         shown before the Paragraph Spacing slide (block 2), no parskip
# SNIPPETS_PARSKIP: shown after it, wrapped by renders/snippet-parskip.tex
# SNIPPETS_ERROR:   like SNIPPETS_PARSKIP, but the listing contains a mistake
#                   on purpose; it is compiled through the error, and the PDF
#                   shows what LaTeX makes of it (block 3 warm-up)
SNIPPETS = 01-styling 01-emph 02-linebreaks 02-newline 02-paragraph 02-percent 02-space 02-tilde 02-lists 02-paragraphs 02-noindent
SNIPPETS_PARSKIP = 02-paragraphs-parskip 02-emph \
                   03-warmup-fix 03-scripts 03-scripts-wrong 03-scripts-right \
                   03-labels-wrong 03-labels-right 03-inline-display \
                   03-equation-1 03-equation-2 03-align 03-derivation 03-cases \
                   04-warmup 04-tabular 04-table-float-render 04-caption 04-caption-bf \
                   04-grid 04-lines 04-figure 04-ref-render 04-autoref-render \
                   04-cite 04-styles-numeric 04-styles-authoryear \
                   04-citecmds 04-org-wrong 04-org-right \
                   04-ref-typo 04-cite-typo \
                   99-siunitx
SNIPPETS_ERROR = 03-warmup

# Listings that are complete documents (with \documentclass). They are
# compiled as they are by `make renders' and cropped on the slide.
DOCUMENTS = 00-class-article 00-class-scrartcl 01-sections 01-toc

# The citation snippets (block 4) say \addbibresource{references.bib},
# as in the template. biber finds that file through BIBINPUTS.
ifeq ($(OS),Windows_NT)
	SNIPPET_ENV = BIBINPUTS='listings;'
else
	SNIPPET_ENV = BIBINPUTS=listings:
endif

# Everything both versions of the deck are built from.
SLIDES_DEPS = slides.tex preamble.tex beamerthemeown.sty beamercolorthemeown.sty \
              $(wildcard sections/*.tex) $(wildcard listings/*)

# The presentation: overlays and speaker notes.
slides.pdf: $(SLIDES_DEPS)
	latexmk slides.tex

# The handout version (one page per frame, no notes), as in the release.
handout: slides-handout.pdf

slides-handout.pdf: slides-handout.tex $(SLIDES_DEPS)
	latexmk slides-handout.tex

# renders/ holds the PDFs the slides include:
#   00-class-*.pdf                compiled from listings/, the class comparison (intro)
#   01-sections.pdf, 01-toc.pdf   compiled from listings/, shown next to their code
#   01-styling.pdf, 01-emph.pdf   snippets from listings/, see SNIPPETS above
#   02-..., 03-..., 04-..., 99-...  snippets of blocks 2 to 4 and the closing, see SNIPPETS above
#   checkpoint-04.pdf             the finished template document (intro slide)
#   figures/cooling-curves.pdf    the template's figure, used by the figure snippet
# They are committed, so this is only needed after changing their sources.
renders: snippets
	latexmk -pdf -outdir=renders/build $(addprefix listings/,$(addsuffix .tex,$(DOCUMENTS)))
	for d in $(DOCUMENTS); do cp renders/build/$$d.pdf renders/ || exit 1; done
	# Generate the student template from its source.
	$(MAKE) -C $(TEMPLATE_SRC)
	# The checkpoints expect figures/ and references.bib next to them.
	rm -rf renders/build/template
	mkdir -p renders/build/template
	cp -r $(TEMPLATE)/figures $(TEMPLATE)/references.bib renders/build/template/
	cp $(TEMPLATE)/checkpoints/checkpoint-04.tex renders/build/template/
	cd renders/build/template && latexmk -pdf -interaction=nonstopmode -halt-on-error checkpoint-04.tex
	cp renders/build/template/checkpoint-04.pdf renders/
	mkdir -p renders/figures
	cp $(TEMPLATE)/figures/cooling-curves.pdf renders/figures/

# Only the snippets, without the template: make snippets
# The job name tells the driver which listing to wrap.
snippets:
	for s in $(SNIPPETS); do \
	    latexmk -pdf -outdir=renders/build -jobname=$$s renders/snippet.tex || exit 1; \
	    cp renders/build/$$s.pdf renders/; \
	done
	# Own build directory, so latexmk never mistakes a snippet built with one
	# driver for an up-to-date build with the other (e.g. after moving a name
	# from SNIPPETS to SNIPPETS_PARSKIP).
	for s in $(SNIPPETS_PARSKIP); do \
	    $(SNIPPET_ENV) latexmk -pdf -outdir=renders/build-parskip -jobname=$$s renders/snippet-parskip.tex || exit 1; \
	    cp renders/build-parskip/$$s.pdf renders/; \
	done
	# These fail on purpose, so they run last: the other snippets are built
	# whatever happens here.
	#   -f            latexmk keeps going despite the error
	#   -g            always rerun: latexmk remembers the error of the last run
	#                 and would otherwise refuse ("error in previous invocation")
	#   -pdflatex=... overrides latexmkrc, so a -halt-on-error there cannot
	#                 stop pdflatex before it writes the PDF
	#   nonstopmode   pdflatex recovers from the error and writes the PDF
	# Only a missing PDF counts as a failure here.
	for s in $(SNIPPETS_ERROR); do \
	    rm -f renders/build-parskip/$$s.pdf; \
	    latexmk -pdf -f -g -pdflatex='pdflatex %O %S' -interaction=nonstopmode \
	        -outdir=renders/build-parskip -jobname=$$s renders/snippet-parskip.tex; \
	    test -f renders/build-parskip/$$s.pdf || exit 1; \
	    cp renders/build-parskip/$$s.pdf renders/; \
	done

clean:
	latexmk -C slides.tex
	latexmk -C slides-handout.tex
	rm -rf _minted-slides _minted-slides-handout renders/build renders/build-parskip

.PHONY: handout renders snippets clean
