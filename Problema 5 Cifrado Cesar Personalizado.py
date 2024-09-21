#Cifrado Cesar Personalizado
resultado=""
frase=input("ingrese frase: " )
for caracter in frase:
    if caracter.isalpha()==True:
        valor=ord(caracter)
        valor+=3
        if valor>=123:
            valor-=26
        valor=chr(valor)
    else:
        valor+=caracter
    resultado+=valor
print(resultado)
