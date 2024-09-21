#Matriz ceros y unos
matriz=[]
fila=int(input("ingresa el numero de filas:"))
col=int(input("ingresa el numero de columnas: " ))
for i in range(fila):
    matriz.append([0]*col)
    for f in range(fila):
        for c in range(col):
            matriz[f][c]=int(input("ingrese el elemento: "))
print(matriz)
        