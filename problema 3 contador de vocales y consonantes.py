#contador de vocaales y consonantes
vocales=["a’, ’e’, ’i’, ’o’, ’u’, ’á’, ’é’, ’í’, ’ó’, ’ú’"]
consonantes=["b’, ’c’, ’d’, ’f’, ’g’, ’h’, ’j’, ’k’, ’l’, ’m’, ’n’, ’p’, ’q’, ’r’, ’s’, ’t’, ’v’, ’w’, ’x’, ’y’, ’z’ "]
contvocales=0
contconsonantes=0
texto=input("ingrese frase: " )
texto=texto.lower()
for letra in texto:
  if letra in vocales:
     contvocales= contvocales+1
  elif letra in consonantes:
     contconsonantes= consonantes+ 1
print("el texto tuvo: ", contvocales)
print("el texto tuvo: ", contconsonantes)
