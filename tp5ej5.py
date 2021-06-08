def inversion_minusculas_mayusculas(texto):
    '''
    intercambia las letras minusculas a mayusculas y viceversa 
    '''
    texto_auxiliar = ""
    longitud_texto = len(texto)
    for i in range(0 , longitud_texto):
        if(texto[i].isupper()):
            texto_auxiliar += texto[i].lower()
        else:
            texto_auxiliar += texto[i].upper()
    return texto_auxiliar
  
  
def prueba():
    texto = input("ingrese texto para modificar mayusculas y minusculas: ")
    texto_invertido = inversion_minusculas_mayusculas(texto)
    print(f"[{texto}] --> [{texto_invertido}]")

if __name__ == "__main__":
    prueba()
