# main.py
from model.database import criar_tabelas
from view.interface import mostrar_menu_principal, mostrar_menu_administrador, mostrar_menu_usuario, limpar_console
from view.interfaceCarro import obter_dados_carro, obter_dados_consulta, mostrar_carro, mostrar_carros
from view.interfaceAluguel import mostrar_aluguel, obter_dados_aluguel, mostrar_alugueis
from view.interfaceUsuario import obter_dados_usuario, obter_dados_login, mostrar_usuarios
from view.interfaceCambio import obter_dados_cambio, mostrar_cambio
from view.interfaceMarca import obter_dados_marca, mostrar_marca
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
                if usuario[4] == 1:
                    menu_administrador()
                else:
                    menu_usuario(usuario)
        elif opcao == "2":
            cadastrar_usuario()
        elif opcao == "0":
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
