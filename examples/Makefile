

CIRCUITS_SRC = $(shell find . -name *.cir)
CIRCUITS_PY  = $(CIRCUITS_SRC:.cir=.py)

all : $(CIRCUITS_PY)

%.py: %.cir
	if [[ $@ == *"/ac/"* ]]; then
		../build/cirsol -i ../examples/$^ -o ../examples/$@ -t ac
	else
		../build/cirsol -i ../examples/$^ -o ../examples/$@ -t trans
	fi

clean:
	-rm -f $(CIRCUITS_PY)