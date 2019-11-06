#Albert Valado Pujol
#Práctica 7 - Ejercicio 1
#Escribe un programa que pida un texto por pantalla, este texto lo pase como parámetro a un procedimiento,
#y éste lo imprima primero todo en minúsculas y luego todo en mayúsculas.

texto=input("Escriba algo, por favor. El programa se lo imprimirá en mayúsculas y en minúsculas.\n")

def cambialetras(texto):
    print (texto.lower())
    print (texto.upper())

cambialetras(texto)

input()
