class IngresoIncorrecto(Exception):
    """Esta es la Excepcion para el ingreso incorrecto"""
    pass

class FueraDeLimite(Exception):
    """Esta es la Excepcion para el ingreso incorrecto por salirse de los limites"""
    pass

def ingrese_numero(mensaje):
    ingresado = input(mensaje+":")
    try:
        entero = int(ingresado)
        return entero
    except ValueError as err:
        raise IngresoIncorrecto("el input no era un numero")

def ingrese_entero_reintento(mensaje, intentos=5):
    i = intentos
    while i > 0:
        try:
            entero = ingrese_numero(mensaje)
            return entero
        except IngresoIncorrecto:
            print("quedan "+str(i - 1)+" intentos")
            i -=1
    raise IngresoIncorrecto("el input no era un numero")

def ingreso_entero_restringido(mensaje, valor_minimo=0, valor_maximo=10):
    try:
        entero = ingrese_numero(mensaje)
        if(valor_minimo < entero and entero < valor_maximo):
            return entero
        else:
            raise FueraDeLimite("el input esta fuera de los limites establecidos")
    except IngresoIncorrecto:
        raise IngresoIncorrecto("el input no era un numero")

def modulo(numero):
    '''
    se aplica valor absoluto, tambien llamado modulo, a numero
    '''
    if(numero < 0):
        numero = -numero
    return numero
        
def es_palindromo(texto):
    inicio = 0
    fin = len(texto) -1
    contador = 0
    control = 0
    while ((texto[inicio] != texto[fin]) and (control != len(texto)-1)):
        if (texto[inicio] == texto[fin]):
            contador = contador +1
        inicio = inicio +1
        fin = fin -1
        control = control +1
    if (contador == control):
        return True
    else:
        return False
        
        
