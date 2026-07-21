import pandas as pd
import seaborn as sns

from data import read


def plot(votes: pd.DataFrame) -> sns.FacetGrid:
    grid = sns.catplot(
        data=votes,
        x="category",  # Usando a coluna correta
        kind="count",  # 'count' é mais apropriado quando não há um eixo y numérico
        height=6,
        aspect=1.5,
    )
    return grid


# Please solve the task in the plot function and do not modify this one
def main():
    votes = read()

    fig = plot(votes)
    fig.savefig("plot.png", dpi=300)


if __name__ == "__main__":
    main()
