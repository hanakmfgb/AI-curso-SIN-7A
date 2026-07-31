# -*- coding: utf-8 -*-
"""
Created on Wed Mar 26 22:58:33 2025

@author: MARCELOFGB
"""

import heapq
import networkx as nx
import matplotlib.pyplot as plt

# Definir el grafo como un diccionario de adyacencia
graph = {
    'Arad': {'Sibiu': 140, 'Timisoara': 118, 'Zerind': 75},
    'Bucharest': {'Urziceni': 85, 'Pitesti': 101, 'Giurgiu': 90, 'Fagaras': 211},
    'Craiova': {'Drobeta': 120, 'Rimnicu Vilcea': 146, 'Pitesti': 138},
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
    'Sibiu': {'Arad': 140, 'Fagaras': 99, 'Oradea': 151, 'Rimnicu Vilcea': 80},
    'Timisoara': {'Arad': 118, 'Lugoj': 111},
    'Urziceni': {'Bucharest': 85, 'Hirsova': 98},
    'Vaslui': {'Iasi': 92, 'Urziceni': 142},
    'Zerind': {'Arad': 75, 'Oradea': 71}
}

# Heurística (distancia euclidiana a Bucharest)
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

def greedy_best_first_search(graph, heuristic, start, target):
    """
    Implementación de la búsqueda voraz (Greedy Best-First Search).

    Args:
        graph (dict): Diccionario que representa el grafo.
        heuristic (dict): Diccionario con la heurística para cada nodo.
        start (str): Nodo inicial.
        target (str): Nodo objetivo.

    Returns:
        tuple: (path, visited_nodes)
               path (list): Lista de nodos que forman el camino encontrado.
               visited_nodes (set): Conjunto de nodos visitados.
    """
    visited = set()
    priority_queue = [(heuristic[start], start, [start])]  # (prioridad, nodo, camino)

    while priority_queue:
        (priority, current_node, path) = heapq.heappop(priority_queue)

        if current_node in visited:
            continue

        visited.add(current_node)

        if current_node == target:
            return path, visited

        for neighbor, cost in graph[current_node].items():
            if neighbor not in visited:
                heapq.heappush(priority_queue, (heuristic[neighbor], neighbor, path + [neighbor]))

    return None, visited  # No se encontró un camino

# Ejecutar la búsqueda
start_node = 'Arad'
target_node = 'Bucharest'
path, visited_nodes = greedy_best_first_search(graph, heuristic, start_node, target_node)

print(f"Camino encontrado: {path}")
print(f"Nodos visitados: {visited_nodes}")


# Crear el grafo de NetworkX para la visualización
G = nx.Graph()
for node, neighbors in graph.items():
    for neighbor, cost in neighbors.items():
        G.add_edge(node, neighbor, weight=cost)

# Posiciones de los nodos (aproximadas para que se parezca a la imagen)
pos = {
    'Arad': (1, 7),
    'Zerind': (2, 8),
    'Oradea': (3, 9),
    'Sibiu': (4, 7),
    'Timisoara': (2, 5),
    'Lugoj': (3, 4),
    'Mehadia': (4, 3),
    'Drobeta': (3, 2),
    'Craiova': (5, 2),
    'Rimnicu Vilcea': (6, 6),
    'Pitesti': (7, 5),
    'Fagaras': (6, 8),
    'Bucharest': (8, 4),
    'Giurgiu': (7, 1),
    'Urziceni': (9, 5),
    'Hirsova': (10, 4),
    'Eforie': (11, 2),
    'Vaslui': (10, 7),
    'Iasi': (9, 8),
    'Neamt': (10, 9)
}


# Dibujar el grafo
plt.figure(figsize=(12, 8))
nx.draw_networkx_nodes(G, pos, node_size=1500, node_color='skyblue')
nx.draw_networkx_edges(G, pos, width=2)
nx.draw_networkx_labels(G, pos, font_size=12, font_family='sans-serif')

# Dibujar las etiquetas de las aristas (distancias)
edge_labels = {(i, j): G[i][j]['weight'] for i, j in G.edges()}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=10)

# Dibujar la heurística como etiquetas de los nodos
heuristic_labels = {node: str(heuristic[node]) for node in G.nodes()}
pos_labels = {node: (x, y - 0.4) for node, (x, y) in pos.items()}  # Ajustar la posición de las etiquetas
nx.draw_networkx_labels(G, pos_labels, labels=heuristic_labels, font_size=8, font_color='red')

# Resaltar el camino encontrado
path_edges = list(zip(path,path[1:]))
nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=3)

# Resaltar el nodo inicial y el nodo objetivo
nx.draw_networkx_nodes(G, pos, nodelist=[start_node], node_color='orange', node_size=2000)
nx.draw_networkx_nodes(G, pos, nodelist=[target_node], node_color='lightgreen', node_size=2000)

plt.title("Greedy Best-First Search")
plt.axis('off')
plt.show()



# Visualización del árbol expandido (simplificado)
def visualize_search_tree(graph, heuristic, start, target):
    """
    Visualiza el árbol de búsqueda generado por Greedy Best-First Search.
    """
    G_tree = nx.DiGraph()
    visited = set()
    queue = [(heuristic[start], start, None)]  # (prioridad, nodo, padre)

    while queue:
        priority, current_node, parent = queue.pop(0)

        if current_node in visited:
            continue

        visited.add(current_node)

        if parent is not None:
            G_tree.add_edge(parent, current_node)
        else:
            G_tree.add_node(current_node)


        if current_node == target:
            break

        neighbors = sorted(graph[current_node].items(), key=lambda item: heuristic[item[0]])
        for neighbor, cost in neighbors:
            if neighbor not in visited:
                queue.append((heuristic[neighbor], neighbor, current_node))
                queue.sort(key=lambda x: x[0]) #Mantener la cola ordenada



    pos = nx.spring_layout(G_tree)  # Layout para el árbol

    plt.figure(figsize=(10, 6))
    nx.draw_networkx_nodes(G_tree, pos, node_size=1500, node_color='skyblue')
    nx.draw_networkx_edges(G_tree, pos, edge_color='gray')
    nx.draw_networkx_labels(G_tree, pos, font_size=12, font_family='sans-serif')
    plt.title("Árbol de Búsqueda Expandido (Greedy Best-First)")
    plt.axis('off')
    plt.show()


# Visualizar el árbol de búsqueda
visualize_search_tree(graph, heuristic, start_node, target_node)