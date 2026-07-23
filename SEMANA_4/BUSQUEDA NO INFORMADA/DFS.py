# -*- coding: utf-8 -*-
"""
Created on Sun Mar 16 18:05:59 2025

@author: MARCELOFGB
"""

import networkx as nx
import matplotlib.pyplot as plt

# Crear un grafo de ejemplo
G = nx.Graph()
G.add_edges_from([
    ('A', 'B'), ('A', 'C'), ('B', 'D'), ('B', 'E'),
    ('C', 'B'),('C', 'F'), ('C', 'G'), ('D', 'H'), ('E', 'I'),
    ('F', 'J'), ('G', 'K'), ('G','H'), ('K','I')
])

# Función para búsqueda en profundidad (DFS)
def dfs(graph, start, target, max_depth=4):  # Limitar la profundidad a 4
    visited = set()
    stack = [(start, [start])]  # Almacena el nodo y el camino hasta él

    while stack:
        (node, path) = stack.pop()
        if node not in visited:
            visited.add(node)
            if node == target:
                return path  # Retorna el camino si encuentra el objetivo
            if len(path) <= max_depth:  # Verifica el límite de profundidad
                for neighbor in graph[node]:
                    stack.append((neighbor, path + [neighbor]))
    return None  # Retorna None si no encuentra el objetivo

# Función para búsqueda en anchura (BFS)
def bfs(graph, start, target):
    visited = set()
    queue = [(start, [start])]  # Almacena el nodo y el camino hasta él

    while queue:
        (node, path) = queue.pop(0)
        if node not in visited:
            visited.add(node)
            if node == target:
                return path  # Retorna el camino si encuentra el objetivo
            for neighbor in graph[node]:
                queue.append((neighbor, path + [neighbor]))
    return None  # Retorna None si no encuentra el objetivo

# Ejecutar las búsquedas
inicio = 'A'
objetivo = 'H'
camino_dfs = dfs(G, inicio, objetivo)
camino_bfs = bfs(G, inicio, objetivo)

# Imprimir los resultados
print("Camino DFS:", camino_dfs)
print("Camino BFS:", camino_bfs)

# Visualización del grafo y los caminos
pos = nx.spring_layout(G, seed=42)  # Fijar la disposición para reproducibilidad

# Dibujar el grafo completo
nx.draw(G, pos, with_labels=True, node_size=800, node_color="skyblue", font_size=12, font_weight="bold")

# Dibujar el camino DFS en rojo
if camino_dfs:
    edges_dfs = list(zip(camino_dfs, camino_dfs[1:]))
    nx.draw_networkx_edges(G, pos, edgelist=edges_dfs, edge_color="red", width=2)

# Dibujar el camino BFS en verde
if camino_bfs:
    edges_bfs = list(zip(camino_bfs, camino_bfs[1:]))
    nx.draw_networkx_edges(G, pos, edgelist=edges_bfs, edge_color="green", width=2)

# Mostrar la leyenda
#plt.legend(["DFS Path", "BFS Path"])
plt.title("Búsqueda en Profundidad (Rojo) vs. Búsqueda en Anchura (Verde)")
plt.show()