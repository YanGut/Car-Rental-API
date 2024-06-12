# view/interface.py
import os
from utils.validacoes import *

limpar_console = lambda: os.system('clear')

def mostrar_menu_principal():
    limpar_console()    
    print("=== Sistema de Aluguel de Carros ===")
    print("1. Login")
    print("2. Cadastrar Usuário")
    print("0. Sair")

def mostrar_menu_administrador():
    limpar_console()  
    print("=== Menu do Administrador ===")
    print("1. Cadastrar Carro")
    print("2. Buscar Carro")
    print("3. Visualizar Detalhes do Carro")
    print("4. Comparar Carros")
    print("5. Editar Carro")
    print("6. Excluir Carro")
    print("7. Cancelar Aluguel pelo Gerente")
    print("0. Logout")

def mostrar_menu_usuario(usuario):
    limpar_console()
    print(f"=== Menu do Usuário ===\nUsuário: {usuario[4]}")
    print("=== Menu do Usuário ===")
    print("1. Buscar Carro")
    print("2. Visualizar Detalhes do Carro")
    print("3. Alugar Carro")
    print("4. Cancelar Aluguel")
    print("5. Editar Perfil")
    print("6. Excluir Conta")
    print("0. Logout")