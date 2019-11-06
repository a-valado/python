#Albert Valado Pujol
#Práctica 7 - Ejercicio 10
#Escribe un programa que te pida una palabra o número,
#pase por parámetro estos datos a una función,
#y ésta te diga si es o no palíndroma o capicúa.
#El programa principal imprimirá el resultado de la función:

print("Este programa determina si una palabra es palíndroma o si un número es capicua.")
palabra=input("Introduzca una palabra o un número.\n")

def palindromo(palabra):
    arbalap=palabra[::-1]
    if palabra==arbalap:
        solucion="es palíndroma o capicúa."
    else:
        solucion="no es palíndroma o capicúa."
    return print(palabra, solucion)

palindromo(palabra)

input()
