import networkx as nx 
import matplotlib.pyplot as plt
import re

#1. Crear clase grafo
class Grafo:
    def __init__(self):
        self.G = nx.Graph()
        self.cargoGraph()
        
        self.pos = nx.shell_layout(self.G)
#a. Construir los nodos con enlaces y pesos    
    def cargoGraph(self):
        self.G.add_weighted_edges_from([
            ('a', 'd', 6),
            ('a', 'f', 2),
            ('b', 'a', 5),
            ('b', 'e', 12),
            ('b', 'g', 1),
            ('c', 'b', 4),
            ('d', 'g', 2),
            ('e', 'c', 6),
            ('f', 'a', 9)
        ])
    
    def dibujoGraph(self):
        nx.draw_networkx_nodes(self.G, self.pos, node_size=600, node_color="violet")
        nx.draw_networkx_labels(self.G, self.pos, font_size=10)
        nx.draw_networkx_edges(self.G, self.pos, width=2, arrowstyle="<|-|>", arrowsize=10)
        
        labels = nx.get_edge_attributes(self.G, "weight")
        nx.draw_networkx_edge_labels(self.G, self.pos, edge_labels=labels)
        plt.show()
    
    def info(self):
        print("B - Emitir los vecinos de 'c'", list(self.G.neighbors('c')))
        
# Error con networkx y la adjacency 
# M = nx.adjacency_matrix(self.G)
# Traceback (most recent call last):
# File "c:\Users\Lidi\Documents\mat3.py", line 55, in <module>
# grafo1.info()
# File "c:\Users\Lidi\Documents\mat3.py", line 39, in info
# M = nx.adjacency_matrix(self.G)
# File "C:\Users\Lidi\AppData\Local\Programs\Python\Python310\lib\site-packages\networkx\linalg\graphmatrix.py", line 173, in adjacency_matrix
# return nx.to_scipy_sparse_matrix(G, nodelist=nodelist, dtype=dtype, weight=weight)
# File "C:\Users\Lidi\AppData\Local\Programs\Python\Python310\lib\site-packages\networkx\convert_matrix.py", line 1010, in to_scipy_sparse_matrix
# import scipy as sp
# ModuleNotFoundError: No module named 'scipy'
        
        ####################### 
        print("C - Crear y emitir la matriz de adyacencia e incidencia: ")
        M = nx.adjacency_matrix(self.G)
        print(M.todense())
        #######################
        print("C - Incidencia: \n")
        I = nx.incidence_matrix(self.G)
        print(I.todense())
        
        print("D - Emitir la ruta ponderada mas corta entre 'd' y 'f' usando el algoritmo de dijkstra", nx.algorithms.dijkstra_path(self.G, "d", "f"))
        print("E - Emitir el radio, diametro, excentricidad, centro, periferia y densidad\n")
        print("Radio : ", nx.radius(self.G))
        print("Diametro: ", nx.diameter(self.G))
        print("Excentricidad: ", nx.eccentricity(self.G))
        print("Centro: ", nx.center(self.G))
        print("Periferia: ", nx.periphery(self.G))
        print("Densidad: ", nx.density(self.G))

grafo1 = Grafo()

grafo1.info()
grafo1.dibujoGraph()

texto = """
"3475",3592,"Male",52,"GBR",217.4833333,"Regular"
"13594",13853,"Female",40,"NY",272.55,"Regular"
"12012",12256,"Male",31,"FRA",265.2833333,"Regular"
"10236",10457,"Female",33,"MI",256.15,"Regular"
"9476",9686,"Male",33,"NY",252.25,"Regular"
"1720",1784,"Male",40,"NJ",201.9666667,"Regular"
"15736",16020,"Female",30,"CA",283.5666667,"Regular"
"""

#Hallar expresion regular para extraer una lista con los nombres de ciudades
# ['GBR', 'NY', 'FRA', 'MI', ....]
x = re.findall('[A-Z]{2,}', texto)
print(x)