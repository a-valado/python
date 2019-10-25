#Albert Valado Pujol
#Practica 4 - Ejercicio 1
#Pida al usuario 5 números y diga cual es el mayor y cuál el menor.
a, b, c, d, e=list(map(int,input("Introduzca cinco números distintos, separados por un espacio. \n").split()))
mayor=a
menor=a
if b>mayor:
    mayor=b
if c>mayor:
    mayor=c
if d>mayor:
    mayor=d
if e>mayor:
    mayor=e
print(mayor, "es el mayor.\n")
if b<menor:
    b=menor
if c<menor:
    menor=c
if d<menor:
    menor=d
if e<menor:
    menor=e
print(menor, "es el menor.\n")
    
    
