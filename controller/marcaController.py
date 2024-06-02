# controller/marcaController.py
from model.marca import Marca
from view.interfaceMarca import obter_dados_marca, mostrar_marca

def cadastrar_marca():
    nome = obter_dados_marca()
    marca = Marca(None, nome)
    marca.salvar()
    print("Marca cadastrada com sucesso!")

def buscar_marca():
    dados = obter_dados_marca()
    where = dados if dados else "1 = 1"
    marca = Marca.buscar(where)
    
    return mostrar_marca(marca) if marca else print("Marca não encontrada.")

def excluir_marca():
    where = obter_dados_marca()
    marca = Marca.buscar(where)
    if marca:
        marca.remover()
        print("Marca removida com sucesso!")
    else:
        print("Marca não encontrada.")

def editar_marca():
    where = obter_dados_marca()
    marca = Marca.buscar(where)
    if marca:
        id_marca, nome = obter_dados_marca()
        marca = Marca(id_marca, nome)
        marca.atualizar()
        print("Marca editada com sucesso!")
    else:
        print("Marca não encontrada.")

def mostrar_marca(marca):
    print(f"Detalhes da marca: {marca.toString()}")