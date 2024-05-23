# main.py
from model.database import criar_tabelas
from view.interface import mostrar_menu_principal, limpar_console
from controller.usuarioController import cadastrar_usuario, login
from controller.loginController import menu_administrador, menu_usuario

def main():
    criar_tabelas()
    while True:
        mostrar_menu_principal()
        opcao = input("Selecione uma opção: ")
        if opcao == "1":
            usuario = login()
            if usuario:
                if usuario[2] == "Administrador":
                    menu_administrador()

                else:
                    menu_usuario()
        elif opcao == "2":
            cadastrar_usuario()
        elif opcao == "0":
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
