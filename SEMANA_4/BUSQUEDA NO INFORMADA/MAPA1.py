# -*- coding: utf-8 -*-
"""
Created on Tue Mar 18 22:24:46 2025

@author: MARCELOFGB
"""

import networkx as nx
import matplotlib.pyplot as plt
import heapq

def busqueda_costo_uniforme(grafo, inicio, objetivo):
    """
    Implementa la búsqueda de costo uniforme para encontrar el camino más corto
    entre dos nodos en un grafo.

    Args:
        grafo (dict): Diccionario que representa el grafo donde las claves son los nodos
                     y los valores son una lista de tuplas (vecino, costo).
        inicio (str): El nodo de inicio.
        objetivo (str): El nodo objetivo.

    Returns:
        tuple: Una tupla que contiene el camino más corto (lista de nodos) y el costo total.
               Retorna (None, float('inf')) si no se encuentra un camino.
    """

    cola_prioridad = [(0, inicio, [])]  # (costo, nodo, camino)
    visitados = set()

    while cola_prioridad:
        costo, nodo, camino = heapq.heappop(cola_prioridad)

        if nodo in visitados:
            continue
        visitados.add(nodo)

        camino = camino + [nodo]

        if nodo == objetivo:
            return camino, costo

        for vecino, costo_vecino in grafo[nodo].items():
            if vecino not in visitados:
                nuevo_costo = costo + costo_vecino
                heapq.heappush(cola_prioridad, (nuevo_costo, vecino, camino))

    return None, float('inf')  # No se encontró camino

# Definición del grafo basado en la imagen proporcionada
grafo = {
    'Oradea': {'Zerind': 71, 'Sibiu': 151},
    'Zerind': {'Oradea': 71, 'Arad': 75},
    'Arad': {'Zerind': 75, 'Sibiu': 140, 'Timisoara': 118},
    'Timisoara': {'Arad': 118, 'Lugoj': 111},
    'Lugoj': {'Timisoara': 111, 'Mehadia': 70},
    'Mehadia': {'Lugoj': 70, 'Drobeta': 75},
    'Drobeta': {'Mehadia': 75, 'Craiova': 120},
    'Craiova': {'Drobeta': 120, 'Rimnicu Vilcea': 146, 'Pitesti': 138},
    'Sibiu': {'Arad': 140, 'Oradea': 151, 'Fagaras': 99, 'Rimnicu Vilcea': 80},
    'Fagaras': {'Sibiu': 99, 'Bucharest': 211},
    'Rimnicu Vilcea': {'Sibiu': 80, 'Craiova': 146, 'Pitesti': 97},
    'Pitesti': {'Rimnicu Vilcea': 97, 'Craiova': 138, 'Bucharest': 101},
    'Bucharest': {'Fagaras': 211, 'Pitesti': 101, 'Giurgiu': 90, 'Urziceni': 85},
    'Giurgiu': {'Bucharest': 90},
    'Urziceni': {'Bucharest': 85, 'Vaslui': 142, 'Hirsova': 98},
    'Vaslui': {'Urziceni': 142, 'Iasi': 92},
    'Iasi': {'Vaslui': 92, 'Neamt': 87},
    'Neamt': {'Iasi': 87},
    'Hirsova': {'Urziceni': 98, 'Eforie': 86},
    'Eforie': {'Hirsova': 86}
}

# Visualización del grafo
G = nx.Graph()
for nodo, vecinos in grafo.items():
    for vecino, costo in vecinos.items():
        G.add_edge(nodo, vecino, weight=costo)

pos = nx.spring_layout(G, seed=42)  # Para una disposición consistente
plt.figure(figsize=(12, 8))
nx.draw(G, pos, with_labels=True, node_size=1500, node_color="skyblue", font_size=10)
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
plt.title("Grafo de Ciudades en Rumania")
plt.show()

# Ejecución de la búsqueda de costo uniforme
inicio = 'Zerind'
objetivo = 'Bucharest'
camino, costo = busqueda_costo_uniforme(grafo, inicio, objetivo)

if camino:
    print(f"Camino más corto de {inicio} a {objetivo}: {camino}")
    print(f"Costo total: {costo}")
else:
    print(f"No se encontró camino de {inicio} a {objetivo}")