# controller/login_controller.py
from view.interface import mostrar_menu_administrador, mostrar_menu_usuario, mostrar_menu_principal
from controller.carroController import cadastrar_carro, buscar_carro, detalhar_carro, comparar_carros, editar_carro, excluir_carro
from controller.aluguelController import excluir_aluguel

def menu_administrador():
    while True:
        mostrar_menu_administrador()
        opcao = input("Selecione uma opção: ")
        
        if opcao == "0":
            break
        elif opcao == "1":
            cadastrar_carro()
        elif opcao == "2":
            buscar_carro()
        elif opcao == "3":
            detalhar_carro()
        elif opcao == "4":
            comparar_carros()
        elif opcao == "5":
            editar_carro()
        elif opcao == "6":
            excluir_carro()
        elif opcao == "7":
            excluir_aluguel()
        else:
            print("Opção inválida!")

def menu_usuario():
    while True:
        mostrar_menu_usuario()
        opcao = input("Selecione uma opção: ")
        
        if opcao == "0":
            break
        elif opcao == "1":
            buscar_carro()
        elif opcao == "2":
            detalhar_carro()
        elif opcao == "3":
            comparar_carros()
        else:
            print("Opção inválida!")
