#model/aluguel.py
from .database import conectar

class Aluguel:
    def __init__(self, id_aluguel, id_carro, id_usuario, data_inicio, data_fim, valor_total):
        self.id_aluguel = id_aluguel
        self.id_carro = id_carro
        self.id_usuario = id_usuario
        self.data_inicio = data_inicio
        self.data_fim = data_fim
        self.valor_total = valor_total

    def salvar(self):
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute("""
            INSERT INTO aluguel (id_usuario, id_carro, dt_inicio, dt_fim, valor_total)
            VALUES (%s, %s, %s, %s, %s)
        """, (self.id_usuario, self.id_carro, self.data_inicio, self.data_fim, self.valor_total))
        conexao.commit()
        cursor.close()
        conexao.close()
    
    def buscaSimplificada(id_carro, id_usuario, data_inicio, data_fim, valor_total):
        conexao = conectar()
        cursor = conexao.cursor(dictionary=True)
        cursor.execute("""
            SELECT 
                id_aluguel,
                id_usuario,
                id_carro,
                dt_inicio,
                dt_fim,
                valor_total
            FROM aluguel
            WHERE id_carro = %s AND id_usuario = %s AND dt_inicio = %s AND dt_fim = %s AND valor_total = %s
        """, (id_carro, id_usuario, data_inicio, data_fim, valor_total))
        aluguel = cursor.fetchone()
        cursor.close()
        conexao.close()
        return aluguel
    
    def buscaAvancada(where = "1 = 1"):
        conexao = conectar()
        cursor = conexao.cursor(dictionary=True)
        cursor.execute("""
            SELECT 
                a.id_aluguel,
                a.id_usuario,
                a.id_carro,
                a.data_inicio,
                a.data_fim,
                u.nome AS usuario,
                c.modelo AS carro,
                m.nome AS marca,
                ca.tipo_cambio AS cambio
            FROM aluguel a
            JOIN usuario u ON a.id_usuario = u.id_usuario
            JOIN carro c ON a.id_carro = c.id_carro
            JOIN marca m ON c.id_marca = m.id_marca
            JOIN cambio ca ON c.id_cambio = ca.id_cambio
            WHERE %s
        """, (where,))
        aluguel = cursor.fetchone()
        cursor.close()
        conexao.close()
        return aluguel
    
    def remover(id_aluguel):
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute("""
            DELETE FROM aluguel WHERE id_aluguel = %s
        """, (id_aluguel,))
        conexao.commit()
        cursor.close()
        conexao.close()
    
    def atualizar(self):
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute("""
            UPDATE aluguel
            SET id_usuario = %s, id_carro = %s, data_inicio = %s, data_fim = %s
            WHERE id_aluguel = %s
        """, (self.id_usuario, self.id_carro, self.data_inicio, self.data_fim, self.id_aluguel))