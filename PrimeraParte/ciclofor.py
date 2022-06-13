# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 02:31:27 2022

@author: wilfr
"""

#%% 1
# Escribe un programa que le permita realizar la escritura de los primeros 100 numeros naturales

for i in range(1,100):
    print(i)


#%% 2
# Escribe un programa que le permita realizar la suma de los primeros N numeros impares.
# El N debe ingresarse por teclado

n = int(input(f"Escriba el numero N: "))
acumulador = 0
cont = 0

for i in range(1, 100000, 2):
    acumulador += i
    cont+=1
    #print(i)
    
    if(cont == n):
        break
print(f"Suma de los primeros {n} numeros impares es de : {acumulador} ")        


#%% 3
# Escribe un programa que calcule el factorial de un numero cualquiera que se ingresa por teclado

num = int(input(f"Escriba u numero cualquiera para calcular factorial: "))
facto = 1

if num < 0:
    print("No existe factorial con numeros negativos")

elif num == 0:
    print("Factorial de 0 es 1")

else:
    for i in range(1, num+1):
        facto = facto * i
    
    print(f"Factorial de {num} es: {facto}")

#%% 4
# Muestre los N primeros numeros de la secuencia de Fibonacci, siendo n un dato entero