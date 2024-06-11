# controller/cambioController.py
from model.cambio import Cambio
from view.interfaceCambio import obter_dados_cambio, mostrar_cambio

def cadastrar_cambio():
    tipo = obter_dados_cambio()
    cambio = Cambio(tipo)
    cambio.salvar()
    return cambio

def buscar_cambio():
    dados = obter_dados_cambio()
    where = dados if dados else "1 = 1"
    cambio = Cambio.buscar(where)
    
    return mostrar_cambio(cambio) if cambio else print("Câmbio não encontrado.")

def excluir_cambio():
    where = obter_dados_cambio()
    cambio = Cambio.buscar(where)
    if cambio:
        cambio.remover()
        print("Câmbio removido com sucesso!")
    else:
        print("Câmbio não encontrado.")

def editar_cambio():
    where = obter_dados_cambio()
    cambio = Cambio.buscar(where)
    if cambio:
        id_cambio, tipo = obter_dados_cambio()
        cambio = Cambio(id_cambio, tipo)
        cambio.atualizar()
        print("Câmbio editado com sucesso!")
    else:
        print("Câmbio não encontrado.")

def mostrar_cambio(cambio):
    print(f"Detalhes do câmbio: {cambio.toString()}")