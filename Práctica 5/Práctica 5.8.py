#Albert Valado Pujol
#Práctica 5 - Ejercicio 7
#Escribe un programa que pida la anchura de un triángulo y lo dibuje de 
#la siguiente manera:
ancho=int(input("Introduce la anchura del triángulo.\n"))
for i in range(ancho):
	print("*"*i)
for j in range(ancho, 0, -1):
	print("*"*j)
input(" ")
