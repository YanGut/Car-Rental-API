# controller/login_controller.py
from view.interface import mostrar_menu_administrador, mostrar_menu_usuario, mostrar_menu_principal
from controller.carroController import cadastrar_carro, buscar_carro, detalhar_carro, comparar_carros, editar_carro, excluir_carro, cancelar_aluguel

def menu_administrador():
    while True:
        mostrar_menu_administrador()
        opcao = input("Selecione uma opção: ")
        switcher = {
            "1": cadastrar_carro,
            "2": buscar_carro,
            "3": detalhar_carro,
            "4": comparar_carros,
            "5": editar_carro,
            "6": excluir_carro,
            "7": cancelar_aluguel,
            "0": lambda : "break"
        }
        func = switcher.get(opcao, lambda: print("Opção inválida!"))
        result = func()
        if result == "break":
            break
def menu_usuario():
    while True:
        mostrar_menu_usuario()
        opcao = input("Selecione uma opção: ")
        if opcao == "0":
            break
        else:
            print("Opção inválida!")
