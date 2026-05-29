import sqlite3

conexao = sqlite3.connect("banco.db")
cursor = conexao.cursor()

# 1. Criação da tabela
cursor.execute("""
CREATE TABLE IF NOT EXISTS carroTB (
    idCarro INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    carro TEXT
)
""")
conexao.commit()

# 2. Inserção dos dados (tudo dentro da mesma string SQL)
cursor.execute("""
INSERT INTO carroTB (idCarro, carro) VALUES
(1, 'Monza'),
(2, 'Opala'),
(3, 'Uno')
""")

# 3. Salvar as inserções no banco
conexao.commit()