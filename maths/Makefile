add_sub_word_problems_%.docx:
	uv run generate_arithmetic_problems.py $*

%.pdf: %.docx
	libreoffice --headless --convert-to pdf $<

