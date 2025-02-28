

all: build
	echo -e "\nFor a quick tour, type \"make run\""

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

.PHONY: all build clean run header
.SILENT:
