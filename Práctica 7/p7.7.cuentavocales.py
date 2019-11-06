#Albert Valado Pujol
#Práctica 7 - Ejercicio 7
#Escribe un programa que lea una frase,
#y la pase como parámetro a un procedimiento. El procedimiento contará el número de vocales (de cada una) que aparecen,
#y lo imprimirá por pantalla.

print("Este programa cuenta el número de vocales de una frase")
frase=input("Escriba la frase.\n")

def contadorAbascal(frase):
    resultado_a=frase.count("a")+frase.count("á")+frase.count("A")+frase.count("Á")
    resultado_e=frase.count("e")+frase.count("é")+frase.count("E")+frase.count("É")
    resultado_i=frase.count("i")+frase.count("í")+frase.count("I")+frase.count("Í")
    resultado_o=frase.count("o")+frase.count("ó")+frase.count("O")+frase.count("Ó")
    resultado_u=frase.count("u")+frase.count("ú")+frase.count("U")+frase.count("Ú")
    print("A:",resultado_a," E:",resultado_e," I:", resultado_i," O:", resultado_o, " U:", resultado_u)

contadorAbascal(frase)

input()
