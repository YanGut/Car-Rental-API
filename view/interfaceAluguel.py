import os
from utils.validacoes import *

limpar_console = lambda: os.system('cls')

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
    valor_total = float(input("Valor Total: "))
    
    return id_carro, id_usuario, data_inicio, data_fim, valor_total


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