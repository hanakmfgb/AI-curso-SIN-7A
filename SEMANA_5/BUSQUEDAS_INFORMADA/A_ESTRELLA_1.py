# -*- coding: utf-8 -*-
"""
Created on Fri Mar 28 23:26:10 2025

@author: MARCELOFGB
"""

import heapq
import numpy as np
import matplotlib.pyplot as plt

class Nodo:
    def __init__(self, posicion, padre=None):
        self.posicion = tuple(posicion)  # Convertir a tupla para usar como clave en diccionarios
        self.padre = padre
        self.g = 0  # Costo desde el nodo inicial
        self.h = 0  # Heurística (estimación del costo hasta el objetivo)
        self.f = 0  # Costo total estimado (g + h)

    def __eq__(self, otro):
        return self.posicion == otro.posicion

    def __lt__(self, otro):  # Necesario para heapq
        return self.f < otro.f

def a_estrella(mapa, inicio, fin):
    """
    Implementación del algoritmo A* para encontrar el camino más corto en un mapa.

    Args:
        mapa (numpy.ndarray): Un array 2D que representa el mapa. 0 es espacio libre, 1 es obstáculo.
        inicio (tuple): Coordenadas (fila, columna) del nodo inicial.
        fin (tuple): Coordenadas (fila, columna) del nodo objetivo.

    Returns:
        list: Una lista de tuplas que representan el camino desde el inicio hasta el fin,
              o None si no se encuentra un camino.
    """

    inicio_nodo = Nodo(inicio, None)
    fin_nodo = Nodo(fin, None)

    cola_abierta = []
    heapq.heappush(cola_abierta, inicio_nodo)

    nodos_visitados = set()  # Conjunto para rastrear nodos visitados (usando tuplas)
    nodos_visitados.add(inicio_nodo.posicion)

    while cola_abierta:
        nodo_actual = heapq.heappop(cola_abierta)

        if nodo_actual == fin_nodo:
            camino = []
            actual = nodo_actual
            while actual is not None:
                camino.append(actual.posicion)
                actual = actual.padre
            return camino[::-1]  # Invertir el camino para que comience en el inicio

        # Generar nodos adyacentes (vecinos)
        adyacentes = []
        for movimiento in [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]:  # Movimientos permitidos (incluyendo diagonales)
            nueva_posicion = (nodo_actual.posicion[0] + movimiento[0], nodo_actual.posicion[1] + movimiento[1])

            # Verificar límites del mapa
            if (nueva_posicion[0] > (mapa.shape[0] - 1) or
                nueva_posicion[0] < 0 or
                nueva_posicion[1] > (mapa.shape[1] - 1) or
                nueva_posicion[1] < 0):
                continue

            # Verificar si es un obstáculo
            if mapa[nueva_posicion[0]][nueva_posicion[1]] != 0:
                continue

            nuevo_nodo = Nodo(nueva_posicion, nodo_actual)
            adyacentes.append(nuevo_nodo)

        # Procesar los nodos adyacentes
        for hijo in adyacentes:
            # Verificar si el nodo ya fue visitado (usando la posición como clave)
            if hijo.posicion in nodos_visitados:
                continue

            # Calcular g, h y f
            hijo.g = nodo_actual.g + 1  # El costo es 1 para moverse a un nodo adyacente
            hijo.h = ((hijo.posicion[0] - fin_nodo.posicion[0]) ** 2) + ((hijo.posicion[1] - fin_nodo.posicion[1]) ** 2) # Distancia Euclídea al objetivo
            hijo.f = hijo.g + hijo.h

            # Agregar el hijo a la cola abierta
            heapq.heappush(cola_abierta, hijo)
            nodos_visitados.add(hijo.posicion)


    return None  # No se encontró un camino

# Ejemplo de uso
if __name__ == '__main__':
    # Crear un mapa de ejemplo (0: espacio libre, 1: obstáculo)
    mapa = np.array([
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1,1, 1, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ])

    inicio = (4, 2)
    fin = (6, 17)

    camino = a_estrella(mapa, inicio, fin)

    if camino:
        print("Camino encontrado:", camino)

        # Visualizar el mapa y el camino
        plt.imshow(mapa, cmap='gray', origin='upper')  # 'upper' para que el origen esté en la esquina superior izquierda
        plt.plot([s[1] for s in camino], [s[0] for s in camino], color='blue', linewidth=2.5, label='RUTA') # Intercambiar x e y para plot
        plt.plot(inicio[1], inicio[0], marker="o", markersize=12, markeredgecolor="green", markerfacecolor="green", label='INICIO') # Intercambiar x e y para plot
        plt.plot(fin[1], fin[0], marker="o", markersize=12, markeredgecolor="red", markerfacecolor="red", label='OBJETIVO') # Intercambiar x e y para plot


        plt.title('A* Resultado de búsqueda del camino óptimo')
        plt.xlabel('Columnas')
        plt.ylabel('Filas')
        plt.grid(True)
        plt.legend()
        plt.show()
    else:
        print("No se encontró un camino.")