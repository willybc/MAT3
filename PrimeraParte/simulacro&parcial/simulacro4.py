# -*- coding: utf-8 -*-
"""
Created on Fri May 13 14:10:12 2022

@author: wilfr
"""

"""
En una comunidad de 100 deportistas se sabe que 30 de ellos entrenan futbol, 50 entrenan squash 
y 60 entrenan tenis. 22 entrenan tenis y futbol, 30 entrenan squash y tenis y 15 entrenan squash y futbol. 
Si 10 deportistas entrenan los tres deportes 
1-¿cuantos entrenan solo tenis?
2-¿cuantos entrenan solo futbol?
3-¿cuantos entrenan solo squash?
4-¿cuantos entrenan tenis o futbol?
"""
from matplotlib import pyplot as plt
from matplotlib_venn import venn3, venn3_circles

lista_futbol = [3, 5, 10, 12]
tupla_squash = (10, 20, 15, 5)
diccio_tenis = {"infantil": 12,
                "juniors": 10,
                "adolescentes": 20,
                "adultos": 18}

universal = 100
ninguno = 0


def sumaLista(lista):
    suma=0
    for elemento in lista:
        suma += elemento
    return suma

def sumaDiccio(diccio):
    suma = 0
    for elemento in diccio.values():
        suma += elemento
    return suma
    
print(f"30 de ellos entrenan futbol, compruebo: { sumaLista(lista_futbol)}")
print(f"50 de ellos entrenan squash, compruebo: { sumaLista(tupla_squash)}")
print(f"60 de ellos entrenan tenis , compruebo: { sumaDiccio(diccio_tenis)}")

#Antes de hacer comparaciones, tengo que transformar todo a conjunto (set)

def setDiccio(diccio):
    conjunto = set()
    for elemento in diccio.values():
        conjunto.add(elemento)
    return conjunto

futbol = set(lista_futbol)
squash = set(tupla_squash)
tenis = setDiccio(diccio_tenis)

#22 entrenan tenis y futbol
#30 entrenan squash y tenis
#15 entrenan squash y futbol
def interseccionAyB(a,b):
    return a&b

print(f"22 entrenan tenis y futbol, compruebo: {interseccionAyB(tenis,futbol)-squash},   sumo: {sumaLista(interseccionAyB(tenis,futbol))}")
print(f"30 entrenan squash y tenis, compruebo: {interseccionAyB(squash,tenis)-futbol},   sumo: {sumaLista(interseccionAyB(squash,tenis))}")
print(f"15 entrenan squash y futbol, compruebo: {interseccionAyB(squash,futbol)-tenis},   sumo: {sumaLista(interseccionAyB(squash,futbol))}")

#10 deportistas entrenan los 3 deportes
def interseccionABC(a,b,c):
    return (a&b)&c
print(f"10 deportistas entrenan los 3 deportes: {interseccionABC(futbol,tenis,squash)}, sumo: {sumaLista(interseccionABC(futbol,tenis,squash))}")

def soloUnDeporte(a,b,c):
    return (a-b)-c
#1-¿cuantos entrenan solo tenis?
print(f"Cuantos entrenan solo tenis?, {soloUnDeporte(tenis,futbol,squash)}")
#2-¿cuantos entrenan solo futbol?
print(f"Cuantos entrenan solo futbol?, {soloUnDeporte(futbol,tenis,squash)}")
#3-¿cuantos entrenan solo squash?
print(f"Cuantos entrenan solo squash?, {soloUnDeporte(squash,tenis,futbol)}")
#4-¿cuantos entrenan tenis o futbol?
def tenisOFutbol(tenis,futbol):
    suma = 0
    tenis_o_futbol = tenis|futbol
    for elemento in tenis_o_futbol:
        suma += elemento
    return suma
print(f"Cuantos entrenan tenis o futbol?, {tenisOFutbol(tenis,futbol)}")

#Grafico
plt.figure("Parcial")

diagram = venn3( (1, 1, 1, 1, 1, 1, 1), set_labels=("Futbol", "Squash", "Tenis") )

for subset in ("001", "010", "011", "100", "101", "110", "111"):
    diagram.get_label_by_id(subset).set_fontsize(10)

diagram.get_label_by_id("100").set_text(soloUnDeporte(futbol,tenis,squash))    
diagram.get_label_by_id("010").set_text(soloUnDeporte(squash,tenis,futbol))
diagram.get_label_by_id("001").set_text(soloUnDeporte(tenis,futbol,squash))

diagram.get_label_by_id("110").set_text(interseccionAyB(futbol,squash) - interseccionABC(futbol,tenis,squash))
diagram.get_label_by_id("101").set_text(interseccionAyB(futbol,tenis) - interseccionABC(futbol,tenis,squash))
diagram.get_label_by_id("011").set_text(interseccionAyB(tenis,squash) - interseccionABC(futbol,tenis,squash))

diagram.get_label_by_id("111").set_text(interseccionABC(futbol,tenis,squash))

plt.text(-0.90, -0.80,
         f"Universal = {universal}", 
         size=10)

plt.text(0.30, -0.80,
         f"Ninguno = {ninguno}", 
         size=10)

plt.text(0.80, 0.50,
         f"Cuantos entrenan solo tenis? {soloUnDeporte(tenis,futbol,squash)}",
         size=7)

plt.text(0.80, 0.40,
         f"Cuantos entrenan solo futbol? {soloUnDeporte(futbol,tenis,squash)}",
         size=7)

plt.text(0.80, 0.30,
         f"Cuantos entrenan solo squash? {soloUnDeporte(squash,tenis,futbol)}",
         size=7)

plt.text(0.80, 0.20,
         f"Cuantos entrenan futbol o tenis? {tenisOFutbol(tenis,futbol)}",
         size=7)

plt.axis('on')
plt.title("Deportes")
plt.show()
        