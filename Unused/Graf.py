import matplotlib.pyplot as plt

import ModoTexto


def exibir_resumo():
    # código para exibir as transações...

    # cria um dicionário para armazenar as despesas por categoria
    despesas_por_categoria = {}
    for transacao in main.transacoes:
        if transacao['tipo'] == 'despesa':
            categoria = transacao['categoria']
            valor = transacao['valor']
            if categoria in despesas_por_categoria:
                despesas_por_categoria[categoria] += valor
            else:
                despesas_por_categoria[categoria] = valor

    # cria um gráfico de barras para exibir as despesas por categoria
    categorias = list(despesas_por_categoria.keys())
    valores = list(despesas_por_categoria.values())
    plt.bar(categorias, valores)
    plt.title('Despesas por Categoria')
    plt.xlabel('Categoria')
    plt.ylabel('Valor')
    plt.show()
