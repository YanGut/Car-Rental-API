# view/interface.py
import os
from utils.validacoes import (
    validar_email,
    validar_senha,
    validar_ano,
    validar_nome,
    validar_potencia,
    validar_marca_modelo,
    validar_combustivel
)

limpar_console = lambda: os.system('cls')

def mostrar_menu_principal():
    limpar_console()
    print("=== Sistema de Aluguel de Carros ===")
    print("1. Login")
    print("2. Cadastrar Usuário")
    print("0. Sair")

def mostrar_menu_administrador():
    limpar_console()
    print("=== Menu do Administrador ===")
    print("1. Cadastrar Carro")
    print("2. Buscar Carro")
    print("3. Visualizar Detalhes do Carro")
    print("4. Comparar Carros")
    print("5. Editar Carro")
    print("6. Excluir Carro")
    print("7. Cancelar Aluguel pelo Gerente")
    print("0. Logout")

# Interface Usuario
def mostrar_menu_usuario():
    limpar_console()
    print("=== Menu do Usuário ===")
    print("1. Buscar Carro")
    print("2. Visualizar Detalhes do Carro")
    print("3. Alugar Carro")
    print("4. Cancelar Aluguel")
    print("5. Editar Perfil")
    print("6. Excluir Conta")
    print("0. Logout")

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

# Interface Carro
def obter_dados_carro():
    limpar_console()
    while True:
        marca = input("Marca: ")
        if validar_marca_modelo(marca):
            break
        print("Marca inválida. Tente novamente.")
        
    while True:
        modelo = input("Modelo: ")
        if validar_marca_modelo(modelo):
            break
        print("Modelo inválido. Tente novamente.")
        
    while True:
        ano = int(input("Ano: "))
        if validar_ano(ano):
            break
        print("Ano inválido. Deve estar entre 1900 e 2025. Tente novamente.")
        
    while True:
        combustivel = input("Combustível (Gasolina, Álcool, Diesel, Flex): ")
        if validar_combustivel(combustivel):
            break
        print("Combustível inválido. Tente novamente.")
        
    while True:
        potencia = int(input("Potência: "))
        if validar_potencia(potencia):
            break
        print("Potência inválida. Deve ser maior que 0. Tente novamente.")
        
    return marca, modelo, ano, combustivel, potencia

def obter_dados_consulta():
    limpar_console()
    while True:
        marca = input("Marca: ")
        if validar_marca_modelo(marca):
            break
        print("Marca inválida. Tente novamente.")
        
    while True:
        modelo = input("Modelo: ")
        if validar_marca_modelo(modelo):
            break
        print("Modelo inválido. Tente novamente.")
        
    return marca, modelo

def mostrar_carro(carro):
    print("=== Carro ===")
    print(f"id: {carro['id']}")
    print(f"Marca: {carro['marca']}")
    print(f"Modelo: {carro['modelo']}")
    print(f"Ano: {carro['ano']}")
    print(f"Combustível: {carro['combustivel']}")
    print(f"Potência: {carro['potencia']}")
    print(f"Alugado: {'Sim' if carro['alugado'] else 'Não'}")

def mostrar_carros(carros):
    for carro in carros:
        print("=== Carro ===")
        print(f"id: {carro['id']}")
        print(f"Marca: {carro['marca']}")
        print(f"Modelo: {carro['modelo']}")
        print(f"Ano: {carro['ano']}")
        print(f"Combustível: {carro['combustivel']}")
        print(f"Potência: {carro['potencia']}")
        print(f"Alugado: {'Sim' if carro['alugado'] else 'Não'}")
        print("")

# Interface Aluguel
def mostrar_aluguel(aluguel):
    print("=== Aluguel ===")
    print(f"id: {aluguel['id']}")
    print(f"Carro: {aluguel['carro']}")
    print(f"Usuário: {aluguel['usuario']}")
    print(f"Data de Início: {aluguel['data_inicio']}")
    print(f"Data de Fim: {aluguel['data_fim']}")
    print(f"Valor: {aluguel['valor']}")
    
def obter_dados_aluguel():
    limpar_console()
    while True:
        id_carro = int(input("ID do Carro: "))
        if id_carro > 0:
            break
        print("ID inválido. Tente novamente.")
        
    while True:
        id_usuario = int(input("ID do Usuário: "))
        if id_usuario > 0:
            break
        print("ID inválido. Tente novamente.")
        
    data_inicio = input("Data de Início (yyyy-mm-dd): ")
    data_fim = input("Data de Fim (yyyy-mm-dd): ")
    
    return id_carro, id_usuario, data_inicio, data_fim

def mostrar_alugueis(alugueis):
    for aluguel in alugueis:
        print("=== Aluguel ===")
        print(f"id: {aluguel['id']}")
        print(f"Carro: {aluguel['carro']}")
        print(f"Usuário: {aluguel['usuario']}")
        print(f"Data de Início: {aluguel['data_inicio']}")
        print(f"Data de Fim: {aluguel['data_fim']}")
        print(f"Valor: {aluguel['valor']}")
        print("")


# Interface Cambio
def obter_dados_cambio():
    limpar_console()
    while True:
        cambio = input("Tipo de Câmbio: ")
        if validar_marca_modelo(cambio):
            break
        print("Tipo de Câmbio inválido. Tente novamente.")
        
    return cambio

def mostrar_cambio(cambio):
    print("=== Câmbio ===")
    print(f"id: {cambio['id']}")
    print(f"Tipo de Câmbio: {cambio['cambio']}")

# Interface Marca
def obter_dados_marca():
    limpar_console()
    while True:
        marca = input("Marca: ")
        if validar_marca_modelo(marca):
            break
        print("Marca inválida. Tente novamente.")
        
    return marca

def mostrar_marca(marca):
    print("=== Marca ===")
    print(f"id: {marca['id']}")
    print(f"Marca: {marca['marca']}")