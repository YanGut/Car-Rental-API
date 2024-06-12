# view/interface.py
import os
from utils.validacoes import *

limpar_console = lambda: os.system('cls')

def mostrar_menu_principal():
    limpar_console()    
    print("=== Sistema de Aluguel de Carros ===")
    print("1. Login")
    print("2. Cadastrar Usuário")
    print("0. Sair")

def mostrar_menu_administrador():
    limpar_console()  
    print("=== Menu do Administrador ===")

    menu_items = [
        "Cadastrar Carro",
        "Buscar Carro",
        "Visualizar Detalhes do Carro",
        "Editar Carro",
        "Excluir Carro",
        "Cancelar Aluguel pelo Gerente",
        "Logout"
    ]

    # Lambda recursiva
    print_menu_items = (lambda f: (lambda items, index=0: f(f, items, index)))(
        lambda self, items, index: (
            print(f"{index + 1}. {items[index]}")
            if index < len(items) else None,
            self(self, items, index + 1) if index < len(items) else None
        )
    )
    
    # Chamar a lambda para imprimir os itens do menu
    print_menu_items(menu_items)

def mostrar_menu_usuario(usuario):
    limpar_console()
    print(f"=== Menu do Usuário ===\nUsuário: {usuario[4]}")
    print("1. Buscar Carro")
    print("2. Visualizar Detalhes do Carro")
    print("3. Alugar Carro")
    print("4. Cancelar Aluguel")
    print("5. Editar Perfil")
    print("6. Excluir Conta")
    print("0. Logout")