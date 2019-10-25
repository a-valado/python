#Albert Valado Pujol
#Practica 4 - Ejercicio 1
#Pida al usuario 5 números y diga cual es el mayor y cuál el menor.
a, b, c, d, e=list(map(int,input("Introduzca cinco números distintos, separados por un espacio. \n").split()))
if (a>b)and(a>c)and(a>d)and(a>e):
    print (a, "es el mayor.")
elif (b>a)and(b>c)and(b>d)and(b>e):
    print (b, "es el mayor.")
elif (c>a)and(c>b)and(c>d)and(c>d):
    print(c, "es el mayor.")
elif (d>a)and(d>b)and(d>c)and(d>e):
    print (d, "es el mayor.")
elif (e>a)and(e>b)and(e>c)and(e>d):
    print(e, "es el mayor.")
else:
    print ("Todos los números son iguales, no hay mayor.")
if (a<b)and(a<c)and(a<d)and(a<e):
    print (a, "es el menor.")
elif (b<a)and(b<c)and(b<d)and(b<e):
    print (b, "es el menor.")
elif (c<a)and(c<b)and(c<d)and(c<e):
    print(c, "es el menor.")
elif (d<a)and(d<b)and(d<c)and(d<e):
    print (d, "es el menor.")
elif (e<a)and(e<b)and(e<c)and(e<d):
    print(e, "es el menor.")
else:
    print ("Todos los números son iguales, no hay menor.")
input("Pulse Enter para cerrar el programa.")



    
