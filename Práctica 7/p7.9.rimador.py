#Albert Valado Pujol
#Práctica 7 - Ejercicio 9

print("Este programa le pide dos palabras y comprueba si estas riman.")
palabra1=input("Introduzca la primera palabra.\n")
palabra2=input("Introduzca la segunda palabra.\n")

def Rimador(palabra1,palabra2):
    rimatotal1=palabra1[-3]
    rimatotal2=palabra2[-3]
    rimaparcial1=palabra1[-2]
    rimaparcial2=palabra2[-2]
    if rimatotal1==rimatotal2:
        solucion="Estas palabras riman."
    elif rimaparcial1==rimaparcial2 and rimatotal1 != rimatotal2:
        solucion="Estas palabras riman un poco."
    else:
        solucion="Estas palabras no riman nada."
    return print(solucion)

Rimador(palabra1,palabra2)
input()
    
   
    
