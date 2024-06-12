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

    def buscar(where):
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
    
    def buscar_carro_por_id(id_carro):
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
            WHERE c.id_carro = %s
        """, (id_carro,))
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
    
    def verificar_id_carro(id_carro):
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute("SELECT 1 FROM carro WHERE id_carro = %s", (id_carro,))
        carro = cursor.fetchone()
        cursor.close()
        conexao.close()
        return carro is not None
    
    def verificar_disponibilidade_carro(id_carro, data_inicio, data_fim):
        conexao = conectar()
        cursor = conexao.cursor()
        query = """
            SELECT 1 
            FROM aluguel 
            WHERE id_carro = %s 
            AND (dt_inicio <= %s AND dt_fim >= %s)
        """
        cursor.execute(query, (id_carro, data_fim, data_inicio))
        resultado = cursor.fetchall()
        cursor.close()
        conexao.close()
        return len(resultado) == 0