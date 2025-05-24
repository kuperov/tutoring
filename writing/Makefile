# Makefile for converting SVG files to PDF using Inkscape

# Find all SVG files in the current directory
SVG_FILES := $(wildcard *.svg)

# Generate PDF filenames from SVG filenames
PDF_FILES := $(SVG_FILES:.svg=.pdf)

# Default target
all: $(PDF_FILES)

# Pattern rule for converting SVG to PDF
%.pdf: %.svg
	inkscape --export-filename=$@ $<

# Print targets
print-%: %.pdf
	lpr $< -P "HL-2270DW"

print-all: $(PDF_FILES)
	lpr $^

printers:
	lpstat -p

# Clean target to remove generated PDFs
clean:
	rm -f $(PDF_FILES)

.PHONY: all clean print-all printers 
