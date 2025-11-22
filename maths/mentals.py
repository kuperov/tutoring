#!/usr/bin/env python3

import random
import click

def generate_mentals(count=12):
    mentals = set[str]()
    while len(mentals) < count:
        x = random.randint(0, 12)
        y = random.randint(0, 12)
        if random.random() < 0.5:
            if x not in [0, 1, 2, 10] and y not in [0, 1, 2, 10]:
                continue
            mentals.add(f"${x} \\times {y}=$")
        else:
            sign = '+' if random.random() < 0.5 else '-'
            if sign == '-' and x < y:
                # no negative answers
                continue
            elif sign == '+' and x + y < 10:
                # too easy
                continue
            mentals.add(f"${x} {sign} {y}=$")

    mental_list = list(mentals)
    random.shuffle(mental_list)
    return mental_list

@click.command()
@click.argument('number', type=int)
@click.option('--count', type=int, default=12)
def print_mentals(number: int, count: int = 12):
    random.seed(number)
    mental_list = generate_mentals(count=count)

    print(f"\\clearpage\\section{{Problem set \\textnumero {number}}}")
    print("\\begin{enumerate}")
    print("\\item")
    print("\\begin{multicols}{3}")
    print("\\begin{enumerate}")
    percol = len(mental_list) // 3
    for i, m in enumerate(mental_list):
        maybe_skip = "" if (i+1) % percol == 0 else "\\bigskip"
        print(f"      \\item {m} \\dotfill{maybe_skip}")
    print("\\end{enumerate}")
    print("\\end{multicols}")

    print("\\end{enumerate}")

if __name__ == '__main__':
    print_mentals()
