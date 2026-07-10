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

# Seleccionar una sola columna
nombres = df['Nombre']
print("\nColumna 'Nombre':")
print(nombres)

# Seleccionar múltiples columnas
sub_df = df[['Nombre', 'Edad','Puntuacion']]  # Doble corchete para lista de columnas
print("\nDataFrame con 'Nombre' y 'Edad':")
print(sub_df)


# Seleccionar un valor de la primera fila (índice 0)
primera_fila = df.loc[0,'Nombre'] #se usa .loc para acceder por etiqueta, : todas las filas
print("\nPrimera fila:")
print(primera_fila)

# Seleccionar un rango de filas (filas 1 a 3, incluyendo el 3)
rango_filas = df.iloc[1:3] #se usa .loc para acceder por etiqueta
print("\nRango de filas (1 a 3):")
print(rango_filas)

 # Seleccionar la primera fila (índice 0)
primera_fila = df.iloc[0] #se usa .iloc para acceder por posición
print("\nPrimera fila:")
print(primera_fila)

# Seleccionar un rango de filas (filas 1 a 3, incluyendo el 3)
rango_filas = df.iloc[1:5] #se usa .iloc para acceder por posición
print("\nRango de filas (1 a 3):")
print(rango_filas)


# Seleccionar filas donde la edad sea mayor a 25
mayores_25 = df[df['Edad'] > 25]
print("\nPersonas mayores de 25:")
print(mayores_25)

# Seleccionar filas donde la ciudad sea 'Londres' y la puntuación mayor a 90
condicion_combinada = df[(df['Ciudad'] == 'Londres') & (df['Puntuacion'] > 90)]
print("\nPersonas de Londres con puntuación mayor a 90:")
print(condicion_combinada)

#######################

