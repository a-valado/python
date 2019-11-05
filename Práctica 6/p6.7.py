#Albert Valado Pujol
#Práctica 6 - Ejercicio 7
#Escribe un programa que pida un número (límite) y luego te pida números hasta que la suma de los números introducidos supere el límite inicial.
#El programa termina escribiendo la lista de números.
limite=int(input("Introduzca el número límite que quiera. \n"))
num=int(input("Escriba un valor. \n"))
suma=num
lista=[]
while suma<limite:
    lista.append(num)
    num=int(input("Escriba otro valor. \n"))
    suma=suma+num
lista.append(num)    
print("El límite a superar era %d. La lista creada es: " %(limite), end=" ")
for i in lista:
    print(i, end=" ")
print(". Ya que la suma total de los valores es %d." %(suma))
input(" ")

