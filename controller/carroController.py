# controller/carro_controller.py
from model.carro import Carro
from view.interfaceCarro import *

def cadastrar_carro():
    modelo, ano, preco, marca,  cambio = obter_dados_carro()
    carro = Carro(None, modelo, ano, preco, marca.id_marca, cambio.id_cambio)
    carro.salvar()
    print("Carro cadastrado com sucesso!")

def buscar_carro():
    marca, modelo = obter_dados_consulta()
    carro = Carro.buscar(modelo, marca)
    
    mostrar_carro(carro) if carro else print("Carro não encontrado.")
    
    while True:
        terminouDeVisualizar = input("Deseja voltar ao menu principal? (s/n) ")
        if terminouDeVisualizar.lower() == "s":
            break
        elif terminouDeVisualizar.lower() == "n":
            continue
        print("Opção inválida.")
    

def detalhar_carro(administrador):
    dados = obter_id_carro(administrador)
    if administrador:
        carro = Carro.buscar_carro_por_id_adm(dados)
        print(f"Detalhes do carro: {carro}") if carro else print("Carro não encontrado.")
    else:
        carro = Carro.bucar_carro_por_id_usuario(dados)
        print(f"Detalhes do carro: {carro}") if carro else print("Nenhum carro alugado.")
    
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