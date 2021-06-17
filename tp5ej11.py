################
# Martín René - @martinvilu
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from funciones_auxiliares import ingrese_numero
from funciones_auxiliares import crear_lista


def promedio_movil(lista, n):
    lista_promedios = []

    for i in range(len(lista)-(n)):
        suma = 0
        for j in range (0,n):
            suma = lista[i+j] + suma
            print (suma)
        promedio = suma / n
        lista_promedios.append(promedio)
        promedio = 0
        
    return lista_promedios

def prueba():
    cantidad = int(input("Ingrese la cantidad de datos a cargar en la lista: "))
    print ("Ingrese los datos de la lista: ")
    lista = crear_lista(cantidad)
    n = int (input("Ingrese la cantidad de datos a incluir en el promedio: "))
    lista_promedios = promedio_movil(lista,n)
    print ("La lista de promedios moviles es: ", lista_promedios)

if __name__ == "__main__":
    prueba()

