################
# Martín René - @martinvilu
# UNRN Andina - Introducción a la Ingenieria en Computación
################



from funciones_auxiliares import ingrese_numero
from funciones_auxiliares import crear_lista

def comparar_listas(lista1, lista2):
    '''Recibe dos listas y retorna True si
    si contienen los mismos elementos que pueden estar estén ubicados
    en diferentes posiciones.'''
    
    contador = 0
    
    for i in range (len(lista1)):
        for n in range (len(lista2)):
            if (lista1[i] == lista2[n]):
                contador = contador +1
    return (contador == len(lista1))
        
def prueba():
    print("      LISTA 1       ")
    lista1 = crear_lista(5)
    print("      LISTA 2       ")
    lista2= crear_lista(5)
    resultado = comparar_listas(lista1, lista2)
    if (resultado):
        print ("Las listas tienen los mismos elementos")
    else:
        print ("Las listas tienen elementos diferentes")

if __name__ == "__main__":
    prueba()

