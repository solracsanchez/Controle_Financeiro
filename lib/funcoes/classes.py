from datetime import date, timedelta
from lib.database.database import adicionar_transacao, retorna_transacoes


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
    #     self.valor = request.form.get("valor")MostrarTransacao
    #     self.descricao = request.form.get("descricao")
    #     self.categoria = request.form.get("categoria")
    #     self.conta = request.form.get("conta")

    def AdicionarTransacao(self):
        adicionar_transacao(self.data, self.valor, self.descricao, self.categoria, self.tipo, self.conta)



def MostrarTransacao(args):

    if args('datainicial') == 'mes':
        final = date.today()
        inicio = final.replace(day=1)
        # query = "SELECT * FROM transacoes WHERE data > datetime ('now','start of month') ORDER BY data"
    elif args('datainicial') == 'trinta':
        final = date.today()
        inicio = final-timedelta(days=30)
    elif args('datainicial') == 'noventa':
        final = date.today()
        inicio = final-timedelta(days=90)
    else:
        final = date.today()
        inicio = final-timedelta(days=365)

    query = f"SELECT * FROM transacoes WHERE data BETWEEN '{inicio}' AND datetime ('{final}') ORDER BY data"

    lista = retorna_transacoes(query)
    return lista
    # for i in lista:
    #     print(i)
# lista = Transacao.MostrarTransacao
# for i in lista:
#     print(lista)
