#!/usr/bin/env python
# coding: utf-8

# # Datos

# ```
# De 1000 televidentes encuestados se obtiene la siguiente información:
# 
# a)
#     391 ven programas deportivos y los datos se han recolectado en un diccionario: 
#         {"Voleybol": 10, "Hockey": 87,  "Equitacion":23, "Ciclismo":81, "Esqui":11, "Futbol": 45, "Tenis": 37,
#         "Rugby": 9, "Basquetbol": 7, "Boxeo": 6, "Natacion":75}
#     
#     230 ven programas cómicos y los datos se han recolectado en una tupla:
#         (41,29,58,4,45,37,9,7)
#     
#     545 ven programas sobre mundo animal y los datos se han recolectado en una lista:
#         [65,14,25,29,12,1,17,18,45,37,6,41,19,8,2,90,103,13]
# 
# b) 
# Por otra parte, se sabe que:
#     98 ven programas cómicos y deportivos
#     152 ven programas cómicos y de mundo animal
#     88 ven programas deportivos y de mundo animal
#     90 no ven ninguno de esos programas
# 
# c)
# Resolver y responder:
#     1. Cuántos entrevistados ven los 3 tipos de programas?
#     2. Cuántos entrevistados sólo lo ven deportivos y cómicos?
#     3. Cuántos entrevistados ven sólo cómicos y mundo animal?
#     4. Cuántos entrevistados ven sólo deportivos y mundo animal
#     5. Cuántos entrevistados ven sólo deportes?
#     6. Cuántos entrevistados ven sólo cómicos?
#     7. Cuántos entrevistados ven sólo mundo animal? 
#     8. Cuántos entrevistados ven 2 de las 3 categorías?
# 
# d) Graficar con matplotlib_venn
# 
# Nota: 
# 
# El ejercicio debe resolverse con variables, estructuras, operaciones de conjuntos, funciones propias y del lenguaje, etc.
#  No se admiten valores literales, salvo en el caso de la asignación del valor universal y en las inicializaciones de variables.
# 
# Una vez resuelto el ejercicio, sube la solución a la carpeta del campus con nombre y apellido como nombre de archivo.
# 
# ```

# # Solución

# In[ ]:

from matplotlib import pyplot as plt
from matplotlib_venn import venn3, venn3_circles

# a)
dic_deportes = {"Voleybol": 10, "Hockey": 87, "Equitacion":23, "Ciclismo":81, "Esqui":11, "Futbol": 45, "Tenis": 37, "Rugby": 9, "Basquetbol": 7, "Boxeo": 6, "Natacion":75}
tupla_comicos = (41,29,58,4,45,37,9,7)
lista_animales = [65,14,25,29,12,1,17,18,45,37,6,41,19,8,2,90,103,13]
universal = 1000

def setDic(diccio):
    conjunto = set() 
    for elemento in diccio.values():
        conjunto.add(elemento)
    return conjunto

animales = set(lista_animales) 
comicos = set(tupla_comicos)
deportivos = setDic(dic_deportes)

def interseccionAyB(a,b):
    return a&b

def interseccionABC(a,b,c):
    return (a&b)&c

def soloUnPrograma(principal,b,c):
    return (principal-b)-c

def sumo(lista):
    suma = 0
    for elemento in lista:
        suma += elemento
    return suma

# b)
print(f"98 ven programas cómicos y deportivos, compruebo: {interseccionAyB(comicos,deportivos)}, sumo: {sumo(interseccionAyB(comicos,deportivos))}")
print(f"152 ven programas comicos y del mundo animal, compruebo: {interseccionAyB(comicos,animales)}, sumo: {sumo(interseccionAyB(comicos,animales))}")
print(f"88 ven programas deportivos y del mundo animal, compruebo: {interseccionAyB(deportivos,animales)}, sumo: {sumo(interseccionAyB(deportivos,animales))}")

def ningunoDeEsosProgramas(universal, a, b, c):
    total = universal
    conjuntos = (a|b)|c
    
    for elemento in conjuntos:
        total -= elemento
    return total
print(f"90 no ven ninguno de esos programas, compruebo:{ningunoDeEsosProgramas(universal, animales,comicos,deportivos)}")

# c)
# Resolver y responder:
print(f"1. Cuántos entrevistados ven los 3 tipos de programas?, respuesta:{sumo(interseccionABC(animales, comicos,deportivos))}")

print(f"2. Cuántos entrevistados sólo lo ven deportivos y cómicos?, respuesta:{sumo(interseccionAyB(deportivos,comicos)-animales)}")
print(f"3. Cuántos entrevistados ven sólo cómicos y mundo animal?, respuesta:{sumo(interseccionAyB(comicos,animales)-deportivos)}")
print(f"4. Cuántos entrevistados ven sólo deportivos y mundo animal, respuesta: {sumo(interseccionAyB(deportivos,animales)-comicos)}")

print(f"5. Cuántos entrevistados ven sólo deportes?, respuesta: {sumo(soloUnPrograma(deportivos,comicos,animales))}")
print(f"6. Cuántos entrevistados ven sólo cómicos?, respuesta: {sumo(soloUnPrograma(comicos,deportivos,animales))}")
print(f"7. Cuántos entrevistados ven sólo mundo animal?, respuesta: {sumo(soloUnPrograma(animales,comicos, deportivos))}")


# 8. Cuántos entrevistados ven 2 de las 3 categorías?
def almenosDosCategoriasSuma(a,b,c):
    conjuntos = interseccionAyB(a, b) | interseccionAyB(a,c) | interseccionAyB(b,c)
    return sumo(conjuntos)
    
print(f"8. Cuántos entrevistados ven 2 de las 3 categorías?, respuesta: {almenosDosCategoriasSuma(deportivos, comicos, animales)}")

# d)
# Graficar con matplotlib_venn

plt.figure("Parcial")

diagram = venn3( (1, 1, 1, 1, 1, 1, 1), set_labels=("Deportivos", "Comicos", "Animales") )

for subset in ("001", "010", "011", "100", "101", "110", "111"):
    diagram.get_label_by_id(subset).set_fontsize(6)
    
diagram.get_label_by_id("100").set_text(soloUnPrograma(deportivos, comicos, animales))
diagram.get_label_by_id("010").set_text(soloUnPrograma(comicos, deportivos, animales))
diagram.get_label_by_id("001").set_text(soloUnPrograma(animales, deportivos, comicos))

diagram.get_label_by_id("110").set_text( interseccionAyB(deportivos, comicos) - interseccionABC(deportivos, comicos, animales))
diagram.get_label_by_id("101").set_text( interseccionAyB(deportivos, animales) - interseccionABC(deportivos, comicos, animales))
diagram.get_label_by_id("011").set_text( interseccionAyB(comicos, animales) - interseccionABC(deportivos, comicos, animales))

diagram.get_label_by_id("111").set_text( interseccionABC(deportivos, comicos, animales))

plt.text(-0.90, 0.67,
         f"Universal = {universal}",
         size = 5)

plt.axis('on')
plt.title("Televidentes encuestados")
plt.show()
