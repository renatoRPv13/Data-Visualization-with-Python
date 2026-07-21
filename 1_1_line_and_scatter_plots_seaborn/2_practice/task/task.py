import pandas as pd
import seaborn as sns

from data import preprocess, read


def plot(games: pd.DataFrame) -> sns.FacetGrid:
    # To plot both 'y' and 'approximated_y' against 'x', we can melt the DataFrame.
    melted_df = games.melt(id_vars=['x'], value_vars=['y', 'approximated_y'],
                           var_name='source', value_name='value')

    grid = sns.relplot(
        data=melted_df,
        x="x",
        y="value",
        hue="source",
        kind="line",
        height=6,
        aspect=1.5
    )

    grid.set_axis_labels("X", "Value")

    return grid


# Please solve the task in the plot function and do not modify this one
def main():
    games = read()
    games = preprocess(games)
    fig = plot(games)

    fig.savefig("plot.png", dpi=300)


if __name__ == "__main__":
    main()
