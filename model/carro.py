# model/carro.py
from .database import conectar


class Carro:
    def __init__(self, marca, modelo, ano, combustivel, potencia, alugado=False):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.combustivel = combustivel
        self.potencia = potencia
        self.alugado = alugado
    def salvar(self):
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute("""
        INSERT INTO Carro (marca, modelo, ano, combustivel, potencia)
        VALUES (%s, %s, %s, %s, %s)
        """, (self.marca, self.modelo, self.ano, self.combustivel, self.potencia))
        conexao.commit()
        cursor.close()
        conexao.close()

    def buscar(marca, modelo):
        conexao = conectar()
        cursor = conexao.cursor(dictionary=True)
        cursor.execute("""
        SELECT * FROM Carro WHERE marca = %s AND modelo = %s
        """, (marca, modelo))
        carro = cursor.fetchone()
        cursor.close()
        conexao.close()
        return carro

    def removar(self):
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute("""
        DELETE FROM Carro WHERE marca = %s AND modelo = %s
        """, (self.marca, self.modelo))
        conexao.commit()
        cursor.close()
        conexao.close()

    def alugar(self):
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute("""
        UPDATE Carro SET alugado = 1 WHERE marca = %s AND modelo = %s
        """, (self.marca, self.modelo))
        conexao.commit()
        cursor.close()
        conexao.close()

    def cancelar_aluguel(self):
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute("""
        UPDATE Carro SET alugado = 0 WHERE marca = %s AND modelo = %s
        """, (self.marca, self.modelo))
        conexao.commit()
        cursor.close()
        conexao.close()

    def listar_todos_carros(self):
        conexao = conectar()
        cursor = conexao.cursor(dictionary=True)
        cursor.execute("""
        SELECT * FROM Carro
        """)
        carros = cursor.fetchall()
        cursor.close()
        conexao.close()
        return carros

    def toString(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}, Combustível: {self.combustivel}, Potência: {self.potencia}"