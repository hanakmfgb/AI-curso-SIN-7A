# -*- coding: utf-8 -*-
"""
Created on Sat Jan 10 20:13:22 2026

@author: MARCELOFGB
"""

import numpy as np

# 1. Creamos 32 números secuenciales (del 0 al 31)
datos = np.arange(32)

# 2. Definimos la forma (shape) de 5 dimensiones
# Estructura: (2 bloques grandes, 2 bloques medios, 2 bloques chicos, 2 filas, 2 columnas)
forma_5d = (2,2,2,2,2)

# 3. Convertimos la lista plana en una matriz 5D
matriz_5d = datos.reshape(forma_5d)

print(f"Dimensiones: {matriz_5d.ndim}D")
print(f"Forma (Shape): {matriz_5d.shape}")
print("-" * 30)
print(matriz_5d)