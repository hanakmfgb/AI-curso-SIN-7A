# -*- coding: utf-8 -*-
"""
Created on Wed Mar 26 22:52:04 2025

@author: MARCELOFGB
"""
import heapq
import networkx as nx
import matplotlib.pyplot as plt
import math

# Definición de las distancias heurísticas (distancia euclidiana a Bucharest)
heuristic = {
    'Arad': 366,
    'Bucharest': 0,
    'Craiova': 160,
    'Drobeta': 242,
    'Eforie': 161,
    'Fagaras': 176,
    'Giurgiu': 77,
    'Hirsova': 151,
    'Iasi': 226,
    'Lugoj': 244,
    'Mehadia': 241,
    'Neamt': 234,
    'Oradea': 380,
    'Pitesti': 100,
    'Rimnicu Vilcea': 193,
    'Sibiu': 253,
    'Timisoara': 329,
    'Urziceni': 80,
    'Vaslui': 199,
    'Zerind': 374
}

# Definición del grafo
graph = {
    'Arad': {'Sibiu': 140, 'Timisoara': 118, 'Zerind': 75},
    'Bucharest': {'Fagaras': 211, 'Giurgiu': 90, 'Pitesti': 101, 'Urziceni': 85},
    'Craiova': {'Drobeta': 120, 'Pitesti': 138, 'Rimnicu Vilcea': 146},
    'Drobeta': {'Mehadia': 75, 'Craiova': 120},
    'Eforie': {'Hirsova': 86},
    'Fagaras': {'Sibiu': 99, 'Bucharest': 211},
    'Giurgiu': {'Bucharest': 90},
    'Hirsova': {'Urziceni': 98, 'Eforie': 86},
    'Iasi': {'Neamt': 87, 'Vaslui': 92},
    'Lugoj': {'Timisoara': 111, 'Mehadia': 70},
    'Mehadia': {'Lugoj': 70, 'Drobeta': 75},
    'Neamt': {'Iasi': 87},
    'Oradea': {'Zerind': 71, 'Sibiu': 151},
    'Pitesti': {'Rimnicu Vilcea': 97, 'Craiova': 138, 'Bucharest': 101},
    'Rimnicu Vilcea': {'Sibiu': 80, 'Pitesti': 97, 'Craiova': 146},
    'Sibiu': {'Arad': 140, 'Oradea': 151, 'Fagaras': 99, 'Rimnicu Vilcea': 80},
    'Timisoara': {'Arad': 118, 'Lugoj': 111},
    'Urziceni': {'Bucharest': 85, 'Hirsova': 98, 'Vaslui': 142},
    'Vaslui': {'Urziceni': 142, 'Iasi': 92},
    'Zerind': {'Arad': 75, 'Oradea': 71}
}

def greedy_best_first_search(graph, start, target, heuristic):
    """
    Implementación de la búsqueda voraz (Greedy Best-First Search).

    Args:
        graph (dict): Un diccionario que representa el grafo con nodos y distancias entre ellos.
        start (str): El nodo de inicio.
        target (str): El nodo objetivo.
        heuristic (dict): Un diccionario con las distancias heurísticas de cada nodo al objetivo.

    Returns:
        tuple: Una tupla que contiene la ruta encontrada (lista de nodos) y el costo total.
               Retorna (None, None) si no se encuentra una ruta.
    """
    visited = set()
    priority_queue = [(heuristic[start], start, [start], 0)]  # (heurística, nodo, ruta, costo)

    while priority_queue:
        (h, current, path, cost) = heapq.heappop(priority_queue)

        if current == target:
            return path, cost

        if current in visited:
            continue
        visited.add(current)

        for neighbor, distance in graph[current].items():
            if neighbor not in visited:
                new_cost = cost + distance
                heapq.heappush(priority_queue, (heuristic[neighbor], neighbor, path + [neighbor], new_cost))

    return None, None  # No se encontró una ruta


def visualize_graph(graph, heuristic, path=None, start=None, target=None):
    """
    Visualiza el grafo con NetworkX y Matplotlib.

    Args:
        graph (dict): Un diccionario que representa el grafo.
        heuristic (dict): Un diccionario con las distancias heurísticas.
        path (list): La ruta encontrada por el algoritmo de búsqueda (opcional).
    """

    G = nx.Graph()
    for node, neighbors in graph.items():
        for neighbor, distance in neighbors.items():
            G.add_edge(node, neighbor, weight=distance)

    # Posicionamiento de los nodos (layout similar a la imagen de referencia)
    pos = {
        'Arad': (1, 5), 'Zerind': (2, 6), 'Oradea': (3, 7), 'Sibiu': (4, 5), 'Timisoara': (2, 3),
        'Lugoj': (3, 2), 'Mehadia': (4, 2), 'Drobeta': (5, 1), 'Craiova': (6, 2), 'Rimnicu Vilcea': (6, 4),
        'Pitesti': (7, 3), 'Fagaras': (6, 6), 'Bucharest': (8, 3), 'Giurgiu': (8, 1), 'Urziceni': (9, 4),
        'Hirsova': (10, 2), 'Eforie': (11, 1), 'Vaslui': (10, 6), 'Iasi': (9, 7), 'Neamt': (10, 8)
    }

    plt.figure(figsize=(12, 8))

    # Dibujar nodos
    nx.draw_networkx_nodes(G, pos, node_size=700, node_color="skyblue")

    # Dibujar aristas y etiquetas de distancia
    nx.draw_networkx_edges(G, pos, edge_color="gray")
    edge_labels = {(u, v): d['weight'] for u, v, d in G.edges(data=True)}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)

    # Dibujar etiquetas de nodos
    nx.draw_networkx_labels(G, pos, font_size=10, font_family="sans-serif")

    # Dibujar distancias heurísticas
    for node, (x, y) in pos.items():
        plt.text(x + 0.2, y, f"h={heuristic[node]}", bbox=dict(facecolor='white', alpha=0.7), fontsize=8)

    # Resaltar la ruta encontrada
    if path:
        path_edges = list(zip(path[:-1], path[1:]))
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color="red", width=2)
        
        # Resaltar el nodo inicial y el nodo objetivo
        nx.draw_networkx_nodes(G, pos, nodelist=[start], node_color="orange", node_size=1200)
        nx.draw_networkx_nodes(G, pos, nodelist=[target], node_color="orange", node_size=1200)

    plt.title("Greedy Best-First Search - Ruta a Bucharest")
    plt.axis("off")
    plt.show()

# Ejemplo de uso
start_node = 'Arad'
target_node = 'Bucharest'
path, cost = greedy_best_first_search(graph, start_node, target_node, heuristic)

if path:
    print(f"Ruta encontrada: {path}")
    print(f"Costo total: {cost}")
    visualize_graph(graph, heuristic, path, start_node, target_node)
else:
    print("No se encontró una ruta.")
    visualize_graph(graph, heuristic)