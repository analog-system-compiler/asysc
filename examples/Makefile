

SHELL = /bin/bash
CIRCUITS_SRC  = $(shell find -name "*.cir")
CIRCUITS_PY   = $(CIRCUITS_SRC:.cir=.py)
EXAMPLE_DIRS  = $(dir $(CIRCUITS_SRC))
BIN_DIR       = ../lightcas/bin

all : $(CIRCUITS_PY)

%.py: %.cir	circuit_base.py	
	-if [[ "$^" == *"ac/"* ]]; \
	then \
		ANALYSIS_MODE="ac"; \
	else \
		ANALYSIS_MODE="trans"; \
	fi; \
	CMD="$(BIN_DIR)/asysc -i $< -o $@ -t $$ANALYSIS_MODE"; \
	printf "Generating %-50s [%s]\n" "$@" "$$CMD"; \
	$$CMD
ifeq ($(GPROF),1)
	gprof $(BIN_DIR)/asysc > gmon.txt
endif	
	-[ -f debug.log ] && mv debug.log $(@D)
	
clean:
	-rm -f $(CIRCUITS_PY) $(addsuffix "circuit_base.py", $(EXAMPLE_DIRS))

run: all
	for EXAMPLE_DIR in $(EXAMPLE_DIRS); do \
		cp -fu circuit_base.py $$EXAMPLE_DIR; \
		pushd $$EXAMPLE_DIR > /dev/null; \
		echo Executing $${EXAMPLE_DIR}simulation.py; \
		python3 simulation.py; \
		popd > /dev/null; \
	done

header:	
	insert-license --license-filepath=LICENSE --use-current-year --comment-style "#" $$(find . -name "*.py")

.SILENT:
.PHONY: all clean run header
