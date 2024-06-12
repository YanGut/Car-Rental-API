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
    while True:
        try:
            id_carro = int(input("ID do Carro: "))
            if id_carro > 0 and Carro.verificar_id_carro(id_carro):
                Carro.remover(id_carro)
                print("Carro removido com sucesso!")
                break
            print("ID do carro inválido ou não encontrado. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número válido.")

def editar_carro():
    while True:
        try:
            id_carro = int(input("ID do Carro: "))
            if id_carro > 0 and Carro.verificar_id_carro(id_carro):
                modelo, ano, preco, marca, cambio = obter_dados_carro()
                carro = Carro(id_carro, modelo, ano, preco, marca.id_marca, cambio.id_cambio)
                carro.atualizar()
                print("Carro editado com sucesso!")
            else:
                print("Nenhum carro encontrado com esse ID")
                print("Deseja tentar novamente: (s/n)")
                opcao = input()
                if opcao.lower() == "n":
                    break
                elif opcao.lower() == "s":
                    continue
                else:
                    print("Opção inválida. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número válido.")