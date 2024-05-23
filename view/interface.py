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


def limpar_console():
    os.system('cls')


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
        print("Ano inválido. Deve estar entre 1900 e 2100. Tente novamente.")

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
