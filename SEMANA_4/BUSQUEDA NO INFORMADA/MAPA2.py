# -*- coding: utf-8 -*-
"""
Created on Tue Mar 18 22:26:22 2025

@author: MARCELOFGB
"""

import heapq
import networkx as nx
import matplotlib.pyplot as plt

# Representación del grafo como un diccionario
graph = {
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

def uniform_cost_search(graph, start, goal):
    """
    Implementa la búsqueda de costo uniforme para encontrar el camino más barato
    desde el nodo 'start' hasta el nodo 'goal' en el grafo dado.

    Args:
        graph (dict): Un diccionario que representa el grafo con nodos y costos.
        start (str): El nodo inicial.
        goal (str): El nodo objetivo.

    Returns:
        tuple: Una tupla que contiene el camino óptimo (lista de nodos) y el costo total.
               Retorna (None, None) si no se encuentra un camino.
    """
    priority_queue = [(0, start)]  # (costo, nodo)
    visited = set()
    cost_so_far = {start: 0}
    path = {}

    while priority_queue:
        cost, current_node = heapq.heappop(priority_queue)

        if current_node in visited:
            continue

        visited.add(current_node)

        if current_node == goal:
            return reconstruct_path(path, current_node), cost

        for neighbor, edge_cost in graph[current_node].items():
            new_cost = cost + edge_cost
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                priority = new_cost
                heapq.heappush(priority_queue, (priority, neighbor))
                path[neighbor] = current_node

    return None, None  # No se encontró un camino

def reconstruct_path(path, current_node):
    """
    Reconstruye el camino desde el nodo inicial hasta el nodo actual
    usando el diccionario 'path' que almacena el camino recorrido.

    Args:
        path (dict): Un diccionario que mapea cada nodo a su nodo padre en el camino.
        current_node (str): El nodo final del camino a reconstruir.

    Returns:
        list: Una lista de nodos que representan el camino desde el nodo inicial
              hasta el nodo actual.
    """
    total_path = [current_node]
    while current_node in path:
        current_node = path[current_node]
        total_path.append(current_node)
    total_path.reverse()
    return total_path

def visualize_graph(graph, path=None):
    """
    Visualiza el grafo utilizando la biblioteca NetworkX, resaltando el camino dado.

    Args:
        graph (dict): Un diccionario que representa el grafo.
        path (list, optional): Una lista de nodos que representan el camino a resaltar.
                                 Defaults to None.
    """
    G = nx.Graph()
    for node, neighbors in graph.items():
        G.add_node(node)
        for neighbor, cost in neighbors.items():
            G.add_edge(node, neighbor, weight=cost)

    pos = nx.spring_layout(G,seed=44)  # Para una disposición consistente

    # Dibujar nodos
    nx.draw_networkx_nodes(G, pos, node_size=100, node_color="skyblue")
    nx.draw_networkx_labels(G, pos, font_size=7, font_family="sans-serif")

    # Dibujar aristas con etiquetas de costo
    nx.draw_networkx_edges(G, pos, width=1, edge_color="gray")
    edge_labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=7)

    # Resaltar el camino si se proporciona
    if path:
        edges = list(zip(path, path[1:]))
        nx.draw_networkx_edges(G, pos, edgelist=edges, width=3, edge_color="red")

    plt.title("Mapa de Rumania con Camino Óptimo")
    plt.show()

# Ejemplo de uso
start_node = 'Zerind'
goal_node = 'Bucharest'
path, cost = uniform_cost_search(graph, start_node, goal_node)

if path:
    print(f"Camino más barato de {start_node} a {goal_node}: {path}")
    print(f"Costo total: {cost}")
    visualize_graph(graph, path)
else:
    print(f"No se encontró un camino de {start_node} a {goal_node}")