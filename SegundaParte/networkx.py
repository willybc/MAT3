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
# Utilizar el algoritmo de Dijkstra para determinar en el grafo ponderado siguiente un camino de longitud minima entre los
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
nx.draw(G, node_color="palevioletred", font_size=10, width=1, with_labels=True, node_size=300)
plt.show()

#%%
# 2.
import networkx as nx
import matplotlib.pyplot as plt
# El plano muestra los puntos de conexion y las posibles lineas telefonicas en una urbanizacion. 
# La zona quedara comunicada cuando dos puntos cualquiera esten conectados
# En rojo esta indicado el precio de cada linea en miles de dolares.
# Calcular el diseño de la red mas barata que conecte la zona.

def emitoGraph(G, pos):
    nx.draw_networkx_nodes(G, pos, node_color='violet', node_size=100)
    nx.draw_networkx_labels(G, pos, font_size=10, font_family='sans-serif')
    
    nx.draw_networkx_edges(G, pos, edge_color='grey', width=1, arrowstyle='<|-|>', arrowsize=10)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.axis('off')
    plt.show()
    
def cargoGraph(G):
    G.add_weighted_edges_from([('a', 'b', 6),
                               ('a', 'd', 3),
                               ('a', 'c', 9),
                               ('b', 'e', 12),
                               ('b', 'c', 10),
                               ('c', 'd', 4),
                               ('c', 'e', 3),
                               ('d', 'g', 10),
                               ('d', 'f', 15),
                               ('e', 'h', 4),
                               ('e', 'i', 11),
                               ('e', 'f', 8),
                               ('f', 'i', 10),
                               ('f', 'g', 9),
                               ('g', 'j', 13),
                               ('h', 'k', 20),
                               ('h', 'i', 7),
                               ('h', 'l', 11),
                               ('i', 'l', 11),
                               ('i', 'j', 15),
                               ('j', 'l', 11),
                               ('j', 'm', 9),
                               ('k', 'l', 13),
                               ('k', 'n', 6),
                               ('l', 'n', 12),
                               ('l', 'm', 5),
                               ('m', 'n', 5)])
    
# Construir el grafo y calcular : Radio, diametro, excentricidad, centro, periferia y densidad

G = nx.Graph()
cargoGraph(G)

#pos = nx.shell_layout(G)
pos = nx.spring_layout(G)
emitoGraph(G, pos)

print("Red mas barata que conecte la zona: :",nx.algorithms.dijkstra_path(G, 'a', 'n'))

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