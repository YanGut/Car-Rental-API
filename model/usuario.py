# model/usuario.py
from .database import conectar

class Usuario:
    def __init__(self, id_usuario, nome, email, senha, adm = False):
        self.id_usuario = id_usuario
        self.nome = nome
        self.email = email
        self.senha = senha
        self.adm = adm

    def salvar(self):
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute("""
            INSERT INTO usuario (nome, email, senha, adm)
            VALUES (%s, %s, %s, %s)
        """, (self.nome, self.email, self.senha, self.adm))
        conexao.commit()
        cursor.close()
        conexao.close()
    
    def buscar(nome, email, senha):
        conexao = conectar()
        cursor = conexao.cursor(dictionary=True)
        cursor.execute("""
            SELECT 
                id_usuario,
                nome,
                email,
                senha,
                adm
            FROM usuario
            WHERE nome = %s AND email = %s AND senha = %s
        """, (nome, email, senha))
        usuario = cursor.fetchone()
        cursor.close()
        conexao.close()
        return usuario
    
    def remover(self):
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute("""
            DELETE FROM aluguel WHERE id_usuario = %s
            
            DELETE FROM usuario WHERE id_usuario = %s
        """, (self.id_usuario))
        conexao.commit()
        cursor.close()
        conexao.close()
    
    def atualizar(self):
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute("""
            UPDATE usuario
            SET nome = %s, email = %s, senha = %s, adm = %s
            WHERE id_usuario = %s
        """, (self.nome, self.email, self.senha, self.adm, self.id_usuario))
        conexao.commit()
        cursor.close()
        conexao.close()
    
    @staticmethod
    def autenticar(email, senha):
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute("""
            SELECT 
                id_usuario,
                nome,
                email,
                senha,
                adm
            FROM usuario u
            WHERE email=%s AND senha=%s
        """, (email, senha))
        usuario = cursor.fetchone()
        cursor.close()
        conexao.close()
        return usuario
    
    def toString(self):
        return f"Nome: {self.nome}, Email: {self.email}, Adm: {self.adm}"
