from funciones_auxiliares import ingrese_numero
from funciones_auxiliares import IngresoIncorrecto

def fibonacci(n):

    #Lo que esta comentado se puede aplicar si quiero devolver una LISTA con la sequencia de fibonacci de los primeros n-esimo numeros
    
    #lista_fibonacci = []
    valor_actual = 1
    valor_anterior = 0
    
    for i in range(0, n):
        #lista_fibonacci.append(valor_actual)
        auxiliar = valor_actual
        valor_actual += valor_anterior
        valor_anterior = auxiliar
        
    return valor_actual #return lista_fibonacci
    
def prueba():
    numero = ingrese_numero("ingrese un numero entero positivo")
    if(numero < 0):
      raise IngresoIncorrecto("Has ingresado un numero negativo... se pidio lo siguiente: NUMERO ENTERO POSITIVO")
    resultados = fibonacci(numero)
    print(resultados)
    
if __name__ == "__main__":
    prueba()
