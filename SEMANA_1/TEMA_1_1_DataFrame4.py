# -*- coding: utf-8 -*-
"""
Created on Mon Mar  3 21:48:19 2025

@author: MARCELOFGB
"""

import pandas as pd

# Crear un diccionario con datos
data = {
    'Nombre': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Edad': [25, 30, 22, 28, 24],
    'Ciudad': ['Nueva York', 'Londres', 'Paris', 'Tokyo', 'Sydney'],
    'Puntuacion': [85, 92, 78, 88, 95]
}

# Crear el DataFrame
df = pd.DataFrame(data)

print("DataFrame Original:")
print(df)

# Ordenar por la columna 'Edad' en orden ascendente
df = df.sort_values(by='Edad')
print("\nDataFrame ordenado por 'Edad' (ascendente):")
print(df)

# Ordenar por la columna 'Puntuacion' en orden descendente
df = df.sort_values(by='Puntuacion', ascending=False)
print("\nDataFrame ordenado por 'Puntuacion' (descendente):")
print(df)

# Ordenar por múltiples columnas (primero por 'Ciudad' y luego por 'Edad')
df = df.sort_values(by=['Ciudad', 'Edad'])
print("\nDataFrame ordenado por 'Ciudad' y luego por 'Edad':")
print(df)