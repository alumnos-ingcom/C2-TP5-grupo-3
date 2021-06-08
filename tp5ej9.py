################
# Martín René - @martinvilu
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from funciones_auxiliares import ingrese_numero

def factorial(numero):
    resultado = numero
    while (numero > 1):
        numero = numero -1
        resultado = resultado * numero
    return resultado

def factorion(numero):
    resultado = 0
    i = 0
    numero = str(numero)
    while(len(numero) > i):
        fact = factorial(int(numero[i]))
        resultado = fact + resultado
        i = i + 1
    return resultado

def factoriones(numero):
    lista = []
    while(numero > 0):
        if (factorion(numero)== numero):
            lista.append(numero)
        numero = numero -1
    return lista

def prueba():
    numero = ingrese_numero("Ingrese un número ")
    resultado = factoriones(numero)
    print (resultado)

if __name__ == "__main__":
    prueba()

