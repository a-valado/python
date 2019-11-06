#Albert Valado Pujol
#Práctica 7 - Ejercicio 11
#Escribe un programa que te pida una frase,
#y pase la frase como parámetro a una función.
#Ésta debe devolver si es palíndroma o no,
#y el programa principal escribirá el resultado por pantalla:

print("Este programa determina si una frase es palíndroma o no.")
frase=input("Introduzca una frase.\n")

def Palindromo(frase):
    frase_junta=frase.replace(" ","")
    atnuj_esarf=frase_junta[::-1]
    if frase_junta==atnuj_esarf:
        solucion="es palíndroma."
    else:
        solucion="no es palíndroma."
    return print(frase.capitalize(), solucion)

Palindromo(frase)

input()
