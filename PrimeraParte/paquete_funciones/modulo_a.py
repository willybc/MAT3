# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 14:00:55 2022

@author: wilfr
"""

# 2.
# Convertir a funciones los siguientes ejercicios:
# a. Practica de rangos listas for while
# - Ejercicio 6 de rangos
# - Ejercicio 6 de listas
# - Ejercicio 4 de ciclo for
# - Ejercicio 7 de ciclo while

#------------------------------- Resolucion  --------------------------------------------------------------------------------

# func ej6_rangos
# Escribe un programa que pida dos numeros enteros y emita una lista de
# numeros pares que hay entre ellos(incluidos ellos mismos si son pares)
def ej6_rangos():
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

# func ej6_listas
# Escribe un programa que permita crear una lista de palabras y que, a cotinuacion, cree una segunda lista
# igual a la primera, pero al reves (crear una lista distinta)
def ej6_listas():
    lista10 = []
    a = int(input("Escriba el tamaño de la lista: "))

    for i in range(a):
        lista10.append(input(f"Escriba palabra para colocar en posicion lista{i} "))
        
    lista11 = []

    for i in reversed(lista10):
        lista11.append(i)
        
    print(lista11)

# func ej4_ciclofor
#def ej4_ciclofor():

# func ej7_ciclowhile
# Escribe un programa que pida primero dos numeros enteros (minimo y maximo) y que despues pida numeros
# enteros situados entre ellos. El programa terminara cuando se escriba un numero que no este comprometido
# entre los dos valores iniciales y emitira la cantidad de numeros ingresados.
def ej7_ciclowhile():
    minimo = int(input(f"Escriba el minimo: "))
    maximo = int(input(f"Escriba el maximo: "))
    cont = 0

    num = int(input(f"Escriba numero: "))

    while minimo<num and maximo>num:
        num = int(input(f"Escriba numero: "))
        cont+=1

    print(f"contador = {cont}")

