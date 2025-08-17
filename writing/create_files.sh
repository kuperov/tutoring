#!/usr/bin/env bash
 
for d in `ls text/`; do
	echo Processing text/$d
	pushd text/$d;
	for f in `ls *svg`; do
		inkscape --export-filename=${f%.*}.pdf $f;
	done
	pdftk *pdf cat output ../../writing_${d}.pdf
	popd
done
echo Finished.
