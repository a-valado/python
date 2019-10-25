#Albert Valado
#Práctica 5 - Ejercicio 4
#Escribe un programa que pida un número y calcule su factorial.
a=int(input("Introduzca un número para calcular su factorial.\n"))
factorial=1
for i in range (1, a+1):
    factorial=i*factorial
print("El factorial de %d es %d." %(a, factorial))
input(" ")
