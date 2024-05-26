# utils/validacoes.py
import re

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

def validar_combustivel(combustivel):
    combustiveis_validos = ["Gasolina", "Álcool", "Diesel", "Flex"]
    return combustivel in combustiveis_validos