from lib.database.database import *
from lib.interface.interface import *
from os import system
from datetime import datetime
from time import sleep


# define uma função para calcular o saldo disponível
def calcular_saldo():
    saldo = 0
    for transacao in retorna_transacoes():
        if transacao["tipo"] == "receita":
            saldo += transacao["valor"]
        else:
            saldo -= transacao["valor"]
    return saldo


# define uma função para exibir o resumo financeiro
def exibir_resumo(query=''):
    system('clear')
    abrir_conexao()
    cabecalho('RESUMO FINANCEIRO', 95)
    print(f"{'Data':<13} {'Descrição':<30} {'Categoria':<15} {'Valor':<12} {'Tipo':<10} {'Conta':<10}")
    linhasimp(95)
    for transacao in retorna_transacoes(query):
        data = datetime.strptime(transacao['data'], '%Y-%m-%d %H:%M:%S')
        if len(transacao['descricao']) > 30:
            print(f"{datetime.strftime(data, '%d/%m/%Y'):<13} {transacao['descricao'][0:28]:<28} > "
                  f"{transacao['categoria']:<15}"
                  f"R${transacao['valor']:<10.2f} {transacao['tipo']:<10} {transacao['conta'][0:11]:<10}")
        else:
            print(f"{datetime.strftime(data, '%d/%m/%Y'):<13} {transacao['descricao'][0:30]:<30} "
                  f"{transacao['categoria']:<15}"
                  f"R${transacao['valor']:<10.2f} {transacao['tipo']:<10} {transacao['conta'][0:11]:<10}")
    linhasimp(95)
    # saldo = calcular_saldo()
    # print(f"Saldo disponível: R${saldo:.2f}")
    linhadpla(95)
    fechar_conexao()
    input("Pressione Enter para continuar: ")


# insere uma despesa no banco
def inserir_despesa():
    while True:
        while True:
            system('clear')
            cabecalho(f'{cor("verm")}INSERIR DESPESA{cor("limpo")}')
            data = valida_data('Insira a data(dd/mm/aaaa): ')
            if data is None:
                break
            valor = valida_vlr("Insira o valor: ")
            if valor is None:
                break
            descricao = input("Insira a descrição: ").strip()
            categoria = input("Insira a categoria: ").strip().title()
            tipo = "despesa"
            conta = input("Insira a conta: ").strip().title()
            confirm = valida_sn('Confirma Dados [S/N]')
            if confirm == 'N' or confirm == '':
                print(f'{cor("verm")}Transação não adicionada!{cor("limpo")}')
                break
            else:
                adicionar_transacao(data, valor, descricao, categoria, tipo, conta)
                break
        resp = valida_sn('Adicionar nova transação [S/N]? ')
        if resp == 'N' or resp == '':
            break


# insere uma receita no banco
def inserir_receita():
    while True:
        while True:
            system('clear')
            cabecalho(f'{cor("verd")}INSERIR RECEITA{cor("limpo")}')
            data = valida_data('Insira a data(dd/mm/aaaa): ')
            if data is None:
                break
            valor = valida_vlr("Insira o valor: ")
            if valor is None:
                break
            descricao = input("Insira a descrição: ").strip()
            categoria = input("Insira a categoria: ").strip().title()
            tipo = "receita"
            conta = input("Insira a conta: ").strip().title()
            confirm = valida_sn('Confirma Dados [S/N]')
            if confirm == 'N' or confirm == '':
                print(f'{cor("verm")}Transação não adicionada!{cor("limpo")}')
                break
            else:
                adicionar_transacao(data, valor, descricao, categoria, tipo, conta)
                break
        resp = valida_sn('Adicionar nova transação [S/N]? ')
        if resp == 'N' or resp == '':
            break


# exibe os ids de transações para exclusão
def exibir_ids():
    print(f"{'id':<7} {'Data':<13} {'Descrição':<25} {'Categoria':<15} {'Valor':<12} {'Tipo':<10} {'Conta':<10}")
    linhasimp(100)
    abrir_conexao()
    for transacao in retorna_transacoes():
        data = datetime.strptime(transacao['data'], '%Y-%m-%d %H:%M:%S')
        print(
            f"{transacao['id']:<7} {datetime.strftime(data, '%d/%m/%Y'):<13} {transacao['descricao'][0:25]:<25} "
            f"{transacao['categoria']:<15} "
            f"R${transacao['valor']:<10.2f} {transacao['tipo']:<10} {transacao['conta']:<10}")
    linhasimp(100)


# Função para excluir uma transação do banco
def excluir_operacao():
    system('clear')
    tam = 100
    cabecalho('EXCLUIR ARQUIVOS', tam)
    exibir_ids()

    idt = valida_int("\nDigite a id da transação a ser excluida [0 para Cancelar]: ")
    if idt == 0 or idt is None:
        print('\nOperação cancelada pelo usuário!')
        sleep(1)
        system('clear')
    else:
        print('\033[31mEsta operação não poderá ser desfeita!\033[m')
        s = valida_sn('Tem certeza que deseja excluir essa operação? ')
        if s in 'SY':
            excluir_transacao(idt)
            print('Operação excluida!')
            system('clear')
        else:
            print('Operação cancelada pelo usuário!')
            sleep(1)
            system('clear')


# Validador de números inteiros (opções)
def valida_int(msg=''):
    while True:
        try:
            num = int(input(msg))
        except KeyboardInterrupt:
            return None
        except:
            print('Opção invalida! ', end='')
        else:
            return num


# Validação de entrada de valores tipo moeda (float)
def valida_vlr(msg=''):
    while True:
        try:
            vlr = float(input(msg).replace(',', '.'))
        except KeyboardInterrupt:
            print('\nUsuario cancelou a entrada!')
            sleep(1)
            return None
        except:
            print('Opção invalida! ', end='')
        else:
            return vlr


# Valida opção de S / N para confirmações
def valida_sn(msg=''):
    while True:
        try:
            resp = str(input(msg)).upper().strip()
            while resp not in 'SYN' or resp == '':
                resp = str(input(f'Opção Invalida! Digite [S / N]')).upper().strip()
        except KeyboardInterrupt:
            print(' ')
            return ''
        else:
            return resp


# Validação de entrada de datas
def valida_data(msg=''):
    while True:
        try:
            ent = input(msg)
        except KeyboardInterrupt:
            print('\nUsuario cancelou a entrada!')
            sleep(1)
            return None
        try:
            data = datetime.strptime(ent, '%d/%m/%Y')
        except ValueError:
            try:
                data = datetime.strptime(ent, '%d/%m')
            except:
                print('Data Invalida! ')
                continue
            else:
                data = data.strftime('%d/%m')+f'/{datetime.today().year}'
                data = datetime.strptime(data, '%d/%m/%Y')
                return data
        except Exception as erro:
            print(erro.__class__)
        else:
            return data
