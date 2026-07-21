import matplotlib.pyplot as plt
import pandas as pd

from data import preprocess, read, get_categories, get_category_product_names, get_category_votes


def plot(votes: pd.DataFrame) -> plt.Figure:
    # Seleciona a primeira categoria para o gráfico de pizza
    category = get_categories(votes)[0]
    
    # Pega os dados para a categoria selecionada
    labels = get_category_product_names(votes, category)
    sizes = get_category_votes(votes, category)

    # Cria a figura e os eixos
    fig, ax = plt.subplots()

    # Cria o gráfico de pizza
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')  # Assegura que o gráfico de pizza seja um círculo.

    # Adiciona um título
    ax.set_title(f'Distribuição de Votos para a Categoria: {category}')

    # Retorna a figura
    return fig


# Please solve the task in the plot function and do not modify this one
def main():
    votes = read()
    votes = preprocess(votes)

    fig = plot(votes)
    fig.savefig("plot.png", dpi=300)


if __name__ == "__main__":
    main()
