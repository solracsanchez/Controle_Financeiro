from lib.database.database import adicionar_transacao, retorna_transacoes
from datetime import datetime


class Transacao:
    def __init__(self, tipo, data, valor, descricao, categoria, conta):
        self.tipo = tipo
        self.data = data
        self.valor = valor
        self.descricao = descricao
        self.categoria = categoria
        self.conta = conta

    # def GetDados():
    #     self.tipo = request.form.get("tipo")
    #     self.data = request.form.get("data")
    #     self.valor = request.form.get("valor")
    #     self.descricao = request.form.get("descricao")
    #     self.categoria = request.form.get("categoria")
    #     self.conta = request.form.get("conta")

    def AdicionarTransacao(self):
        adicionar_transacao(self.data, self.valor, self.descricao, self.categoria, self.tipo, self.conta)



def MostrarTransacao():
    lista = retorna_transacoes()
    return lista
    for i in lista:
        print(i)
# lista = Transacao.MostrarTransacao
# for i in lista:
#     print(lista)
