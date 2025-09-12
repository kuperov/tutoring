from figures import draw_clock
import matplotlib.pyplot as plt
import random
import math
import string

HEADER = r"""\documentclass[a4paper, 11pt]{article}
\usepackage[a4paper, margin=1.5cm]{geometry}
\usepackage{graphicx}

\title{What's the Time?}
\date{}
\author{}

\begin{document}
\maketitle

"""
FOOTER = r"""\end{document}"""

def make_time_sheet(sheet_number: int):
    with open(f"time/time_{sheet_number}.tex", "w") as f:
        tex = ""
        for i in range(0, 2):
            fig, axes = plt.subplots(1, 5, figsize=(15, 3))
            for j, ax in enumerate(axes):
                # random time
                rhr = random.randint(1, 12)
                rmin = random.randint(0, 59)
                rsec = random.randint(0, 59)
                draw_clock(rhr, rmin, rsec, ax=ax)
                ax.set_title(f"({string.ascii_lowercase[j+5*i]})")
            fig.tight_layout()
            fig.savefig(f"time/clocks_{sheet_number}_{i}.pdf", bbox_inches="tight")
            plt.close(fig)
            tex += f"\\includegraphics[width=\\textwidth]{{clocks_{sheet_number}_{i}.pdf}}\n"
            tex += r"\begin{enumerate}"
            for j in range(5):
                tex += f"\\item[({string.ascii_lowercase[j+5*i]})] \\dotfill\\bigskip\n"
            tex += r"\end{enumerate}"
        f.write(HEADER)
        f.write(tex)
        f.write(FOOTER)

if __name__ == "__main__":
    for i in range(1, 6):
        make_time_sheet(i)
