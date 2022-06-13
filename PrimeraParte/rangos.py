# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 02:30:48 2022

@author: wilfr
"""

#%% 1
# Escribe un tipo range() que emita: [100, 101, 102, 103]
a = range(100, 104)

#%% 2
# Escribe un tipo range() que emita: [-50, -2050, -4050, -6050]
b = range(50, 6051, 2000)
c = range(-50, 6051, 2000)

#%% 3
# Escribe un programa que pida un número entero y emita una 
# lista de números consecutivos del 0 al valor dado

num1 = int(input("Escriba un numero entero: ") )
print( list(range(0, num1)) )

#%% 4
# Escribe un programa que pida dos números enteros
# (el segundo mayor que el primero)
# y emita listas de números consecutivos al derecho y al revés.

num2 = int( input("Ingrese primer numero entero: ") )
num3 = int( input("Ingrese segundo numero entero mayor al primero: ") )

print( list(range(num2, num3)) )
print( list(range(num3, num2, -1)) )

#%% 5
# Escribe un programa que pida dos números enteros y emita la lista
# de numeros consecutivos que hay entre ellos, de menor a mayor.

num4 = int( input("Ingrese primer numero entero: ") )
num5 = int( input("Ingrese segundo numero entero: ") )

if (num4 > num5):
    print( list(range(num5, num4)))
elif(num4 == num5):
    print("Los numeros son iguales, lista vacia []")
else:
    print( list(range(num4, num5)))

#%% 6
# Escribe un programa que pida dos numeros enteros y emita una lista de
# numeros pares que hay entre ellos(incluidos ellos mismos si son pares)

num6 = int( input("Ingrese primer numero entero: ") )
num7 = int( input("Ingrese segundo numero entero: ") )

lista3 = []

if (num6 < num7):
    lista1 = list(range(num6, num7, 1))
    for i in lista1:
        if( i % 2 == 0):
            #print(i)
            lista3.append(i)
else:
    lista2 = list(range(num7, num6, 1))
    for j in lista2:
        if( j % 2 == 0):
            lista3.append(j)

print(lista3)

#%% 7
# Escribe tres programas que emitan las siguientes secuencias de números
# Primer programa, el tipo range() que se utilice en cada bucle debe tener un único
# argumento
# Segundo programa, el tipo range() que se utilice en cada bucle debe tener un único
# argumento
# Tercer programa, el tipo range() que se utilice en cada bucle debe tener tres
# argumentos