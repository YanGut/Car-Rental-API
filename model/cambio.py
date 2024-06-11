#model/cambio.py
from .database import conectar

class Cambio:
    def __init__(self, tipo_cambio):
        self.id_cambio = None
        self.tipo_cambio = tipo_cambio

    def salvar(self):
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute("""
            INSERT INTO cambio (tipo_cambio)
            VALUES (%s)
        """, (self.tipo_cambio,))
        conexao.commit()
        self.id_cambio = cursor.lastrowid
        cursor.close()
        conexao.close()

    def buscar(where = "1 = 1"):
        conexao = conectar()
        cursor = conexao.cursor(dictionary=True)
        cursor.execute("""
            SELECT 
                id_cambio,
                tipo_cambio
            FROM cambio
            WHERE %s
        """, (where,))
        cambio = cursor.fetchone()
        cursor.close()
        conexao.close()
        return cambio

    def remover(self):
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute("""
            DELETE FROM aluguel WHERE id_carro IN (SELECT id_carro FROM carro WHERE id_cambio = %s)
            
            DELETE FROM carro WHERE id_cambio = %s
            
            DELETE FROM cambio WHERE id_cambio = %s
        """, (self.id_cambio,))
        conexao.commit()
        cursor.close()
        conexao.close()

    def atualizar(self):
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute("""
            UPDATE cambio
            SET tipo_cambio = %s
            WHERE id_cambio = %s
        """, (self.tipo_cambio, self.id_cambio))