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

# Cambiar el valor de la edad de 'Bob' a 31 (usando .loc para buscar por índice y columna)
df.loc[df['Nombre'] == 'Bob', 'Edad'] = 31
print("\nDataFrame con edad de 'Bob' modificada:")
print(df)

# Cambiar la ciudad de la primera fila
df.loc[0, 'Ciudad'] = 'Madrid'
print("\nDataFrame con ciudad de la primera fila modificada:")
print(df)

# Reemplazar 'Nueva York' por 'New York' en la columna 'Ciudad'
df['Ciudad'] = df['Ciudad'].replace('Madrid', 'New York')
print("\nDataFrame con 'Nueva York' reemplazado por 'New York':")
print(df)

# Definir una función para aumentar la puntuación en un 10%
def aumentar_puntuacion(puntuacion):
    return puntuacion * 1.1

# Aplicar la función a la columna 'Puntuacion'
df['Puntuacion'] = df['Puntuacion'].apply(aumentar_puntuacion)
print("\nDataFrame con puntuación aumentada:")
print(df)

