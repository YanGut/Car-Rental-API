import os
from utils.validacoes import *

limpar_console = lambda: os.system('cls')

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