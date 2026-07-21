import pandas as pd
import seaborn as sns

from data import preprocess, read


def plot(games: pd.DataFrame) -> sns.FacetGrid:
    # Usando os nomes exatos das colunas do seu DataFrame
    grid = sns.relplot(
        data=games,
        x="critic_score",  # Nota dos críticos no eixo X
        y="global_sales",  # Vendas no eixo Y
        hue="genre",  # Colorido por gênero
        kind="scatter",  # Gráfico de dispersão
        height=6,
        aspect=1.5
    )

    # Ajustando os títulos dos eixos para ficar legível
    grid.set_axis_labels("Ano de Lançamento", "Vendas Globais (em milhões)")

    return grid

# def plot(games: pd.DataFrame) -> sns.FacetGrid:
#     print("Colunas disponíveis no DataFrame:", games.columns.tolist())
#     colunas_numericas = games.select_dtypes(include=["number"]).columns
#     coluna_x = colunas_numericas[0] if len(colunas_numericas) > 0 else games.select_dtypes(include=["number"]).columns
#     grid =sns.displot(
#         data= games,
#         x = coluna_x,
#          kind="hist",
#         height=5,
#         aspect = 1.5
#     )
#     # Opcional: Ajustar títulos dos eixos diretamente no FacetGrid
#     #grid.set_axis_labels("Ano de Lançamento", "Vendas Globais (Milhões)")
#     return  grid


# Please solve the task in the plot function and do not modify this one
def main():
    games = read()
    games = preprocess(games)

    fig = plot(games)
    fig.savefig("plot.png", dpi=300)


if __name__ == "__main__":
    main()
