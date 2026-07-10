# -*- coding: utf-8 -*-
"""
Created on Thu Mar  6 21:52:31 2025

@author: MARCELOFGB
"""

import networkx as nx
import matplotlib.pyplot as plt

# 1. Creación de un grafo
#   - Podemos crear grafos vacíos y luego añadir nodos y aristas.
#   - O podemos crear grafos directamente con nodos y aristas predefinidos.

# Grafo vacío
G = nx.Graph()

# Añadir nodos
G.add_node(1)
G.add_node(2)
G.add_node(3)
G.add_node(4)
G.add_node("A") # Los nodos pueden ser cualquier objeto hasheable (string, int, tuple, etc.)

# Añadir aristas (conexiones entre nodos)
G.add_edge(1, 2)
G.add_edge(2, 3)
G.add_edge(3, "A")
G.add_edge("A", 1)
G.add_edge(4,"A")


# Forma alternativa de crear un grafo con datos iniciales:
H = nx.Graph([(0, 1), (1, 2), (2, 3)]) # Lista de tuplas que representan las aristas

# Combinar grafos
G.add_nodes_from(H) # Añade los nodos de H a G (si no existen ya)
G.add_edges_from(H.edges()) # Añade las aristas de H a G

print("Nodos del grafo G:", G.nodes)
print("Aristas del grafo G:", G.edges)



# 2. Atributos de Nodos y Aristas
#   - Podemos asociar atributos a nodos y aristas.  Esto es muy útil para representar datos adicionales sobre la red.

# Atributos de Nodos:
G.nodes[1]['weight'] = 10  # Asigna un peso al nodo 1
G.nodes[2]['label'] = "nodo_importante" # Asigna una etiqueta al nodo 2

# Atributos de Aristas:
G.edges[1, 2]['weight'] = 5   # Asigna un peso a la arista entre 1 y 2
G.edges[3, 'A']['relation'] = "amigo" # Asigna una relación a la arista entre 3 y 'A'

print("\nAtributos del nodo 1:", G.nodes[1])
print("Atributos de la arista (1, 2):", G.edges[1, 2])



# 3. Tipos de Grafos

# - Graph: Grafos no dirigidos (las aristas no tienen dirección). (Ya hemos estado usando este)
# - DiGraph: Grafos dirigidos (las aristas tienen una dirección).
# - MultiGraph: Grafos que permiten múltiples aristas entre dos nodos.
# - MultiDiGraph: Grafos dirigidos que permiten múltiples aristas entre dos nodos.

DG = nx.DiGraph()  # Grafo Dirigido
DG.add_edge(1, 2)  # La arista va de 1 a 2, no de 2 a 1.
DG.add_edge(2, 1) # Podemos agregar una arista en la dirección opuesta
print("\nNodos del grafo dirigido DG:", DG.nodes)
print("Aristas del grafo dirigido DG:", DG.edges)



# 4. Análisis Básico del Grafo

# Grado de un nodo:  El número de aristas conectadas a un nodo.
print("\nGrado del nodo 1 en G:", G.degree(1)) # Para grafos no dirigidos
print("Grado de entrada del nodo 1 en DG:", DG.in_degree(1)) # Para grafos dirigidos
print("Grado de salida del nodo 1 en DG:", DG.out_degree(1)) # Para grafos dirigidos

# Vecinos de un nodo:  Los nodos directamente conectados a un nodo.
print("Vecinos del nodo 1 en G:", list(G.neighbors(1)))

# Calcular la longitud del camino más corto entre dos nodos
try:
    shortest_path_length = nx.shortest_path_length(G, source=1, target=3)
    print("Longitud del camino más corto entre 1 y 3:", shortest_path_length)
except nx.NetworkXNoPath:
    print("No existe camino entre 1 y 3.")

# Verificar si el grafo está conectado
print("¿Está el grafo G conectado?:", nx.is_connected(G))



# 5. Visualización del Grafo
#   - NetworkX en sí mismo no tiene capacidades de visualización sofisticadas,
#     pero se integra muy bien con Matplotlib.

plt.figure(figsize=(8, 6))  # Ajusta el tamaño de la figura

#  Opciones de diseño (layout) para la visualización.  Hay varios disponibles.
#  Algunos comunes son:
#   - spring_layout:  Intenta colocar los nodos de forma que las aristas tengan longitudes similares.
#   - circular_layout:  Coloca los nodos en un círculo.
#   - kamada_kawai_layout: Utiliza un algoritmo para minimizar la energía del grafo.
#   - random_layout: Coloca los nodos aleatoriamente.
pos = nx.spring_layout(G)  # Calcula la posición de los nodos

# Dibujar los nodos
nx.draw_networkx_nodes(G, pos, node_color='skyblue', node_size=700)

# Dibujar las aristas
nx.draw_networkx_edges(G, pos, edge_color='gray')

# Dibujar las etiquetas de los nodos
nx.draw_networkx_labels(G, pos, font_size=12, font_family='sans-serif')

# Mostrar el gráfico
plt.title("Ejemplo de Grafo con NetworkX")
plt.axis('off')  # Oculta los ejes
plt.show()


pos = nx.spring_layout(DG)
nx.draw_networkx_edges(DG, pos, edge_color='gray')

# Dibujar las etiquetas de los nodos
nx.draw_networkx_labels(DG, pos, font_size=12, font_family='sans-serif')
plt.title("Ejemplo de Grafo con NetworkX")
plt.axis('off')  # Oculta los ejes
plt.show()


# 6. Algoritmos Comunes

# Encontrar componentes conectados (para grafos no dirigidos)
connected_components = list(nx.connected_components(G))
print("\nComponentes conectados:", connected_components)

# Encontrar componentes fuertemente conectados (para grafos dirigidos)
#strongly_connected_components = list(nx.strongly_connected_components(DG))
#print("Componentes fuertemente conectados:", strongly_connected_components) # Esto dará error porque no definimos un grafo dirigido conectado.  Tendrías que ajustar el grafo DG para que lo estuviera.


print("\n¡Ejemplo completado!")