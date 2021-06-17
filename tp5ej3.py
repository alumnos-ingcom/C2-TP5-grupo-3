from funciones_auxiliares import ingrese_numero
from funciones_auxiliares import IngresoIncorrecto

def tribonacci(n):
    lista = []
    lista.append(0)
    lista.append(0)
    lista.append(1)
    
    for i in range(0, n):

        numero = (lista[i] + lista[i +1] + lista[i+2])
        lista.append(numero)
        
    return lista 
    
def prueba():
    numero = 0
    while(numero < 3):
      numero = ingrese_numero("Ingrese la cantidad de números que desea listar, debe ser mayor a 3: ")
    resultados = tribonacci(numero)
    print(resultados)
    
if __name__ == "__main__":
    prueba()
