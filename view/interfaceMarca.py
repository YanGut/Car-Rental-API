import os
from utils.validacoes import *

# Interface Marca
def obter_dados_marca():
    while True:
        dic = ["Chevrolet", "Ford", "Fiat", "Volkswagen", "Renault", "Toyota", "Hyundai", "Honda", "Jeep", "Nissan"]
        print(dic.map(lambda x: f"{dic.index(x)} - {x}"))
        marca = input("Marca: ")
        if validar_marca(marca):
            break
        print("Marca inválida. Tente novamente.")
        
    return marca

def mostrar_marca(marca):
    print("=== Marca ===")
    print(f"id: {marca['id']}")
    print(f"Marca: {marca['marca']}")