#Albert Valado Pujol
#Práctica 4 - Ejercicio 3
#Pida al usuario si quiere calcular el área de un triángulo o un cuadrado, y pida los datos según que caso y muestre el resultado.
calculadora=input("Introduzca triangulo para comenzar a calcular su área, o cuadrado para hacer lo propio con este polígono.\n")
triangulo="triangulo"
cuadrado="cuadrado"
if(calculadora==triangulo):
    altura=float(input("Introduzca la altura del triángulo.\n"))
    base=float(input("Introdizca la base del triángulo.\n"))
    area_tri=base*altura//2
    print("El área del triángulo es %f." %(area_tri))
elif(calculadora==cuadrado):
    lado=float(input("Introduzca el lado del cuadrado.\n"))
    area_cua=lado*lado
    print("El área del cuadrado es %f." %(area_cua))
else:
    print("Por favor, escriba triangulo o cuadrado. Este programa solo calcula áreas de triángulos o cuadrados, no de %s" %(calculadora))
input("Pulsa Enter para cerrar el programa.")
