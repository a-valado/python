#Albert Valado Pujol
#Práctica 3 - Ejercicio 2
#Pida al usuario el espacio recorrido por un coche y el tiempo que ha tardado en horas y que calcule a qué velocidad media había realizado el recorrido.
tiempo=float(input("Introduzca el número de horas. \n"))
distancia=float(input("Ahora introduzca la distancia en kilómetros. \n"))
velocidad=float(distancia//tiempo)
print ("La velocidad es igual a %f kilómetros por hora." %(velocidad))
input ("Pulse una tecla para cerrar el programa.")
