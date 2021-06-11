from funciones_auxiliares import ingrese_numero
from funciones_auxiliares import IngresoIncorrecto

def mover_abecedario(N):
    '''
    A partir de un parametro N, se retorna un String con un abecedario inglés en minusculas (no incluye la 'ñ') desplazado N espacios.
    -si N < 0 ==> en la posicion de una letra se encontrará la letra N espacios a la izquierda de esta.
    -si N > 0 ==> en la posicion de una letra se encontrará la letra N espacios a la derecha de esta.
    '''
    #creo un String que contendrá el abecedario movido N espacios
    abecedario_movido = ""
    
    #valores de los ASCII utiles para los for que siguen  
    a = ord('a')
    z = ord('z') + 1
    letras = z - a
    
    if(N >= 0):
        #el valor N quedará acotado entre 0 y 25
        N = N % letras
        #agrego al abecedario desde la N-esima letra hasta la 'z'. 
        for i in range(a + N , z):
            abecedario_movido += chr(i)
        #agrego al abecedario desde la 'a' hasta la N-esima letra. 
        for i in range(a , a + N):
            abecedario_movido += chr(i)
    else:
        #el valor N quedará acotado entre -25 y 0
        N = N % -letras
        #agrego al abecedario desde la N-esima letra hasta la 'z'.
        for i in range(z + N, z):
            abecedario_movido += chr(i)
        #agrego al abecedario desde la 'a' hasta la N-esima letra.
        for i in range(a , z + N):
            abecedario_movido += chr(i)
            
    return abecedario_movido
    


def cifrar_cesar(texto, N):
    '''
    A partir de un parametro texto y otro N, se retorna un String con el contenido de 'texto' desplazado N espacios.
    -si N < 0 ==> "desplazamiento a la izquierda": una letra se transforma en la letra N espacios a la derecha de esta.
    -si N > 0 ==> "desplazamiento a la derecha"  : una letra se transforma en la letra N espacios a la izquierda de esta.
    '''
    
    #el abecedario esta en minusculas
    abecedario = mover_abecedario(N)
    
    #creo un String vacio para cargar el mensaje codificado
    modificado = ""
    
    for i in texto:
        #si es una letra...
        if(i.isalpha()):
            #si es mayuscula ==> agrego la letra del abecedario modificado convertida en mayuscula
            if(i.isupper()):
                modificado += abecedario[ord(i) - ord('A')].upper()
            #si es minuscula ==> agrego la letra del abecedario modificado
            else:
                modificado += abecedario[ord(i) - ord('a')]
        #si no es una letra ==> se agrega
        else:
            modificado += i

    return modificado
    

def descifrar_cesar(texto, N):
    '''
    A partir de un parametro texto y otro N, se retorna un String con el contenido de 'texto' desplazado N espacios.
    -si N < 0 ==> "desplazamiento a la izquierda": una letra se transforma en la letra N espacios a la derecha de esta.
    -si N > 0 ==> "desplazamiento a la derecha"  : una letra se transforma en la letra N espacios a la izquierda de esta.
    '''
    return cifrar_cesar(texto, -N)

def prueba():
    texto_original = input("ingrese texto para codificar: ")
    corrimiento_codigo_cesar = ingrese_numero("ingrese numero para codificar y decodificar")
    
    print("-"*42)
    print("\t...Codificando Mensaje...")
    texto_codificado = cifrar_cesar(texto_original , corrimiento_codigo_cesar)
    print(f"MENSAJE CODIFICADO: [{texto_codificado}]")
    
    print("-"*42)
    
    print("\t...Decodificando Mensaje...")
    texto_decodificado = descifrar_cesar(texto_codificado , corrimiento_codigo_cesar)
    print(f"MENSAJE DECODIFICADO: [{texto_decodificado}]")
    print("-"*42)
    
if __name__ == "__main__":
    prueba()
