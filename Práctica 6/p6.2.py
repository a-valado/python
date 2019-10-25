#Albert Valado Pujol
#Práctica 6.2
#Escribe un programa que te pida números y los guarde en una lista. Para terminar de introducir número, simplemente escribe “Salir”.
#El programa termina escribiendo la lista de números.

num=int(input("Introduzca un número.\n"))
lista=[]
while num != "Salir":
    lista.append(num)
    num=input("Introduzca otro número o escriba Salir.\n")
#El programa funciona, queda pendiente averiguar la forma de que si le pones otra cosa que no sea un número
#sea capaz de reconocerlo como tal.
print("Los números que ha escrito son", lista)
input(" ")
