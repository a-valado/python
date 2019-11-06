#Albert Valado Pujol
#Práctica 7 - Ejercico 12b
#Escribir un programa que lea una frase, y pase ésta como parámetro a una función
#que debe contar el número de palabras que contiene.
#Debe imprimir el programa principal el resultado.
#No se sabe cómo están separadas las palabras. Pueden estar separadas por más de un blanco o por signos de puntuación.

print("Este programa cuenta el número de palabras de una frase")
frase=input("Introduzca una frase.\n")
signos=[",",".",";",":","?","¿","!","¡"]

def cuentaPalabras(a):
    for i in a:
        if i in signos:
            frase_sin_signos=a.replace(i," ")
    lista=frase_sin_signos.strip(" ")
    numero=len(lista)
    return numero

print("La frase tiene", cuentaPalabras(frase)," palabras.")
input()
