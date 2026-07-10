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

# Crear una nueva columna con un valor constante
df['Profesion'] = 'Estudiante' # a todas las filas se le asigna Estudiante
print("\nDataFrame con columna 'Profesion':")
print(df)

# Crear una columna calculada a partir de otra
df['Puntuacion_Doble'] = df['Puntuacion'] * 2
print("\nDataFrame con columna 'Puntuacion_Doble':")
print(df)

# Eliminar la columna 'Profesion'
df = df.drop('Profesion', axis=1)  # axis=1 indica que es una columna
print("\nDataFrame sin columna 'Profesion':")
print(df)

# Eliminar múltiples columnas
df = df.drop(['Puntuacion_Doble'], axis=1)
print("\nDataFrame sin columna 'Puntuacion_Doble':")
print(df)

# Crear una nueva fila como un diccionario
nueva_fila = {'Nombre': 'Frank', 'Edad': 35, 'Ciudad': 'Berlin', 'Puntuacion': 90}

# Agregar la nueva fila al DataFrame (se debe usar ignore_index=True para reindexar)
df = pd.concat([df, pd.DataFrame([nueva_fila])], ignore_index=True) #para evitar problemas de indexación
print("\nDataFrame con nueva fila:")
print(df)

# Eliminar la fila con índice 4
df = df.drop(4)
print("\nDataFrame sin la fila con índice 4:")
print(df)

# Eliminar filas basadas en una condición (ej: eliminar personas menores de 25)
df = df[df['Edad'] >= 25]
print("\nDataFrame sin personas menores de 25:")
print(df)


