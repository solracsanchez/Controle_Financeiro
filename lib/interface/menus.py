from lib.funcoes.funcoes import *
from lib.interface.interface import *


def menu_inicial():  # Menu opções da tela inicial
    while True:
        cabecalho('CONTROLE FINANCEIRO PESSOAL')
        print("1 - Adicionar Receita")
        print("2 - Adicionar Despesa")
        print("3 - Exibir Resumo Financeiro")
        print("4 - Excluir uma transação")
        print("0 - Sair")
        linhasimp()
        # solicita a escolha do usuário
        escolha = valida_int("Escolha uma opção: ")

        # processa a escolha do usuário
        if escolha == 1:
            inserir_receita()
            system('clear')

        elif escolha == 2:
            inserir_despesa()
            system('clear')

        elif escolha == 3:
            system('clear')
            menu_resumo()
            system('clear')

        elif escolha == 4:
            excluir_operacao()
            system('clear')

        elif escolha == 0 or escolha is None:
            fechar_conexao()
            break

        else:
            print("Opção inválida, tente novamente.")
            input('\nAperte Enter para continuar')
            system('clear')


def menu_resumo():
    while True:
        cabecalho('RESUMO FINANCEIRO')
        print("1 - Últimos 30 dias")
        print("2 - Mês atual")
        print("3 - Meses anteriores")
        print("4 - Escolher período")
        print("0 - Sair")
        linhasimp()
        escolha = valida_int('Escolha um período: ')

        # processa a escolha do usuário
        if escolha == 1:
            query = "SELECT * FROM transacoes WHERE data > datetime ('now', '-1 months') ORDER BY data"
            exibir_resumo(query)
            system('clear')

        elif escolha == 2:
            query = "SELECT * FROM transacoes WHERE data > datetime ('now','start of month') ORDER BY data"
            exibir_resumo(query)
            system('clear')

        elif escolha == 3:
            meses = valida_int('Quantos meses? ')
            query = f"SELECT * FROM transacoes WHERE data > datetime ('now','start of month', '-{meses-1} months') " \
                    f"ORDER BY data"
            exibir_resumo(query)
            system('clear')

        elif escolha == 4:
            inicio = valida_data('Data Inicial? ')
            final = valida_data('Data final?')
            query = f"SELECT * FROM transacoes WHERE data BETWEEN '{inicio}' AND datetime ('{final}') ORDER BY data"
            exibir_resumo(query)
            # print(query)
            # input('preess')
            system('clear')

        elif escolha == 0 or escolha is None:
            fechar_conexao()
            break

        else:
            print("Opção inválida, tente novamente.")
            input('\nAperte Enter para continuar')
            system('clear')
