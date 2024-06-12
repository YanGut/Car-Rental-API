import os
from model.carro import Carro
from model.usuario import Usuario
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
    
def obter_dados_aluguel(limpar = True):
    if limpar:
        limpar_console()
    while True:
        try:
            id_carro = int(input("ID do Carro: "))
            if id_carro > 0 and Carro.verificar_id_carro(id_carro):
                break
            print("ID do carro inválido ou não encontrado. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número válido.")
        
    while True:
        try:
            id_usuario = int(input("ID do Usuário: "))
            if id_usuario > 0 and Usuario.verificar_id_usuario(id_usuario) :
                break
            print("ID do usuário inválido ou não encontrado. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número válido.")

    while True:
        data_inicio = input("Data de Início (yyyy-mm-dd): ")
        if validar_data(data_inicio):
            data_inicio_dt = datetime.strptime(data_inicio, '%Y-%m-%d')
            break
        print("Data inválida. Tente novamente.")
        
    while True:
        data_fim = input("Data de Fim (yyyy-mm-dd): ")
        if validar_data(data_fim):
            data_fim_dt = datetime.strptime(data_fim, '%Y-%m-%d')
            if data_fim_dt > data_inicio_dt:
                break
            print("Data de fim deve ser posterior à data de início.")
        print("Data inválida. Tente novamente.")
    
    if not Carro.verificar_disponibilidade_carro(id_carro, data_inicio, data_fim):
        print("O carro já está alugado nesse período. Tente novamente.")
        return obter_dados_aluguel(False)
    
    while True:
        try:
            valor_total = float(input("Valor Total: "))
            if valor_total > 0:
                break
            print("Valor inválido. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número válido.")
    
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