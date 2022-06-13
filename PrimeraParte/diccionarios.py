# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 10:16:07 2022

@author: wilfr
"""

#%% 1
# Crea un diccionario donde la clave sea el nombre del usuario y el valor sea el telefono (no es necesario validar)
# Tendras que ir pidiendo contactos hasta el usuario diga que no quiere insertar mas. No se podran ingresar
# nombres repetidos

dic = { "user111" : 111, "user222" : 222, "user333" : 333 }

flag=1

while flag == 1:
    
    new_user = str(input("Escriba usuario:"))
    new_number = int(input("Escriba num: "))
    
    dic[ new_user ] = new_number
    
    try:
        flag = int(input("Quiere seguir añadiendo contactos? si(1) en caso contrario se cerrará el programa"))
    except ValueError:
        flag=0
        
print(dic)
    

#%% 2
# Crear un programa donde vamos a declarar un diccionario para guardar los precios de las distintas frutas. El
# programa pedira el nombre de la fruta y la cantidad que se ha vendido y nos mostrara el precio final de la fruta
# a partir de los datos guardados en el diccionario. Si la fruta no existe nos dara un error. Tras cada consulta
# el programa nos preguntara si queremos hacer otra consulta.
dic2 = {}

flag=1

while flag == 1:
    
    new_product = str(input("Escriba fruta:"))
    
    new_price = int(input(f"Escriba precio del producto {new_product}: "))
    new_cantVen = int(input(f"Escriba la cantidad que se ha vendido de la fruta {new_product}:"))
    recaudacion = new_price * new_cantVen
    
    #datos_product = [ (new_price, recaudacion) ]
    
    dic2[ new_product ] = recaudacion
    
    try:
        flag = int(input("Quiere hacer otra consulta? \n Si(1) en caso contrario se cerrará el programa: "))
    except ValueError:
        flag=0
        
consulta = input(f"Escriba el nombre de la fruta para saber la recaudacion hasta el momento: ")
    
try:
    print( dic2[consulta] )
except ValueError:
    print("La fruta no existe! error 404")


#%% 3
# Codifica un programa que permita guardar los nombres de alumnos de una clase y las notas que han obtenido. Cada
# alumno puede tener distinta cantidad de notas. Guarda la informacion en un diccionario cuya claves seran los
# nombres de los alumnos y los valores seran listas con las notas de cada alumno. El programa pedira el numero
# de los alumnos que vamos a introducir, pedira su nombre e ira pidiendo sus notas hasta que introduzcamos un
# numero negativo. Al final el programa nos mostrara la lista de alumnos y la nota media obtenida por cada uno
# de ellos. Nota: si se introduce el nombre de un alumno que ya existe el programa nos dara error.

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
    