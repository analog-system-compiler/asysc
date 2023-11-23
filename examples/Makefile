

MAKEFLAGS = --jobs 1

CIRCUITS_SRC = $(shell find -name "*.cir")
CIRCUITS_PY  = $(CIRCUITS_SRC:.cir=.py)

all : $(CIRCUITS_PY)

%.py: %.cir	
	-if [[ "$^" == *"ac/"* ]] \
	then \
		ANALYSIS_MODE="ac"; \
	else \
		ANALYSIS_MODE="trans"; \
	fi; \
	echo "Generating $@"; \
	../lightcas/asysc -i ../examples/$^ -o ../examples/$@ -t $$ANALYSIS_MODE
	#cp -f circuit_base.py $(@D)
	-[ -f debug.log ] && mv debug.log $(@D)
	
clean:
	-rm -f $(CIRCUITS_PY)

.SILENT: