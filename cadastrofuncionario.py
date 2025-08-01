# Cadastro de Funcionário com SQlite + Python

import sqlite3

# Conectar ou criar o banco de dados
conexao = sqlite3.connect("sistema.db")
cursor = conexao.cursor()

# Criação da tabela se ela ainda não existir
cursor.execute("""
CREATE TABLE IF NOT EXISTS funcionarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    cpf TEXT NOT NULL UNIQUE,
    cargo TEXT,
    senha TEXT NOT NULL
)                              
""")
conexao.commit()

# Função para cadastrar um novo funcionário
def cadastro_funcionario():
    nome = input("Nome: ")
    cpf = input("CPF (somente numero): ")
    cargo = input("Cargo:")
    senha = input("Senha: ")

    try:
        cursor.execute("""
        INSERT INTO funcionarios (nome, cpf, cargo, senha)
        VALUES (?, ?, ?, ?)
        """, (nome, cpf, cargo, senha))
        conexao.commit()
        print("Funcionario cadastrado com sucesso!\n")
    except sqlite3.IntegrityError:
        print("CPF já cadastrado. Tente outro.\n")

# Função para listar todos os funcionários cadastrados
def lista_funcionarios():
    cursor.execute("SELECT id, nome, cpf, cargo FROM funcionarios")
    funcionarios = cursor.fetchall()

    if funcionarios:
        for f in funcionarios:
            print(f"ID: {f[0]}, NOME: {f[1]}, CPF: {f[2]}, Cargo: {f[3]}")
    else:
        print("Nenhum funcionario cadastrado.")

# Menu principal
def menu():
    while True:
     print("-" * 30)
     print("\n=== Sistema de Cadastro de Funcionário ===")
     print("1. Cadastrar Funcionário")
     print("2. Lista Funcionários")
     print("3. Sair.")
     print("-" * 30)

     opcao = input("Escolha: ")      

     if opcao == "1":
        cadastro_funcionario()
     elif opcao == "2":
        lista_funcionarios()
     elif opcao == "3":
        print("Sistema incerrado.")
        break  
     else:
         print("Opção invalida. Tente novamente.")
    
menu()

# Fecha conexão com banco de dados
conexao.close()