# -*- coding: utf-8 -*-
"""
Created on Tue Mar 18 22:34:30 2025

@author: MARCELOFGB
"""

import networkx as nx
import matplotlib.pyplot as plt
import heapq

def uniform_cost_search(graph, start, goal):
    """
    Implementa la búsqueda de costo uniforme para encontrar el camino de costo mínimo
    desde el nodo 'start' al nodo 'goal' en un grafo.

    Args:
        graph (dict): Un diccionario que representa el grafo. Las claves son los nodos y
                       los valores son listas de tuplas (vecino, costo).
        start (str): El nodo inicial.
        goal (str): El nodo objetivo.

    Returns:
        tuple: Una tupla que contiene:
            - La lista de nodos que forman el camino de costo mínimo (en orden).
            - El costo total del camino.
            Retorna (None, None) si no se encuentra un camino.
    """

    frontier = [(0, start, [])]  # (costo, nodo, camino)
    explored = set()

    while frontier:
        cost, current_node, path = heapq.heappop(frontier)

        if current_node in explored:
            continue

        explored.add(current_node)
        path = path + [current_node]

        if current_node == goal:
            return path, cost

        for neighbor, neighbor_cost in graph[current_node].items():
            heapq.heappush(frontier, (cost + neighbor_cost, neighbor, path))

    return None, None  # No se encontró un camino

def visualize_graph(graph, path=None):
    """
    Visualiza el grafo con NetworkX y Matplotlib.

    Args:
        graph (dict): Un diccionario que representa el grafo.
        path (list, optional): Una lista de nodos que representan el camino a destacar.
                                 Defaults to None.
    """

    G = nx.Graph()

    # Añade nodos y aristas al grafo de NetworkX
    for node, neighbors in graph.items():
        for neighbor, cost in neighbors.items():
            G.add_edge(node, neighbor, weight=cost)

    # Define las posiciones de los nodos para que se parezcan al mapa de Rumania
    pos = {
        'Arad': (1, 5), 'Zerind': (1.5, 6), 'Oradea': (2, 7), 'Sibiu': (3, 5),
        'Fagaras': (4, 4), 'Rimnicu Vilcea': (3, 3), 'Pitesti': (4, 2),
        'Bucharest': (5, 1), 'Craiova': (3, 1), 'Drobeta': (2, 0),
        'Mehadia': (2, 1.5), 'Timisoara': (1, 3), 'Lugoj': (1.5, 2.5),
        'Giurgiu': (5, 0), 'Urziceni': (6, 1), 'Vaslui': (7, 3),
        'Iasi': (7, 4), 'Neamt': (6.5, 5), 'Hirsova': (7, 1.5),
        'Eforie': (8, 1)
    }

    # Etiqueta de pesos de aristas
    edge_labels = {(i, j): G[i][j]['weight'] for (i, j) in G.edges()}

    # Dibuja el grafo
    plt.figure(figsize=(12, 8))
    nx.draw_networkx_nodes(G, pos, node_size=700, node_color="skyblue")
    nx.draw_networkx_edges(G, pos, width=2, edge_color="gray")
    nx.draw_networkx_labels(G, pos, font_size=8, font_family="sans-serif")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)

    # Si hay un camino, destácalo
    if path:
        path_edges = list(zip(path, path[1:]))
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color="red", width=3)

    plt.title("Mapa de Rumania con Búsqueda de Costo Uniforme")
    plt.axis("off")
    plt.show()

# Define el grafo de Rumania
romania_map = {
    'Arad': {'Zerind': 75, 'Sibiu': 140, 'Timisoara': 118},
    'Zerind': {'Arad': 75, 'Oradea': 71},
    'Oradea': {'Zerind': 71, 'Sibiu': 151},
    'Sibiu': {'Arad': 140, 'Oradea': 151, 'Fagaras': 99, 'Rimnicu Vilcea': 80},
    'Fagaras': {'Sibiu': 99, 'Bucharest': 211},
    'Rimnicu Vilcea': {'Sibiu': 80, 'Pitesti': 97, 'Craiova': 146},
    'Pitesti': {'Rimnicu Vilcea': 97, 'Craiova': 138, 'Bucharest': 101},
    'Bucharest': {'Fagaras': 211, 'Pitesti': 101, 'Giurgiu': 90, 'Urziceni': 85},
    'Craiova': {'Rimnicu Vilcea': 146, 'Pitesti': 138, 'Drobeta': 120},
    'Drobeta': {'Craiova': 120, 'Mehadia': 75},
    'Mehadia': {'Drobeta': 75, 'Lugoj': 70},
    'Timisoara': {'Arad': 118, 'Lugoj': 111},
    'Lugoj': {'Timisoara': 111, 'Mehadia': 70},
    'Giurgiu': {'Bucharest': 90},
    'Urziceni': {'Bucharest': 85, 'Vaslui': 142, 'Hirsova': 98},
    'Vaslui': {'Urziceni': 142, 'Iasi': 92},
    'Iasi': {'Vaslui': 92, 'Neamt': 87},
    'Neamt': {'Iasi': 87},
    'Hirsova': {'Urziceni': 98, 'Eforie': 86},
    'Eforie': {'Hirsova': 86}
}

# Encuentra el camino de Zerind a Bucharest
path, cost = uniform_cost_search(romania_map, 'Arad', 'Neamt')

if path:
    print("Camino encontrado:", path)
    print("Costo total:", cost)
    visualize_graph(romania_map, path)
else:
    print("No se encontró un camino.")
    visualize_graph(romania_map)  # Muestra el grafo completo aunque no haya camino