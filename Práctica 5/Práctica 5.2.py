#Albert Valado Pujol
#Práctica 5 - Ejercicio 1
#Escribe un programa que pida dos números y escriba qué números entre ese par de números son pares y cuáles impares
a=int(input("Escriba un número.\n"))
b=int(input("Escriba un número mayor que %d.\n" %(a)))
for i in range(a,b+1):
    if (i%2==0):
        print("El número ", i, "es par.")
    else:
        print("El número ", i, "es impar.")
input(" ")
