#Albert Valado Pujol
#Práctica 3 - Ejercicio 7
#Pida al usuario tres números que serán el día, mes y año. Comprueba que la fecha introducida es válida.
dia=int(input("Introduzca el día.\n"))
mes=int(input("Introduzca el mes.\n"))
año=int(input("Introduzca el año.\n"))
if(dia>=1)and(dia<=31)and(mes<=12):
    if(mes==2)and(dia>29):
        print ("Fecha no válida.")
    elif(mes==4 or mes==6 or mes==9 or mes==11)and(dia>30):
        print("Fecha no válida.")
    else:
        print (dia, "/", mes, "/" , año, "es una fecha válida.")
else:
    print ("Fecha no válida.")
input("Pulse ENTER para cerrar el programa.")
