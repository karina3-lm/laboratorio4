#eliminacion de espacios extras
from re import sub
cadena=input("ingrese texto: " )
patron=  " +"
resultado=sub(patron, " ",cadena)
 
print(resultado )
