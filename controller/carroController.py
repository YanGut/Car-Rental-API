# controller/carro_controller.py
from model.carro import Carro
from view.interfaceCarro import obter_dados_carro, obter_dados_consulta, mostrar_carro

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
    dados = obter_dados_consulta()
    where = dados if dados else "1 = 1"
    carro = Carro.buscar(where)
    
    return print(f"Detalhes do carro: {carro}") if carro else print("Carro não encontrado.")

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