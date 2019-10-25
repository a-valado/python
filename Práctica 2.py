#Albert Valado Pujol - Práctica 2 - Introducción a Python
#Ejercicio 1 - Calcular el área de un triángulo
print ("Vamos a calcular el área de un triángulo.\n")
base= int(input("Introduce la base.\n"))
altura= int(input ("Introduce la altura.\n"))
area= int(base*altura)/2
print ("El área del triangulo es %d." %(area))
input (" ")

#Ejercicio 2 - Convertir grados centígrados en Fahrenheit
print ("Ahora vamos a convertir grados centígrados en Fahrenheit.\n")
grados_c= float(input("Introduce la temperatura en grados centígrados.\n"))
grados_f= float(grados_c*(9/5)+32)
print ("Son %f grados Fahrenheit." %(grados_f))
input (" ")

#Ejercicio 3 - Determinar si un número es par o impar
print ("A continuación, determinaremos si un número es par o impar.\n")
numero= int(input("Introduce un número.\n"))
if (numero%2==0):
    print ("\nEl número es par.")
else:
    print ("\nEl número es impar.")
input (" ")

#Ejercicio 4 - Determinar el mayor de dos números
print ("Finalmente, comprobaremos cuál es el mayor de dos números.\n")
num_1= int(input("Introduce el primer número.\n"))
num_2= int(input("Introduce el segundo número.\n"))
if (num_1>num_2):
    print ("\n %d es mayor." %(num_1))
elif (num_2>num_1):
    print ("\n %d es mayor." %(num_2))
else:
    print ("\n Son iguales.")
