#Albert Valado Pujol
#Práctica 7 - Ejercicio 3
#Escribe un programa que lea una frase, y la pase como parámetro a un procedimiento,
#y éste debe mostrar la frase con un carácter en cada línea.

print("Este programa lee una frase y la devuelve por carácteres.")
frase=input("Escriba la frase.\n")

def troceaFrase(frase):
    for i in range(len(frase)):
        print (frase[i])

troceaFrase(frase)

input()
