# -*- coding: utf-8 -*-
"""
Created on Fri Jun 24 02:01:41 2022

@author: wilfr
"""

import networkx as nx
import matplotlib.pyplot as plt

class Grafo:
    def __init__(self):
        self.G = nx.Graph()
        self.cargoGraph()
        
        self.pos = nx.shell_layout(self.G)


    def cargoGraph(self):
        self.G.add_weighted_edges_from([
        ('a', 'b', 12),
        ('a', 'd', 14),
        ('b', 'c', 7),
        ('b', 'd', 4),
        ('b', 'e', 11),
        ('b', 't', 23),
        ('c', 'e', 2),
        ('c', 't', 10),
        ('d', 'e', 6),
        ('e', 't', 9)
    ])
        

    def dibujoGraph(self):
        nx.draw_networkx_nodes(self.G , self.pos, node_size=600)
        nx.draw_networkx_labels(self.G , self.pos, font_size=10)
        nx.draw_networkx_edges(self.G , self.pos, width=2, arrowstyle="<|-|>", arrowsize=10)

        labels = nx.get_edge_attributes(self.G , 'weight')
        nx.draw_networkx_edge_labels(self.G , self.pos, edge_labels=labels)
        plt.show()


g1 = Grafo()