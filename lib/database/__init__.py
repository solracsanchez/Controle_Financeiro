import sqlite3


# cria a conexão com o banco de dados
def abrir_conexao():
    conn = sqlite3.connect('controle_financeiro.db')
    return conn


# fecha a conexão com o banco de dados
def fechar_conexao():
    sqlite3.connect('controle_financeiro.db').close()


# define uma função para adicionar uma nova transação
def adicionar_transacao(data, valor, descricao, categoria, tipo, conta=None, vlr_original=None, data_pgto=None,
                        recorrente=None):
    conn = abrir_conexao()
    conn.execute('INSERT INTO transacoes (data, valor, descricao, categoria, tipo, conta, vlr_original, data_pgto, '
                 'recorrente) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)',
                 (data, valor, descricao, categoria, tipo, conta, vlr_original, data_pgto, recorrente))
    conn.commit()
    fechar_conexao()


def exibir_transacao():  # modulo texto — Necessário traduzir para o modo gráfico
    conn = abrir_conexao()
    cursor = conn.execute('SELECT * FROM transacoes')
    transacoes = []
    for row in cursor:
        transacao = {"id": row[0], "data": row[1], "valor": row[2], "descricao": row[3], "categoria": row[4],
                     "tipo": row[5], "conta": row[6], "vlr_original": row[7], "data_pgto": row[8], "recorrente": row[9]}
        transacoes.append(transacao)
        fechar_conexao()
    return transacoes


def excluir_transacao(id_transacao):
    # executa o comando SQL para excluir a transação com o ID especificado
    conn = abrir_conexao()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM transacoes WHERE id = ?", (id_transacao,))
    conn.commit()
    fechar_conexao()


# cria a tabela de transações se ela não existir
conn = abrir_conexao()
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
fechar_conexao()
