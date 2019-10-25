#Albert Valado Pujol
#Practica 4 - Ejercicio 4
#Pida al usuario tres números y un cuarto número, y compruebe si éste último es divisor de los tres números primeros.
a, b, c=list(map(int,input("Introduzca tres números distintos, separados por un espacio. \n").split()))
d=int(input("Introduzca un cuarto número para comprobar si es divisor de los tres anteriores4.\n"))
if (a%d==0):
    print(d, "es divisor de", a)
else:
    print(d, "no es divisor de", a)
if (b%d==0):
    print(d, "es divisor de", b)
else:
    print(d, "no es divisor de", b)
if (c%d==0):
    print(d, "es divisor de", c)
else:
    print(d, "no es divisor de", a)
input("Pulse Enter para cerrar el programa.")

    
