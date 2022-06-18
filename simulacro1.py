# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 01:45:00 2022

@author: wilfr
"""

import networkx as nx
import matplotlib.pyplot as plt

# a. Construir los nodos
def emitoGraph(G, pos):
    nx.draw_networkx_nodes(G, pos, node_color='violet', node_size=600)
    nx.draw_networkx_labels(G, pos, font_size=10, font_family='sans-serif')
    nx.draw_networkx_edges(G, pos, edge_color='grey', width=2, arrowstyle= '<|-|>', arrowsize = 10)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.axis('off')
    plt.show()

# b. Construir con enlaces y pesos
def cargoGraph(G):
    G.add_weighted_edges_from([('a', 'b', 12),
                               ('a', 'd', 14),
                               ('b', 'd', 4),
                               ('b', 'e', 11),
                               ('b', 'c', 7),
                               ('b', 't', 23),
                               ('c', 't', 10),
                               ('c', 'e', 2),
                               ('d', 'e', 6),
                               ('e', 't', 9)])

G = nx.Graph()
cargoGraph(G)

# c. Emitir los nodos
print("Número de nodos: ", G.number_of_nodes())

# d. Emitir los nodos
print("Nodos: ", G.nodes())

# e. Emitir numeros de enlaces
print("Número de enlaces: ", G.number_of_edges())

# f. Emitir los enlaces
print("Enlaces: ", G.edges())

# g. Emitir los vecinos de 'b'

print("Vecinos: ", list(G.neighbors('b')))

# h. Emitir cantidad de aristas de cada nodo
print("Cantidad de aristas de cada nodo: ",G.degree()) 

# i. Convertir en diccionario la salida anterior ( cantidad de aristas )
print(dict(G.degree()))

# j. Crear matriz de adyacencia y emitirla
M = nx.adjacency_matrix(G)
print(M.todense()) 

# k. Crear la matriz de incidencia y emitirla
I =  nx.incidence_matrix(G)
print(I.todense())

# l. Emitir valores de los enlaces del nodo 'c'
print("Valores de los enlaces del nodo: ",G['c'])

# m. Emitir el peso de la relacion entre 'b' y 'e'
print("Peso de la relación entre ", G['b']['e']['weight'])

# n. Emitir la ruta mas corta desde 'a' al objeto
print("Ruta mas corta al objetivo: ", nx.algorithms.shortest_path(G, 'a')) 

# o. Emitir la longitud desde 'a' hasta el objetivo
print("Longitud de Ruta mas corta desde: ",nx.single_source_shortest_path_length(G, 'a'))

# p. Emitir el promedio de la ruta mas corta usando el meotodo de floyd-warshall
print("Promedio de la ruta mas corta ", nx.algorithms.average_shortest_path_length(G, method="floyd-warshall"))

# q. Emitir la ruta ponderada mas corta entre 'a' y 't'
print("Ruta mas corta usando el algoritmo de Dijkstra entre:",nx.algorithms.dijkstra_path(G, 'a', 't'))

# r. Emitir la longitud de la ruta ponderada entre 'a' y 't'
print("Longitud de Ruta ponderada más corta entre:",nx.dijkstra_path_length(G,'a','t'))

# s. Emitir la longitud de la ruta desde el nodo 'c'
print("Longitud de Ruta ponderada más corta desde el nodo:", nx.single_source_dijkstra_path_length(G,'c'))

# t. Emitir el radio del grafo
print("Radio:",nx.radius(G))

# u. Emitir el diametro del grafo
print("Diámetro:", nx.diameter(G))

# v. Emitir la excentricidad
print("Excentricidad:", nx.eccentricity(G))

# w. Emitir el centro del grafo
print("Centro:", nx.center(G))

# x. Emitir la periferia del grafo
print("Periferia:", nx.periphery(G))

# y. Emitir la densidad
print("Densidad:", nx.density(G))

# z. Dibujar el grafo y emitir con matplotlib.pyplot
pos = nx.shell_layout(G)
emitoGraph(G, pos)

# aa. Convertir en grafo dirigido y emitir con matplotlib.pyplot
H = G.to_directed()
cargoGraph(H)

pos = nx.shell_layout(H)
emitoGraph(H, pos)

# Ejercicio 3

#%%
import re 

texto = """
98.140.180.244 - harber4797 [21/Jun/2019:16:01:53 -0700] "POST /seize/b2b/synergistic HTTP/2.0" 203 9396
229.231.201.185 - - [21/Jun/2019:16:01:35 -0700] "HEAD /supply-chains/brand/strategic HTTP/1.1" 405 28109
197.150.196.204 - thiel4558 [21/Jun/2019:16:01:05 -0700] "PATCH /compelling HTTP/2.0" 500 14180
"""

a_buscar = r'[A-Z]{1,}\s\/*.*\d\.\d'

x = re.findall(a_buscar, texto) 

print(x)
