#Albert Valado Pujol
#Práctica 6 - Ejercicio 6
#Escribe un programa que pida primero dos números (máximo y mínimo) y que después te pida números intermedios. Para terminar de escribir números, escribe un número que no esté comprendido entre los dos valores iniciales.
#El programa termina escribiendo la lista de números.
num_1=int(input("Introduzca un número. \n"))
num_2=int(input("Introduzca un número mayor que %d. \n" %(num_1)))
lista=[]
while num_1>num_2:
    num_2=int(input("%d no es mayor que %d. Por favor, escriba otro número.\n" %(num_2, num_1)))
medio=num_1+1
while medio>num_1 and medio<num_2:
   medio= int(input("Introduzca un número entre %d y %d. Para terminar, escriba un número fuera de ese rango.\n" %(num_1, num_2)))
   lista.append(medio)
del lista[-1]
print("Los números entre %d y %d que ha escrito son" %(num_1,num_2))
for i in lista:
    print (i, end= " ")
input(" ")
