# programa de controle financeiro pessoal

""" Linha para lista interna - Substituido por DB"""

# define uma lista vazia para armazenar as transações financeiras
transacoes = []


# define uma função para adicionar uma nova transação
def adicionar_transacao(data, valor, descricao, categoria, tipo):
    transacoes.append({"data": data, "valor": valor, "descricao": descricao, "categoria": categoria, "tipo": tipo})


def exibir_resumo():  # modulo texto — Necessário traduzir para o modo gráfico
    print("Resumo financeiro:")
    print("-" * 30)
    print(f"{'Data':<15} {'Descrição':<15} {'Categoria':<15} {'Valor':<10} {'Tipo':<10}")
    print("-" * 30)
    for transacao in transacoes:
        print(f"{transacao['data']:<15} {transacao['descricao']:<15} {transacao['categoria']:<15} R${transacao['valor']:<10.2f} {transacao['tipo']:<10}")
    print("-" * 30)
    saldo = calcular_saldo()
    print(f"Saldo disponível: R${saldo:.2f}")


# define uma função para calcular o saldo disponível
def calcular_saldo():
    saldo = 0
    for transacao in transacoes:
        if transacao["tipo"] == "Receita":
            saldo += transacao["valor"]
        else:
            saldo -= transacao["valor"]
    return saldo
