# -*- coding: utf-8 -*-
"""
Created on Wed Mar 26 22:44:50 2025

@author: MARCELOFGB
"""

import heapq
import networkx as nx
import matplotlib.pyplot as plt

# Función heurística (distancia en línea recta desde un nodo al objetivo)
def heuristic(node, target, positions):
    x1, y1 = positions[node]
    x2, y2 = positions[target]
    return ((x1 - x2)**2 + (y1 - y2)**2)**0.5  # Distancia euclidiana

# Búsqueda Voraz (Greedy Best-First Search)
def greedy_best_first_search(graph, start, target, positions):
    
    visited = set()  # Nodos ya visitados
    priority_queue = [(heuristic(start, target, positions), start, [start])]  # (heurística, nodo, camino)
    
    while priority_queue:
        (priority, current_node, path) = heapq.heappop(priority_queue)  # Obtiene el nodo con menor heurística
        
        if current_node in visited:
            continue
        
        visited.add(current_node)
        
        if current_node == target:
            return path  # ¡Objetivo encontrado!
        
        for neighbor in graph.neighbors(current_node):
            if neighbor not in visited:
                new_path = path + [neighbor]
                priority = heuristic(neighbor, target, positions)  # Heurística del vecino
                heapq.heappush(priority_queue, (priority, neighbor, new_path))  # Agrega a la cola de prioridad
    
    return None  # No se encontró un camino

# Crear un grafo de ejemplo
graph = nx.Graph()
graph.add_edges_from([
    ('A', 'B'), ('A', 'C'), ('B', 'D'), ('B', 'E'),
    ('C', 'F'), ('C', 'G'), ('D', 'H'), ('E', 'I'),
    ('F', 'J'), ('G', 'K'), ('H', 'L'), ('I', 'M'),
    ('L', 'N'), ('M', 'O')
])

# Posiciones de los nodos para visualización
positions = {
    'A': (0, 5), 'B': (2, 7), 'C': (2, 3), 'D': (4, 8),
    'E': (4, 6), 'F': (4, 2), 'G': (4, 0), 'H': (6, 9),
    'I': (6, 5), 'J': (6, 1), 'K': (6, -1), 'L': (8, 8),
    'M': (8, 4), 'N': (10, 7), 'O': (10, 3)
}

# Definir el nodo inicial y el objetivo
start_node = 'A'
target_node = 'O'

# Ejecutar la búsqueda voraz
path = greedy_best_first_search(graph, start_node, target_node, positions)

# Visualización del grafo y el camino encontrado
plt.figure(figsize=(12, 8))
nx.draw(graph, positions, with_labels=True, node_size=500, node_color='skyblue', font_size=12)

if path:
    path_edges = list(zip(path[:-1], path[1:]))
    nx.draw_networkx_edges(graph, positions, edgelist=path_edges, edge_color='red', width=2)
    plt.title(f"Búsqueda Voraz: Camino de {start_node} a {target_node}")
    print("Camino encontrado:", path)
else:
    plt.title(f"Búsqueda Voraz: No se encontró camino de {start_node} a {target_node}")
    print("No se encontró un camino.")

plt.show()