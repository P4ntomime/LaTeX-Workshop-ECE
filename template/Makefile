# Generate the student template:        make
# Generate it and build every state:    make test
# Zip it for a release:                 make zip
# Remove the build folder:              make clean
#
# Edit master.tex, never the generated files in build/.

OUT = build/workshop-template
ZIP = build/workshop-template.zip

ifeq ($(OS),Windows_NT)
export PATH := /usr/bin:$(PATH)
endif

all:
	python3 gen.py $(OUT)

test: all
	./test.sh build/workshop-template build/test

# The files sit at the root of the zip, not in a folder:
# Overleaf's "Upload Project" expects it that way.
zip: test
	rm -f $(ZIP)
	cd $(OUT) && zip -q -r -X ../workshop-template.zip .
	@echo "wrote $(ZIP)"

diag:
	@echo "SHELL=$(SHELL)"
	@echo "PATH=$$PATH"
	@command -v bash env latexmk
	@bash -c 'echo "bash $$BASH_VERSION on $$(uname -s)"'

clean:
	rm -rf build

.PHONY: all test zip clean
