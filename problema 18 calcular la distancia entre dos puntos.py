#calcular la distancia entre dos puntos
from math import sqrt
x1=float(input("ingrese los valores de x1: " ))
y1=float(input("ingrese los valores de y1: " ))
x2=float(input("ingrese los valores de x2: " ))
y2=float(input("ingrese los valores de y2: " ))
distancia=sqrt((x2-x1)**2+ (y2-y1)**2)
print(distancia)

### distancia entre dos puntos
A=[4,6]
B=[3,5]
cA=(B[0]-A[0])**2
cB=(B[1]-A[1])**2
distancia=sqrt(cA+cB)
print("la distancia es :", distancia )

