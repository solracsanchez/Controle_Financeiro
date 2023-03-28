import sqlite3
import base

# cria a conexão com o banco de dados SQLite
conn = sqlite3.connect('transacoes.db')

# cria a tabela "transacoes" no banco de dados
conn.execute('''CREATE TABLE IF NOT EXISTS transacoes
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  data TEXT,
                  valor REAL,
                  descricao TEXT,
                  categoria TEXT,
                  tipo TEXT)''')

# insere as transações da lista main.transacoes na tabela "transacoes" do banco de dados
for transacao in base.transacoes:
    conn.execute('INSERT INTO transacoes (valor, descricao, categoria, tipo) VALUES (?, ?, ?, ?)',
                 (transacao["valor"], transacao["descricao"], transacao["categoria"], transacao["tipo"]))

# commita as mudanças no banco de dados e fecha a conexão
conn.commit()
conn.close()