# -*- coding: utf-8 -*-
"""
Created on Mon Mar  3 15:33:53 2025

@author: MARCELOFGB
"""

# Ejemplo de matriz 3D
matriz_3d = [
    [
        [1, 2],
        [3, 4]
    ],
    [
        [5, 6],
        [7, 8]
    ],
    [
        [9, 10],
        [11, 12]
    ]
]

# Dimensiones de la matriz (profundidad x filas x columnas)
profundidad = len(matriz_3d)
filas = len(matriz_3d[0])
columnas = len(matriz_3d[0][0])

# Imprimir la matriz
print('---Matriz 3D----')
for capa in matriz_3d:
    for fila in capa:
        print(fila)
    print("-" * 20)  # Separador entre capas
    
print(f"Dimensiones: {profundidad}x{filas}x{columnas}")

print(matriz_3d[1][1][0])  # Imprime 7


