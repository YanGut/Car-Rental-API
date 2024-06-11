# controller/login_controller.py
from view.interface import mostrar_menu_administrador, mostrar_menu_usuario, mostrar_menu_principal
from controller.carroController import cadastrar_carro, buscar_carro, detalhar_carro, comparar_carros, editar_carro, excluir_carro
from controller.aluguelController import excluir_aluguel, cadastrar_aluguel, mostrar_aluguel
from controller.usuarioController import editar_usuario, mostrar_usuario, excluir_usuario

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

def menu_usuario(usuario):
    while True:
        mostrar_menu_usuario(usuario)
        opcao = input("Selecione uma opção: ")
        
        if opcao == "0":
            break
        elif opcao == "1":
            buscar_carro()
        elif opcao == "2":
            detalhar_carro()
        elif opcao == "3":
            alugs = cadastrar_aluguel()
            mostrar_aluguel(alugs)
        elif opcao == "4":
            mostrar_aluguel()
            excluir_aluguel()
        elif opcao == "5":
            editar_usuario() 
        elif opcao == "6":
            certezaDeExclusaoDoUsuario = input("Tem certeza que deseja excluir sua conta? (s/n) ")
            if certezaDeExclusaoDoUsuario.lower() == "s":
                print("Usuário que será excluído:")
                excluir_usuario()
                break
        else:
            print("Opção inválida!")
