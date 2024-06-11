# model/marca.py
from .database import conectar

class Marca:
    def __init__(self, nome):
        self.id_marca = None
        self.nome = nome

    def salvar(self):
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute("""
            INSERT INTO marca (nome)
            VALUES (%s)
        """, (self.nome,))
        conexao.commit()
        cursor.close()
        conexao.close()

    def buscar(where = "1 = 1"):
        conexao = conectar()
        cursor = conexao.cursor(dictionary=True)
        cursor.execute("""
            SELECT 
                id_marca,
                nome
            FROM marca
            WHERE %s
        """, (where,))
        marca = cursor.fetchone()
        cursor.close()
        conexao.close()
        return marca

    def remover(self):
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute("""
            DELETE FROM aluguel WHERE id_carro IN (SELECT id_carro FROM carro WHERE id_marca = %s)
            
            DELETE FROM carro WHERE id_marca = %s
            
            DELETE FROM marca WHERE id_marca = %s
        """, (self.id_marca,))
        conexao.commit()
        cursor.close()
        conexao.close()

    def atualizar(self):
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute("""
            UPDATE marca
            SET nome = %s
            WHERE id_marca = %s
        """, (self.nome, self.id_marca))
    
    def toString(self):
        return f"Marca: {self.nome}"