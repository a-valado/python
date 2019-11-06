#Albert Valado Pujol
#Práctica 6 - Ejercicio 9
#Escribe un programa que te pida nombres de personas y sus números de teléfono. Para terminar debe pulsar “S” cuando te pida el nombre.
#El programa termina escribiendo nombres y números de teléfono.

print("Este programa pide nombres y números de teléfono. Para terminar, introduzca S cuando le pida un nombre." )
persona=[]
lista=[]
info_nom=()
info_num=()

#pedimos la info
while not info_nom =="S":
    info_nom=input("Introduzca un nombre")
    if info_nom !="S":
        info_num=input("Introduzca un número")
        persona.append(info_nom)
        persona.append(info_num)
        lista.append(persona)
        persona=[]


#recorremos e imprimimos dicha info
print("Estos son los nombres y números que me ha proporcionado:\n")
for i in range(len(lista)):
    print(" ")
    print("Este es el número", i)
    for j in range(len(lista[i])):
        print(lista[i][j])
input()
  
    
