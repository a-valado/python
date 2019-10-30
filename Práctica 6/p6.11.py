#Albert Valado Pujol
#Práctica 6 - Ejercicio 11
import random
import time

random.seed (time.time ())
print("El ordenador va a pensar un número. Trate de adivinarlo.\n")
minimo = int (input ( "Introduzca un valor mínimo:\n"))
maximo = int (input ( "Introduzca un valor máximo:\n"))
secreto = random.randint (minimo, maximo)
respuesta=int(input("El número a adivinar está entre %d y %d. Escriba un número.\n" %(minimo, maximo)))
contador=1

while not respuesta == secreto:
    if respuesta>secreto and respuesta<maximo:
       respuesta=int(input("¡Demasiado grande! Vuélvalo a intentar.\n"))
       contador+=1
        
    elif respuesta<secreto and respuesta>minimo:
        respuesta=int(input("¡Demasiado pequeño! Vuélvalo a intentar.\n"))
        contador+=1

    else:
        print("Le recuerdo que el número a adivinar está entre %d y %d. Escriba un número entre esos dos.\n" %(minimo, maximo))
        respuesta=int(input("Vuélvalo a intentar.\n"))
        contador+=1

print("¡Correcto! Lo ha adivinado y tan sólo ha necesitado %d intentos." %(contador))

    
