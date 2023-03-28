"""# programa de controle financeiro pessoal

import sqlite3


# cria a conexão com o banco de dados
conn = sqlite3.connect('controle_financeiro.db')
curs = conn.cursor()

# cria a tabela de transações se ela não existir
conn.execute('''CREATE TABLE IF NOT EXISTS transacoes
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  data TEXT,
                  valor REAL,
                  descricao TEXT,
                  categoria TEXT,
                  tipo TEXT,
                  conta TEXT,
                  vlr_original TEXT,
                  data_pgto TEXT,
                  recorrente TEXT)''')


# define uma função para adicionar uma nova transação
def adicionar_transacao(data, valor, descricao, categoria, tipo, conta=None, vlr_original=None, data_pgto=None,
                        recorrente=None):
    conn.execute('INSERT INTO transacoes (data, valor, descricao, categoria, tipo, conta, vlr_original, data_pgto, '
                 'recorrente) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)',
                 (data, valor, descricao, categoria, tipo, conta, vlr_original, data_pgto, recorrente))
    conn.commit()


def exibir_resumo():  # modulo texto — Necessário traduzir para o modo gráfico
    cursor = conn.execute('SELECT * FROM transacoes')
    transacoes = []
    for row in cursor:
        transacao = {"id": row[0], "data": row[1], "valor": row[2], "descricao": row[3], "categoria": row[4],
                     "tipo": row[5], "conta": row[6], "vlr_original": row[7], "data_pgto": row[8], "recorrente": row[9]}
        transacoes.append(transacao)
    return transacoes


def excluir_operacao(id_transacao):
    # executa o comando SQL para excluir a transação com o ID especificado
    curs.execute("DELETE FROM transacoes WHERE id = ?", (id_transacao,))


# fecha a conexão com o banco de dados
def fechar_conexao():
    conn.close()


# define uma função para calcular o saldo disponível
def calcular_saldo():
    saldo = 0
    for transacao in transacoes:
        if transacao["tipo"] == "Receita":
            saldo += transacao["valor"]
        else:
            saldo -= transacao["valor"]
    return saldo"""

