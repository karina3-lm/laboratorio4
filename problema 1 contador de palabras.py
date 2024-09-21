#contador de palabras 
def contador_de_palabras(texto):
    texto_limpio=texto.replace("," , "")
    palabras=texto_limpio.split()
    cantidad_de_palabras=len(palabras)
    return cantidad_de_palabras
texto_ingresado=input("ingrese el texto para contar las palabras: " )
resultado=contador_de_palabras(texto_ingresado)
print("la cantidad de palabras en el texto es: ", resultado)
