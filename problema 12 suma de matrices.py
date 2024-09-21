#suma de matices
matrizA=[[3,2,4],
         [3,4,5],
         [3,5,6]]
matrizB=[[1,2,3],
         [4,5,6],
         [3,4,5]]
matriz_r=[]
for m in range (len(matrizA)):
    nueva_m=[]
    for columna in range (len(matrizA[0])):
        nueva_m.append(matrizA[m][columna] + matrizB[m][columna])
    matriz_r.append(nueva_m)
for m in range (len(matrizA)):
 print(matriz_r)