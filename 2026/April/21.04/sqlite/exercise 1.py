import sqlite3

conn = sqlite3.connect('exercise.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE
  )'''
)

cursor.execute('INSERT OR IGNORE INTO users (name, email) VALUES (?, ?)', ('alice', 'alice@example.com'))

# Mostra os utilizadores antes das alterações
print("Antes do update/delete:")
cursor.execute('SELECT * FROM users')
for aluno in cursor.fetchall():
    print(aluno)

cursor.execute('UPDATE users SET email = ? WHERE name = ?', ('alice_updated@example.com', 'alice'))
cursor.execute('DELETE FROM users WHERE id = ?', (1,))

# Mostra os utilizadores depois das alterações
print("Depois do update/delete:")
cursor.execute('SELECT * FROM users')
for aluno in cursor.fetchall():
    print(aluno)

conn.commit()
conn.close()