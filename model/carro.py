# model/carro.py
from .database import conectar


class Carro:
    def __init__(self, id_carro ,modelo, ano, preco, marca, cambio):
        self.id_carro = id_carro
        self.modelo = modelo
        self.ano = ano
        self.preco = preco
        self.marca = marca
        self.cambio = cambio
    
    def salvar(self):
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute("""
            INSERT INTO carro (modelo, ano, preco, id_marca, id_cambio)
            VALUES (%s, %s, %s, %s, %s)
        """, (self.modelo, self.ano, self.preco, self.marca, self.cambio))
        conexao.commit()
        cursor.close()
        conexao.close()

    def buscar(where = "1 = 1"):
        conexao = conectar()
        cursor = conexao.cursor(dictionary=True)
        cursor.execute("""
            SELECT 
                c.id_carro,
                c.modelo,
                c.ano,
                c.preco,
                m.nome AS marca,
                ca.tipo_cambio AS cambio
            FROM carro c
            JOIN marca m ON c.id_marca = m.id_marca
            JOIN cambio ca ON c.id_cambio = ca.id_cambio
            WHERE %s
        """, (where))
        carro = cursor.fetchone()
        cursor.close()
        conexao.close()
        return carro

    def remover(self):
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute("""
            DELETE FROM aluguel WHERE id_carro = %s
            
            DELETE FROM carro WHERE id_carro = %s
        """, (self.id_carro))
        conexao.commit()
        cursor.close()
        conexao.close()
    
    def atualizar(self):
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute("""
            UPDATE carro
            SET modelo = %s, ano = %s, preco = %s, id_marca = %s, id_cambio = %s
            WHERE id_carro = %s
        """, (self.modelo, self.ano, self.preco, self.marca, self.cambio, self.id_carro))

    def toString(self):
        return f"Modelo: {self.modelo}, Ano: {self.ano}, Preço: {self.preco}, Marca: {self.marca}, Câmbio: {self.cambio}"