import matplotlib.pyplot as plt
import pandas as pd

from data import read


def plot(experiment: pd.DataFrame) -> plt.Figure:
    # Cria a figura e os eixos
    fig, ax = plt.subplots()

    # Plota o histograma nos eixos especificados
    experiment.plot.hist(ax=ax)

    # Retorna o objeto Figure
    return fig


# Please solve the task in the plot function and do not modify this one
def main():
    experiment = read()

    fig = plot(experiment)
    fig.savefig("plot.png", dpi=300)


if __name__ == "__main__":
    main()
