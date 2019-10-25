#Albert Valado Pujol
#Práctica 5 - Ejercicio 9
#Escribe un programa que pida la anchura y la altura de un rectángulo
#y lo dibuje de la siguiente manera:
altura=int(input("Introduce la altura del rectángulo.\n"))
ancho=int(input("Introduce el ancho del rectángulo.\n"))
for i in range(1,altura+1):
    if i==1:
        print("*"*ancho)
    elif i==altura:
        print("*"*ancho)
    else:
        print("*"+(" "*(ancho-2))+"*")
input("")
