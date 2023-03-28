from lib.interface import *


# #print(base.exibir_resumo())
#
# data_str = datetime.strptime(input("Insira a data(dd/mm/aa): "), '%d/%m/%Y')
# print(datetime.strftime(data_str, '%d/%m/%Y'))
# print(f"Data = {datetime.strftime(data_str, '%d/%m/%y')}")
# print(f'Data = {data_str}')

# while True:
#
#     try:
#         resp = str(input('Digite S / N: ')).upper()
#     except KeyboardInterrupt:
#         print('\nUsuario cancelou a entrada!')
#         break
#     else:
#         if resp not in 'SYN' or resp == '':
#             resp = str(input('Opção Invalida!!! Digite S / N: ')).upper()
#         else:
#             print(resp)
#             break


def cor(cor):
    color = {
        'limpo': "\033[m",
        'verm': '\033[31m',
        'verd': '\033[32m',
        'amar': '\033[33m',
        'azul': '\033[34m',
        'fverm': '\033[41:1m',
        'fverd': '\033[42:1m',
        'famar': '\033[30;43:1m',
        'fazul': '\033[30;44:1m'}
    # cod =

    return color[cor]
f'{cor("fverm")}Inserir despesa{cor("limpo")}'
# print(f'{cor("fverm")}teste{cor("limpo")}')
cabecalho(f'{cor("fverm")}Inserir despesa{cor("limpo")}')