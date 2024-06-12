import os
from utils.validacoes import *
from controller.marcaController import *
from controller.cambioController import *
from view.interfaceMarca import obter_dados_marca

limpar_console = lambda: os.system('cls')

# Interface Carro
def obter_dados_carro():
    limpar_console()
    
    marca = cadastrar_marca()
    
    print("marca, ", marca.id_marca)
        
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
        preco = input("Preco: ")
        if validar_preco(preco):
            break
        print("Preco inválido. Tente novamente.")
        
    cambio = cadastrar_cambio()
        
    return modelo, ano, preco, marca, cambio

def obter_dados_consulta():
    limpar_console()
    while True:
        print("Marcas disponíveis: Chevrolet, Ford, Fiat, Volkswagen, Renault, Toyota, Hyundai, Honda, Jeep, Nissan")
        marca = input("Marca: ")
        if validar_marca(marca):
            break
        print("Marca inválida. Tente novamente.")
        
    while True:
        modelo = input("Modelo: ")
        if validar_marca_modelo(modelo):
            break
        print("Modelo inválido. Tente novamente.")
        
    return marca, modelo

def obter_id_carro(administrador):
    limpar_console()
    while True:
        if administrador:
            id_carro = int(input("id_carro: "))
            if id_carro > 0:
                return id_carro
            print("id_carro inválido. Tente novamente.")
        else:
            id_usuario = int(input("id_usuario: "))
            if id_usuario > 0:
                return id_usuario
            print("id_usuario inválido. Tente novamente.")
        
    

def mostrar_carro(carro):
    print("=== Carro ===")
    print(f"id: {carro['id_carro']}")
    print(f"Marca: {carro['marca']}")
    print(f"Modelo: {carro['modelo']}")
    print(f"Ano: {carro['ano']}")
    print(f"Preco: {carro['preco']}")
    print(f"Cambio: {carro['cambio']}")

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