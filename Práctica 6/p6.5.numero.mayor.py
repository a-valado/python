#Albert Valado Pujol
#Práctica 6 - Ejercicio 5
#Escribe un programa que te pida números cada vez más grandes y que se guarden en una lista. Para acabar de escribir los números, escribe un número que no sea mayor que el anterior.
#El programa termina escribiendo la lista de números
num_1=int(input("Introduzca un número.\n"))
num_2=int(input("Introduzca un número mayor que %d. \n" %num_1))
lista=[]
while num_2>num_1:
    lista.append(num_1)
    num_1=num_2
    num_2=int(input("Escriba un número mayor que %d. (Para terminar, escriba un número menor.) \n" %num_2))
lista.append(num_1)
print("Los números que ha escrito son ")
for i in lista:
    print (i, end= " ")
input(" ")

