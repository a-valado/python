#Albert Valado
#Práctica 5 - Ejercicio 3
#Escribe un programa que pida dos números
#y escriba la suma de enteros desde el primero hasta el último.
a=int(input("Introduzca un número.\n"))
b=int(input("Introduzca un número mayor que %d.\n" %(a)))
suma=0
for i in range(a,b+1):
    suma=i+suma       
print("La suma desde %d a %d es " %(a,b), suma)
input(" ")
