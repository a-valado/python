#Albert Valado Pujol
#Practica 3 - Ejercicio 5
#Pida un número que como máximo tenga tres cifras (por ejemplo serían válidos 1, 99 i 213 pero no 1001). Si el usuario introduce un número de más de tres cifras debe un informar con un mensaje de error como este “ ERROR: El número 1005 tiene más de tres cifras”.
num=int(input("Introduzca un número de tres cifras.\n"))
if (num>=1000):
    print ("ERROR. %d tiene más de tres cifras." %(num))
else:
    print ("Yup. Tal y como pensaba, %d es un número de tres o menos cifras." %(num))
input("Pulse ENTER para cerrar el programa.")
