# controller/usuario_controller.py
from model.usuario import Usuario
from view.interface import obter_dados_usuario, obter_dados_login

def cadastrar_usuario():
    nome, email, senha = obter_dados_usuario()
    usuario = Usuario(nome, email, senha)
    usuario.salvar()
    print("Usuário cadastrado com sucesso!")

def login():
    email, senha = obter_dados_login()
    usuario = Usuario.autenticar(email, senha)
    if usuario:
        print(f"Bem-vindo, {usuario[1]}!")
        return usuario
    else:
        print("Email ou senha incorretos.")
        return None
