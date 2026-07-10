# -*- coding: utf-8 -*-
"""
Created on Tue Mar  4 18:23:14 2025

@author: MARCELOFGB
"""

import pandas as pd

# Cargar el archivo CSV
try:
    df = pd.read_csv('Air_Quality.csv')
except FileNotFoundError:
    print("Error: El archivo 'Air_Quality.csv' no se encuentra.")
    exit()

# Imprimir información general del DataFrame
print("Información general del DataFrame:")
df.info()

# Convertir la columna 'Start_Date' a tipo datetime
df['Start_Date'] = pd.to_datetime(df['Start_Date'])
df.info()

# Imprimir las primeras filas del DataFrame
print("\nPrimeras filas del DataFrame:")
pd.set_option('display.max_columns', None)
print(df.head())



# Operación avanzada 1: Agregación condicional y pivoteo
# Calcular el promedio de 'Data Value' para cada 'Geo Place Name' y 'Indicator ID', pero solo
# para filas donde 'Measure' es 'Mean'. Luego, pivotear la tabla resultante.

df_mean = df[df['Measure'] == 'Mean'] \
    .groupby(['Geo Place Name', 'Indicator ID'])['Data Value'] \
    .mean() \
    .unstack()

print("\nTabla pivote con promedios de 'Data Value' para 'Measure' == 'Mean':")
print(df_mean)


# Operación avanzada 2: Agrupamiento con transformación y función personalizada

# Definir una función para calcular la diferencia entre el valor máximo y mínimo de 'Data Value'
# para cada grupo.

def calculate_difference(group):
    max_value = group['Data Value'].max()
    min_value = group['Data Value'].min()
    return max_value - min_value

# Agrupar por 'Geo Place Name', ordenar los datos por 'Start_Date' dentro de cada grupo,
# y luego aplicar la función 'calculate_difference' a cada grupo.  'include_groups=False' evita el warning.

df_sorted = df.sort_values(by=['Geo Place Name', 'Start_Date'])
df_with_difference = df_sorted.groupby('Geo Place Name', group_keys=False).apply(calculate_difference) # Importante: group_keys=False


print("\nDiferencia entre el valor máximo y mínimo de 'Data Value' por 'Geo Place Name':")
print(df_with_difference)

# Operación avanzada 3:  Multi-Index y selección avanzada

# Crear un multi-índice con 'Geo Place Name' y 'Time Period'
df_multi = df.set_index(['Geo Place Name', 'Time Period'])

# Seleccionar datos para un 'Geo Place Name' específico y un 'Time Period' específico.  Usar .loc
# para indexación basada en etiquetas.
try:
    seleccion = df_multi.loc[('Southeast Queens', 'Annual Average 2012')]
    print("\nSelección de 'Southeast Queens' y 'Annual Average 2012':")
    print(seleccion)
except KeyError:
    print("\nNo se encontraron datos para '409 Southeast Queens' y 'Annual Average 2012'.")

# Operación avanzada 4:  Uso de `pd.NamedAgg` en `groupby.agg` (para un código más limpio).

df_agg = df.groupby('Indicator ID').agg(
    max_value = pd.NamedAgg(column='Data Value', aggfunc='max'),
    min_value = pd.NamedAgg(column='Data Value', aggfunc='min'),
    average_value = pd.NamedAgg(column='Data Value', aggfunc='mean')
)

print("\nAgregación de 'Data Value' por 'Indicator ID':")
print(df_agg)