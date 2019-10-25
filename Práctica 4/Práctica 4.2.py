#Albert Valado Pujol
#Práctica 4 - Ejercicio 2
#Pida al usuario 5 números y diga si estos estaban en orden decreciente, creciente o desordenados.
a=int(input("Introduzca el primer número.\n"))
b=int(input("Introduzca el segundo número.\n"))
c=int(input("Introduzca el tercer número.\n"))
d=int(input("Introduzca el cuarto número.\n"))
e=int(input("Introduzca el quinto número.\n"))
if(a>b>c>d>e):
    print("Están en orden decreciente.")
elif(a<b<c<d<e):
    print("Están en orden creciente.")
else:
    print("Están desordenados.")
input("Pulse Enter para cerrar el programa.")
