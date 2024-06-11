# controller/aluguelController.py
from model.aluguel import Aluguel
from view.interfaceAluguel import obter_dados_aluguel, mostrar_aluguel

def cadastrar_aluguel():
    id_carro, id_usuario, data_inicio, data_fim, valor_total = obter_dados_aluguel()
    aluguel = Aluguel(None, id_carro, id_usuario, data_inicio, data_fim, valor_total)
    aluguel.salvar()
    print("Aluguel cadastrado com sucesso!")
    return aluguel

def buscar_aluguel():
    dados = obter_dados_aluguel()
    where = dados if dados else "1 = 1"
    aluguel = Aluguel.buscar(where)
    
    return mostrar_aluguel(aluguel) if aluguel else print("Aluguel não encontrado.")

def excluir_aluguel():
    where = obter_dados_aluguel()
    aluguel = Aluguel.buscar(where)
    if aluguel:
        aluguel.remover()
        print("Aluguel removido com sucesso!")
    else:
        print("Aluguel não encontrado.")

def editar_aluguel():
    where = obter_dados_aluguel()
    aluguel = Aluguel.buscar(where)
    if aluguel:
        id_aluguel, id_carro, id_usuario, data_inicio, data_fim = obter_dados_aluguel()
        aluguel = Aluguel(id_aluguel, id_carro, id_usuario, data_inicio, data_fim)
        aluguel.atualizar()
        print("Aluguel editado com sucesso!")
    else:
        print("Aluguel não encontrado.")

def mostrar_aluguel(aluguel):
    print(f"Detalhes do aluguel: {aluguel}")