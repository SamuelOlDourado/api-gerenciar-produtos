import sqlite3
conexao = sqlite3.connect('banco_produtos.db')
cursor = conexao.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS Produtos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    descricao TEXT NOT NULL,
    preco REAL NOT NULL,
    estoque INTEGER NOT NULL,
    categoria TEXT NOT NULL
)
''')
conexao.commit()
conexao.close()