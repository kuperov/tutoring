
all: worksheets.pdf

%.pdf: %.tex
	pdflatex -interaction=nonstopmode -halt-on-error -output-directory=build $<
