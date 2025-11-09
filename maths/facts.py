#!/usr/bin/env python3

import click
import numpy as np
import random
import os


def generate_facts(number: int, limit: int, ncolumns: int, seed: int) -> str:
    random.seed(seed)
    percol = number // ncolumns
    facts = np.zeros((limit+1,limit+1))
    while facts.sum() < number:
        i = random.randint(0, limit+1)
        j = random.randint(0, limit+1)
        if i >= limit or j >= limit:
            continue
        facts[i, j] = 1

    nonzero = np.argwhere(facts.reshape((-1,))).squeeze()
    def prob(x, y, i):
        text = f'      \\item ${x} + {y} =$ \\dotfill'
        if (i+1) % percol != 0:
            text += '\\bigskip'
        return text

    problems = list(zip(nonzero // (limit+1), nonzero % (limit+1)))
    random.shuffle(problems)
    problem_text = [prob(x, y, i) for i, (x, y) in enumerate(problems)]

    text = []
    text.append(fr"""    \begin{{enumerate}}\bigskip""")
    text.append('\n'.join(problem_text))
    text.append(r"""    \end{enumerate}""")
    return '\n'.join(text)

@click.group()
def cli():
    """Maths facts questions generator"""
    pass

@cli.command('questions')
@click.argument('seed', type=int)
@click.option('--number', type=int, default=12)
@click.option('--limit', type=int, default=12)
@click.option('--ncolumns', type=int, default=3)
def questions(seed: int, number: int, limit: int, ncolumns: int):
    facts = [fr"""\item
  \begin{{multicols}}{{{ncolumns}}}"""]
    facts.append(generate_facts(number, limit, ncolumns, seed))
    facts.append(r"""  \end{multicols}""")
    print('\n'.join(facts))

@cli.command('test')
@click.option('--number', type=int, default=42)
@click.option('--limit', type=int, default=12)
@click.option('--ncolumns', type=int, default=3)
@click.option('--seed', type=int, default=1)
def generate_timed_test_cli(number:int, limit:int, ncolumns: int, seed: int):
    tt = generate_timed_test(number, limit, ncolumns, seed)
    print(tt)

def generate_timed_test(number:int, limit:int, ncolumns: int, seed: int):
    lines = [fr"""\documentclass[a4paper, 11pt]{{article}}
\usepackage[a4paper, margin=1.5cm]{{geometry}}
\usepackage{{multicol}}

\title{{Addition Maths Facts Test \textnumero {seed}}}
\author{{}}
\date{{}}
\begin{{document}}
\maketitle

Answer as many as you can in 60 seconds.
You won't get them all---just do your best!\bigskip

"""]
    lines.append(fr"""\begin{{multicols}}{{{ncolumns}}}""")
    lines.append(generate_facts(number, limit, ncolumns, seed))
    lines.append(r"""\end{multicols}""")
    lines.append(r"""\end{document}""")
    return '\n'.join(lines)

@cli.command('many-tests')
@click.option('--count', type=int, default=10)
@click.option('--number', type=int, default=54)
@click.option('--limit', type=int, default=12)
@click.option('--ncolumns', type=int, default=3)
@click.option('--seed', type=int, default=1)
def many_tests_cli(count: int, number: int, limit: int, ncolumns: int, seed: int):
    for i in range(count):
        tt = generate_timed_test(number, limit, ncolumns, seed + i)
        with open(f"addition_facts_test_{i+1}.tex", "w") as f:
            f.write(tt)
        os.system(f"pdflatex addition_facts_test_{i+1}.tex")
        os.remove(f"addition_facts_test_{i+1}.log")
        os.remove(f"addition_facts_test_{i+1}.aux")

if __name__ == "__main__":
    cli()
