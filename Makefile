

all:
	$(MAKE) -C lightcas --no-print-directory
	$(MAKE) -C examples --no-print-directory

clean:
	$(MAKE) -C lightcas --no-print-directory clean 
	$(MAKE) -C examples --no-print-directory clean

run:
	$(MAKE) -C examples --no-print-directory run

header:	
	insert-license --license-filepath=LICENSE --use-current-year --comment-style "#" $$(find . -name "*.py")

.SILENT:
