################
# Martín René - @martinvilu
# UNRN Andina - Introducción a la Ingenieria en Computación
################


from funciones_auxiliares import ingrese_numero
from funciones_auxiliares import modulo

def distancia(num1, num2):
    num1 = modulo(num1)
    num2 = modulo(num2)
    resultado = num1 + num2
    return resultado
    
def prueba():
    num1 = ingrese_numero("Ingrese un numero: ")
    num2 = ingrese_numero("Ingrese otro numero: ")
    resultado = distancia(num1,num2)
    print ("La distancia entre ",num1, " y ", num2, " es:", resultado)

if __name__ == "__main__":
    prueba()

