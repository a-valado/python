#Albert Valado Pujol
#Práctica 7 - Ejercicio 6
#Escribe un programa que lea el nombre de una persona y un carácter,
#le pase estos datos a una función que comprobará si dicho carácter está en su nombre.
#El resultado de dicha función lo imprimirá el programa principal por pantalla.

print("Este programa determina el número de veces que un caracter está en un nombre.")
nombre=input("Introduzca un nombre. \n")
caracter=input("Introduzca un carácter. \n")

def contador(nombre):
    resultado=nombre.count(caracter)
    return resultado
print("El carácter %s aparece" %(caracter),contador(nombre),"veces.")
input()
