# utils/validacoes.py
import re
from datetime import datetime

def validar_email(email):
    padrao = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(padrao, email) is not None

def validar_senha(senha):
    return len(senha) >= 6

def validar_ano(ano):
    return 1900 <= ano <= 2100

def validar_nome(nome):
    return len(nome.strip()) > 0

def validar_potencia(potencia):
    return potencia > 0

def validar_marca_modelo(valor):
    return len(valor.strip()) > 0

#Dicionario e List Comprehension
validar_marca = lambda marca: marca in {marca for marca in [
    "Chevrolet",
    "Ford",
    "Fiat",
    "Volkswagen",
    "Renault",
    "Toyota",
    "Hyundai",
    "Honda",
    "Jeep",
    "Nissan"
]}

def validar_combustivel(combustivel):
    combustiveis_validos = ["Gasolina", "Álcool", "Diesel", "Flex"]
    return combustivel in combustiveis_validos

def validar_cambio(cambio):
    cambios_validos = ["Manual", "Automático"]
    return cambio in cambios_validos

def validar_preco(preco):
    return preco.isdigit() and float(preco) > 0

def validar_data(data):
    padrao = r'^\d{4}-\d{2}-\d{2}$'
    if not re.match(padrao, data):
        return False
    try:
        datetime.strptime(data, '%Y-%m-%d')
        return True
    except ValueError:
        return False

#Monad
def validar_id_carro(id_carro):
    return id_carro.isdigit() and int(id_carro) > 0
