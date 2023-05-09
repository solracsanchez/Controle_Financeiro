
from flask import Flask, request, render_template, flash
from lib.funcoes.classes import Transacao, MostrarTransacao
app = Flask(__name__)
app.secret_key = 'carlos'


@app.route('/', methods=['GET', 'POST'])
def index():
    # if request.method == 'GET':
    titulo = 'Bem vindo ao Controle Financeiro'
    return render_template("index.html", titulo=titulo)


@app.route('/adicionar', methods=['GET', 'POST'])
def adicionar():
    if request.method == 'GET':
        titulo = 'Adicionar transação'
        return render_template('transacao.html', titulo=titulo)
    if request.method == 'POST':
        tipo = request.form.get("tipo")
        data = request.form.get("data")
        valor = request.form.get("valor")
        descricao = request.form.get("descricao")
        categoria = request.form.get("categoria")
        conta = request.form.get("conta")

        c = Transacao(tipo, data, valor, descricao, categoria, conta)
        c.AdicionarTransacao()
        flash('Transação adicionada com sucesso')
        titulo = 'Adicionar transação'
        return render_template('transacao.html', titulo=titulo)


@app.route('/resumo', methods=['GET', 'POST'])
def exibir_resumo():
    if request.method == "GET":
        titulo = 'Resumo Financeiro'
        # lista = {}
        args= request.args.get
        print (args)

        # print(inicio, final)
        lista = MostrarTransacao(args)
        # for item in lista:
        #     print(item)
        return render_template('resumo.html', titulo=titulo, lista=lista)
    
    else:
        ids = request.form.get
        print(ids)
        
        titulo = 'Resumo Financeiro'
        args= request.args.get
        # print (args)

        # print(inicio, final)
        lista = MostrarTransacao(args)
        # for item in lista:
        #     print(item)
        return render_template('resumo.html', titulo=titulo, lista=lista)




if __name__ == '__main__':
    app.run(port=4002, debug=True)
