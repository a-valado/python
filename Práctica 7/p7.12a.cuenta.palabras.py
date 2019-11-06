#Albert Valado Pujol
#Práctica 7 - Ejercico 12a
#Escribir un programa que lea una frase,
#y pase ésta como parámetro a una función que debe contar el número de palabras que contiene.
#Debe imprimir el programa principal el resultado.
#Asumir que cada palabra está separada por un solo blanco:

print("Este programa cuenta el número de palabras de una frase.")
frase=input("Introduzca la frase.\n")

def cuentaPalabras(a):
    lista=a.split(" ")
    numero=len(lista)
    return numero

print("La frase tiene", cuentaPalabras(frase)," palabras.")
input()
