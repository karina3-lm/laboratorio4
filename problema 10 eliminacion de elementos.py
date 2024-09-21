#eliminacion de elementos
lista=[2,3,4,5,6,7,8,9,22,23,24,]
i=0
for i in lista:
    if i%2==0:
        lista.remove(i)

print(lista)
