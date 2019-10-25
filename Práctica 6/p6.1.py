#Albert Valado Pujol
#Práctica 6 - Ejercicio 1
#Escribe un programa que te pida palabras y las guarde en una lista. Para terminar de introducir palabras, simplemente pulsa Enter.
#El programa termina escribiendo la lista de palabras.

palabra=input("Escriba una palabra.\n")
lista=[]
while palabra !="":
    lista.append(palabra)
    palabra=input("Escriba una palabra o pulse Enter.\n")
print("Las palabras que has escrito son", lista)
input(" ")
