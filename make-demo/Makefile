# it's good practice to include these three lines in any Makefile
MAKEFLAGS += --no-builtin-rules
.DELETE_ON_ERROR:
.SUFFIXES:

# again, it's good practice to specify what goal should be used
# if none is specified on the command line
.DEFAULT_GOAL := report.pdf

# phony targets are ones that do not correspond to actual files
# in this case, we use a 'clean' target which deletes files which
# might have been created by the Makefile
.PHONY: clean

report.pdf: report.tex heathrow-sun.pdf
	pdflatex report

heathrow-sun.pdf: plot-sun.py heathrow-sun.dat
	plot-sun.py < heathrow-sun.dat

clean:
	rm *.aux *.log *.pdf
