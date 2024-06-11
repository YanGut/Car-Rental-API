# controller/usuario_controller.py
from model.usuario import Usuario
from view.interfaceUsuario import obter_dados_usuario, obter_dados_login

def cadastrar_usuario():
    nome, email, senha = obter_dados_usuario()
    usuario = Usuario(None, nome, email, senha)
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
    
def buscar_usuario():
    dados = obter_dados_usuario()
    where = dados if dados else "1 = 1"
    usuario = Usuario.buscar(where)
    
    return mostrar_usuario(usuario) if usuario else print("Usuário não encontrado.")

def excluir_usuario():
    where = obter_dados_usuario()
    usuario = Usuario.buscar(where)
    if usuario:
        Usuario.remover()
        print("Usuário removido com sucesso!")
    else:
        print("Usuário não encontrado.")
    
def editar_usuario():
    where = obter_dados_usuario()
    usuario = Usuario.buscar(where)
    if usuario:
        id_usuario, nome, email, senha = obter_dados_usuario()
        usuario = Usuario(id_usuario, nome, email, senha)
        usuario.atualizar()
        print("Usuário editado com sucesso!")
    else:
        print("Usuário não encontrado.")

def mostrar_usuario(usuario):
    print(f"Detalhes do usuário: {usuario.toString()}")

