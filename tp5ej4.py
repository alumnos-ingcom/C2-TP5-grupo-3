from funciones_auxiliares import ingrese_numero
from funciones_auxiliares import IngresoIncorrecto


def es_num_perfecto(numero):
    contador=0
    for i in range(1,numero):
        if(numero%i == 0):
            contador+=i
    return contador==numero


def prueba():
    numero = ingrese_numero("ingrese un numero positivo")
    respuesta = es_num_perfecto(numero)
    if(respuesta):
        print(f"el numero {numero} ES PERFECTO")
    else:
        print(f"el numero {numero} NO ES PERFECTO")

if __name__ == "__main__":
    prueba()
