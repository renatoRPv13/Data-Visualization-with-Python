import pandas as pd
import seaborn as sns

from data import preprocess, read


def plot(games: pd.DataFrame) -> sns.FacetGrid:
    grid = sns.catplot(
        data=games,
        x="genre",
        y="global_sales",
        kind="bar",
        height=6,
        aspect=1.5

    )
    return  grid
# Please solve the task in the plot function and do not modify this one
def main():
    games = read()
    games = preprocess(games)

    fig = plot(games)
    fig.savefig("plot.png", dpi=300)


if __name__ == "__main__":
    main()
