import sqlite3

conexao = sqlite3.connect("banco.db")
cursor = conexao.cursor()

# 1. CREATE
cursor.execute("""
CREATE TABLE IF NOT EXISTS carroTB (
    idCarro INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    carro TEXT
)
""")
conexao.commit()

# 2. INSERT
cursor.execute("""
INSERT INTO carroTB (idCarro, carro) VALUES
(1, 'Monza'),
(2, 'Opala'),
(3, 'Uno')
""")


conexao.commit()