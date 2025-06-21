# code fragment to generate links and pdfs

import glob
import os

path = "writing/text/6mm"
files = sorted(list(glob.glob(f"{path}/*.svg")))
links = []

for i, f in enumerate(files, 1):
    pdf_file = f.replace(".svg", ".pdf")
    cmd = f"inkscape --export-filename={pdf_file} {f}"
    if not os.path.exists(pdf_file):
        os.system(cmd)
    links.append(f"[{i}](https://github.com/kuperov/vic-school-worksheets/raw/refs/heads/master/{pdf_file})")

print("\n".join(links))
