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
    id_carro, id_usuario, data_inicio, data_fim, valor_total = obter_dados_aluguel()
    aluguel_dic = Aluguel.buscaSimplificada(id_carro, id_usuario, data_inicio, data_fim, valor_total)
    if aluguel_dic:
        # aluguel = Aluguel(
        #     aluguel_dic['id_aluguel'],
        #     aluguel_dic['id_carro'], 
        #     aluguel_dic['id_usuario'], 
        #     aluguel_dic['dt_inicio'],
        #     aluguel_dic['dt_fim'], 
        #     aluguel_dic['valor_total']
        # )
        # aluguel.remover()
        Aluguel.remover(aluguel_dic['id_aluguel'])

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