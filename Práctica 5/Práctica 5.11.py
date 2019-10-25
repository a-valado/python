#Albert Valado Pujol
#Práctica 5 - Ejercicio 11
#Escribe un programa que pida un número e imprima todos sus divisores.
num=int(input("Introduzca un número para conocer sus divisores.\n"))
print("Los divisores de %d son: " %(num))
for i in range(1,num+1):
	if (num%i==0):
		print(i,end=" ")
input(" ")
