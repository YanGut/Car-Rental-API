# controller/carro_controller.py
from model.carro import Carro
from view.interface import obter_dados_carro, obter_dados_consulta, mostrar_carro

def cadastrar_carro():
    marca, modelo, ano, combustivel, potencia = obter_dados_carro()
    carro = Carro(marca, modelo, ano, combustivel, potencia)
    carro.salvar()
    print("Carro cadastrado com sucesso!")

def buscar_carro():
    marca, modelo = obter_dados_consulta()
    carro = Carro.buscar(marca, modelo)
    if carro:
        mostrar_carro(carro)
    else:
        print("Carro não encontrado.")
def detalhar_carro():
    marca, modelo = obter_dados_consulta()
    carro = Carro.buscar(marca, modelo)
    if carro:
        print(f"Detalhes do carro: {carro}")
    else:
        print("Carro não encontrado.")

def comparar_carros():
    marca1, modelo1 = obter_dados_consulta()
    carro1 = Carro.buscar(marca1, modelo1)
    marca2, modelo2 = obter_dados_consulta()
    carro2 = Carro.buscar(marca2, modelo2)

    if carro1 and carro2:
        print(f"Comparação entre carros: {carro1} e {carro2}")
    else:
        print("Carro não encontrado.")

def excluir_carro():
    marca, modelo = obter_dados_consulta()
    carro = Carro.buscar(marca, modelo)
    if carro:
        carro.remover()
        print("Carro removido com sucesso!")
    else:
        print("Carro não encontrado.")

def alugar_carro():
    marca, modelo = obter_dados_consulta()
    carro = Carro.buscar(marca, modelo)
    if carro:
        carro.alugar()
        print(f"Carro alugado: {carro}")
    else:
        print("Carro não encontrado.")
def cancelar_aluguel():
    marca, modelo = obter_dados_consulta()
    carro = Carro.buscar(marca, modelo)
    if carro:
        carro.cancelar_aluguel()
        print(f"Aluguel cancelado: {carro}")

def editar_carro():
    marca, modelo = obter_dados_consulta()
    carro = Carro.buscar(marca, modelo)
    if carro:
        carro.remover()
        marca, modelo, ano, combustivel, potencia = obter_dados_carro()
        carro = Carro(marca, modelo, ano, combustivel, potencia)
        carro.salvar()
        print("Carro editado com sucesso!")
    else:
        print("Carro não encontrado.")