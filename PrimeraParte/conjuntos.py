# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 10:09:21 2022

@author: wilfr
"""

#%% 1
# Diseña un programa que reciba dos conjuntos y devuelva los elementos comunes a ambas, sin repetir ninguno.
# Ejm: si recibe los conjuntos [1, 2, 1], devolvera 2.

#Interseccion
conjunto_A = { 2, 4, 6, 8, 10}
conjunto_B = { 5, 6, 7}

print( conjunto_A & conjunto_B)
print( conjunto_A.intersection(conjunto_B) )

#%% 2
# Diseña un programa que reciba dos conjuntos y devuelva los elementos que pertenecen a una o a otra, pero sin
# repetir ninguno. Ejemplo: si recibe los conjuntos [1, 2, 1] y [2, 3, 2, 4], devolvera el conjunto
# [1, 2, 3, 4].

#Union
conjunto_A = { 1, 2, 1}
conjunto_B = { 2, 3, 2, 4}

print( conjunto_A | conjunto_B )
print( conjunto_A.union(conjunto_B) )

#%% 3
# Diseña un programa que reciba dos conjuntos y devuelve los elementos que pertenecen al primero pero no al 
# segundo, sin repetir ninguno. Ejemplo: si recibe las listas [1, 2, 1] y [2, 3, 2, 4], devolvera la lista [1]

#Diferencia
conjunto_A = { 1, 2, 1}
conjunto_B = { 2, 3, 2, 4}

print( conjunto_A.difference(conjunto_B) )
print( conjunto_A - conjunto_B)


#%% 4
# Diseña un programa que facilite el trabajo con conjuntos. Recuerda que un conjunto es una lista en la que no hay
# elementos repetidos. Debes implementar:

# .lista_a_conjunto(lista) : Develve un conjunto con los mismos elementos que hay en lista, pero sin repeticiones.
# (Ejemplo: lista_a_conjunto([1,1,3,2,3])) devolvera la lista [1,2,3] (aunque tambien se acepta como equivalente 
# cualquier permutacion de esos mismos elementos, como [3,1,2] o [3,2,1])
# .union(A, B): devuelve el conjunto resultante de unir los conjuntos A y B
# .interseccion(A,B): devuelve el conjunto cuyos elementos pertenecen a A y a B
# .diferencia(A,B): devuelve el conjunto de elementos que pertenecen a A y no a B.
# .iguales(A,B): devuelve cierto si ambos conjuntos tienen los mismos elementos, y falso en caso contrario

def lista_a_conjunto(lista):
    return lista


