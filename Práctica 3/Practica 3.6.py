#Albert Valado Pujol
#Practica 3 - Ejercicio 6
#Pida al usuario el precio de un producto y el nombre del producto y muestre el mensaje con el precio del IVA (21%). Por ejemplo: “ Tu bicicleta vale 100 euros y con el 21 % de IVA se queda en 121 euros en total”.
nombre=input("Introduzca su producto.\n")
precio=float(input("Introduzca el precio de dicho producto.\n"))
iva= precio*21/100
precio_total= precio+iva
print("Su(s)", nombre, "vale", precio, "euros y con el 21 por ciento de IVA se queda en", precio_total, "euros en total.")
input("Pulse ENTER para cerrar el programa.")
             
