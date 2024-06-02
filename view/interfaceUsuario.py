import os
from utils.validacoes import *

limpar_console = lambda: os.system('cls')

# Interface Usuario
def obter_dados_usuario():
    limpar_console()
    while True:
        nome = input("Nome: ")
        if validar_nome(nome):
            break
        print("Nome inválido. Tente novamente.")
        
    while True:
        email = input("Email: ")
        if validar_email(email):
            break
        print("Email inválido. Tente novamente.")
        
    while True:
        senha = input("Senha: ")
        if validar_senha(senha):
            break
        print("Senha deve ter pelo menos 6 caracteres. Tente novamente.")
        
    return nome, email, senha

def obter_dados_login():
    limpar_console()
    while True:
        email = input("Email: ")
        if validar_email(email):
            break
        print("Email inválido. Tente novamente.")
        
    while True:
        senha = input("Senha: ")
        if validar_senha(senha):
            break
        print("Senha inválida. Tente novamente.")
        
    return email, senha

def mostrar_usuarios(usuarios):
    for usuario in usuarios:
        print("=== Usuário ===")
        print(f"id: {usuario['id']}")
        print(f"Nome: {usuario['nome']}")
        print(f"Email: {usuario['email']}")
        print(f"Administrador: {'Sim' if usuario['adm'] else 'Não'}")
        print("")