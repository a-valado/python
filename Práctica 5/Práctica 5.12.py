#Albert Valado Pujol
#Práctica 5 - Ejercicio 6
#Escribe un programa que pida un número y escriba si primo o no
num=int(input("Escriba un número del que quiera saber si es primo o no.\n"))
solucion="Es primo."
for i in range (2,num):
    if num%i==0:
        solucion="No es primo."
        break
print(solucion)
input(" ")
