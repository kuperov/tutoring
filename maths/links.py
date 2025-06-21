# code fragment to generate links and pdfs

import glob
import os

path = "maths"
files = sorted(list(glob.glob(f"{path}/*.pdf")))
links = []

for i, f in enumerate(files, 1):
    links.append(f"[{i}](https://github.com/kuperov/vic-school-worksheets/raw/refs/heads/master/{f})")

print("\n".join(links))
