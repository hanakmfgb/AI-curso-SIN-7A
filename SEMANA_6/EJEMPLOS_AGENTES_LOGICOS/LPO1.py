# -*- coding: utf-8 -*-
"""
Created on Sun Apr  6 21:18:18 2025

@author: MARCELOFGB
"""
import networkx as nx
import matplotlib.pyplot as plt

# 1. Base de Conocimiento (Hechos y Reglas)
# Hechos: vuelos directos (origen, destino, precio)
vuelos = [
    ("Madrid", "Paris", 80),
    ("Madrid", "Roma", 100),
    ("Madrid", "Berlin", 120),
    ("Paris", "Berlin", 70),
    ("Paris", "Londres", 60),
    ("Roma", "Berlin", 90),
    ("Berlin", "Londres", 80),
    ("Berlin", "Viena", 100),
    ("Londres", "Viena", 110),
    ("Madrid", "Lisboa", 50),
    ("Lisboa", "Londres", 90),
    ("Madrid", "Bruselas", 90),
    ("Bruselas", "Londres", 50),
    ("Madrid", "Copenhague", 150),
    ("Copenhague", "Oslo", 70),
    ("Oslo", "Estocolmo", 80),
    ("Copenhague", "Estocolmo", 90),
    ("Estocolmo", "Helsinki", 100),
    ("Helsinki", "Moscu", 130),
    ("Madrid", "Varsovia", 130),
    ("Varsovia", "Kiev", 80),
    ("Kiev", "Moscu", 90)
]

#Hechos: Capitales de Europa
capitales = ["Paris", "Roma", "Berlin", "Londres", "Viena", "Lisboa", "Bruselas", "Copenhague", "Oslo", "Estocolmo", "Helsinki", "Moscu", "Varsovia", "Kiev"]

# Regla:  ruta(A, B, Costo) :- vuelo(A, B, Costo).  (vuelo directo)
# Regla:  ruta(A, B, Costo) :- vuelo(A, C, Costo1), ruta(C, B, Costo2), Costo is Costo1 + Costo2. (ruta con conexión)

# 2. Crear el Grafo
grafo = nx.Graph()
grafo.add_edges_from([(origen, destino, {'costo': precio}) for origen, destino, precio in vuelos])

# 3. Interfaz de Usuario
def mostrar_destinos(capitales):
    print("\nDestinos disponibles desde Madrid:")
    print("------------------------------------")
    print("Número | Capital")
    print("-------|--------")
    for i, capital in enumerate(capitales):
        print(f"{i+1:4}  | {capital}")
    print("------------------------------------")

def obtener_destino_usuario(capitales):
    while True:
        mostrar_destinos(capitales)
        try:
            opcion = int(input("Elige el número de destino: "))
            if 1 <= opcion <= len(capitales):
                return capitales[opcion - 1]
            else:
                print("Opción inválida. Por favor, elige un número de la lista.")
        except ValueError:
            print("Entrada inválida. Por favor, introduce un número.")

# 4. Inferencia (Búsqueda de la Ruta Más Económica)
def encontrar_ruta_mas_economica(grafo, origen, destino):
    try:
        ruta = nx.shortest_path(grafo, source=origen, target=destino, weight='costo')
        costo = nx.shortest_path_length(grafo, source=origen, target=destino, weight='costo')
        return ruta, costo
    except nx.NetworkXNoPath:
        return None, None

# 5. Visualización del Grafo y la Ruta
def visualizar_ruta(grafo, ruta):
    pos = nx.spring_layout(grafo, seed=42)  # Layout para mejor visualización
    nx.draw(grafo, pos, with_labels=True, node_size=1500, node_color="skyblue", font_size=10)
    #Etiquetas de los costos
    labels = nx.get_edge_attributes(grafo,'costo')
    nx.draw_networkx_edge_labels(grafo,pos,edge_labels=labels)

    ruta_edges = list(zip(ruta, ruta[1:]))
    nx.draw_networkx_edges(grafo, pos, edgelist=ruta_edges, edge_color="red", width=2)
    plt.title("Ruta Óptima")
    plt.show()

# --- Programa Principal ---
if __name__ == "__main__":
    print("¡Bienvenido al planificador de vuelos inteligentes!")

    destino = obtener_destino_usuario(capitales)

    if destino:
        ruta, costo = encontrar_ruta_mas_economica(grafo, "Madrid", destino)

        if ruta:
            print(f"\nRuta más económica de Madrid a {destino}: {ruta}")
            print(f"Costo total: {costo} euros")
            visualizar_ruta(grafo, ruta)
        else:
            print(f"No se encontró ruta de Madrid a {destino}.")
    else:
        print("No se seleccionó un destino válido.")
