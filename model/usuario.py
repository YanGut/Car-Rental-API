# model/usuario.py
from .database import conectar

class Usuario:
    def __init__(self, nome, email, senha, tipo="Usuario"):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.tipo = tipo

    def salvar(self):
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute("""
        INSERT INTO Usuario (nome, email, senha, tipo)
        VALUES (%s, %s, %s, %s)
        """, (self.nome, self.email, self.senha, self.tipo))
        conexao.commit()
        cursor.close()
        conexao.close()

    @staticmethod
    def autenticar(email, senha):
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute("""
        SELECT id, nome, tipo FROM Usuario WHERE email=%s AND senha=%s
        """, (email, senha))
        usuario = cursor.fetchone()
        cursor.close()
        conexao.close()
        return usuario
