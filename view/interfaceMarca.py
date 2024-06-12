import os
from utils.validacoes import *

# Interface Marca
def obter_dados_marca():
    while True:
        #Dicionário das marcas
        dic = {"Chevrolet", "Ford", "Fiat", "Volkswagen", "Renault", "Toyota", "Hyundai", "Honda", "Jeep", "Nissan"}
        print("Marcas disponíveis: ")
        list(map(print, dic))
        marca = input("Marca: ")
        if validar_marca(marca):
            break
        print("Marca inválida. Tente novamente.")
        
    return marca

def mostrar_marca(marca):
    print("=== Marca ===")
    print(f"id: {marca['id']}")
    print(f"Marca: {marca['marca']}")