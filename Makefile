

all: build
	echo "\nTo run the examples, type \"make run\"\n"

build:
	$(MAKE) -C lightcas --no-print-directory
	$(MAKE) -C examples --no-print-directory

clean:
	$(MAKE) -C lightcas --no-print-directory clean 
	$(MAKE) -C examples --no-print-directory clean

run: build
	$(MAKE) -C examples --no-print-directory run

header:	
	insert-license --license-filepath=LICENSE --use-current-year --comment-style "#" $$(find . -name "*.py")

pdf:
	asciidoctor-pdf -D doc/build -r asciidoctor-kroki -r asciidoctor-mathematical -a allow-uri-read -a mathematical-format=svg -a pdf-theme=pdf -a pdf-themesdir=doc doc/index.adoc

html:
	asciidoctor -D doc/build -r asciidoctor-kroki -a allow-uri-read doc/index.adoc

.PHONY: all build clean run header pdf html
.SILENT:
