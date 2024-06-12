# controller/carro_controller.py
from model.carro import Carro
from view.interfaceCarro import *

def cadastrar_carro():
    modelo, ano, preco, marca,  cambio = obter_dados_carro()
    carro = Carro(None, modelo, ano, preco, marca.id_marca, cambio.id_cambio)
    carro.salvar()
    print("Carro cadastrado com sucesso!")

def buscar_carro():
    dados = obter_dados_consulta()
    where = dados if dados else "1 = 1"
    carro = Carro.buscar(where)
    
    return mostrar_carro(carro) if carro else print("Carro não encontrado.")

def detalhar_carro():
    dados = obter_id_carro()
    carro = Carro.buscar_carro_por_id(dados)
    
    print(f"Detalhes do carro: {carro}") if carro else print("Carro não encontrado.")
    
    while True:
        terminouDeVisualizar = input("Deseja voltar ao menu principal? (s/n) ")
        if terminouDeVisualizar.lower() == "s":
            break
        elif terminouDeVisualizar.lower() == "n":
            continue
        print("Opção inválida.")

def comparar_carros():
    dados = obter_dados_consulta()
    where = dados if dados else "1 = 1"
    carro = Carro.buscar(where)
    
    return print(f"Comparação entre carros:\n {carro[0]} \n {carro[1]}") if carro else print("Carro não encontrado.")

def excluir_carro():
    where = obter_dados_consulta()
    carro = Carro.buscar(where)
    if carro:
        carro.remover()
        print("Carro removido com sucesso!")
    else:
        print("Carro não encontrado.")

def editar_carro():
    where = obter_dados_consulta()
    carro = Carro.buscar(where)
    if carro:
        id_carro, modelo, ano, preco, marca,  cambio = obter_dados_carro()
        carro = Carro(id_carro, modelo, ano, preco, marca, cambio)
        carro.atualizar()
        print("Carro editado com sucesso!")
    else:
        print("Carro não encontrado.")