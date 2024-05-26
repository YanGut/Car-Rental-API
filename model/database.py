# model/database.py
import mysql.connector

def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="12345678",
        database="aluguel_de_carros"
    )


def criar_tabela(cursor, comando_sql):
    cursor.execute(comando_sql)

def criar_tabelas():
    comandos_sql = [
        """
        CREATE TABLE IF NOT EXISTS marca (
            id_marca INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(255) NOT NULL
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS cambio (
            id_cambio INT AUTO_INCREMENT PRIMARY KEY,
            tipo_cambio VARCHAR(255) NOT NULL
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS carro (
            id_carro INT AUTO_INCREMENT PRIMARY KEY,
            modelo VARCHAR(45) NOT NULL,
            ano INT NOT NULL,
            preco DECIMAL(10,2) NOT NULL,
            id_marca INT,
            id_cambio INT,
            FOREIGN KEY (id_marca) REFERENCES marca(id_marca),
            FOREIGN KEY (id_cambio) REFERENCES cambio(id_cambio)
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS usuario (
            id_usuario INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL,
            senha VARCHAR(255) NOT NULL,
            adm TINYINT DEFAULT 0
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS aluguel (
            id_aluguel INT AUTO_INCREMENT PRIMARY KEY,
            dt_inicio DATETIME NOT NULL,
            dt_fim DATETIME NOT NULL,
            valor_total DECIMAL(10,2) NOT NULL,
            id_usuario INT,
            id_carro INT,
            FOREIGN KEY (id_usuario) REFERENCES usuario(id_usuario),
            FOREIGN KEY (id_carro) REFERENCES carro(id_carro)
        )
        """
    ]

    conexao = conectar()
    cursor = conexao.cursor()

    list(map(lambda comando: criar_tabela(cursor, comando), comandos_sql))

    conexao.commit()
    cursor.close()
    conexao.close()
