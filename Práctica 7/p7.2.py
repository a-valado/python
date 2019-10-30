#Albert Valado Pujol
#Práctica 7 - Ejercicio 2
#Escribe un programa que lea el nombre y los dos apellidos de una persona (en tres cadenas de caracteres diferentes),
#los pase como parámetros a una función, y ésta debe unirlos y devolver una única cadena.
#La cadena final la imprimirá el programa por pantalla.

print("Este programa imprime el nombre y los apellidos.")
nombre=input("Introduzca un nombre.\n")
apellido_1=input("Introduzca el primer apellido.\n")
apellido_2=input("Introduzca el segundo apellido.\n")

def juntaNombre(nombre, apellido_1, apellido_2):
    final=nombre+" "+apellido_1+" "+apellido_2
    return final

print(juntaNombre(nombre, apellido_1, apellido_2))

input()


