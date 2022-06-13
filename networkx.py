# -*- coding: utf-8 -*-
"""
Created on Fri Jun  3 01:06:35 2022

@author: wilfr
"""

import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


# 1.
# Utilizar el algoritmo de Dijkstra para determinar en el grafo ponderado sigueinte un camino de longitud minima entre los
# vertices Z y A. Construir el grafo

#Pasos para Algoritmo Dijkstra
L1 = [('A', 'B', 'C', 'D', 'E', 'F', 'G', 'Z')]
L2 = [('A','D'), ('A','G'), ('A','B'), ('D','G'), ('D','E'), ('G','B'), ('E','F'), ('E','Z'), ('C','F'), ('C','Z'), ('C','B'), ('F','Z')]

G = nx.Graph(L2)
G.add_nodes_from(L1) #vertices
G.add_edges_from(L2) #aristas

print("Camino de longitud minima entre los vertices Z y A: \n", nx.algorithms.shortest_path(G, 'Z', 'A'))

#Pasos para construir grafo
plt.rcParams["figure.figsize"] = [4,4]
plt.rcParams["figure.autolayout"] = True
fig, ax = plt.subplots()

#L2 = [('A','D'), ('A','G'), ('A','B'), ('D','G'), ('D','E'), ('G','B'), ('E','F'), ('E','Z'), ('C','F'), ('C','Z'), ('C','B'), ('F','Z')]
#G = nx.Graph()
nx.draw(G, node_color="palevioletred", font_size=10, width=1, with_labels=True, node_size=1000)
plt.show()

#%%
# 2.
# El plano muestra los puntos de conexion y las posibles lineas telefonicas en una urbanizacion. 
# La zona quedara comunicada cuando dos puntos cualquiera esten conectados
# En rojo esta indicado el precio de cada linea en miles de dolares.
# Calcular el diseño de la red mas barata que conecte la zona.

g = nx.Graph()

g.add_node('a')
g.add_node('b')
g.add_node('c')
g.add_node('d')
g.add_node('e')
g.add_node('f')
g.add_node('g')
g.add_node('h')
g.add_node('i')
g.add_node('j')
g.add_node('k')
g.add_node('l')
g.add_node('m')
g.add_node('n')

g.add_edge('a', 'b', weidght=6)
g.add_edge('a', 'd', weidght=3)
g.add_edge('a', 'c', weidght=9)

g.add_edge('b', 'e', weidght=12)
g.add_edge('b', 'c', wedight=10)

g.add_edge('c', 'd', weidght=4)
g.add_edge('c', 'e', weidght=3)

g.add_edge('d', 'g', weidght=10)
g.add_edge('d', 'f', weidght=15)

g.add_edge('e', 'h', weidght=4)
g.add_edge('e', 'i', weidght=11)
g.add_edge('e', 'f', weidght=8)

g.add_edge('f', 'i', weidght=10)
g.add_edge('f', 'g', weidght=9)

g.add_edge('g', 'j', weidght=13)

g.add_edge('h', 'k', weidght=20)
g.add_edge('h', 'i', weidght=7)
g.add_edge('h', 'l', weidght=11)

g.add_edge('i', 'l', weidght=11)
g.add_edge('i', 'j', weidght=15)

g.add_edge('j', 'l', weidght=11)
g.add_edge('j', 'm', weidght=9)

g.add_edge('k', 'l', weidght=13)
g.add_edge('k', 'n', weidght=6)

g.add_edge('l', 'n', weidght=12)
g.add_edge('l', 'm', weidght=5)

g.add_edge('m', 'n', weidght=5)

pos = nx.get_node_attributes(g)
labels = nx.get_edge_attributes(g, 'weight')

nx.draw_networkx_edge_labels(g, pos, edge_labels=labels)
nx.draw(g, pos, with_labels=True)

print(nx.shortest_path(g, source=1, target=10))
plt.show()
# Construir el grafo y calcular : Radio, diametro, excentricidad, centro, periferia y densidad

#%%
# 3.
# Sea G = (V,A) el grafo ponderado de 8 vertices, los cuales etiquetamos de A a H
# que representan poblaciones entre las cuales se implementara un
# medio de transporte. Los valores representan cantidad de combustible a utilizar.

# Determinar que cantidad de combustible se necesitara utilizar en una ruta que 
# conecte las poblaciones A y H, corresponde con el problema de encontrar el camino mas corto de A a H

#%%
# 4.
# Se considera el grafo ponderado G definido por la siguiente tabla, donde los vertices
# representan ciudades y las aristas representan rutas existentes entre las poblaciones.
# Los pesos indican longitudes en Kms

# a. Usando el algoritmo apropiado, calcular la distancia mas cortas desde A a las restantes poblaciones
# y especificar cuales son dichas distancias.

# b. Se ha construido una nueva ruta entre las poblaciones B y G de forma que ahora,
# la distancia entre A y H es de 68Kms.
# Determinar cual es el peso que le corresponde a la arista {B,G}

#%%
# 5.
# Dos amigos, Ana y Pedro, quieren visitar la ciudad de Praga, en la que los lugares turisticos de
# mayor importancia, las rutas entre los mismos y las distancias en kilometros vienen dados por la siguiente tabla:
    
# Dibujar el grafo asociado al problema.

#%%
# 6.
# En la siguiente tabla se muestran las conexiones entre las computadoras de los 12 empleados de una oficina
# (en cada cuadro se muestra la longitud del cable que une las correspondientes computadoras)

# a. El jefe decide que deben trabajar entre pares, formados de la siguiente manera: A con B, C con D, etc. Es posible?
# b. Obtener, la minima distancia en metros de cable entre las computadoras A y J y el camino minimo entre ellas.

#%%
# 7.
# En todos los casos dados, obtener la matriz de adyacencia e incidencia