from funciones_auxiliares import ingrese_numero
from funciones_auxiliares import IngresoIncorrecto

def binario(decimal):
    binario = ''
    while (decimal // 2 !=0):

        binario = str(decimal % 2) + binario
        decimal = decimal // 2
        
    return str(decimal) + binario

def prueba():
    numero = ingrese_numero("Ingrese el número a conevrtir: ")
    resultado = binario(numero)
    print(resultado)
    
if __name__ == "__main__":
    prueba()
