from figures import draw_clock
import matplotlib.pyplot as plt
import random
import math
import string

HEADER = r"""\documentclass[a4paper, 11pt]{article}
\usepackage[a4paper, margin=1.5cm]{geometry}
\usepackage{graphicx}

\begin{document}

"""
FOOTER = r"""\end{document}"""

with open(f"time.tex", "w") as f:
    f.write(HEADER)
    sheet_number = 1
    for kind in ['five_minutes', 'exact', 'digital']:
        for j in range(1, 6):
            if j == 1:
                desc = {
                    'five_minutes': 'Time to five minutes',
                    'exact': 'Time to the minute',
                    'digital': 'Time in digital format',
                }
                f.write(f"\\clearpage\\section*{{{desc[kind]}}}\n")
            else:
                f.write(r"\clearpage")
            f.write(f"\n\\subsection*{{Problem Set \\textnumero {sheet_number}}}\n")
            instruct = {
                'five_minutes': 'Write the time in words, to the nearest five minutes.',
                'exact': 'Write the time in words, to the nearest minute. For example, ``twenty-three minutes past four."',
                'digital': 'Write the time in words (e.g. ``twenty-three minutes past four") and in digital format (e.g. ``04:23").',
            }
            f.write(f"\n{instruct[kind]}\n\n")
            for i in range(0, 2):
                fig, axes = plt.subplots(1, 5, figsize=(15, 3))
                for k, ax in enumerate(axes):
                    random.seed(sheet_number*10000 + 100*i + k)
                    # random time
                    rhr = random.randint(1, 12)
                    if kind == 'five_minutes':
                        rmin = 5 * random.randint(0, 11)
                    else:
                        rmin = random.randint(0, 59)
                    rsec = random.randint(0, 59)
                    draw_clock(rhr, rmin, rsec, ax=ax)
                    ax.set_title(f"({string.ascii_lowercase[k+5*i]})")
                fig.tight_layout()
                fig.savefig(f"time/clocks_{sheet_number}_{i}.pdf", bbox_inches="tight")
                plt.close(fig)
                f.write(f"\\includegraphics[width=\\textwidth]{{time/clocks_{sheet_number}_{i}.pdf}}\n")
                f.write(r"\begin{enumerate}")
                for k in range(5):
                    f.write(f"\\item[({string.ascii_lowercase[k+5*i]})] \\dotfill\\bigskip\n")
                f.write(r"\end{enumerate}")
            sheet_number += 1
    f.write(FOOTER)
