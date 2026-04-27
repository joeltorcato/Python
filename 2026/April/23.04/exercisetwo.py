import sqlite3

def criar_tabela():
    conn = sqlite3.connect('agenda.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS contatos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        telefone TEXT NOT NULL,
        email TEXT NOT NULL
    )''')
    conn.commit()
    conn.close()

def adicionar_contato(nome, telefone, email):
    conn = sqlite3.connect('agenda.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO contatos (nome, telefone, email) VALUES (?, ?, ?)', (nome, telefone, email))
    conn.commit()
    conn.close()

def listar_contatos():
    conn = sqlite3.connect('agenda.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id, nome, telefone, email FROM contatos')
    contatos = cursor.fetchall()
    conn.close()
    return contatos

def menu():
    criar_tabela()
    while True:
        print("\nMenu:")
        print("1. Adicionar contato")
        print("2. Listar contatos")
        print("3. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            nome = input("Nome: ")
            telefone = input("Telefone: ")
            email = input("Email: ")
            adicionar_contato(nome, telefone, email)
            print("Contato adicionado com sucesso!")
        elif escolha == '2':
            for c in listar_contatos():
                print(f"ID: {c[0]}, Nome: {c[1]}, Telefone: {c[2]}, Email: {c[3]}")
        elif escolha == '3':
            break

menu()