import os
from utils.validacoes import *

limpar_console = lambda: os.system('cls')

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