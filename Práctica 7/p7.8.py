#Albert Valado Pujol
#Práctica 7 - Ejercicio 8
#Escribe un programa que pida una frase, y pase la frase como parámetro a una función que debe eliminar los espacios en blanco (compactar la frase).
#El programa principal imprimirá por pantalla el resultado final.

print("Este programa pide una frase y luego borra los espacios.")
frase=input("Escriba su frase. \n")

def borraEspacios(frase):
    frase_final=frase.replace(" ","")
    return frase_final

print(borraEspacios(frase))

input()
