from Funciones_Auxiliares import ingrese_numero
from Funciones_Auxiliares import IngresoIncorrecto

def fibonacci(n):

    lista_fibonacci = []
    valor_actual = 1
    valor_anterior = 0
    
    for i in range(0, n):
        lista_fibonacci.append(valor_actual)
        aux = valor_actual
        valor_actual += valor_anterior
        valor_anterior = aux
        
    return lista_fibonacci
    
def prueba():
    numero = ingrese_numero("ingrese un numero entero positivo")
    if(numero < 0):
      raise IngresoIncorrecto("Has ingresado un numero negativo... se pidio lo siguiente: NUMERO ENTERO POSITIVO")
    resultados = fibonacci(numero)
    print(resultados)
    
if __name__ == "__main__":
    prueba()
