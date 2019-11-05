#Albert Valado Pujol
#Práctica 7 - Ejercicio 5
#Escribe un programa que te pida una frase y una vocal,
#y pase estos datos como parámetro a una función que se encargará
#de cambiar todas las vocales de la frase por la vocal seleccionada.
#Devolverá la función la frase modificada, y el programa principal la imprimirá:

print("Este programa lee una frase y cambia todas las vocales por la vocal que usted quiera.")
frase=input("Escriba la frase.\n")
vocal=input("Escriba la vocal.\n")

if vocal=="a" or vocal=="e" or vocal=="i" or vocal=="o" or vocal=="u":
    def cambiaVocales(frase):
        frase=frase.lower()
        frase_nueva=frase.replace("a", vocal)
        frase_nueva=frase_nueva.replace("e", vocal)
        frase_nueva=frase_nueva.replace("i", vocal)
        frase_nueva=frase_nueva.replace("o", vocal)
        frase_nueva=frase_nueva.replace("u", vocal)
        frase_nueva=frase_nueva.capitalize()
        return frase_nueva
print(cambiaVocales(frase))
        
