#Albert Valado Pujol
#Práctica 6 - Ejercicio 8
#Escribe un programa que te pida primero un número y luego te pida números hasta que la suma de los números introducidos coincida con el número inicial.
#El programa termina escribiendo la lista de números.
limite=int(input("Introduzca el número límite que quiera. \n"))
num=int(input("Escriba un valor. \n"))
suma=num
lista=[]
while suma !=limite:
    lista.append(num)
    num=int(input("Introduzca otro valor para sumarlo al anterior. \n"))
    while suma+num>limite:
        num=int(input("%d es demasiado grande. Introduzca otro valor. \n" %(num)))
    suma=suma+num
lista.append(num)
print("El límite a alcanzar es %d. La lista es: " %(limite))
for i in lista:
      print (i, end= " ")
input(" ")

    
        
    
