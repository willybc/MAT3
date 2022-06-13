# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 14:01:30 2022

@author: wilfr
"""
# 2.
# Convertir a funciones los siguientes ejercicios:
# b. Practica de tuplas-conjuntos-diccionarios
# - Ejercicio 3 de tuplas
# - Ejercicio 4 de conjuntos
# - Ejercicio 3 de diccionarios

#------------------------------- Resolucion  --------------------------------------------------------------------------------

# func ej3_tuplas
# Escribir un programa que permita procesar datos de pasajeros de viaje en una lista de tuplas con
# la sigueinte forma: (nombre, dni, destino)
# Ejm [("Manuel Juares", 19823451, "Liverpool")]
def ej3_tuplas():
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

# fun ej4_conjuntos
#def ej4_conjuntos():

# fun ej3_diccionarios
# Codifica un programa que permita guardar los nombres de alumnos de una clase y las notas que han obtenido. Cada
# alumno puede tener distinta cantidad de notas. Guarda la informacion en un diccionario cuya claves seran los
# nombres de los alumnos y los valores seran listas con las notas de cada alumno. El programa pedira el numero
# de los alumnos que vamos a introducir, pedira su nombre e ira pidiendo sus notas hasta que introduzcamos un
# numero negativo. Al final el programa nos mostrara la lista de alumnos y la nota media obtenida por cada uno
# de ellos. Nota: si se introduce el nombre de un alumno que ya existe el programa nos dara error.
def ej3_diccionarios():
    dic3 = {}

    total = int(input("Escriba el numero de alumnos que se van a introducir: "))
    i = 0
    anterior_alumno = 0

    while i < total:
        new_alumno = input("Escriba nombre de alumno: ")
        nota = []
        new_nota = 0
        
        while new_nota >= 0:
            new_nota = int(input(f"Escriba nota: "))
            
            if new_nota >= 0:
                nota.append(new_nota)
            
        #datos_product = [ (new_materia, new_nota) ]
        
        dic3[ new_alumno ] = nota
        
        i +=1
        
    print(dic3)