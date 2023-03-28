# programa de controle financeiro pessoal

import base
from os import system

""""# define uma função para adicionar uma nova transação
def adicionar_transacao(valor, descricao, categoria, tipo):
    transacoes.append({"valor": valor, "descricao": descricao, "categoria": categoria, "tipo": tipo})"""


# define uma função para calcular o saldo disponível
def calcular_saldo():
    saldo = 0
    for transacao in base.exibir_resumo():
        if transacao["tipo"] == "receita":
            saldo += transacao["valor"]
        else:
            saldo -= transacao["valor"]
    return saldo


# define uma função para exibir o resumo financeiro
def exibir_resumo():
    system('clear')
    print("Resumo financeiro:")
    print("-" * 30)
    print(f"{'Data':<10} {'Descrição':<15} {'Categoria':<15} {'Valor':<10} {'Tipo':<10}")
    print("-" * 30)
    for transacao in base.exibir_resumo():
        print(
            f"{transacao['data']:<15} {transacao['descricao']:<15} {transacao['categoria']:<15} R${transacao['valor']:<10.2f} {transacao['tipo']:<10}")
    print("-" * 30)
    saldo = calcular_saldo()
    print(f"Saldo disponível: R${saldo:.2f}")
    i = input("\nPressione Enter para continuar: ")
    system('clear')


# insere uma despesa no banco
def inserir_despesa():
    data = input("Insira a data da despesa")
    valor = float(input("Insira o valor da despesa: "))
    descricao = input("Insira a descrição da despesa: ")
    categoria = input("Insira a categoria da despesa: ")
    base.adicionar_transacao(data, valor, descricao, categoria, conta, tipo="despesa")


# insere uma receita no banco
def inserir_receita():
    data = input("Insira a data da receita")
    valor = float(input("Insira o valor da receita: "))
    descricao = input("Insira a descrição da receita: ")
    categoria = input("Insira a categoria da receita: ")
    base.adicionar_transacao(data, valor, descricao, categoria, conta, tipo="receita")


# exibe o menu principal
while True:
    # Tela de escolha
    print("Controle Financeiro Pessoal")
    print("-" * 30)
    print("1 - Adicionar Receita")
    print("2 - Adicionar Despesa")
    print("3 - Exibir Resumo Financeiro")
    print("0 - Sair")

    # solicita a escolha do usuário
    escolha = input("Escolha uma opção: ")

    # processa a escolha do usuário
    if escolha == "1":
        system('clear')
        print("Inserir Receita")
        print("-" * 30)
        inserir_receita()
        system('clear')

    elif escolha == "2":
        system('clear')
        print("Inserir Despesa")
        print("-" * 30)
        inserir_despesa()
        system('clear')

    elif escolha == "3":
        exibir_resumo()
        base.fechar_conexao()

    elif escolha == "0":
        base.fechar_conexao()
        break

    else:
        print("Opção inválida, tente novamente.")
        i = input('\nAperte Enter para continuar')
        system('clear')

print("\nObrigado por utilizar o Controle Financeiro Pessoal!")
