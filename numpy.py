# -*- coding: utf-8 -*-
"""
Created on Fri May 20 18:28:01 2022

@author: wilfr
"""
import numpy as np
import pandas as pd

# 1.
#Resolver con numpy
lista_de_listas = [ [-44,12], 
                    [12.0, 51],
                    [1300, -5.0]
                ]

a = np.array(lista_de_listas)
print(f"Matriz original \n{a} \n")

#Restarle 5 a la fila 2 de la matriz
a[2:] = a[2:]-5
print(f"Restarle 5 a la fila 2 de la matriz: {a} \n")

#Multiplicar por 2 toda la matriz
mult = a *2
print(f"Multiplicar por 2 toda la matriz: \n {mult} \n")

#Dividir por -5 las dos primeras filas de la matriz
a[0:] = a[0:]/-5
a[1:] = a[1:]/-5

print(f"Dividir por -5 las dos primeras filas de la matriz: \n{a} \n")

#Imprimir la ultima fila de la matriz
lenght = len(a)     
print(f"Ultima fila de la matriz: {a[ lenght-1]} \n")

#%%
# 2.
import numpy as np
import pandas as pd

#Resolver con numpy. Calcular la suma de los elementos de a(ejercicio anterior) utilizando dos fors anidados
suma = 0
lista_de_listas = [ [-44,12], 
                    [12.0, 51],
                    [1300, -5.0]
                ]

a = np.array(lista_de_listas)

for i in a:
    for j in i:
        suma += j
        
print(f"Calculo de la suma de los elementos de a: {suma}")

#Calcular la suma de los elementos utilizando np.sum
print(f"Suma de los elementos usando np: {np.sum(a)}")

#Calcular el promedio de los elementos de las primeras dos filas de a utilizando dos fors anidados
cont = 0
suma = 0
for i in a[2:]:
    for j in i:
        cont += 1
        suma += j
promedio = suma/cont
print(f"Calculo del promedio de los elementos de las primeras dos filas utilizando dos fors anidados {promedio}")

#Calcular el promedio de los elementos de las primeras dos filas utilizando slices(notacion ( :) ) y np.mean
print(f"Calculo del promedio de los elementos de las primeras dos filas utilizando slices y np mean: {np.mean(a[2:])}")

#%%
# 3.
import numpy as np
import pandas as pd
# Generar una matriz de 7 x 9.
a = np.random.randint(10, size=(7,9))
# Las primeras 3 columnas de la matriz tienen que tener el valor 0.
a[0:7,0] = 0
a[0:7,1] = 0
a[0:7,2] = 0
# Las otras tres columnas deben tener el valor 1.
a[0:7,3] = 1
a[0:7,4] = 1
a[0:7,5] = 1
# Luego imprimir la matriz.
print(a)
# Imprimir tambien el promedio de la ultima fila
#Obtengo la ultima fila
b = a[-1]
print(np.mean(b))
     
#%%
# 4.
# La siguiente linea crea una matriz aleatoria de 5 por 5 con valores entre 0 y 1
matriz_aleatoria = np.random.randint(2, size=(5,5))
np.asarray(matriz_aleatoria)
#print(matriz_aleatoria)

# Imprimir las posiciones (Fila y Columna) de los elementos de la matriz que son mayores que 0.5
print("Impresion de posiciones en donde los elementos son mayores a 0.5")

np.transpose( np.where(matriz_aleatoria>0.5) )

#%%
# 5.
# Resuelve el practico: 13. Ejercicios Introduccion a Numpy.ipynb

