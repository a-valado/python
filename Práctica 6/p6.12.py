#Albert Valado Pujol
#Práctica 6 - Ejercicio 12

import random
import time
random.seed (time.time ())
minimo = int (input ( "Introduzca un valor mínimo:\n"))
maximo = int (input ( "Introduzca un valor máximo:\n"))
print("Ahora piense un número entre %d y %d. Yo, el ordenador trataré de adivinarlo. Para ayudarme en esta difícile tarea, responda mayor, menor o igual." %(minimo,maximo))
input("¿Ya lo tiene? Pulse Enter para empezar a jugar.")
numero= random.randint (minimo, maximo)
respuesta=0
contador=1
contador_trampa=0
if maximo<minimo:
    while not respuesta=="igual" or contador_trampa==2:
        respuesta=input("¿Es %d?\n" %(numero))
        if respuesta=="mayor":
            minimo=numero+1
            contador+=1
            numero= random.randint (minimo, maximo)
        elif respuesta=="menor":
            maximo=numero-1
            contador+=1
            numero= random.randint (minimo, maximo)
        elif repuesta=="mayor" and numero>maximo:
            print("¡Es usted un tramposo!")
            contador+=1
            contador_trampa+=1
        elif respuesta=="menor" and numero<minimo:
            print("¡Es usted un tramposo!")
            contador+=1
            contador_trampa+=1
else:
    print("No ha introducido los valores correctamente.")
if respuesta=="igual":
    print("Lo he logrado tras %d intentos. ¡Gracias por jugar!" %(contador))
elif contador_trampa==2:
    print("Es usted un sucio y despreciable humano tramposo. Ya no quiero jugar más.")
input()
