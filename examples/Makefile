

CIRCUITS_SRC = $(shell find . -name *.cir)
CIRCUITS_PY  = $(CIRCUITS_SRC:.cir=.py)

all : $(CIRCUITS_PY)

%.py: %.cir	
	if [[ "$^" == *"ac/"* ]] \
	then \
		ANALYSIS_MODE="ac"; \
	else \
		ANALYSIS_MODE="trans"; \
	fi; \
	echo "Generating $@"; \
	../build/cirsol -i ../examples/$^ -o ../examples/$@ -t $$ANALYSIS_MODE
	cp -f circuit_base.py $(@D)

clean:
	-rm -f $(CIRCUITS_PY)
	#-rm $(shell find examples -name circuit_base.py)

.SILENT: