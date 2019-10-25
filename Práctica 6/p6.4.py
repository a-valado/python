#Albert Valado Pujol
#Práctica 6 - Ejercicio 4
#Escribe un programa que te pida dos números, de manera que el segundo sea mayor que el primero.
#El programa termina escribiendo los dos números tal y como se pide:
num_1=int(input("Escriba un número. \n"))
num_2=int(input("Escriba un número mayor que %d. \n" %(num_1)))
while num_1>num_2:
    num_2=int(input("%d no es mayor que %d. Escriba otro número. \n" %(num_2,num_1)))
print("Los números que ha introducido son %d y %d. \n" %(num_1, num_2))
