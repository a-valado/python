#Albert Valado Pujol
#Práctica 6 - Ejercicio 3
#Escribe un programa que pida notas y los guarde en una lista. Para terminar de introducir notas, escribe una nota que no esté entre 0 y 10.
#El programa termina escribiendo la lista de notas.

num=float(input("Escriba una nota entre 0 y 10.\n"))
lista=[]
while num>0 and num<10:
    lista.append(num)
    num=" " 
    num=float(input("Introduzca otra nota.\n"))
print("Las notas que has escrito son ", lista)
