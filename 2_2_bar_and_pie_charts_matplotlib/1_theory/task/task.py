import matplotlib.pyplot as plt
import pandas as pd

from data import aggregate, preprocess, read


def plot_region(ax: plt.Axes, games: pd.DataFrame, region: str, trace: int = 0):
    # Agrupa os dados para somar as vendas da região por plataforma
    region_data = (
        games.groupby("platform")[region]
        .sum()
        .reset_index()
        .sort_values(by=region, ascending=False)
    )

    # Plota as barras para a região no eixo (ax) fornecido
    ax.bar(
        region_data["platform"],
        region_data[region],
        label=region.upper().replace("_SALES", "")
    )

    # Configurações do eixo individual
    ax.set_title(f"Vendas - {region.upper()}")
    ax.set_xlabel("Plataforma")
    ax.set_ylabel("Vendas (milhões)")
    ax.tick_params(axis='x', rotation=90)


def plot(games: pd.DataFrame) -> plt.Figure:
    # Cria uma figura para mostrar, por exemplo, comparações de regiões
    fig, ax = plt.subplots(figsize=(12, 7))

    # Exemplo chamando plot_region para vendas da América do Norte
    plot_region(ax, games, region="na_sales")

    plt.tight_layout()
    return fig


def main():
    games = read()
    games = preprocess(games)

    fig = plot(games)
    fig.savefig("plot.png", dpi=300)


if __name__ == "__main__":
    main()

# import matplotlib.pyplot as plt
# import pandas as pd
#
# from data import preprocess, read, aggregate
#
#
# def plot_region(ax: plt.Axes, games: pd.DataFrame, region: str, trace: int = 0):
#     pass
#
#
# def plot(games: pd.DataFrame) -> plt.Figure:
#     # 1. Agrega os dados
#     platform_counts = aggregate(games)
#
#     # 2. Cria a figura e os eixos
#     fig, ax = plt.subplots(figsize=(12, 7))
#
#     # 3. Cria o gráfico de barras
#     ax.bar(platform_counts['platform'], platform_counts['count'])
#
#     # Adiciona títulos e rótulos para clareza
#     ax.set_title('Número de Jogos por Plataforma')
#     ax.set_xlabel('Plataforma')
#     ax.set_ylabel('Número de Jogos')
#     plt.xticks(rotation=90)  # Rotaciona os nomes das plataformas para melhor leitura
#     plt.tight_layout()  # Ajusta o layout para evitar que os rótulos se sobreponham
#
#     # 4. Retorna a figura
#     return fig
#
#
# # Please solve the task in the plot function and do not modify this one
# def main():
#     games = read()
#     games = preprocess(games)
#
#     fig = plot(games)
#     fig.savefig("plot.png", dpi=300)
#
#
# if __name__ == "__main__":
#     main()
