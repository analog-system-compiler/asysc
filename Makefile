

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

.PHONY: all build clean run
.SILENT:
