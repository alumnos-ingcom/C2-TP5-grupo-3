def esta_balanceado(texto, caracter='[]'):
    resultado = balanceo_interno(texto, caracter[0], caracter[1])
    if(resultado == 0):
        return True
    else:
        return False
    
def balanceo_interno(texto, caracter_open, caracter_close, i=0):
    #Si el string es vacio, retorno '0'
    if(texto == ""):
        return 0
    #Sino aumento 'i' y hago que 'j' valga lo que devuelva 'balanceo_interno' con el string sin su primer caracter
    i+=1
    j = balanceo_interno(texto[i:], caracter_open, caracter_close)
    #Ahora que está "volviendo" debo comparar lo que tenía respecto de lo que tengo en este momento en la primera posición del string
    
    #Logica interna:
    # +Solo hay 3 opciones para 'texto[0]':
    #    a) es el caracter de apertura == "apertura"
    #    b) es el caracter de cierre   == "cierre"
    #    c) es un caracter cualquiera  == "cualquiera"
    # +Y solo hay 3 opciones para 'j':
    #    1) es mayor a 0 == "aun puede ser balanceado"
    #    2) es menor a 0 == "ya no puede ser balanceado"
    #    3) es igual a 0 == "está balanceado"
    #
    # entonces:
    #  si tengo apertura y "está balanceado"       ==> devuelvo que "ya no puede balancearse esta apertura"                 ==> "j-1"
    #  si tengo apertura y "aun puede balancearse" ==> devuelvo que "gasté un cierre, esto se balancea o aun puedo hacerlo" ==> "j-1"
    #  si tengo cierre y "está balanceado"         ==> devuelvo que "hay un cierre pero aun podría balancearse"             ==> "j+1"
    #  si tengo cierre y "aun puede balancearse"   ==> devuelvo que "hay un cierre mas pero bueno aun podría balancearse"   ==> "j+1"
    #  si es un caracter cualquiera                ==> no afecta y devuelvo lo que tenía                                    ==> "j"
    #  si "ya no puede balancearse"                ==> devuelvo lo que tenía ("seguirá sin poder ser balanceado")           ==> "j"
    #
    
    if(texto[0] == caracter_open):
        if(j >= 0):
            return j-1
        else:
            return j
    if(texto[0] == caracter_close):
        if(j >= 0):
            return j+1
        else:
            return j
    return j
    


def prueba():
    texto = input("ingrese texto para analizar su balance: ")
    caracteres = input("ingrese los caracteres de apertura y cierre para usarlos en el balance: ")
    
    if(caracteres == ""):
        print(f" apertura: 'apertura_default' \n   cierre: 'cierre_default'")
        resultado = esta_balanceado(texto)#por defecto los caracteres son '[' y ']'
    else:
        print(f" apertura: '{caracteres[0]}' \n   cierre: '{caracteres[1]}'")
        resultado = esta_balanceado(texto, caracteres)
    
    if(resultado):
        print(f"{texto}\tOK")
    else:
        print(f"{texto}\tNO OK")
        
