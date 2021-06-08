################
# Martín René - @martinvilu
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from funciones_auxiliares import ingrese_numero
from funciones_auxiliares import es_palindromo

def es_capicua(numero):
    #Retorna TRUE si el número recibido por parametros es capicua
    numero = str(numero)
    return es_palindromo(numero)

def prueba():
    numero = ingrese_numero("Ingrese un número ")
    resultado = es_capicua(numero)
    if (resultado):
        print ("El número ingresado es capicúa")
    else:
        print ("El número ingresado no es capicúa") 

if __name__ == "__main__":
    prueba()

