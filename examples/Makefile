

SHELL = /bin/bash
CIRCUITS_SRC  = $(shell find -name "*.cir")
CIRCUITS_PY   = $(CIRCUITS_SRC:.cir=.py)
SIMULATION_PY = $(shell find -name simulation.py)

all : $(CIRCUITS_PY)

%.py: %.cir	circuit_base.py
	-if [[ "$^" == *"ac/"* ]]; \
	then \
		ANALYSIS_MODE="ac"; \
	else \
		ANALYSIS_MODE="trans"; \
	fi; \
	echo "Generating $@"; \
	../lightcas/asysc -i ../examples/$< -o ../examples/$@ -t $$ANALYSIS_MODE
ifeq ($(GPROF),1)
	gprof ../lightcas/asysc > gmon.txt
endif	
	cp -f circuit_base.py $(@D)
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