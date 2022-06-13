# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 18:08:09 2022

@author: Infolab
"""
#%% 1
# Escribe un programa que permita crear una lista de palabras. Para ello, el programa tiene que
# pedir un número y luego solicitar esa cantidad de palabras para crear la lista. Por último, el
# programa tiene que emitir la lista

lista = []
a = int(input("Escriba el tamaño de la lista: "))

for i in range(a):
    lista.append(input("Escriba palabra para colocar en posicion lista{i} "))

print(lista)


#%% 2
# Escribe un programa que permita crear una lista de palabras y que, a continuacion, pida una palabra
# y diga cuantas veces aparece esa palabra en la lista

lista2 = []
a = int(input("Escriba el tamaño de la lista: "))

for i in range(a):
    lista2.append(input(f"Escriba palabra para colocar en posicion lista{i} "))

b = input("Escribe primer palabra: ")
c = input("Escribe segund palabra: ")

contb = 0
contc = 0

for i in lista2:
    if (i == b):
        contb += 1

    if(i == c):
        print("sumo c")
        contc += 1

print(f"Veces en las que aparece primera palabra : {contb}")
print(f"Veces en las que aparece segunda palabra : {contc}")


#%% 3
# Escribe un programa que permita crear una lista de palabras y que, a continuacion, pida dos palabras
# y sustituya la primera (que debe estar en la lista) por la segunda. Emitir la lista.

lista3 = []
lista4 = []
a = int(input("Escriba el tamaño de la lista: "))

for i in range(a):
    lista3.append(input(f"Escriba palabra para colocar en posicion lista{i} "))

d = input("Escribe primer palabra: (que debe estar en la lista) ")
e = input("Escribe segund palabra: (palabra que va a pisarla)")

for i in lista3:
    if ( i == d ):
        lista4.append(e)
    else:
        lista4.append(i)
        
print(lista4)


#%% 4 METODO 1
# Escribe un programa que permita crear una lista de palabras y que, a continuacion, pida una palabra
# y elimine esa palabra de la lista

lista5 = []
lista6 = []

a = int(input("Escriba el tamaño de la lista: "))

for i in range(a):
    lista5.append(input(f"Escriba palabra para colocar en posicion lista{i} "))

f = input("Escribe una palabra para eliminarla de la lista ")

for i in lista5:
    if (i == f):
        pass
    else:
        lista6.append(i)

print(lista6)

#%% 4 METODO 2

lista5 = []

a = int(input("Escriba el tamaño de la lista: "))

for i in range(a):
    lista5.append(input(f"Escriba palabra para colocar en posicion lista{i} "))

f = input("Escribe una palabra para eliminarla de la lista ")

for i in range(len(lista5)-1, -1, -1):
    if lista5[i] == f:
        del lista5[i]
        

print(lista5)

#%% 5
# Escribe un programa que permita crear dos listas de palabras y que, a continuacion, elimine de la
# primera lista los nombres de la segunda lista

lista7 = []
lista8 = []

tamanio1 = int(input("Escriba el tamaño de las listas num 1: "))
for i in range(tamanio1):
    lista7.append(input(f"Escriba palabra para colocar en posicion lista{i} "))

for j in range(tamanio1):
    lista8.append(input(f"Escriba palabra para colocar en posicion lista{j} "))

for i in range(len(lista7)-1, -1, -1):
    for j in range(len(lista8)):
        if (lista7[i] == lista8[j]):
            del lista7[i]
    
print(lista7)


#%% 6 METODO 1
# Escribe un programa que permita crear una lista de palabras y que, a cotinuacion, cree una segunda lista
# igual a la primera, pero al reves (crear una lista distinta)

lista10 = []
a = int(input("Escriba el tamaño de la lista: "))

for i in range(a):
    lista10.append(input(f"Escriba palabra para colocar en posicion lista{i} "))
    
lista11 = []

for i in reversed(lista10):
    lista11.append(i)
    
print(lista11)

#%% 6 METODO 2

lista10 = []
a = int(input("Escriba el tamaño de la lista: "))

for i in range(a):
    lista10.append(input(f"Escriba palabra para colocar en posicion lista{i} "))

lista11 = []

for i in range(len(lista10)-1, -1, -1):
    lista11.append(lista10[i])
    
print(lista11)