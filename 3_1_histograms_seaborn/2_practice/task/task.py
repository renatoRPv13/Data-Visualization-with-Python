import pandas as pd
import seaborn as sns

from data import read


def plot(sales: pd.DataFrame) -> sns.FacetGrid:
    return  # TODO


# Please solve the task in the plot function and do not modify this one
def main():
    sales = read()

    fig = plot(sales)
    fig.savefig("plot.png", dpi=300)


if __name__ == "__main__":
    main()
