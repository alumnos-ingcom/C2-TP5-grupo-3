from Funciones_Auxiliares import ingrese_numero

def es_par(numero):
    '''
    recibe un numero entero positivo o negativo.
    retorna True si el numero es par.
    retorna False si el numero es impar.
    '''
    if(numero < 0):
        auxiliar = -numero
    else:
        auxiliar = numero
    
    while (auxiliar > 1):
        auxiliar -= 2
        
    if(auxiliar == 0):
        return True
    else:
        return False
    
def prueba():
    numero = ingrese_numero("ingrese un numero entero")
    valor = es_par(numero)
    if(valor):
        print(f"{numero} es PAR")
    else:
        print(f"{numero} es IMPAR")  
        
        
if __name__ == "__main__":
    prueba()
