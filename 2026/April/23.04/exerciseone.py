import sqlite3

conn = sqlite3.connect('loja.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS produtos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    preco REAL NOT NULL,
    stock INTEGER NOT NULL
)''')

produtos = [
    ('arroz', 12.5, 30),
    ('azeite', 22.0, 15),
    ('massa', 8.9, 50),
    ('leite', 1.2, 100),
    ('café', 21.0, 40)
]

cursor.executemany('INSERT OR IGNORE INTO produtos (nome, preco, stock) VALUES (?, ?, ?)', produtos)

cursor.execute('SELECT id, nome, preco, stock FROM produtos WHERE preco < 20')
resultados = cursor.fetchall()

print('Produtos com preço inferior a 20€:')
print(f"{'ID':<3} {'Nome':<10} {'Preço (€)':<10} {'Stock':<6}")
print('-'*35)
for prod in resultados:
    print(f"{prod[0]:<3} {prod[1]:<10} {prod[2]:<10.2f} {prod[3]:<6}")

conn.commit()
conn.close()
