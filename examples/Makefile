

SHELL = /bin/bash
CIRCUITS_SRC  = $(shell find -name "*.cir")
CIRCUITS_PY   = $(CIRCUITS_SRC:.cir=.py)
SIMULATION_PY = $(shell find -name simulation.py)
BIN_DIR       = ../lightcas/bin

all : $(CIRCUITS_PY)

%.py: %.cir	circuit_base.py
	cp -f circuit_base.py $(@D)
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
	-rm -f $(CIRCUITS_PY)

run: all
	for SIM_FILE in $(SIMULATION_PY); do \
		pushd $$(dirname $$SIM_FILE) > /dev/null; \
		echo Executing $$(dirname $$SIM_FILE)/simulation.py; \
		python3 simulation.py; \
		popd > /dev/null; \
	done

.SILENT:
.PHONY: all clean run
