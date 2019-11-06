#Albert Valado Pujol
#Práctica 7 - Ejercicio 4
#Escribe un programa que pida una frase, y le pase como parámetro a una función dicha frase.
#La función debe sustituir todos los espacios en blanco de una frase por un asterisco,
#y devolver el resultado para que el programa principal la imprima por pantalla.

print("Este programa lee una frase y la devuelve cambiando los espacios por asteriscos.")
frase=input("Escriba la frase.\n")

def estrellaEspacios(frase):
   frase_nueva=frase.replace(" ","*")
   return print(frase_nueva)

estrellaEspacios(frase)

input()
