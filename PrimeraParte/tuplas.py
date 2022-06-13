# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 10:03:44 2022

@author: wilfr
"""

#%% 1
# Crea una tupla con numeros, pide un numero por teclado e indica cuantas veces se repite

tupla1 = (65,67,5,67,34,76,67,231,98,67)

num = int(input("Escriba un numero por teclado"))

a = tupla1.count(num)

#%% 2
# Crea una tupla con valores ya predefinidos del 1 al 10, pide un indice por teclado y muestra
# los valores de la tupla

tupla2 = (1,2,3,4,5,6,7,8,9,10)
print(tupla2)


#%% 3
# Escribir un programa que permita procesar datos de pasajeros de viaje en una lista de tuplas con
# la sigueinte forma: (nombre, dni, destino)
# Ejm [("Manuel Juares", 19823451, "Liverpool")]

pasajeros = [
    ("Manuel Juares", 123, "Liverpool"),
    ("Manuela Suarez", 159, "Manchester"),
    ("Maria Muarez", 741, "Leeds")
]

for nombre, dni, destino in pasajeros:
    print(f"{nombre} con dni {dni} va al destino {destino}")
# Ademas, en otra lista de tuplas se almacenan los datos de cada ciudad y el pais al que pertenecen
# Ejm [("Buenos Aires", "Argentina")]

datos_ciudad = [
    ("Buenos Aires", "Argentina"),
    ("Liverpool", "Inglaterra"),
    ("Manchester", "Inglaterra"),
    ("Leeds", "Inglaterra")
]

# Hacer un programa que permita al usuario realizar las siguientes operaciones:
# -Agregar pasajeros a la lista de viajeros
# -Agregar ciudades a la lista de ciudades
# -Dado el DNI de un pasajero, emitir a que ciudad y pais viaja
# -Salir del programa

print("1. Agregar pasajeros a la lista de viajeros")
print("2. Agregar ciudades a la lista de ciudades")
print("3. Dado el DNI de un pasajero, emitir a que ciudad y pais viaja")
print("4. Salir del programa")

opcion = int(input(f"Seleccione una opcion: "))

while(opcion != 4):
    
    if(opcion == 1):
        print("Ingrese pasajero: ")
        nombre = input("Ingrese nombre: ")
        dni = input("Ingrese DNI: ")
        destino = input("Ingrese destino: ")
        
        tupla_pasajero = (nombre, dni, destino)
        pasajeros.append(tupla_pasajero)
        
    
    if(opcion == 2):
        ciudad = input("Ingrese ciudad: ")
        pais = input("Ingrese pais: ")
        
        tupla_ciudad = (ciudad, pais)
        datos_ciudad.append(tupla_ciudad)
        
    if(opcion == 3):
        dni2 = int(input("Ingrese DNI del pasajero"))
        
        for nombre, dni, destino in pasajeros:
            if dni2 == dni:
                for ciudad, pais in datos_ciudad:
                    if destino == ciudad:
                        print(f"El pasajero de nombre {nombre} viajara a {ciudad}, {pais} \n")
        
    opcion = int(input(f"Escriba 4 si desea salir del programa"))
    