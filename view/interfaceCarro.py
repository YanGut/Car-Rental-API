import os
from utils.validacoes import *

limpar_console = lambda: os.system('cls')

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