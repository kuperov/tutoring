
all_docx := $(wildcard *.docx)
all_pdfs := $(all_docx:.docx=.pdf)

all: $(all_pdfs)

add_sub_word_problems_%.docx:
	uv run generate_arithmetic_problems.py $*

%.pdf: %.docx
	libreoffice --headless --convert-to pdf $<

all_add_sub_word_problems.pdf: $(filter add_sub_word_problems%.pdf,$(all_pdfs))
	pdftk $^ cat output $@
