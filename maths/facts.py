import click
import numpy as np
import random


@click.command()
@click.option('--number', type=int, default=12)
@click.option('--limit', type=int, default=12)
@click.option('--ncolumns', type=int, default=3)
@click.option('--seed', type=int, default=123)
def generate_facts(number: int, limit: int, ncolumns: int, seed: int):
    random.seed(seed)
    percol = number // ncolumns
    facts = np.zeros((limit+1,limit+1))
    while facts.sum() < number:
        i = random.randint(0, limit+1)
        j = random.randint(0, limit+1)
        facts[i, j] = 1

    nonzero = np.argwhere(facts.reshape((-1,))).squeeze()
    def prob(x, y, i):
        text = f'      \\item {x} + {y} = \\dotfill'
        if (i+1) % percol != 0:
            text += '\\bigskip'
        return text

    problems = list(zip(nonzero // (limit+1), nonzero % (limit+1)))
    random.shuffle(problems)
    problem_text = [prob(x, y, i) for i, (x, y) in enumerate(problems)]

    print(fr"""\item
  \begin{{multicols}}{{{ncolumns}}}
    \begin{{enumerate}}\bigskip""")
    print('\n'.join(problem_text))
    print(r"""    \end{enumerate}
  \end{multicols}""")


if __name__ == "__main__":
    generate_facts()