#Albert Valado Pujol
#Practica 4 - Ejercicio 5
#Pida al usuario un importe en euros y diga si el cajero automático le puede dar dicho importe utilizando el mismo billete y el más grande (recuerda que el billete puede ser de 500, 200, 100, 50, 20, 10 y 5€).
importe=int(input("Por favor, introduzca el importe.\n"))
if (importe%500==0):
    print("Le da", (importe//500),"billete(s) de 500.")
elif (importe%200==0):
    print("Le da", (importe//200),"billete(s) de 200.")
elif (importe%100==0):
    print("Le da", (importe//100),"billete(s) de 100.")
elif (importe%50==0):
    print("Le da", (importe//50),"billete(s) de 50.")
elif (importe%20==0):
    print("Le da", (importe//20),"billete(s) de 20.")
elif (importe%10==0):
    print("Le da", (importe//10),"billete(s) de 10.")
elif (importe%5==0):
    print("Le da", (importe//10),"billete(s) de 5.")
else:
    print("El cajero no le puede dar el importe exacto en billetes.")
input(" ")
