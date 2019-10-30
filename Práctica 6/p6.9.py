#Albert Valado Pujol
#Práctica 6 - Ejercicio 9
#Escribe un programa que te pida nombres de personas y sus números de teléfono. Para terminar debe pulsar “S” cuando te pida el nombre.
#El programa termina escribiendo nombres y números de teléfono.

print("Este programa pide nombres y números de teléfono. Para terminar, introduzca S cuando le pida un nombre." )
#definimos variables
nom_tel=[]
lista_nombres=[]
lista_telefonos=[]
nombre=""
telefono=""

#pedimos la info
while nombre !="S":
    nombre=input("Deme un nombre.\n")
    telefono=input("Deme un número de teléfono.\n")
    lista_nombres.append(nombre)
    lista_telefonos.append(telefono)
    nom_tel.append(lista_nombres)
    nom_tel.append(lista_telefonos)

#recorremos e imprimimos dicha info
print("Estos son los nombres y números que me ha proporcionado:\n")
for i in range(len(nom_tel)):
    print("===============================================")
    print (nom_tel)
    
    
    
