import matplotlib.pyplot as plt
import pandas as pd

from data import preprocess, read


def plot(games: pd.DataFrame) -> plt.Figure:
    # Cria a figura e os eixos
    fig, ax = plt.subplots(figsize=(10, 6))

    # O método plot.scatter do pandas retorna um objeto de eixos (Axes)
    # Não precisamos passar 'data' ou 'kind' aqui.
    # O argumento 'c' pode ser usado para cor, mas 'hue' como no seaborn requer mais trabalho.
    # Por simplicidade, vamos criar um gráfico de dispersão simples.
    games.plot.scatter(
        x="critic_score",  # Nota dos críticos no eixo X
        y="global_sales",  # Vendas no eixo Y
        ax=ax  # Especifica em quais eixos desenhar
    )

    # Retorna o objeto Figure para que possa ser salvo
    return fig


# Please solve the task in the plot function and do not modify this one
def main():
    games = read()
    games = preprocess(games)

    fig = plot(games)
    fig.savefig("plot.png", dpi=300)


if __name__ == "__main__":
    main()
