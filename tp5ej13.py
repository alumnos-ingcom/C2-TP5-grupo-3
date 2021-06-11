class ElementoNoEncontrado(Exception):
    """Esta es la Excepcion para cuando no se encuentra un elemento"""
    pass
        
def encuentra(texto1, texto2):
    texto2_primer_caracter = texto2[0]
    texto1_longitud = len(texto1)
    texto2_longitud = len(texto2)
    for i in range(0 , texto1_longitud):
        if(texto1[i] == texto2_primer_caracter):
            if(texto1[i:i + texto2_longitud] == texto2):
                return i
    raise ElementoNoEncontrado()



def prueba():
    texto1 = input("ingrese texto: ")
    texto2 = input("ingrese palabra a buscar: ")
    try:
        posicion = encuentra(texto1 , texto2)
        print(f"[{texto2}] se encuentra en la posicion [{posicion}] del texto [{texto1}]")
    except ElementoNoEncontrado:
        raise ElementoNoEncontrado(f"No se ha encontrado [{b}] en [{a}]")
 
if __name__ == "__main__":
    prueba()
