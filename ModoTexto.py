from lib.funcoes import *
from os import system


# programa de controle financeiro pessoal
while True:
    # Tela de escolha
    system('clear')
    cabecalho('CONTROLE FINANCEIRO PESSOAL')
    menu()

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
        exibir_resumo()
        system('clear')
        
    elif escolha == 4:
        excluir_operacao()
        system('clear')

    elif escolha == 0 or escolha is None:
        fechar_conexao()
        break
    
    else:
        print("Opção inválida, tente novamente.")
        i = input('\nAperte Enter para continuar')
        system('clear')

print("\nObrigado por utilizar o Controle Financeiro Pessoal!")
