def cabecalho(msg='', tam=60):
    """
    Imprime cabeçalho padrão com bordas
    :param msg: Texto centralizado no cabeçalho
    :param tam: Tamanho padrão é 60
    """
    linhadpla(tam)
    print(msg.center(tam))
    linhadpla(tam)


def linhasimp(tam=60):  # Imprime uma linha simples conforme o tamanho fornecido
    print('-' * tam)


def linhadpla(tam=60):  # Imprime uma linha simples conforme o tamanho fornecido
    print('=' * tam)


def cor(clr):
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
    return color[clr]
