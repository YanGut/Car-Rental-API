import os
from utils.validacoes import *

limpar_console = lambda: os.system('cls')

# Interface Cambio
def obter_dados_cambio():
    while True:
        cambio = input("Câmbio (Manual, Automático): ")
        if validar_cambio(cambio):
            break
        print("Tipo de Câmbio inválido. Tente novamente.")
        
    return cambio

def mostrar_cambio(cambio):
    print("=== Câmbio ===")
    print(f"id: {cambio['id']}")
    print(f"Tipo de Câmbio: {cambio['cambio']}")